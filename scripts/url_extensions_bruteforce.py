import argparse
import requests
from extensions_list import EXTENSIONS


BASE_URL = "http://localhost:8003"

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
    if response.status_code != 404:
        print(f"Something found in: {url}")
