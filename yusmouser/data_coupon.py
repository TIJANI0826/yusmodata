from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from .models import Data_Coupon

def get_data_coupon(request):
    networks = network.objects.all()
    return render(request, 'network_list.html', {'networks': networks})

def create_data_coupon(request):
    if request.method == 'POST':
        network_id = request.POST.get('network_id')
        network_name = request.POST.get('network_name')
        network.objects.create(network_id=network_id, network_name=network_name)
        return JsonResponse({'message': 'Network created successfully!'})

def update_data_coupon(request, pk):
    net = get_object_or_404(network, pk=pk)
    if request.method == 'POST':
        network_id = request.POST.get('network_id')
        network_name = request.POST.get('network_name')
        net.network_id = network_id
        net.network_name = network_name
        net.save()
        return JsonResponse({'message': 'Network updated successfully!'})

def delete_data_coupon(request, pk):
    net = get_object_or_404(network, pk=pk)
    net.delete()
    return JsonResponse({'message': 'Network deleted successfully!'})
