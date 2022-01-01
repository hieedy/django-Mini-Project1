from django.http import HttpResponseNotFound
from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse
from django.template.loader import render_to_string
from django.http import Http404

# Create your views here.
challenges = {
    "january": "Eat a food you’ve never tried before.",
    "february": "Visit a nearby town–staying the weekend is optional.",
    "march" : "Try a different way of getting to work – walking, cycling, taking the bus, or even skating.",
    "april" : "Go geocaching – an outdoor recreational activity that involves hunting for hidden objects using GPS coordinates posted on a website.",
    "may" : "Sleep under the moon (it can even be in your own backyard).",
    "june" : "Swim in the wild – find a river or a lake, and jump in.",
    "july" : "Go to a beach you’ve never been to before (bonus points if you try a new water sport).",
    "august" : "Spend a day eating only what you catch or forage.",
    "september" : "Climb a hill and have a picnic when you get to the top.",
    "october" : "Get on the subway and go to the end of the line.",
    "november" : "Be a tourist in your own town – visit a place in your town",
    "december" : None,
}


def monthly_challenges(request,month):
    
    # try:
        challenge = challenges[month]
        return render(request, "challenges/monthly_challenges.html", {
            "challenge": challenge,
            "month" : month
        })
    # except:
    #     raise Http404() # it will automatically pick 404.html file form the templates folder in the root directory. In the Debug=True we can't see that page also. but it will work in the production.

    #     # render_result = render_to_string("404.html")
    #     # return HttpResponseNotFound(render_result)


def index(request):
    list_of_months = list(challenges.keys())
    return render(request, "challenges/index.html", {
        "months": list_of_months,
    })


# def monthly_challenges(request, month):
#     try:
#         return HttpResponse(challenges[month])
#     except:
#         return HttpResponseNotFound(f"Please give us a valid input in between {challenges.keys()}")    

# def monthly_challenges_in_numbers(request, month):
#     try: 
#         # return HttpResponse(challenges[list(challenges.keys())[month-1]])
#         return HttpResponseRedirect(f"/challenges/{list(challenges.keys())[month-1]}")
#     except Exception as e:
#         print(e)    
#         return HttpResponseNotFound(f"Please givve us valid input in between {challenges.keys()} ")    




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