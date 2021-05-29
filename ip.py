#!/usr/bin/python3
#Coded By: Anikin Luke

try:
 import json, urllib.request, os, sys
 import ip_address as pip
except:
 pip3 install json, urllib.requests, ip_address
 import json, urllib.request, os, sys
 import ip_address as pip
 
print("""
██   ██    ████████ 
 ██ ██      ██    
  ███  █████ ██    
 ██ ██     ██    
██   ██      ██    
                  
smart-ip-tracer
by: Anikin Luke
""")
public_ip = pip.get()
print("==================>")
print(f"your ip: {public_ip}")
print("==================>\n")

ui = input("ip to trace: ")

api = "http://ip-api.com/json/"
req = urllib.request.urlopen(api + ui)
reader = read.read()
conv = json.loads(reader)

print("")
print("IP: " + conv["query"])
print("Country: " + conv["country"])
print("country code: " + conv["countryCode"])
print("region: " + conv["region"])
print("Region Name: " + conv["regionName"])
print("City: " + conv["city"])
print("zip code: " + conv["zip"])
print("ISP: " + conv["isp"])



