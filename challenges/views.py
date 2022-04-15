from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse

challenges = {
    "january": "Eat no meat for a month",
    "february": "Drink no alcohol for a month",
    "march": "Read 20 pages of a book everyday",
    "april": "Walk for at least 3k everyday",
    "may": "Talk with one family member everyday",
    "june": "Meditate 10 mins everyday",
    "july": "Eat no meat for a month",
    "august": "Drink no alcohol for a month",
    "september": "Read 20 pages of a book everyday",
    "october": "Walk for at least 3k everyday",
    "november": "Talk with one family member everyday",
    "december": "Meditate 10 mins everyday"
}

# Create your views here.

def index(request):
    list_items = ""
    months = list(challenges.keys())

    for month in months:
        capitalized_month = month.capitalize()
        month_path = reverse("month-challenge", args=[month])
        list_items += f"<li><a href=\"{month_path}\">{capitalized_month}</a></li>"

    response_data = f"<ul>{list_items}</ul>"
    
    return HttpResponse(response_data)

def monthly_challenge_by_number(request, month):
    months = list(challenges.keys())

    if month > len(months):
        return HttpResponseNotFound("<h1>Invalid Month</h1>")
    forward_month = months[month - 1]
    redirect_month = reverse("month-challenge", args=[forward_month])
    return HttpResponseRedirect(redirect_month)

def monthly_challenge(request, month):
    try:
        challenge_text = challenges[month]
        response_data = f"<h1>{challenge_text}</h1>"
        return HttpResponse(response_data)
    except:
        return HttpResponseNotFound("<h1>This month is not supported</h1>")
    
