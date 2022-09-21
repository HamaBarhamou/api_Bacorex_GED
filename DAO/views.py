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
from rest_framework import status, generics, mixins
from DAO.serializers import DAOSerializer
from DAO.models import DAO
from DAO.permissions import IsOwnerOrReadOnly

# Create your views here.
class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class GroupViewSet(viewsets.ModelViewSet):
    """"
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]

class DaoList(generics.ListCreateAPIView):
#class DaoList(generics.ListAPIView):
    queryset = DAO.objects.all()
    serializer_class = DAOSerializer
    permission_classes = [permissions.IsAuthenticated]

    #def perform_create(self, serializer):
    #    serializer.save(owner=self.request.user)


class DaoDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = DAO.objects.all()
    serializer_class = DAOSerializer
    permission_classes = [permissions.IsAuthenticated, IsOwnerOrReadOnly]
    #permission_classes = [permissions.IsAuthenticated]

""""
class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
"""
