#-*- coding:utf-8 -*-
import requests
import sys
from sys import argv
from bs4 import BeautifulSoup
import urllib  
import urllib2  
import json

def main(doctor_id,name):  
	data = {'name':name,'doctor_id':doctor_id,'main_desc':'test','url':'http://www.sina.com','hospital':'fuwai','room':'xinxueguan','rank':'yishi','level':0,'sex':'male','reservations':[{'support_number':5,'price_type':'love'},{'support_number':5,'price_type':'fee','price':5},{'support_number':5,'price_type':'plus','price':25}]   }
	url = "http://117.34.78.201:8081/doctors"
	req = urllib2.Request(url)
	req.add_header('Content-Type', 'application/json')
	response = urllib2.urlopen(req,json.dumps(data))
	result = response.read()
	print result

if __name__ == '__main__':  
	if len(sys.argv) != 3:
		print 'Usage: python input_name output_name'
		exit(1)
	doctor_id = sys.argv[1]
	name = sys.argv[2]
	main(doctor_id,name) 

