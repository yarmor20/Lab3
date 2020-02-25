import urllib.request, urllib.parse, urllib.error
import twurl
import json
import ssl

# https://apps.twitter.com/
# Create App and get the four strings, put them in hidden.py

TWITTER_URL = 'https://api.twitter.com/1.1/friends/list.json'

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE


def get_info_by_nickname(user):
    """
    Return user dict from Twitter API
    :param user: (str)
    :return: dict = { users(str): (list(dict)), ...}
    """
    acct = user
    url = twurl.augment(TWITTER_URL,
                        {'screen_name': acct, 'count': '15'})
    connection = urllib.request.urlopen(url, context=ctx)
    data = connection.read().decode()

    js = json.loads(data)
    return js
