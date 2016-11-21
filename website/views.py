
from django.shortcuts import render
# Create your views here.


def index(request):
    return render(request, 'website/index.html', {
    })


def forward(request):
    with open("test.csv", 'r+') as f:
        f.truncate()
        f.write("0.2,0")
        f.close()
    return render(request, 'website/index.html', {})


def back(request):
    with open("test.csv", 'r+') as f:
        f.truncate()
        f.write("-0.2,0")
        f.close()
    return render(request, 'website/index.html', {})


def left(request):
    with open("test.csv", 'r+') as f:
        f.truncate()
        f.write("0.2,0.01")
        f.close()
    return render(request, 'website/index.html', {})


def right(request):
    with open("test.csv", 'r+') as f:
        f.truncate()
        f.write("0.2,-0.01")
        f.close()
    return render(request, 'website/index.html', {})


def topright(request):
    with open("test.csv", 'r+') as f:
        f.truncate()
        f.write("0,-0.1")
        f.close()
    return render(request, 'website/index.html', {})


def topleft(request):
    with open("test.csv", 'r+') as f:
        f.truncate()
        f.write("0.2,0.1")
        f.close()
    return render(request, 'website/index.html', {})


def bottomright(request):
    with open("test.csv", 'r+') as f:
        f.truncate()
        f.write("-0.2,0.01")
        f.close()
    return render(request, 'website/index.html', {})


def bottomleft(request):
    with open("test.txt", 'r+') as f:
        f.truncate()
        f.write("-0.2,-0.01")
        f.close()
    return render(request, 'website/index.html', {})

