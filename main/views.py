from django.shortcuts import render
import requests

def main(request):
    
    args = {}
    return render(request, 'main/main.html', args)