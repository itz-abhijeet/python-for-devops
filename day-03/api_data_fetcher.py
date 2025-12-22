import requests
import json

def get_usd_shareholders_data(url, headers):
    try:
        response = requests.get(url=url, headers=headers)
        response.raise_for_status
        data_json = response.json()
        filtered_results = []

        if "results" in data_json:
            for item in data_json["results"]:
                records = {
                    "id" : item.get('id', '0'),
                    "ticker" : item.get('ticker', 'N/A'),
                    "cash_amount" : item.get('cash_amount', '0'),
                    "record_date" : item.get('record_date', 'N/A')
                }

                print(f"ID: {records["id"]} | Ticker: {records["ticker"]} | Amount: {records["cash_amount"]} | Record Date: {records["cash_amount"]}")

                filtered_results.append(records)
        else:
            print("No results found")

        with open("output.json","w") as f:
            json.dump(filtered_results, f, indent=4)

    except PermissionError as perm_err:
        print(f"Error: {perm_err}")
    except Exception as err:
        print(f"Unexpected error occured: {err}")
        

if __name__ == "__main__":

    api_key = "gzRn7DddPG5GUpYiGBZuArfpIO8IFJLH" 
    base_url= "https://api.massive.com/v3/reference/dividends"
    headers = {
        "Authorization": f"Bearer {api_key}",
    }

    get_usd_shareholders_data(base_url, headers)
