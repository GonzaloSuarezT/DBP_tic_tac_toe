import http.client
import json

data={"username":"gonzalo","password":"1234"}

conn = http.client.HTTPConnection("127.0.0.1",5000)

conn.request("GET", "/players")

response  =  conn.getresponse()

print("Status:", response.status)

print("Response:", response.read().decode())

conn.request("GET","/players/id")

response  =  conn.getresponse()

print("Status:", response.status)

print("Response:", response.read().decode())


json_data=json.dumps(data)
headers={"Content-type":"application/json"}

conn.request("POST","/players/add",body=json_data,headers=headers)

response  =  conn.getresponse()

print("Status:", response.status)

print("Response:", response.read().decode())

conn.request("GET", "/players")

response  =  conn.getresponse()

print("Status:", response.status)

print("Response:", response.read().decode())

conn.close()
