import requests

#It provides details on how much shareholders are being paid and the currency used.

api_key = "gzRn7DddPG5GUpYiGBZuArfpIO8IFJLH"
api_url = "https://api.massive.com/"
api_query = f"v3/reference/dividends?apiKey={api_key}"   

api = api_url + api_query
# print(api)
headers = {
    "Authorization": "Bearer gzRn7DddPG5GUpYiGBZuArfpIO8IFJLH",
    "Host": "api.massive.com"
}
response = requests.get(url=api, headers=headers)
data_json = response.json()
if "results" in data_json:
    for item in data_json["results"]:
        print(f"ID: {item['id']} | Ticker: {item['ticker']} | Amount: {item['cash_amount']} | Record Date: {item['record_date']}")


with open("output.json","w") as f:
    f.write(response.text)
