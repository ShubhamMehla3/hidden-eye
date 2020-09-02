#!/usr/bin/env python3
import argparse
import validators
import requests
import yaml
from urllib.parse import urlparse
from bs4 import BeautifulSoup,Comment

def basics(url):
	config={'forms':True,'comments':True,'passwords':True}
	report=""
	fail=""
	if validators.url(url):
		result_html=requests.get(url).text
		parsed_html=BeautifulSoup(result_html,"html.parser")
		forms=(parsed_html.find_all("form"))
		comments=parsed_html.find_all(string=lambda test:isinstance(test,Comment))
		password_type=parsed_html.find_all('input',{'name':'password'})

		if(config['forms']):
			for form in forms:
				if((form.get('action').find("https")<0) and (urlparse(url).scheme!='https')):
					report=""+"form issue:Insecure form action "+form.get('action')+" found in document!\n"

		if(config['comments']):
			for comment in comments:
				if(comment.find('key:')>-1):
					report+="Comment issue: key is found in the HTML comments,please remove it!\n"
	
		if(config['passwords']):
			for password in password_type:
				if(password.get('type')!='password'):
					report+="Input issue: Plain text password input found, Please change password type input!\n"

		#XSS vulnerability check
		report=xss_check(url,report)
	
	else:	
		fail="Invalid Url found!"
		return fail
	if report == "":
  		report="Nice job! Your HTML document is secure!"

	else:
  		header="Vulnerability Report is as follows:\n"
  		header+="==================================\n\n"
  		report=header+report
	return report

def xss_check(url,report):
	with open('xss-payload-list.txt','r') as f:
		for line in f:
			payload=line
			req = requests.post(url + payload)
			if payload in req.text:
				report+="XSS Vulnerablity discovered!"
				report+="Refer to XSS payloads for further escalation"
				return report
	report+="Secure from XSS Vulnerablity"
	return report
