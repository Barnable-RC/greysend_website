from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def test_view(request):
    return HttpResponse("This is a test endpoint!")


def landing_page(request):
    return render(request, 'landing_page.html')


def index(request):
    return render(request, 'chat/index.html')

def room(request, room_name):
    return render(request, 'chat/room.html', {
        'room_name': room_name
    })