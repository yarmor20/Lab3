import json


def json_parser():
    """
    Return parsed json dictionary
    :return: dict = {str: str, str: list, ...}
    """
    with open('json-4.json') as json_file:
        json_dict = json.load(json_file)
    return json_dict


def user_interface(json_dict):
    """
    Return json info the user was looking for
    :param json_dict: dict = {str: str, str: list, ...}
    :return: (str)
    """
    print("This JSON dictionary has these keys:\n", list(json_dict.keys()))
    key = input("Chose a key: ")
    try:
        json_object = json_dict[key]
    except KeyError:
        return "Wrong input!"
    while not isinstance(json_object, str):
        json_object = check_for_type(json_object)
    return json_object


def check_for_type(json_object):
    """
    Return json_object according to its type
    :param json_object: (str) or (dict) or (list)
    :return: (str) or (dict) or (list)
    """
    if isinstance(json_object, list):
        print("This object is list. List range is 0 - {}".format(len(json_object) - 1))
        n = int(input("Chose the index: "))
        try:
            json_object = json_object[n]
        except ValueError:
            return "Wrong input!"
        return json_object
    elif isinstance(json_object, dict):
        print("This object is dictionary with keys:\n", list(json_object.keys()))
        key = input("Chose the key: ")
        try:
            json_object = json_object[key]
        except KeyError:
            return "Wrong input!"
        return json_object
    else:
        return "The object you are looking for is:\n {}".format(json_object)


if __name__ == "__main__":
    dct = json_parser()
    print(dct['users'][4]['url'])
    print(user_interface(dct))
