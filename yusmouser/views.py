# Create your views here.
import json
from decimal import *
import hashlib
import hmac
import os
import re
from django.shortcuts import render, redirect, get_object_or_404, get_list_or_404
from django.contrib.auth import login, authenticate, logout
from django.http import HttpResponseBadRequest, JsonResponse, HttpResponse

from django.contrib import messages
from .forms import UserCreationForm, LoginForm
from django.contrib.auth.models import User
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
from .apis.monnify_api import create_reserverd_account, get_account_details, get_access_token, get_transaction_status, get_all_transaction, MONNIFY_CONTRACT_CODE, MONNIFY_WALLET_ACCOUNT_NUMBER, MONNIFY_BASE_URL, MONNIFY_SECRET_KEY,MONNIFY_API_KEY
from .apis.husmodata_api import buyAirtimeVTU, buyData, buyElectricityBill, cableSub, getAllDataTransaction, queryDataTransaction, queryAirtimeTransaction, queryBillTransaction, queryCableTransaction, validateIUC, validateMeterNumber, buyResultChecker, generateRechargeCard, buyMTNGiftingCoupon,HUSMODATA_TOKEN
import datetime
from .models import Customer, DataTransaction, AirtimeTransaction, MonnifyTransaction


@login_required()
def homepage(request):
    user_id = request.user.id
    customer = Customer.objects.get(customer=user_id)
    accountReference = Customer.objects.get(customer=user_id).accountReference
    customersTransaction = get_all_transaction(
        account_reference=accountReference)
    for transaction in customersTransaction:
        referencExist = MonnifyTransaction.objects.filter(
            transactionRefrence=transaction['transactionReference'])
        if not referencExist:
            # customer = Customer.objects.get(
            #     customer_email=transaction['customerDTO']['email'])
            monnifyTransact = MonnifyTransaction(
                customer=customer,
                transactionRefrence=transaction['transactionReference'],
                paymentReference=transaction['paymentReference'],
                amountPaid=transaction['amountPaid'],
                totalPayable=transaction['amountPaid'],
                paidOn=transaction['completedOn'],
                paymentStatus=transaction['paymentStatus'],
                paymentDescription=transaction['paymentDescription'],
                currency='NGN',
                paymentMethod=transaction['paymentMethod'])
            monnifyTransact.save()
            customer.customer_wallet_balance += Decimal(
                int(transaction['amountPaid']))
            customer.save()
    wallet_balance = Customer.objects.get(
        customer=user_id).customer_wallet_balance
    g = get_account_details(accountReference)
    accountName = ""
    accounts = []
    for key, value in g['responseBody'].items():
        if key == "accountName":
            accountName = value
        if key == "accounts":
            for item in value:
                accounts.append([
                    item['bankName'], item['accountNumber'],
                    item['accountName']
                ])

    return render(
        request, "home.html", {
            "accountName": accountName,
            "accounts": accounts,
            "wallet_balance": wallet_balance
        })


def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            email = form.cleaned_data.get('email')
            accountReference = username + email
            cr = create_reserverd_account(accountReference, username, email,
                                          username)
            c = Customer(
                customer=user,
                accountReference=accountReference,
                customer_name=cr['responseBody']['customerName'],
                customer_account_name=cr['responseBody']['accountName'],
                customer_email=cr['responseBody']['customerEmail'])
            c.save()
            #messages.success(request, f"New account created{username}")
            login(request,
                  user,
                  backend='django.contrib.auth.backends.ModelBackend')
        else:
            #messages.error(request, f"Account creation failed")
            return render(request, "registration/register.html",
                          {"form": form})

        return redirect("yusmouser:homepage")

    form = UserCreationForm()
    return render(request, "registration/register.html", {"form": form})


