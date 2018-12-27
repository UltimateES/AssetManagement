from .models import Asset
from rest_framework import serializers
import pyqrcode
from assetmanage.settings import MEDIA_ROOT
from django.core.files.storage import FileSystemStorage

class AssetSerializer(serializers.ModelSerializer):

    class Meta:
        model = Asset
        fields =  '__all__'
