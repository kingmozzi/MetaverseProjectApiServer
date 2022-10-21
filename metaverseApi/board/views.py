from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt

from .models import Board
from .serializers import BoardSerializer

from rest_framework.parsers import JSONParser

from django.core.paginator import Paginator


# Create your views here.
@csrf_exempt
def board_list(request):
    if request.method == 'GET':
        queryset = Board.objects.all()
        paginator = Paginator(queryset, 8)

        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        serializer = BoardSerializer(page_obj, many=True)
        return JsonResponse(serializer.data, safe=False)
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = BoardSerializer(data = data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

@csrf_exempt
def board(request, id):
    obj = Board.objects.get(id=id)

    if request.method == 'GET':
        serializer = BoardSerializer(obj)
        return JsonResponse(serializer.data, safe=False)
    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = BoardSerializer(obj, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)
    elif request.method == 'DELETE':
        obj.delete()
        return HttpResponse(status=204)

