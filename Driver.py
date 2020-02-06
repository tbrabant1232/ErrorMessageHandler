import dash
import dash_core_components as dcc
import dash_html_components as html
import json as json
import csv
import urllib.request
import sys
from datetime import date

today = date.today()
# dateStr = today.strftime("%d-%b-%Y")
dateStr = today.isoformat()
csvfile = (dateStr + "raw.csv")

def get_responses(paths: list, fetch: str) -> list:
    output_list = []
    if fetch == 'file':
        for path in paths:
            handle = open(path.strip('\n'), 'r')
            output_list.append(handle)
    elif fetch == 'url':
        for path in paths:
            handle = get_url_response(path)
    else:
        raise ValueError("Unsupported Fetch type")
    return output_list


def get_url_response(url: str):
    return url


def get_error_from_json(handle):
    json_object = json.load(handle)
    errors = list(find_json("error_message", json_object))
    if errors:
        return errors


def get_json_paths(path: str):
    handle = open(path, 'r')
    lines = handle.readlines()
    return lines


def find_json(key, collection):
    bad_chars = [',', "\"", "\n"]
    if isinstance(collection, dict):
        for k in collection.items():
            if k[0] == key:
                yield k[1]
            elif isinstance(k[1], dict):
                for result in find_json(key, k[1]):
                    yield result
            elif isinstance(k[1], list):
                for d in k[1]:
                    for result in find_json(key, d):
                        yield result
    elif isinstance(collection, list):
        for value in collection:
            for r in find_json(key, value):
                for i in bad_chars :
                    r = r.replace(i, '')
                yield r


def main():
    paths = get_json_paths('Resources\links.txt')
    responses = get_responses(paths, 'file')
    errors = []
    for response in responses:
        errors.append(get_error_from_json(response))
    print(errors)

    res = []
    for val in errors:
        if val != None :
            res.append(val)

    with open(csvfile, 'w') as file:
     writer = csv.writer(file, escapechar='\\', delimiter="\n", quoting=csv.QUOTE_NONE,)
     writer.writerow(["Error"])
     writer.writerows(res)
    print("Created csv file", csvfile)


if __name__ == "__main__":
    main()
