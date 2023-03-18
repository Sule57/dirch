# Dirch (Directory Search) is a simple python tool for discovering directories on a website
# Created by github.com/sule57

import time
import requests
import argparse
import sys
import requests

print()
print()
print("-------------------------------------------------------------")
print("Welcome to dirch.py - A directory discovery tool")
print("Created by github.com/sule57")
print("-------------------------------------------------------------")

parser = argparse.ArgumentParser(description="A simple directory checker")
parser.add_argument("-u", "--url", help="The url to check", required=True)
parser.add_argument("-w", "--wordlist", help="The wordlist to use", required=False)
parser.add_argument("-d", "--delay", help="Add delay between requests", required=False)
# TODO: Custom headers
args = parser.parse_args()

# If a wordlist is passed use it, if not use the default wordlist
# Default Wordlist: https://github.com/v0re/dirb/blob/master/wordlists/common.txt

if args.wordlist:
    wordlist = args.wordlist
    print("Using wordlist: " + wordlist)
    print("-------------------------------------------------------------")
else:
    wordlist = "./dirch-default.txt"
    print ("No wordlist passed, using common.txt by Marc Rivero López: ")
    print("-------------------------------------------------------------")

print()

# Check if the url passed is valid, if not print out an error message saying
# "The url is not valid please use formatting like https://example.com"
try:
    url = args.url
    requests.get(url)
except requests.exceptions.MissingSchema:
    print("[Error] The url is not valid please use formatting like https://example.com")
    sys.exit()

# If the user passes a delay, use it, if not use 0
if args.delay:
    delay = args.delay
else:
    delay = 0

# Check if the value passed is a number, if not print out an error message saying
# "The delay must be a number"
try:
    delay = int(delay)
    print("[Info] Delay between requests: " + str(delay) + "ms")
    print()
except ValueError:
    print("[Error] The delay must be a number")
    sys.exit()

# Sends a request to each subdirectory in the wordlist, if status codes are 200, 301, 303, 403, 405, 408, 412, 451, 500, 508, 511, print out the url
# If at any point the user presses ctrl + C exit the program
def send_request():
    codes = [200, 301, 303, 403, 405, 408, 412, 451, 500, 508, 511]
    try:
        with open(wordlist) as f:
            for line in f:
                word = line.strip()

                # If the word starts with a "/"" remove it
                if word.startswith("/"):
                    word = word[1:]

                full_url = f"{url}/{word}"
                response = requests.get(full_url)
                if response.status_code in codes:
                    print(f"[Info] Found: {full_url}" + "  |  " + str(response.status_code) + "  |  " + response.reason + "  |")
                
                # If the user passes a delay, wait that amount of miliseconds before sending the next request
                if delay != 0:
                    time.sleep(delay / 1000)
                    
    except KeyboardInterrupt:
        print()
        print("Exiting...")
        sys.exit()

send_request()
print()