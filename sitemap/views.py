from django.shortcuts import render
from django.http import HttpResponse
import folium

# Create your views here.
def index(request):
    return render(request, 'index.html')

def kart(request):
    #Create map
    m = folium.Map(location=[63.417190066978264, 10.404224395751953], zoom_start = 12)
    folium.Marker(location=[63.417190066978264, 10.404224395751953]).add_to(m)
    #Get html representation of the map
    m = m._repr_html_()

    context = {
        'm': m,
    }
    return render(request, 'kart.html', context)
