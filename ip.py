#!/usr/bin/python3
import optparse, os
try:
 import urllib.request as ul
 import ip_address
 import json
except:
 #print('Grant Us Root To Auto Install Required Modules!.')
 os.system('pip3 install urllib.request, json, ip_address')
 import urllib.request as ul
 import ip_address
 import json
parser = optparse.OptionParser()
parser.add_option('-t','--target',dest='ip',help='target ip')
(value, key) = parser.parse_args()
ipx = value.ip

class Tracer:
	def __init__(self, ip):
		self.ip = ip
		

	def trace(self):
		#api = "http://ip-api.com/json/"
		conv = ul.urlopen(f"http://ip-api.com/json/{self.ip}")
		read = conv.read()
		load = json.loads(read)

		print("")
		print(f"IP: {load['query']}")
		print(f"Country: {load['country']}")
		print(f"country code: {load['countryCode']}")
		print(f"region: {load['region']}")
		print(f"Region Name: {load['regionName']}")
		print(f"City: {load['city']}")
		print(f"currency: {load['currency']}")
		print(f"zip code: {load['zip']}")
		print(f"ISP: {load['isp']}")
		print(f"proxy: {load['proxy']}")
		print(f"mobile: {load['mobile']}")
		print(f"org: {load['org']}")


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
			self.ip = input("ip to trace: ")
			ip_trace.banner()
			ip_trace.trace()
		else:
			ip_trace.banner()
			ip_trace.trace()


if __name__=='__main__':
	ip_trace = Tracer(ipx)
	ip_trace.check()
