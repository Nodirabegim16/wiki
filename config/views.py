from django.shortcuts import render, redirect


def Base(request):
    return render(request, 'base.html')

def Wiki(request):
    return render(request, 'wiki.html')