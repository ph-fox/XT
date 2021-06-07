#!/usr/bin/python3
import json, os, sys, publicip, optparse
import urllib.request as ul
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
		print(f"zip code: {load['zip']}")
		print(f"ISP: {load['isp']}")


	def check(self):
		if self.ip is None:
			self.ip = input("ip to trace: ")
			ip_trace.trace()
		else:
			ip_trace.trace()


if __name__=='__main__':
	ip_trace = Tracer(ipx)
	ip_trace.check()
