#!/usr/bin/python3
import optparse, os
try:
 import urllib.request as ul
 import ip_address, json
except ImportError:
 #print('Grant Us Root To Auto Install Required Modules!.')
 os.system('pip3 install ip_address')
 os.system(f'python3 {os.path.basename(__file__)}')
 exit(0)
parser = optparse.OptionParser()
parser.add_option('-t','--target',dest='ip',help='target ip')
(value, key) = parser.parse_args()
ipx = value.ip

class Tracer:
 def __init__(self, ip):
  self.ip = ip
		

 def trace(self):
  conv = ul.urlopen(f"http://ip-api.com/json/{self.ip}")
  read = conv.read()
  load = json.loads(read)
  res = f"""
  IP: {load['query']}
  Country: {load['country']}
  country code: {load['countryCode']}
  region: {load['region']}
  Region Name: {load['regionName']}
  City: {load['city']}
  zip code: {load['zip']}
  time zone: {load['timezone']}
  ISP: {load['isp']}
  org: {load['org']}
  as: {load['as']}
  latitude: {load['lat']}
  longitude: {load['lon']}"""
  return res

 def banner(self):
  print(f"""
=========================
 __  _______             |
 \\ \\/ /_   _|            |
  >  <  | |              |
 /_/\\_\\ |_|              |
                         |
X-Tracer By: Anikin Luke |
-------------------------|
Your Ip: {ip_address.get()}   |
=========================
result:""")


 def check(self):
  if self.ip is None:
   self.ip = input("\nip to trace: ")
   ip_trace.banner()
   print(ip_trace.trace())
  else:
   ip_trace.banner()
   print(ip_trace.trace())


if __name__=='__main__':
 ip_trace = Tracer(ipx)
 ip_trace.check()
