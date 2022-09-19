import imp
from django.shortcuts import render
from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import permissions
from DAO import serializers
from DAO.serializers import UserSerializer, GroupSerializer
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from rest_framework.decorators import api_view
from rest_framework import status, generics
from DAO.serializers import DAOSerializer
from DAO.models import DAO

# Create your views here.
class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]

class DaoList(generics.ListCreateAPIView):
    queryset = DAO.objects.all()
    serializer_class = DAOSerializer

class DaoDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = DAO.objects.all()
    serializer_class = DAOSerializer

"""
@api_view(['GET', 'POST'])
def DAO_list(request):
    
    List of DAO object
    

    if request.method == 'GET':
        dao = DAO.objects.all()
        serializer = DAOSerializer(dao, many = True)
        return JsonResponse(serializer.data, safe = False)
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = DAOSerializer(data = data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status = status.HTTP_201_CREATED)
        return JsonResponse(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
"""