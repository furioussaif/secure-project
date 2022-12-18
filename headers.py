from urllib.request import urlopen, Request
import re
import time

class colors:
	def __init__(self):
	        self.green = "\033[92m"
	        self.blue = "\033[94m"
	        self.bold = "\033[1m"
	        self.yellow = "\033[93m"
	        self.red = "\033[91m"
	        self.end = "\033[0m"
ga = colors()


class HTTP_HEADER:
    HOST = "Host"
    SERVER = "Server"

def headers_reader(url):
	print(" \n [!] Fingerprinting the backend Technologies.")
	with urlopen(Request(url, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:22.0) Gecko/20100101 Firefox/22.0'})) as opener:
		pass
	if opener.code == 200:
		 print(" [!] Status code: 200 OK")
	if opener.code == 404 or opener.code ==400:
		 print(" [!] Page was not found! Please check the URL \n")
		 exit()
	Server = opener.headers.get(HTTP_HEADER.SERVER)
	Host = url.split("/")[2]
	print(f" [!] Host: {str(Host)}")
	print(f" [!] WebServer: {str(Server)}")
	for item in opener.headers.items():
	    for powered in item:
	    	sig = "x-powered-by"		
	    	if sig in item:
	    		print(f" [!] {str(powered).strip()}")
