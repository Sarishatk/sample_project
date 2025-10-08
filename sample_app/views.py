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
    
class AditionView(View):

    def get(self,request):

        num1 = int(input("enter first number: "))

        num2 = int(input("enter second number: "))

        sum = num1 + num2

        return HttpResponse(f"sum of two numbers is {sum}")
    

class OddEven(View):

    def get(self,request):

        number = int(input("enter a number"))

        if number%2==0:

            result = "even"

        else:

            result = "odd"

        return HttpResponse(f"The number {number} is {result}")

    