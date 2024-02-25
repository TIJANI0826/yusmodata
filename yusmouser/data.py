from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from .models import Data
def get_data(request):
  is_ajax = request.headers.get('X-Requested-With') == 'XMLHttpRequest'
  if is_ajax:
    data = Data.objects.all()
    return JsonResponse({'data': data}, safe=False)

def get_single_data(request, pk):
  
  is_ajax = request.headers.get('X-Requested-With') == 'XMLHttpRequest'
  if is_ajax:
    data = get_object_or_404(Data, pk=pk)
    return JsonResponse({'data': data}, safe=False)

def create_network(request):
    is_ajax = request.headers.get('X-Requested-With') == 'XMLHttpRequest'
    if is_ajax:
        if request.method == 'POST':
          network = Data(
            data_id=request.POST.get('data_id'),
            network=request.POST.get('network'),
            plan_type=request.POST.get('plan_type'),
            amount=request.POST.get('amount'),
            size=request.POST.get('size'),
            validity=request.POST.get('validity'),)
          return JsonResponse({"data" : "Data created successfully" })
   

def update_data(request, pk):
    data = get_object_or_404(Data, pk=pk)
    if request.method == 'POST':
      data_id=request.POST.get('data_id')
      network=request.POST.get('network')
      plan_type=request.POST.get('plan_type')
      amount=request.POST.get('amount')
      size=request.POST.get('size')
      validity=request.POST.get('validity')
      
      data.data_id = data_id
      data.network = network
      data.plan_type = plan_type
      data.amount = amount
      data.size = size
      data.validity = validity

      data.save()
      return JsonResponse({'message': 'Data  updated successfully!'})

def delete_data(request, pk):
    data = get_object_or_404(Data, pk=pk)
    data.delete()
    return JsonResponse({'message': 'Data deleted successfully!'})
