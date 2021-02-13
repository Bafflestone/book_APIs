"""JSON API Exercise 2
Write a Python script that:
- Pages through the endpoint below
- Extends an author_list variable with each page of author data
- Stops paging when either:
o There are no more authors
o 15 pages have been processed
- Tells the user which condition above stopped the loop
- Prints the author_list variable
Starting endpoint: https://jsonapiplayground.reyesoft.com/v2/authors?page%2525255b
size%2525255d=10&page%2525255bnumber%2525255d=1"""

import requests

URL_TEMPLATE = 'https://jsonapiplayground.reyesoft.com/v2/authors?page[size]=10&page[number]={page_num}'
FAILED = 1


def get_author_list(page_limit):

    page_list = range(1, page_limit + 1)
    authors_list = []

    for page_num in page_list:
        url = URL_TEMPLATE.format(page_num=page_num)
        authors_return = requests.get(url)
        if authors_return.status_code != 200:
            return FAILED
        next_page = authors_return.json()
        page_author_data = next_page['data']

        # Check whether there is no data on the page and return if it's empty.
        if not page_author_data:
            message = "No more authors to process on page {page_num}, ending connection."
            print(message.format(page_num=page_num))
            return authors_list

        authors_list += page_author_data

        # If we are on the end page provided then we exit.
        if page_num == page_limit:
            message = "Reached end page provided {page_num}," \
                      " you may not have all author data, ending connection."
            print(message.format(page_num=page_num))
            return authors_list


if __name__ == '__main__':
    print(get_author_list(15))
