""""JSON API Exercise 3
Write a Python function that:
- Accepts an author_id parameter
- Sends a GET request to https://jsonapiplayground.reyesoft.com/v2/authors/{author_id}
- Parses the JSON response
- Returns a single dictionary containing:
o The author name in a “name” key
o The number of books they have written in a “book_count” key
- Raises a meaningful exception if the author_id is not found
For bonus points, write a unit test to prove that your function raises the expected exception
if author_id is not found. You will need to mock the API response to achieve this."""

import requests
import unittest
from urllib.error import URLError

URL_TEMPLATE = 'https://jsonapiplayground.reyesoft.com/v2/authors/{author_id}'
NOT_FOUND = 404
RETURN_OK = 200
FAILED = 'failed'
SUCCESS = 'success'


def get_author_by_id(author_id):

    url = URL_TEMPLATE.format(author_id=author_id)

    author_return = requests.get(url)
    author_json = author_return.json()

    if author_return.status_code != RETURN_OK:
        status = author_json['errors'][0]['status']
        message = f"Author not found for author_id {author_id} " \
                  f"status code {status} for url {url}"
        raise URLError(message)

    author_dict = {'name': author_json['data']['attributes']['name'],
                   'book_count': len(author_json['data']['relationships']['books']['data'])}

    return author_dict


class TestAuthors(unittest.TestCase):

    def test_exception(self):
        result = FAILED
        try:
            get_author_by_id("author")
        except URLError:
            result = SUCCESS
        self.assertEqual(result, SUCCESS)

    def test_author(self):
        self.assertEqual(get_author_by_id(1), {'name': 'Mr. Friedrich Walker Jr.', 'book_count': 0})


if __name__ == '__main__':
    unittest.main()
