from django.shortcuts import render, redirect
from django.http import HttpResponse
import requests
from django.http import JsonResponse
import os
from django.conf import settings

def home(request):
    return render(request,"index.html")

def camera(request):
    return render(request,"hhe.html")

def team(request):
    return render(request,"Team.html")

def about(request):
    return render(request,"about.html")