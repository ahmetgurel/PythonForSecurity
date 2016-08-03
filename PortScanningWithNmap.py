# !/usr/bin/env python
# -*- coding:utf-8 -*-

# Nmap Setup --> http://xael.org/pages/python-nmap-en.html

try:
	import nmap
	import re
	import os
	import argparse
	import urllib2




except ImportError,e:
	import sys
	sys.stdout.write("%s\n" %e)
	sys.exit(1)



class Tarama:
	def __init__(self):
		self.cmd_arg = "-n -Pn -sS -sV -T4 --top-ports 10"
		self.nmap_services_file = "/usr/share/nmap/nmap-services"
		self.nm = nmap.PortScanner()

	def get_service_name(self, port, proto):
		nmap_file = open(self.nmap_services_file,"r")
		service = ""
		for line in nmap_file:
				if re.search("([^\s]+)\s%d/%s\s"% (port, proto), line):
					service = re.search("([^\s]+)\s%d/%s\s"% (port, proto), line).groups(1)[0]
					break
		return service


	def run_scan(self,targets):
		self.nm.scan(hosts = "%s"% targets, arguments = "%s"% self.cmd_arg)


		for host in self.nm.all_hosts():
			print "IP i ADRESINIZ",host
			print "\n"
			print("PORT     STATE     SERVICE")
			for proto in self.nm[host].all_protocols():
				result = self.nm[host][proto].keys()
				result.sort()

				for port in result:
						res = str(port) + "/" + proto
						space = str(" " * (9 - len(res)))
						service = self.get_service_name(port, proto)
						state = self.nm[host][proto][port]['state']
						space2 = str(" " * (10 - len(state)))
						print "%s/%s%s%s%s%s" % (port,proto,space,state,space2,service)


print "Domain Adresi :"
domain_name = raw_input("Domain adresi=")

if __name__ == "__main__":
	parser = argparse.ArgumentParser(description='Nmap Ile Port Tarama Programi')
	try:
			tarama = Tarama()
			tarama.run_scan(domain_name)
	except Exception, e:
			print >> sys.stderr, "Hata: %s"% e
			sys.exit(2)