def sign_in(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            email = request.POST['email']
            password = request.POST['password']
            try:
                username = User.objects.get(email=email).username
                user = authenticate(username=username, password=password)
                if user is not None:
                    login(request,user,backend='django.contrib.auth.backends.ModelBackend')
                    if user.is_staff:
                      return redirect('yusmouser:yusmo_admin_dashboard')
                    else:
                      return redirect('yusmouser:homepage')
            except:
                user = authenticate(username=email, password=password)
                if user:
                    login(request,
                          user,
                          backend='django.contrib.auth.backends.ModelBackend')
                    if user.is_staff:
                      return redirect('yusmouser:yusmo_admin_dashboard')
                    else:
                      return redirect('yusmouser:homepage') 
    form = LoginForm()
    return render(request, 'registration/login.html', {'form': form})


def sign_out(request):
    logout(request)
    messages.success(request, f'You have been logged out.')
    return redirect('yusmouser:login')


@login_required()
def buydata(request):
    user_id = request.user.id
    wallet_balance = Customer.objects.get(
        customer=user_id).customer_wallet_balance
    access_token = get_access_token()
    if request.method == "POST":
        mobile_number = request.POST['mobile_number']
        network = request.POST['network']
        plan_id = request.POST['dataid']
        amount = request.POST['amount']

        if Decimal(amount[1:]) > wallet_balance:
            messages.error(
                request,
                f'Wallet balance is insufficient for this transaction')
            return render(request, "buydata.html", {
                "wallet_balance": wallet_balance,
                "access_token": access_token
            })
        network_id = 0
        if network == "MTN":
            network_id = 1
        elif network == "GLO":
            network_id = 2
        elif network == "9MOBILE":
            network_id = 3
        else:
            network_id = 4
        dataResponse = buyData(network_id, mobile_number, plan_id)
        with open("dataresponse.txt", "a") as f:
            print(dataResponse, file=f)
        if dataResponse.status_code != 200:
            error2 = dataResponse
            
            messages.error(request,
                           f'{mobile_number} {network} {plan_id} {error2}')
            return render(request, "buydata.html",
                          {"wallet_balance": wallet_balance})
        else:
            with open("dataresponse.txt", "a") as f:
                print(dataResponse, file=f)
            c = DataTransaction(customer=request.user,
                                transaction_id=dataResponse['id'],
                                ident=dataResponse['ident'],
                                mobile_number=dataResponse['mobile_number'],
                                status=dataResponse['Status'],
                                plan_network=dataResponse['plan_network'],
                                plan_name=dataResponse['plan_name'],
                                plan_amount=dataResponse['plan_amount'],
                                balance_before=dataResponse['balance_before'],
                                balance_after=dataResponse['balance_after'],
                                ported_number=dataResponse['Ported_number'],
                                api_response=dataResponse['api_response'])
            c.save()
            customer = Customer.objects.get(customer=user_id)
            plan_amount = Decimal(dataResponse[plan_amount]) + Decimal(5)
            # trim = re.compile(r'[^\d.,]+')
            new_cleaned_amount = plan_amount.quantize(Decimal('.01'), rounding=ROUND_DOWN)
            new_customer_wallet_balance = customer.customer_wallet_balance - new_cleaned_amount
            # customer.save(update_fields=["customer_wallet_balance"])
            Customer.objects.filter(customer=user_id).update(customer_wallet_balance=new_customer_wallet_balance)
            messages.success(
                request,
                f'Purchase of data with the following details \n {mobile_number} {network} {network_id} successful'
            )
            return render(request, "buydata.html",
                          {"wallet_balance": wallet_balance})
    else:
        return render(request, "buydata.html",
                      {"wallet_balance": wallet_balance})


@login_required()
def buyairtime(request):
    user_id = request.user.id
    wallet_balance = Customer.objects.get(
        customer=user_id).customer_wallet_balance
    if request.method == "POST":
        mobile = request.POST['mobile']
        network = request.POST['network']
        airtimetype = request.POST['airtimetype']
        amount = request.POST['amount']
        if Decimal(amount) > wallet_balance:
            messages.error(
                request,
                f'Wallet balance is insufficient for this transaction')
            return render(request, "buyairtime.html",
                          {"wallet_balance": wallet_balance})
        network_id = 0
        if network == "MTN":
            network_id = 1
        elif network == "GLO":
            network_id = 2
        elif network == "9MOBILE":
            network_id = 3
        else:
            network_id = 4
        if int(amount) < 50:
            messages.error(request, f'minimum airtime topup is ₦50')
            return render(request, "buyairtime.html",
                          {"wallet_balance": wallet_balance})
        airtimeData = buyAirtimeVTU(network_id, amount, mobile, airtimetype)
       
        if airtimeData['Status'] != "successful":
            error1 = airtimeData
            messages.error(
                request, f'{mobile} {network} {network_id} {amount} {error1}')
            return render(request, "buyairtime.html",
                          {"wallet_balance": wallet_balance})
        else:
            
            c = AirtimeTransaction(
                customer=request.user,
                transaction_id=airtimeData['id'],
                ident=airtimeData['ident'],
                mobile_number=airtimeData['mobile_number'],
                status=airtimeData['Status'],
                plan_network=airtimeData['plan_network'],
                airtime_type=airtimeData['airtime_type'],
                paid_amount=airtimeData['plan_amount'],
                balance_before=airtimeData['balance_before'],
                balance_after=airtimeData['balance_after'],
                ported_number=airtimeData['Ported_number'],
                api_response=airtimeData['api_response'])
            c.save()
            customer = Customer.objects.get(customer=user_id)
            plan_amount = Decimal(airtimeData['paid_amount']) + Decimal(1)
            
            new_cleaned_amount = plan_amount.quantize(Decimal('.01'), rounding=ROUND_DOWN)
            new_customer_wallet_balance = customer.customer_wallet_balance - new_cleaned_amount
            # customer.save(update_fields=["customer_wallet_balance"])
            Customer.objects.filter(customer=user_id).update(customer_wallet_balance=new_customer_wallet_balance)
            messages.success(
                request,
                f'Purchase of airtime with the following details \n {mobile} {network} {network_id} {amount} successful'
            )
            return render(request, "buyairtime.html",
                          {"wallet_balance": wallet_balance})
    else:
        return render(request, "buyairtime.html",
                      {"wallet_balance": wallet_balance})


@login_required()
def result_checker(request):
    user_id = request.user.id
    wallet_balance = Customer.objects.get(
        customer=user_id).customer_wallet_balance
    if request.method == "POST":
        exam_name = request.POST['exam_name']
        quantity = request.POST['quantity']
        amount = request.POST['amount']
        if Decimal(amount) > wallet_balance:
            messages.error(
                request,
                f'Wallet balance is insufficient for this transaction')
            return render(request, "resultChecker.html",
                          {"wallet_balance": wallet_balance})

        resultCheckerResponse = buyResultChecker(exam_name, quantity)
        if resultCheckerResponse.status_code != 200:
            error1 = resultCheckerResponse
            
            messages.error(request, f'{exam_name} {quantity} {amount} {error1}')
            return render(request, "resultChecker.html",
                          {"wallet_balance": wallet_balance})
        else:
            with open("resultresponse.txt", "a") as f:
                print(resultCheckerResponse.text, file=f)
            customer = Customer.objects.get(customer=user_id)
            customer.customer_wallet_balance -= Decimal(amount)
            customer.save()
            messages.success(
                request,
                f'Purchase of {quantity} {exam_name} pin/s at {amount} naira is successful'
            )
            return render(request, "resultChecker.html",
                          {"wallet_balance": wallet_balance})
    else:
        return render(request, "resultChecker.html",
                      {"wallet_balance": wallet_balance})


@login_required
def print_recharge_card(request):
    user_id = request.user.id
    wallet_balance = Customer.objects.get(
        customer=user_id).customer_wallet_balance
    if request.method == "POST":
        network = request.POST['network']
        network_amount = request.POST['network_amount']
        name_on_card = request.POST['name_on_card']
        quantity = request.POST['quantity']
        amount = request.POST['amount']
        network_id = 0
        if network == "MTN":
            network_id = 1
        elif network == "GLO":
            network_id = 2
        elif network == "9MOBILE":
            network_id = 3
        else:
            network_id = 4
        network_amount_id = 0
        if network_amount == 100:
            network_amount_id = 1
        elif network_amount == 200:
            network_amount_id = 2
        elif network_amount == 500:
            network_amount_id = 3
        else:
            network_amount_id = 4
        if Decimal(amount) > wallet_balance:
            messages.error(
                request,
                f'Wallet balance is insufficient for this transaction')
            return render(request, "printRechargeCard.html",
                          {"wallet_balance": wallet_balance})

        rechargePinResponse = generateRechargeCard(network_id,
                                                   network_amount_id, quantity,
                                                   name_on_card)
        with open("rechargeCard.txt", "a") as f:
            print(rechargePinResponse.text, file=f)
        if rechargePinResponse.status_code != 200:
            error1 = rechargePinResponse
            
            messages.error(
                request,
                f'{network} {network_amount} {quantity} {amount} {error1}')
            return render(request, "printRechargeCard.html",
                          {"wallet_balance": wallet_balance})
        else:

            customer = Customer.objects.get(customer=user_id)
            customer.customer_wallet_balance -= Decimal(amount)
            customer.save()
            messages.success(
                request,
                f'Purchase of {network} {network_amount} {quantity} pin/s at {amount} naira is successful'
            )
            return render(request, "printRechargeCard.html",
                          {"wallet_balance": wallet_balance})
    else:
        return render(request, "printRechargeCard.html",
                      {"wallet_balance": wallet_balance})


@login_required
def mtn_data_pin(request):
    user_id = request.user.id
    wallet_balance = Customer.objects.get(
        customer=user_id).customer_wallet_balance
    if request.method == "POST":
        data_plan = request.POST['data_plan']
        quantity = request.POST['quantity']
        name_on_card = request.POST['name_on_card']
        amount = 0
        if data_plan == 5:
            amount = quantity * 331
        elif data_plan == 7:
            amount = quantity * 663
        elif data_plan == 8:
            amount = quantity * 1104
        elif data_plan == 9:
            amount = quantity * 442
        elif data_plan == 10:
            amount = quantity * 166
        elif data_plan == 11:
            amount = quantity * 221

        if Decimal(amount) > wallet_balance:
            messages.error(
                request,
                f'Wallet balance is insufficient for this transaction')
            return render(request, "mtnGiftingCoupon.html",
                          {"wallet_balance": wallet_balance})

        mtnDataPinResponse = buyMTNGiftingCoupon(data_plan, quantity,
                                                 name_on_card)
        with open("mtnGiftingCoupon.txt", "a") as f:
            print(mtnDataPinResponse.text, file=f)
        if mtnDataPinResponse.status_code != 200:
            error1 = mtnDataPinResponse
            
            messages.error(request, f'{data_plan} {quantity} {amount} {error1}')
            return render(request, "mtnGiftingCoupon.html",
                          {"wallet_balance": wallet_balance})
        else:

            customer = Customer.objects.get(customer=user_id)
            customer.customer_wallet_balance -= Decimal(amount)
            customer.save()
            messages.success(
                request,
                f'Purchase of {data_plan}  {quantity} pin/s at {amount} naira is successful'
            )
            return render(request, "mtnGiftingCoupon.html",
                          {"wallet_balance": wallet_balance})
    else:
        return render(request, "mtnGiftingCoupon.html",
                      {"wallet_balance": wallet_balance})


@login_required()
def buyelectricity(request):
    user_id = request.user.id
    wallet_balance = Customer.objects.get(
        customer=user_id).customer_wallet_balance
    if request.method == "POST":
        disco = request.POST['disco']
        meter_number = request.POST['meternumber']
        meter_type_id = request.POST['metertype']
        amount = request.POST['amount']
        if Decimal(amount) > wallet_balance:
            messages.error(
                request,
                f'Wallet balance is insufficient for this transaction')
            return render(request, "electricity.html",
                          {"wallet_balance": wallet_balance})
        electricityData = buyElectricityBill(disco, amount, meter_number,
                                             meter_type_id)
        if electricityData.status_code != 200:
            error1 = electricityData
            messages.error(request, f'{error1}')
            return render(request, "electricity.html",
                          {"wallet_balance": wallet_balance})
        else:
            responseBody = electricityData['response']
            customer = Customer.objects.get(customer=user_id)
            customer.customer_wallet_balance -= Decimal(amount)
            customer.save()
            with open("buycable.txt", "a") as f:
                print(responseBody.text, file=f)
            messages.success(request, f'Transaction successful {responseBody}')
            return render(request, "electricity.html",
                          {"wallet_balance": wallet_balance})

    else:
        return render(request, "electricity.html",
                      {"wallet_balance": wallet_balance})


@login_required()
def buycable(request):
    user_id = request.user.id
    wallet_balance = Customer.objects.get(
        customer=user_id).customer_wallet_balance
    access_token = HUSMODATA_TOKEN
    if request.method == "POST":
        cableName = request.POST['cable']
        cableplan = request.POST['cableplan']
        mobile = request.POST['mobile']
        amount = request.POST['amount']

        smartcardnumber = request.POST['smartcardnumber']
        # customerName = request.POST['customername']
        if Decimal(amount) > wallet_balance:
            messages.error(
                request,
                f'Wallet balance is insufficient for this transaction')
            return render(request, "buycable.html", {
                "wallet_balance": wallet_balance,
                "access_token": access_token
            })
        cabledata = cableSub(cableName, cableplan, smartcardnumber)
        if cabledata.status_code != 200:
            error1 = cabledata.json()
            messages.error(request, f'{error1}')
            return render(request, "buycable.html", {
                "wallet_balance": wallet_balance,
                "access_token": access_token
            })
        else:
            responseBody = cabledata['response']
            customer = Customer.objects.get(customer=user_id)
            customer.customer_wallet_balance -= Decimal(amount)
            customer.save()
            messages.success(request, f'Transaction successful {responseBody}')
            with open("buycable.txt", "a") as f:
                print(responseBody.text, file=f)
            return render(request, "buycable.html", {
                "wallet_balance": wallet_balance,
                "access_token": access_token
            })

    else:
        return render(request, "buycable.html", {
            "wallet_balance": wallet_balance,
            "access_token": access_token
        })


@login_required()
def airtime_to_cash(request):
    pass


@login_required()
def data_transanction(request):
    username1 = request.user.username
    user_id = request.user.id
    customersTransaction = get_list_or_404(DataTransaction, customer=user_id)

    return render(request, 'data-transaction.html',
                  {"customersTransaction": customersTransaction})


@login_required()
def airtime_transanction(request):
    username1 = request.user.username
    user_id = request.user.id
    customersTransaction = get_list_or_404(AirtimeTransaction,
                                           customer=user_id)

    return render(request, 'airtime-transaction.html',
                  {"customersTransaction": customersTransaction})
  
@login_required()
def wallet_finding(request):
  username1 = request.user.username
  user_id = request.user.id
  customersTransaction = get_list_or_404(MonnifyTransaction,
                                         customer=user_id)

  return render(request, 'wallet-funding.html',
                {"customersTransaction": customersTransaction})
@login_required()
def fund_wallet(request):
    is_ajax = request.headers.get('X-Requested-With') == 'XMLHttpRequest'
    if request.method == "GET":
        user_id = request.user.id
        customer_name = Customer.objects.get(customer=user_id).customer_name
        accountReference = Customer.objects.get(
            customer=user_id).accountReference
        customer_account_name = Customer.objects.get(
            customer=user_id).customer_account_name
        customer_email = Customer.objects.get(customer=user_id).customer_email
        return render(
            request, 'fund-wallet.html', {
                "customerFullName": customer_name,
                "customerAccountName": customer_account_name,
                "customer_email": customer_email,
                "accountReference": accountReference,
                "access_token": get_access_token()
            })
    elif is_ajax:
        if request.method == 'POST':
            data = json.load(request)
            payload = data.get('payload')
            user_id = request.user.id
            Customer.objects.filter(customer=user_id).update(
                customer_wallet_balance=int(payload))
            # customer.customer_wallet_balance += request.GET.get('amount')
            json_response = {'response': "wallet updated successfully"}
            return JsonResponse(json_response)


@login_required()
def fund_wallet2(request):
    if request.method == "GET":
        wallet_response = ""
        user_id = request.user.id
        paymentReference = request.GET.get('paymentReference')
        get_status = get_transaction_status(paymentReference)
        status = get_status["responseBody"]["paymentStatus"]
        if status == "PAID":
            customer = Customer.objects.get(customer=user_id)
            customer.customer_wallet_balance += Decimal(
                get_status["responseBody"]["amountPaid"])
            customer.save()
            wallet_response = "Payment Successful"
        else:
            wallet_response = "Transaction Failed"
        return render(request, 'fund-wallet2.html',
                      {'wallet_response': wallet_response})


def computeSha512(txtohas1, txtToHash):
    m = hmac.HMAC(txtohas1, txtToHash, digestmod=hashlib.sha512)
    return m.hexdigest()


@csrf_exempt
@require_POST
def webhook_paystack_payment(request):
    with open("paystack.txt", "a") as f:
        print(request.body, file=f)
    return HttpResponse(request.body, status=200)


@csrf_exempt
@require_POST
def webhook_payment(request):
    with open("webhook.txt", "a") as f:
        print(request.body, file=f)
    message = json.loads(request.body.decode('utf-8'))
    requestBody = message['responseBody']
    # The formula is: SHA-512(client secret key + object of request body).
    clientSecret = bytes(MONNIFY_SECRET_KEY, 'utf-8')
    requestBodyBytes = bytes(request.body, 'utf-8')
    if computeSha512(clientSecret,
                     requestBodyBytes) == request.GET.get['monnify-signature']:
        referencExist = MonnifyTransaction.object.filter(
            transactionRefrence=requestBody['eventData']
            ['transactionReference'])
        if not referencExist:
            customer = Customer.objects.get(
                customer_email=requestBody['eventData']['customer']['email'])
            monnifyTransact = MonnifyTransaction(
                customer=customer.id,
                transactionRefrence=requestBody['eventData']
                ['transactionReference'],
                paymentReference=requestBody['eventData']['paymentReference'],
                amountPaid=requestBody['eventData']['amountPaid'],
                totalPayable=requestBody['eventData']['totalPayable'],
                settlementAmount=requestBody['eventData']['settlementAmount'],
                paidOn=requestBody['eventData']['transactionReference'],
                paymentStatus=requestBody['eventData']['paymentStatus'],
                paymentDescription=requestBody['eventData']
                ['paymentDescription'],
                currency='NGN',
                paymentMethod=requestBody['eventData']['transactionReference'])
            monnifyTransact.save()
            customer.customer_wallet_balance += requestBody['eventData'][
                'amountPaid']
            return HttpResponse(request.body, status=200)


@login_required()
def get_uic_number(request):
    is_ajax = request.headers.get('X-Requested-With') == 'XMLHttpRequest'
    if is_ajax:
        if request.method == 'GET':
            smart_card = request.GET.get('smartcard')
            cable_name = request.GET.get('cable_name')
            iuc_validate_response = validateIUC(smart_card, cable_name)
            
            return JsonResponse(iuc_validate_response.text, safe=False)


def get_meter(request):
    is_ajax = request.headers.get('X-Requested-With') == 'XMLHttpRequest'
    if is_ajax:
        if request.method == 'GET':
            meter_number = request.GET.get('meterNumber')
            disco_name = request.GET.get('disco_name')
            meter_type_id = request.GET.get('metertypeid')
            meter_response = validateMeterNumber(meter_number, disco_name,
                                                 meter_type_id)

            return JsonResponse(meter_response.text, safe=False)
