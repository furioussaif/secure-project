import urllib
from headers import *
from vulnz import *

print('Secure E-Commerce Project')

def urls_or_list():
	url = input(" [!] Enter the URL: ")
	if "?" in url:
		rce_func(url)
		xss_func(url)
		error_based_sqli_func(url)
		insecure_direct_obj_ref(url)
		broken_authentication(url)
	else:
		print(f"\n [Warning] {url} is not a valid URL")		
		print(f" [Warning] You should write a Full URL .e.g http://site.com/page.php?id=value \n")
		exit()
if __name__ == '__main__':
	urls_or_list()





