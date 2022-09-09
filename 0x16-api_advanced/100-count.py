#!/usr/bin/python3
"""
Module for storing the count_words function.
"""
import requests

get = requests.get
url = 'https://www.reddit.com/r/{}/hot.json'
user_agent_str = ('Mozilla/5.0 (Windows NT 6.1; WOW64; rv:77.0)'
                  'Gecko/20190101 Firefox/77.0')
user_ag = {'User-Agent': user_agent_str}
payload_default = {'limit': 100}


def count_words(subreddit, word_list, payload={}, hot_list=[]):
    """
    Prints the count of the given words present in the title of the
    subreddit's hottest articles.
    """
    url = url.format(subreddit)

    if payload == {}:
        payload = payload_default

    request = get(url, headers=user_ag)

    if (request.status_code == 404):
        return

    request = get(url, headers=user_ag, params=payload)
    request_data = request.json().get('data')

    post_page = request_data.get('children')
    hot_list.extend([post.get('data').get('title') for post in post_page])

    if (request_data.get('after') is not None):
        payload = {
            'after': request_data.get('after'),
            'limit': 100
        }
        return count_words(subreddit, word_list, payload, hot_list)

    word_list = [word.lower() for word in word_list]
    freq_dict = {word: 0 for word in word_list}
    for title in hot_list:
        title_words = title.lower().split(' ')
        for word in word_list:
            freq_dict[word] += title_words.count(word)

    freq_list = [(key, val) for key, val in freq_dict.items() if val != 0]

    for entry in sorted(freq_list, key=lambda x: (-x[1], x[0])):
        print("{}: {}".format(entry[0], entry[1]))
