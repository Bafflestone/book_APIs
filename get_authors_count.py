"""JSON API Exercise 1
Write a Python script that:
- Sends a GET request to https://jsonapiplayground.reyesoft.com/v2/authors?page[size]=10
- Parses the JSON response
- Prints a list of dictionaries containing:
o Each author’s name in a “name” key
o The number of books they have written in a “book_count” key """


import requests
import json

URL1 = 'https://jsonapiplayground.reyesoft.com/v2/authors?page[size]=10'
FAILED = 1


def get_authors_count():

    authors = requests.get(URL1)

    if authors.status_code != 200:
        return FAILED

    authors_dict = json.loads(authors.text)
    output_list = []
    for item in authors_dict['data']:
        count_dict = {'name': item['attributes']['name'],
                      'book_count': len(item['relationships']['books']['data'])}
        output_list.append(count_dict)
    return output_list


if __name__ == '__main__':
    print(get_authors_count())
