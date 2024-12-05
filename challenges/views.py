from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
# Create your views here.

month_challenges = {
    "january": "Eat no sugar for the entire month!",
    "february": "Walk for at least 30 minutes every day!",
    "march": "Read a book for at least 40 minutes!",
    "april": "Eat healthy",
    "may": "Eat no sugar for the entire month!",
    "june": "Walk for at least 30 minutes every day!",
    "july": "Read a book for at least 40 minutes!",
    "august": "Eat healthy",
    "september": "Eat no sugar for the entire month!",
    "october": "Walk for at least 30 minutes every day!",
    "november": "Read a book for at least 40 minutes!",
    "december": None
}


def menu(request):
    months = list(month_challenges.keys())
    return render(request, "challenges/menu.html", {
        "month_list": months
    })


def monthly_challenge_by_number(request, month):
    months = list(month_challenges.keys())
    redirect_month = months[month-1]
    redirect_path = reverse("month-challenge", args=[redirect_month])
    if month > len(months):
        return HttpResponseNotFound("Invalid month")
    return HttpResponseRedirect(redirect_path)


def monthly_challenge(request, month):

    try:
        challenge_text = month_challenges[month]
        return render(request, "challenges/challenge.html", {
            "text": challenge_text,
            "month": month
        })
    except:
        return HttpResponseNotFound("<h1>No challenges for the month :(</h1>")

    ## response_data = f"<h1>{month_challenges[month]}</h1>"#
