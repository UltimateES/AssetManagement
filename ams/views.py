from django.shortcuts import render
from rest_framework.views import APIView
# Create your views here.
from .models import Asset
from rest_framework import viewsets
from .serializers import AssetSerializer
from django.shortcuts import get_object_or_404, render
from rest_framework import filters

class AssetViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Asset.objects.all()
    serializer_class = AssetSerializer
    filter_backends = (filters.SearchFilter,)
    search_fields = ('id', 'asset_name')

def home(request):
    asset_list = Asset.objects.all()
    return render(request, 'index.html',{'asset_list':asset_list})
