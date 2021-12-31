from django.http import HttpResponseNotFound
from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse

# Create your views here.
challenges = {
    "january": "Walk for 30 minutes",
    "february": "Yoga for 10 minutes",
    "march" : "Leanr new skill every day for 30 minutes",
    "april" : "Listen Podcast for 30 minutes",
    "may" : "Listen Podcast for 30 minutes",
    "june" : "Listen Podcast for 30 minutes",
    "july" : "Listen Podcast for 30 minutes",
    "august" : "Listen Podcast for 30 minutes",
    "september" : "Listen Podcast for 30 minutes",
    "october" : "Listen Podcast for 30 minutes",
    "november" : "Listen Podcast for 30 minutes",
    "december" : "Listen Podcast for 30 minutes",
}


def index(request):
    output = "<ul>"
    list_of_months = list(challenges.keys())
    
    for i in range(12):
        redirected_path = reverse("monthly-challenge", args = [list_of_months[i]])
        output = output+f" <li> <a href='{redirected_path}'>{list_of_months[i].upper()}</a> </li>"
    output = output+ "</ul>"
   
    return HttpResponse(output)


def monthly_challenges(request, month):
    try:
        return HttpResponse(challenges[month])
    except:
        return HttpResponseNotFound(f"Please give us a valid input in between {challenges.keys()}")    

def monthly_challenges_in_numbers(request, month):
    try: 
        # return HttpResponse(challenges[list(challenges.keys())[month-1]])
        return HttpResponseRedirect(f"/challenges/{list(challenges.keys())[month-1]}")
    except Exception as e:
        print(e)    
        return HttpResponseNotFound(f"Please givve us valid input in between {challenges.keys()} ")    




# def january(request):
#     return HttpResponse("Hello Dude!!!")


# def february(request):
#     return HttpResponse("Walk for at least 30 minutes. ")


# def monthly_challenges(request, month):
#     challenges = [ 
#             "Walk for 30 minutes",
#             "Yoga for 10 minutes",
#             "Leanr new skill every day for 30 minutes",
#             "Listen Podcast for 30 minutes",
#             ] 
    
#     months = ["january","february","march","april"]

#     if month in months:
#         return HttpResponse(challenges[months.index(month)])

#     return HttpResponseNotFound(f"Please provide valid input i.e. {months}")

# def monthly_challenges_in_numbers(request,month):
#     challenges = [ 
#             "Walk for 30 minutes",
#             "Yoga for 10 minutes",
#             "Leanr new skill every day for 30 minutes",
#             "Listen Podcast for 30 minutes",
#             ] 
#     if month in [1,2,3,4]:
#         return HttpResponse(challenges[month])

#     return HttpResponseNotFound(f"Please provide valid input i.e. {months}")


# def bool_testing(request, is_it):
#     return HttpResponse("Its working")