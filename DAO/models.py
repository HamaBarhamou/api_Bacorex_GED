from pyexpat import model
from statistics import mode
from xml.dom.minidom import Document
from django.db import models
from django.utils import timezone

# Create your models here.
class DAO(models.Model):
    id_DAO = models.CharField(max_length = 25, default = "N:0000")
    description_DAO = models.CharField(max_length = 200, default = "DAO")
    created_at = models.DateTimeField(default = timezone.now())
    updated_at = models.DateTimeField(default = timezone.now())
    publication_date = models.DateTimeField()
    date_submitted = models.DateTimeField()
    document_link = models.CharField(max_length=300)
    departement_head_approval = models.BooleanField()
    ceo_approval = models.BooleanField()

    def __str__(self):
        return ("{} \n {}".format(self.id_DAO, self.description_DAO))