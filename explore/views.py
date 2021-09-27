import re
from django.shortcuts import render,redirect
import requests
from .models import Posts

# Create your views here.


def Location(ip):
    try:
        from geopy.geocoders import Nominatim
        import geocoder

        g = geocoder.ip(ip)
        print(g.latlng)
        print(g.city)
        geolocator = Nominatim(user_agent="geoapiExercises")
        Latitude = g.latlng[0]
        Longitude = g.latlng[1]

        location = geolocator.reverse(f"{Latitude},{Longitude}")

        # Display
        return f"{g.city},{g.country}"
    except Exception as e:
        print("Error")




def explore(request):
    if request.user.is_anonymous:
        return redirect('/accounts/login')
    journeys=Posts.objects.all()

    return render(request,"explore.html",{"journeys":journeys,"current_user":request.user})
    
    

def profile(request,username):
    if request.user.is_anonymous:
        return redirect('/accounts/login')
    profile_posts=Posts.objects.all().filter(author=username)
    return render(request, "profile.html", {"profile_posts": profile_posts, "profile_user": username, "current_user": request.user})

def post(request):
    if request.user.is_anonymous:
        return redirect('/accounts/login')
    if request.method == 'POST':
        description = request.POST.get('desc')
        img=request.POST.get('img')
        from ipware import get_client_ip
        client_ip, is_routable = get_client_ip(request)
        city=Location(client_ip)
        img=request.FILES.get('img')
        if(city==None):
            city="Anonymous"
        new_post=Posts.objects.create(author=request.user.username,description=description,img=img,location=city)
        new_post.save()
        return redirect('/')
    
    return render(request,"post.html")


