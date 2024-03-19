from django.shortcuts import render, HttpResponse

# Create your views here.

def privacy(request):
    return render(request, 'privacy_policy.html')

def privacy2(request):
    return render(request, 'privacy_policy2.html')

def privacy2_ITA(request):
    return render(request, 'privacy_policy2_ITA.html')

def privacy_iMeditazione(request):
    return render(request, 'privacy_iMeditazione.html')

def privacy_Scateno(request):
    return render(request, 'privacy_Scateno.html')

def privacy_Signin(request):
    return render(request, 'privacy_fb_signin.html')

def privacy_MegaHelp(request):
    return render(request, 'privacy_MegaHelp.html')

def privacy_MegaHelp_en(request):
    return render(request, 'privacy_MegaHelp_EN.html')

