#Coded by: Anikin Fuckin Luke xD
#Coded By: Anikin Luke
import json, urllib2, os, sys

os.system("python3 banner/shit.py")

your = raw_input("ip to trace: ")

ass = "http://ip-api.com/json/"
hole = urllib2.urlopen(ass + your)
fuck = hole.read()
you = json.loads(fuck)

print("")
print("IP: " + you["query"])
print("Country : " + you["country"])
print("country code: " + you["countryCode"])
print("region: " + you["region"])
print("Region Name: " + you["regionName"])
print("ISP: " + you["isp"])



