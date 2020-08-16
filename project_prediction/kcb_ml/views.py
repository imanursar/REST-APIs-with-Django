from django.shortcuts import render
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework import status

from kcb_ml.models import Kcb
from kcb_ml.serializers import KcbSerializer
from rest_framework.decorators import api_view
from .apps import PredictorConfig

# Create your views here.
@api_view(['GET', 'POST', 'DELETE'])
def kcb_ml_list(request):
    # Retrieve objects (with condition)
    if request.method == 'GET':
        Kcb_list = Kcb.objects.all()
        prob = request.GET.get('prob_topay', None)
        if prob is not None:
            Kcb_list = Kcb_list.filter(prob__icontains=prob)

        Kcb_list_serializer = KcbSerializer(Kcb_list, many=True)
        return JsonResponse(Kcb_list_serializer.data, safe=False)
        # 'safe=False' for objects serialization

    # Create a new object
    elif request.method == 'POST':
        Kcb_list_data = JSONParser().parse(request)
        Kcb_list_serializer = KcbSerializer(data=Kcb_list_data)
        if Kcb_list_serializer.is_valid():
            Kcb_list_serializer.save()
            return JsonResponse(Kcb_list_serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(Kcb_list_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Create your predict here.
@api_view(['GET', 'POST', 'DELETE'])
def kcb_ml_pred(request):
    # Create a new object
    if request.method == 'POST':
        Kcb_list_data = JSONParser().parse(request)
        Kcb_list_serializer = KcbSerializer(data=Kcb_list_data)
        if Kcb_list_serializer.is_valid():
            Kcb_list_serializer.save()
            return JsonResponse(PredictorConfig.predict(Kcb_list_serializer.data,request.headers.get('reason')),status = 200)
        return JsonResponse(Kcb_list_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# @api_view(['GET'])
def userview(request):
	Kcb_list = Kcb.objects.all()
	context = {
		'Kcb_list':Kcb_list
	}
	return render(request,'kcb_ml/userview.html', context)
