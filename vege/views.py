from django.shortcuts import render, redirect
from .models import Receipe
from django.http import HttpResponse

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
    
    queryset = Receipe.objects.all()

    if request.GET.get('search_receipe'):
       queryset = queryset.filter(receipe_name__icontains = request.GET.get('search_receipe'))
    
    context = {'receipes': queryset}
    print(queryset)
    return render(request, 'receipes.html', context)
    # return render(request, 'receipes.html')

def delete_receipe(request, id):
    print(id)
    queryset = Receipe.objects.get(id = id)
    queryset.delete()
    return redirect('/receipes/')
    # return HttpResponse({/id})

def update_receipe(request, id):
    queryset = Receipe.objects.get(id = id)
    if request.method == "POST":
        data = request.POST

        receipe_image = request.FILES.get('receipe_image')
        receipe_name  = data.get('receipe_name')
        receipe_description = data.get('receipe_description')

        # updating the data in query set
        queryset.receipe_name = receipe_name
        queryset.receipe_description = receipe_description
        if receipe_image :
            queryset.receipe_image = receipe_image
        
        queryset.save()
        return redirect('/receipes/')
    
    context = {'receipe': queryset}
    return render(request, 'update_receipes.html', context)
    # return HttpResponse("This is the update Page")