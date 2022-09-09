#!/usr/bin/python3
"""
1. Top Ten
"""
import requests


def top_ten(subreddit):
    """
    function that queries the Reddit API
    and prints the titles of the first 10
    hot posts listed for a given subreddit."""

    if not subreddit:
        print("None")

    url = "https://www.reddit.com/r/{}/hot.json?limit=10".format(subreddit)
    headers = {"User-Agent":
               "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:47.0)\
                    Gecko/20100101 Firefox/47.0"}

    res = requests.get(url, headers=headers)
    if res.status_code == 200:
        data = res.json()['data']['children']
        [print(post['data']['title']) for post in data]
    elif res.status_code == 404:
        print("None")
