#!/usr/bin/python3
"""
Write a recursive function that queries the Reddit API and returns a list
containing the titles of all hot articles for a given subreddit.
If no results are found for the given subreddit,
the function should return None.
"""
import json
import pprint
import requests
import sys

headers = {
    'User-Agent': 'My User Agent 1.0'
}
after = None


def recurse(subreddit, hot_list=[]):
    """function that returns a list with the titles of all hot articles"""
    try:
        url = 'https://www.reddit.com/r/'
        global after
        if after:
            response = requests.get(url + subreddit + "/hot.json?after=" +
                                    after, headers=headers,
                                    allow_redirects=False)
            # pprint.pprint(response.json())
        else:
            response = requests.get(url + subreddit + "/hot.json",
                                    headers=headers, allow_redirects=False)
            # pprint.pprint(response.json())
        after = response.json()['data']['after']
        hot_list += [element['data']['title'] for element in response.
                     json()['data']['children']]
        if after:
            return recurse(subreddit, hot_list)
        return hot_list
    except:
        return None
