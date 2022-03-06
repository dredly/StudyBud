from django.shortcuts import render
from django.template import context

rooms = [
    {"id": 1, "name": "ReactJS basics"},
    {"id": 2, "name": "Serverless functions"},
    {"id": 3, "name": "Styling with TailwindCSS"},
]

# Create your views here.
def home(request):
    context={"rooms": rooms}
    return render(request, "base/home.html", context)

def room(request, pk):
    room = None
    for r in rooms:
        if r["id"] == int(pk):
            room = r
    context={"room": room}
    return render(request, "base/room.html", context)