from django.shortcuts import render, redirect
from .models import Receipe

# Create your views here.
def receipes(request):
    if(request.method == "POST"):
        data = request.POST

        receipe_image = request.FILES.get('receipe_image')
        receipe_name  = data.get('receipe_name')
        receipe_description = data.get('receipe_description')

        Receipe.objects.create(
            receipe_name = receipe_name,
            receipe_description = receipe_description,
            receipe_image =receipe_image
        )
        return redirect('/receipes/')
        print(receipe_name,receipe_description,receipe_image, sep='\n')
    return render(request, 'receipes.html')