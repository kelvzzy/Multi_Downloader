from django.http import HttpResponse
from django.shortcuts import render
from pytube import YouTube

# Create your views here.
def youtube(request):
    link2=None
    yt_title=None
    if request.method=="POST":
        link2=request.POST.get("link")
        try:
            yt = YouTube(link2)
            yt_title = yt.title  # Get the title of the YouTube video
        except Exception as e:
            # Handle any exceptions that may occur (e.g., invalid URL)
            print(f"Error: {e}")
    return render(request, "youtube/index.html", 
                  {"link":yt_title}
                  )