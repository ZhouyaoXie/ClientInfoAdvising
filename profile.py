import requests
import xml.etree.ElementTree as ET
import json
import datetime
now = datetime.datetime.now()

url = "https://api-wufthacks.xlabs.one:8243/td/userprofile/V1.0.0/profile"

headers = {
    'Accept': "application/json",
    'X-Api-Key': "eyJhbGciOiJIUzUxMiJ9.eyJzdWIiOiJzdGVwaGFuam9lMTU0IiwiZXhwIjoxNTE4NTUyOTUyfQ.ALqPYoE_JtblCyuXMFXSDhWcGgmBBG14u4B-9J5nrmvoTmU3Rhrl3nodmCIq7G6J9eHNP1F641DVU3qheND6-A",
    'Authorization': "Bearer 4a0da130-f48f-3ea4-8f92-c54518ca86c3",
    'Cache-Control': "no-cache",
    'Postman-Token': "28fde2bb-203f-3c43-041f-c07a7c323b3a"
    }

response = requests.request("GET", url, headers=headers)
profile = json.loads(response.text)

url = "http://www.zillow.com/webservice/GetSearchResults.htm"

querystring = {"zws-id":"X1-ZWz1g8ajhqs7wr_a2eph","address":"2114+Bigelow+Ave","citystatezip":"Seattle, WA"}

headers = {
    'Cache-Control': "no-cache",
    'Postman-Token': "9c3e59c3-a0d6-18de-655c-3a9374ae52e8"
    }

response = requests.request("GET", url, headers=headers, params=querystring)


root = ET.fromstring(response.text)
housePrice = root[2][0][0][3][0].text
houseLow = root[2][0][0][3][4][0].text
houseHigh = root[2][0][0][3][4][1].text

forename = profile["person"]["forename"]
lastname = profile["person"]["lastname"]
birthstamp = profile["person"]["dateOfBirth"]
birthDay = datetime.datetime.fromtimestamp(int(birthstamp)/100).strftime('%Y-%m-%d %H:%M:%S')
age=now.year - datetime.datetime.fromtimestamp(int(birthstamp)/100).year - 1
married = profile["person"]["maritalStatus"]
sex = profile["person"]["sex"]
