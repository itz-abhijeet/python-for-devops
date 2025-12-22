import requests
import json

def get_usd_shareholders_data(url, headers):
    try:
        response = requests.get(url=url, headers=headers, timeout=10)
        response.raise_for_status() 
        
        data_json = response.json()
        filtered_results = []

        if "results" in data_json and isinstance(data_json["results"], list):
            for item in data_json["results"]:
                records = {
                    "id": item.get('id', '0'),
                    "ticker": item.get('ticker', 'N/A'),
                    "cash_amount": item.get('cash_amount', '0'),
                    "record_date": item.get('record_date', 'N/A')
                }

                print(f"ID: {records['id']} | Ticker: {records['ticker']} | Amount: {records['cash_amount']} | Record Date: {records['record_date']}")

                filtered_results.append(records)
        else:
            print("No results found in the response.")

        with open("output.json", "w") as f:
            json.dump(filtered_results, f, indent=4)
        print("\nSuccessfully saved data to output.json")

    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
    except requests.exceptions.ConnectionError:
        print("Error: Could not connect to the server. Check your internet.")
    except json.JSONDecodeError:
        print("Error: Failed to parse API response as JSON.")
    except Exception as err:
        print(f"An unexpected error occurred: {err}")

if __name__ == "__main__":
    api_key = "gzRn7DddPG5GUpYiGBZuArfpIO8IFJLH" 
    base_url = "https://api.massive.com/v3/reference/dividends"
    
    request_headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }

    get_usd_shareholders_data(base_url, request_headers)