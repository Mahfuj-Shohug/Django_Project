from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseNotFound


# Create your views here.
def monthNumber(request, month):
    return HttpResponse(month * month)


def monthlyChallanges(request, month):
    challangesText = None
    if month == "january":
        challangesText = "This is january"
    elif month == "february":
        challangesText = "This is february"
    elif month == "march":
        challangesText = "This is march"
    elif month == "april":
        challangesText = "This is april"
    elif month == "may":
        challangesText = "This is may"
    elif month == "june":
        challangesText = "This is june"
    elif month == "july":
        challangesText = "This is july"
    elif month == "auguest":
        challangesText = "This is auguest"
    elif month == "september":
        challangesText = "This is september"
    elif month == "october":
        challangesText = "This is october"
    elif month == "november":
        challangesText = "This is november"
    elif month == "december":
        challangesText = "This is december"
    else:
        return HttpResponseNotFound("Your URL is wrong")
    return HttpResponse(challangesText)
