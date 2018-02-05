import requests
import json
import datetime

now = datetime.datetime.now()

url = "https://api-wufthacks.xlabs.one:8243/LinkedinApi/1.0.0/v1/people/~:(id,num-connections,picture-url)"

querystring = {"oauth2_access_token":"AQWN_yqfE3REmcbO5QJJ-qJUzB7rHoB-jfn68Mv3j601eKY9X5Prcg9G637g22pwIKzKYwi0hVJ_3H0Jz2rIdffV28VzYKgJHhFoKmZjfoaoyohqbCKoMqgEDt-RapARV54fXfKpk3DotbkjpfXB2aIDDpFhw9LOEY9EzjVAwy6f8CwC8zHk2N_ha1h7Fu1QP5fQn8LsE-pMTFjse4IN1frrNZQpK03KbJgdGK0WY3IXemE2IN2LlKvOxCwyRf73kFR6IrxokPP73eV41woHlcbRWQfO9j14MqC5Fbj3PMvpS-4TwPR6xspeXrO3xVyAOrAUblENlgOhHLWxln-O-WF1vxRxRg","format":"json"}

headers = {
    'Accept': "application/json",
    'Authorization': "Bearer 4a0da130-f48f-3ea4-8f92-c54518ca86c3",
    'Cache-Control': "no-cache",
    'Postman-Token': "b4d5ccbe-465b-aff8-2b5d-15f517ca891c"
    }

response = requests.request("GET", url, headers=headers, params=querystring)
d1=json.loads(response.text)

url = "https://api-wufthacks.xlabs.one:8243/LinkedinApi/1.0.0/v1/people/~:(id,first-name,last-name,maiden-name,formatted-name,headline,location,industry,picture-url,positions,email-address,summary)"

querystring = {"oauth2_access_token":"AQWN_yqfE3REmcbO5QJJ-qJUzB7rHoB-jfn68Mv3j601eKY9X5Prcg9G637g22pwIKzKYwi0hVJ_3H0Jz2rIdffV28VzYKgJHhFoKmZjfoaoyohqbCKoMqgEDt-RapARV54fXfKpk3DotbkjpfXB2aIDDpFhw9LOEY9EzjVAwy6f8CwC8zHk2N_ha1h7Fu1QP5fQn8LsE-pMTFjse4IN1frrNZQpK03KbJgdGK0WY3IXemE2IN2LlKvOxCwyRf73kFR6IrxokPP73eV41woHlcbRWQfO9j14MqC5Fbj3PMvpS-4TwPR6xspeXrO3xVyAOrAUblENlgOhHLWxln-O-WF1vxRxRg","format":"json"}

headers = {
    'Accept': "application/json",
    'Authorization': "Bearer 4a0da130-f48f-3ea4-8f92-c54518ca86c3",
    'Cache-Control': "no-cache",
    'Postman-Token': "84d651a0-73c2-8fd0-dc4a-bcfd67525f18"
    }

response = requests.request("GET", url, headers=headers, params=querystring)


d2=json.loads(response.text)

connectNum = d1["numConnections"]
position = d2["positions"]
value = position["values"]
employed = False
summary = d2["summary"]
salaryTotal = 0
jobInfo=[]
for i in range(position["_total"]):
        job = value[i]
        if(job["isCurrent"]):
                employed = True
                endMonth = now.month
                endYear = now.year
                endDate = {
                        "month": endMonth,
                        "year": endYear
                }
                job["endDate"] = endDate
        else:
                endMonth = job["endDate"]["month"]
                endYear = job["endDate"]["year"]
        startMonth = job["startDate"]["month"]
        startYear = job["startDate"]["year"]
        totalMonth = endMonth - startMonth + 12 * (endYear - startYear)
        job["length"]=totalMonth
	
	#should get from glassdoor if we were partner company
        salary = 50000

        job["salary"] = salary
        salaryTotal += salary * totalMonth / 12.0
        jobInfo.append(job)
#print(jobInfo)

