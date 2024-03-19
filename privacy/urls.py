from django.urls import path
from . import views


urlpatterns = [
    path('privacy/', views.privacy),
    path('nonna_italia/', views.privacy2),
    path('nonna_italia_ITA/', views.privacy2_ITA),
    path('iMeditazione/', views.privacy_iMeditazione),
    path('Scateno/', views.privacy_Scateno),
    path('FB_Sign_in/', views.privacy_Signin),
    path('MegaHelp/', views.privacy_MegaHelp),
    path('MegaHelp_en/', views.privacy_MegaHelp_en),
]

