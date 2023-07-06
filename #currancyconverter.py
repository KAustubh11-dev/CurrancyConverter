#currancyconverter
import requests
import json


while True:
    Y = input("Welcome to currancy COnvereter : \n press enter to continue " )
    
    from_Currency=input("From:")
    to_Currency=input("To:")
    amount = int(input('amount :'))

    url =f"http://data.fixer.io/api/latest?access_key=251ed1c9781fef2288bbfd96bfccdfa5"
    responce =requests.get(url)

    rdic = json.loads(responce.text)
    C1 = rdic["rates"][from_Currency]
    C2 = rdic["rates"][to_Currency]

    temp1= (amount/C1)*C2

    print(round(temp1,2))
    from_rate = responce.json 

    
            





