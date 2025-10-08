from django.shortcuts import render
from django.views.generic import View
from django.http import HttpResponse
# Create your views here.
class SampleView(View):

    def get(self,request):

        print("get method")

        return HttpResponse("response displayed by browser")
    
class test_view(View):

    def get(self,request):

        print("my first view")

        return HttpResponse("response succefully completed")

    