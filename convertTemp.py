#this isn't the cleanest code but it works

import json 
import sys
import re

query = sys.argv[1].lower()
alfred_results = []

match = re.match('(\d+)([cfkr]$)', query)

if(match != None):
	groups = match.groups()
	temp = (int(groups[0]))
	unit = (groups[1])
	
	if(unit == 'f'):
		# alfred doesn't like fractions for some reason. this approximation is dirty but it works
		celsius = round(((temp-32)*(0.5555555555555555))*100)/100
		kelvin = round(((temp+459.67)*(0.5555555555555555))*100)/100
		rankine = round((temp+459.67)*100)/100
		
		alfred_results = [{
			"title": str(celsius)+"C",
			"arg": str(celsius)
		}, {
			"title": str(kelvin)+"K",
			"arg": str(kelvin)
		}, {
			"title": str(rankine)+"R",
			"arg": str(rankine)
		}, {
			"title": "Copy All",
			"subtitle": str(temp)+"F: "+str(celsius)+"C, "+str(kelvin)+"K, "+str(rankine)+"R",
			"arg": str(temp)+"F: "+str(celsius)+"C, "+str(kelvin)+"K, "+str(rankine)+"R"
		}]
	elif(unit == 'c'):
		fahrenheit = round(((temp*(1.8))+32)*100)/100
		kelvin = round((temp+273.15)*100)/100
		rankine = round(((temp+273.15)*(1.8))*100)/100
		alfred_results = [{
			"title": str(fahrenheit)+"F",
			"arg": str(fahrenheit)
		}, {
			"title": str(kelvin)+"K",
			"arg": str(kelvin)
		}, {
			"title": str(rankine)+"R",
			"arg": str(rankine)
		}, {
			"title": "Copy All",
			"subtitle": str(temp)+"C: "+str(fahrenheit)+"F, "+str(kelvin)+"K, "+str(rankine)+"R",
			"arg": str(temp)+"C: "+str(fahrenheit)+"F, "+str(kelvin)+"K, "+str(rankine)+"R"
		}]
	elif(unit == 'k'):
		fahrenheit = round(((temp*(1.8))-459.67)*100)/100
		celsius = round((temp-273.15)*100)/100
		rankine = round((temp*(1.8))*100)/100
		alfred_results = [{
			"title": str(fahrenheit)+"F",
			"arg": str(fahrenheit)
		}, {
			"title": str(celsius)+"C",
			"arg": str(celsius)
		}, {
			"title": str(rankine)+"R",
			"arg": str(rankine)
		}, {
			"title": "Copy All",
			"subtitle": str(temp)+"K: "+str(fahrenheit)+"F, "+str(celsius)+"C, "+str(rankine)+"R",
			"arg": str(temp)+"K: "+str(fahrenheit)+"F, "+str(celsius)+"C, "+str(rankine)+"R"
		}]
	else:
		fahrenheit = round((temp-459.67)*100)/100
		celsius = round(((temp-491.67)*(0.5555555555555555))*100)/100
		kelvin = round((temp*(0.5555555555555555))*100)/100
		alfred_results = [{
			"title": str(fahrenheit)+"F",
			"arg": str(fahrenheit)
		}, {
			"title": str(celsius)+"C",
			"arg": str(celsius)
		}, {
			"title": str(kelvin)+"K",
			"arg": str(kelvin)
		}, {
			"title": "Copy All",
			"subtitle": str(temp)+"R: "+str(fahrenheit)+"F, "+str(celsius)+"C, "+str(kelvin)+"K",
			"arg": str(temp)+"R: "+str(fahrenheit)+"F, "+str(celsius)+"C, "+str(kelvin)+"K"
		}]
	response = json.dumps({
		"items": alfred_results
	})
	
	sys.stdout.write(response)
else:
	alfred_results = [{
			"title": "Invalid Temp",
			"subtitle": "Enter a valid temp."
		}]
	response = json.dumps({
		"items": alfred_results
	})
	
	sys.stdout.write(response)