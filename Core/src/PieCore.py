import http.client

conn = http.client.HTTPSConnection("apidojo-yahoo-finance-v1.p.rapidapi.com")

headers = {
    'x-rapidapi-key': "ccb236ec50mshf31a65d277861d4p1ba219jsn581dea6fde36",
    'x-rapidapi-host': "apidojo-yahoo-finance-v1.p.rapidapi.com"
    }

conn.request("GET", "/auto-complete?q=tesla&region=US", headers=headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8")) 