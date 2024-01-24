from django.shortcuts import render, HttpResponse
from .forms import ApartmentForm
from .models import Apartment, ApartmentImage

from rest_framework.views import APIView
from rest_framework import generics, viewsets

from .serializers import ApartmentSerializer


def index(request):
    if request.method == 'POST':
        form = ApartmentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponse('Success')
    form = ApartmentForm()
    return render(request, 'core/index.html', context={'form': form})


#
# class ApartmentApiView(generics.ListAPIView):
#     queryset = Apartment.objects.all()
#     serializer_class = ApartmentSerializer

class ApartmentApiView(viewsets.ModelViewSet):
    queryset = Apartment.objects.all()
    serializer_class = ApartmentSerializer
