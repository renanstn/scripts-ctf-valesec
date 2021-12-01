import argparse
import requests
from extensions_list_simplified import EXTENSIONS


BASE_URL = "https://valesecconf.com.br/786745433234434322"

parser = argparse.ArgumentParser(
    description="Bruteforce URL trying various extensions"
)
parser.add_argument(
    "word", help="The world to be bruteforced"
)

args = parser.parse_args()
word = args.word

for extension in EXTENSIONS:
    url = f"{BASE_URL}/{word}.{extension}"
    response = requests.get(url)
    print(f"Trying: {url}")
    print(response.status_code)
