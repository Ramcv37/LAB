import requests
import argparse
import json

# Define the API endpoint URL
API_URL = "https://www.travel-advisory.info/api"

def lookup_country_by_code(country_code, data):
    for iso_code, country_data in data['data'].items():
        if country_data['iso_alpha2'] == country_code:
            return country_data['name']

    return "Country code not found"

def main():
    parser = argparse.ArgumentParser(description="Lookup country names by country code")
    parser.add_argument("--countryCodes", nargs='+', help="One or more country codes to lookup")
    parser.add_argument("--loadFromFile", action="store_true", help="Load data from a file instead of the API")
    args = parser.parse_args()

    # Load data from a file or the API
    if args.loadFromFile:
        with open('data.json', 'r') as file:
            data = json.load(file)
    else:
        response = requests.get(API_URL)
        data = response.json()
        with open('data.json', 'w') as file:
            json.dump(data, file, indent=4)

    if args.countryCodes:
        for country_code in args.countryCodes:
            country_name = lookup_country_by_code(country_code.upper(), data)
            print(f"{country_code}: {country_name}")

if __name__ == "__main__":
    main()
