from django.shortcuts import render
from django.http import HttpResponse
from . import PredictFromModel as pfm
from . import achilles
#from PredictFromModel import prediction
import joblib 
import json


def home(request):
	return render(request,'realsecurity/home.html')
def Services(request):
	return render(request,'realsecurity/Services.html')
def Contact(request):
	return render(request,'realsecurity/Contact.html')
def pawn_check(request):
	return render(request,'realsecurity/pawn_check.html')
def pawn_user(request):
	username=request.POST["username"]
	username+='\n'
	result=""
	with open('/usr/share/wordlists/rockyou.txt','r') as f:
		for line in f:
			if line==username:
				result="Oh no - Pwned!!!"
				return render(request,'realsecurity/result.html',{'result':result})
		result="Good news — no pwnage found"
		return render(request,'realsecurity/result.html',{'result':result})

def pawn_pass(request):
	password=request.POST["password"]
	password+='\n'
	result=""
	with open('/usr/share/wordlists/rockyou.txt','r') as f:
		for line in f:
			if line==password:
				result="Oh no - Pwned!!!"
				return render(request,'realsecurity/result.html',{'result':result})
		result="Good news — no pwnage found"
		return render(request,'realsecurity/result.html',{'result':result})

def vulnerability_scanner(request):
	return render(request,'realsecurity/vulnerability_scanner.html')

def vuln(request):
	url=request.POST["url"]
	vulnerabilies=achilles.basics(url)
	return HttpResponse(vulnerabilies)

def malware(request):
	return render(request, 'realsecurity/malware.html')

def predictMal(request):
    try:
        if request.POST is not None:
            path = request.POST["csvfile"]

            path = pfm.predictionFromModel(path) #object initialization

            # predicting for dataset present in database
            #path = pred.predictionFromModel()
            return HttpResponse("Prediction File created at %s!!!" % path)
        elif request.form is not None:
            path = request.form['csvfile']

            path = pfm.predictionFromModel(path) #object initialization

            # predicting for dataset present in database
            #path = pred.predictionFromModel()
            return HttpResponse("Prediction File created at %s!!!" % path)

    except ValueError:
        return HttpResponse("Error Occurred! %s" %ValueError)
    except KeyError:
        return HttpResponse("Error Occurred! %s" %KeyError)
    except Exception as e:
        return HttpResponse("Error Occurred! %s" %e)
