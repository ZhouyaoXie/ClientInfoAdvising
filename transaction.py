import requests
import json

url = "https://api-wufthacks.xlabs.one:8243/td/transaction/V1.0.0/transaction/all"

querystring = {"page":"1","size":"10"}

headers = {
    'Accept': "application/json",
    'X-Api-Key': "eyJhbGciOiJIUzUxMiJ9.eyJzdWIiOiJzdGVwaGFuam9lMTU0IiwiZXhwIjoxNTE4NTUyOTUyfQ.ALqPYoE_JtblCyuXMFXSDhWcGgmBBG14u4B-9J5nrmvoTmU3Rhrl3nodmCIq7G6J9eHNP1F641DVU3qheND6-A",
    'Authorization': "Bearer 4a0da130-f48f-3ea4-8f92-c54518ca86c3",
    'Cache-Control': "no-cache",
    'Postman-Token': "1bc6c556-c863-6c95-ff84-075c625a8e7d"
    }

response = requests.request("GET", url, headers=headers, params=querystring)

profile = json.loads(response.text)
content = profile["content"]
debit = 0;
credit = 0;
for item in content:
	if item["method"] == "DEBIT":
		debit += item["amount"]
	elif item["method"] == "CREDIT":
		credit += item["amount"]

ratio = debit/credit

if __name__ == "__main__":
	print(debit)
	print(credit)
	print(ratio)