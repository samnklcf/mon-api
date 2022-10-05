from dataclasses import field
from pyexpat import model
from rest_framework import serializers
from .models import *

class TacheSerial(serializers.ModelSerializer):
    class Meta:
        model = tache
        fields = "__all__"

