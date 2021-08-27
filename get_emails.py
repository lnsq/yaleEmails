import requests
import json
import argparse
import sys

from bs4 import BeautifulSoup
import collections

# {"filters": {"school_code": ["YC"], "year": 2025}}

def flatten(x):
    if isinstance(x, dict) :
        return [x]
    elif isinstance(x, collections.abc.Iterable) :
        return [a for i in x for a in flatten(i)]
    else:
        return [x]

def parse(response):
    S = BeautifulSoup(response, 'html.parser')
    s = str(S)
    s = s.replace('null', 'None')
    s = s.replace('false', 'False')
    s = s.replace('true', 'True')
    res = list(eval(str(s)))
    get_list = flatten(res)

    emails = []
    for name in get_list :
        emails.append(name['email'])

    return emails

def main(args):
    if not args.token and not args.payload:
        print("Require authorization token and payload request json file.")
        return
    api_url = "https://yalies.io/api/people"
    headers = {"Authorization": "Bearer %s" %args.token}

    with open(args.payload) as json_file:
        payload = json.load(json_file)
        response = requests.post(api_url, json = payload, headers = headers)
    emails = parse(response.text)
    for email in emails:
        print(email, file = sys.stdout, end = '\n')

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-t", "--token", type=str, help="Bearer Token created from yalies.io")
    parser.add_argument("-p", "--payload", type=str, help="Payload .json file -- see repo for example or go to https://yalies.io/apidocs")
    args = parser.parse_args()

    main(args)