import requests
#i will need to create get and post requests
#in get i need (url,params=meta data for the input)
r_get = requests.get(url="http://192.168.1.223:8080/data_receiver",params={"Name":"Dlayel"}) #this is the local host of my device that i got from typing ipconfig getifaddr en0 in my terminal
print(r_get.text)
r_post =requests.post(url="http://192.168.1.223:8080/data_receiver",json={"Name":"Shahad"}) #url=https/localhost:port/endpoint
print(r_post.text)