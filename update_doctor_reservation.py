#-*- coding:utf-8 -*-
import requests
import sys
from sys import argv
from bs4 import BeautifulSoup
import urllib  
import urllib2  

def main(doctor_id,price_type,price):  
	payload = {'price_type':price_type,'price':price,'support_number':'20','remark':'hi'}
	url = "http://117.34.78.201:8081/"+doctor_id+"/update_doctor_reservation"
	headers = { "Accept":"text/html,application/xhtml+xml,application/xml;",
            "Accept-Encoding":"gzip",
            "Accept-Language":"zh-CN,zh;q=0.8",
            "Referer":"http://www.example.com/",
            "User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.90 Safari/537.36"
            }
	data = urllib.urlencode(payload)
	req = urllib2.Request(url, data)
	response = urllib2.urlopen(req)
	result = response.read()
	print result

if __name__ == '__main__':  
	if len(sys.argv) != 4:
		print 'Usage: python input_name output_name'
		exit(1)
	doctor_id = sys.argv[1]
	price_type = sys.argv[2]
	price = sys.argv[3]
	main(doctor_id,price_type,price) 

