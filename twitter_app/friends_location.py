import folium
import geopy
import ssl
from twitter2 import get_info_by_nickname

# Ignore SSL certificate errors
ssl._create_default_https_context = ssl._create_unverified_context


def get_friends(json_dict):
    """
    Return list of users' location and screen name
    :param json_dict: dict = { users(str): (list(dict)), ...}
    :return: list = [list[str, str], ...]
    """
    users = []
    for user in json_dict['users']:
        users.append([user['location'].split(', ')[0], user['screen_name']])
    return users


def map_locations(users):
    """
    Return map
    :param users: dict = {tuple(float, float): list(str), ...}
    :return: map
    """
    location_map = folium.Map(location=[40.730610, 73.935242], zoom_start=2)
    fg = folium.FeatureGroup(name="Friends")
    for user in users.keys():
        fg.add_child(folium.Marker(location=[user[0], user[1]],
                                   popup=users[user]))
    location_map.add_child(fg)
    # location_map.save('friends_map.html')
    map_location = location_map.get_root().render()
    return map_location


def get_location(users):
    """
    Return a final dict with coordinates as a key
    :param users: list = [list[str, str], ...]
    :return: dict = {tuple(float, float): list(str), ...}
    """
    users_dict = dict()
    for user in users:
        location = user[0]

        locator = geopy.Nominatim(user_agent="Friend Location", timeout=10)
        coordinates = locator.geocode(location)
        try:
            user_coordinates = (coordinates.latitude, coordinates.longitude)
        except AttributeError:
            user_coordinates = (37.7790262, -122.4199061)

        if user_coordinates not in users_dict:
            users_dict[user_coordinates] = user[1] + '\n'
        else:
            users_dict[user_coordinates] += user[1] + '\n'

    return users_dict


def main(user):
    """
    Return a rendered map
    :param user: (str)
    :return: map
    """
    dct = get_info_by_nickname(user)
    dct = get_friends(dct)
    dct = get_location(dct)
    return map_locations(dct)
