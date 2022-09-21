from dataclasses import field
from pyexpat import model
from unittest.util import _MAX_LENGTH
from django.contrib.auth.models import User, Group
from DAO.models import DAO
from rest_framework import serializers


class UserSerializer(serializers.HyperlinkedModelSerializer):
    #dao = serializers.PrimaryKeyRelatedField(many=True, queryset=DAO.objects.all())
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']
        #fields = ['id', 'username', 'dao']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']

class DAOSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    class Meta:
        model = DAO
        fields = [
            'id', 
            'id_DAO', 
            'description_DAO', 
            'created_at', 
            'updated_at',
            'publication_date',
            'date_submitted',
            'document_link',
            'departement_head_approval',
            'ceo_approval',
            'owner'
        ]