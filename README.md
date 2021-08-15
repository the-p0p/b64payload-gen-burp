# b64payload-gen-burp
Have a multiline payload in burp with an lfi? You want to quickly run through an lfi list in intruder to see what hits back?<br /> 
This script lets you modify one section of the payload to include your wordlist, then base64 encodes it so that when you run intruder you can just add the b64 decode action per payload to get the multiline payload back with the modified section.<br /> 

NOTE: There is probably a native way to do this...
