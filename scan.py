import os
from colorama import Fore, Back, Style
from turtle import color

if os.name == "td":
	os.system("cls")
else:
	os.system("clear")

def tool1():
	mylist = input("Select List: : ")
	try:
		hosts = open(mylist,"r").read().splitlines()
		for host in hosts:
			print("Scann => " + host)
			try:
				r = requests.get("http://api.hackertarget.com/reverseiplookup/?q=" + host)
				if "error check your search parameter" in r.text or "No DNS A records" in r.text: 
					print("Bad --> " + host)
				elif "API count exceeded" in r.text:
					print("API count exceeded! Change your IP with VPN!") 
					input()
				else: 
					sites = r.text
					sites = sites.replace("webmail.", "")
					sites = sites.replace("mail.", "")
					sites = sites.replace("cpanel.", "")
					sites = sites.replace("whm.", "")
					sites = sites.replace("www.", "")
					sites = sites.replace("autodiscover.", "")
					sites = sites.replace("webdisk.", "")
					sites = sites.replace("ns.", "")
					sites = sites.replace("ns1.", "")
					sites = sites.replace("ns2.", "")
					sites = sites.replace("admin.", "")
					sites = sites.replace("hostmaster.", "")
					sites = sites.replace("smtp.", "")
					sites = sites.replace("smtp2.", "")
					sites = sites.replace("cdn.", "")
					sites = sites.replace("cloud.", "")
					sites = sites.replace("whois.", "")
					with open("ip.txt","a") as f:
						f.write(sites + "\n")
					lines_seen = set()
					outfile = open('DomainScan.txt', "a")
					infile = open('ip.txt', "r")
					for line in infile:
						print(line)
						if line not in lines_seen:
							outfile.write(line)
							lines_seen.add(line)
					outfile.close()
					infile.close()
					if os.name == "td":
						os.system("del ip.txt")
					else:
						os.system("rm -rf ip.txt")
			except:
				pass
	except:
		print("File not found!")
		
		
def about():
	
	print(Fore.GREEN + """ 
		[#] Make by Drake Lam     
		[#] Website: https://drakelam.net/
		[#] Contact : github.com/drakelam/Scan-Domain 
	"""
	)

print(Fore.RED + """

			██████╗ ██████╗  █████╗ ██╗  ██╗███████╗    ██╗      █████╗ ███╗   ███╗
			██╔══██╗██╔══██╗██╔══██╗██║ ██╔╝██╔════╝    ██║     ██╔══██╗████╗ ████║
			██║  ██║██████╔╝███████║█████╔╝ █████╗      ██║     ███████║██╔████╔██║
			██║  ██║██╔══██╗██╔══██║██╔═██╗ ██╔══╝      ██║     ██╔══██║██║╚██╔╝██║
			██████╔╝██║  ██║██║  ██║██║  ██╗███████╗    ███████╗██║  ██║██║ ╚═╝ ██║
			╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝╚══════╝    ╚══════╝╚═╝  ╚═╝╚═╝     ╚═╝
                                                                       
[#] Make by Drake Lam     
[#] Website: https://drakelam.net/
[#] Contact : github.com/drakelam/Scan-Domain                           
""")

try:
	import requests
except:
	print("[-] It looks like you haven't installed the required credentials. You can refer to github.com/drakelam  - README.md")
	
tool = input("[1] Scanner\n[2] About\n\nSelect : ")
if tool == "1":
	tool1()
elif tool == "2":
	about()
else:
	pass