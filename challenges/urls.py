from django.urls import path

from . import views

# lets create URLCnfig
urlpatterns = [
    # path('january',views.january),
    # path('february', views.february),
    # path("<double:is_it>", views.bool_testing), invalid

    path("<int:month>", views.monthly_challenges_in_numbers),
    path("<str:month>", views.monthly_challenges),
   
    
]