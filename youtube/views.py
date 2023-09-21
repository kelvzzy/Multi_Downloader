from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def youtube(request):
    link2=None
    if request.method=="POST":
        link2=request.POST.get("link")

    return render(request, "youtube/index.html", 
                  {"link":link2}
                  )