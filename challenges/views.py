from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def monthly_challenges(request, month):
    challenge_text = None
    if month == "january":
        challenge_text = "Eat no meat for a month"
    return HttpResponse()
