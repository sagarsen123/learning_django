from django.shortcuts import render
from django.http import HttpResponse 

# def home(request):
#     return HttpResponse("""
#                         <h1>Hey I am a Django Server...</h1>
#                         <h2> This is the Mutlti line Response from the django server</h2>
#                         <hr>
#                         """)

def home(request):
    return render(request , 'home/index.html')

def success_page(request):
    return HttpResponse("<h1>Hey this is the sucess page</h1>")