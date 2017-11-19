import sys
import json
from math import sqrt


def load_data(enter_file):
    with open(enter_file) as json_file:
        json_content = json.load(json_file)
    return json_content


def get_biggest_bar(input_content):
    return max(input_content['features'][0:],
               key=lambda bar: bar['properties']['Attributes']['SeatsCount'])


def get_smallest_bar(input_content):
    return min(input_content['features'][0:],
               key=lambda bar: bar['properties']['Attributes']['SeatsCount'])


def get_closest_bar(input_content, longitude, latitude):
    return min(input_content['features'][0:],
               key=lambda point: get_distance(latitude,
                                              longitude,
                                              point['geometry']
                                                   ['coordinates']))


def get_distance(latitude, longitude, user_point):
    return sqrt((latitude - user_point[0])**2 + (longitude - user_point[1])**2)


if __name__ == '__main__':
    if len(sys.argv) > 1:
        input_file_name = sys.argv[1]
    else:
        input_file_name = input('Input filepath: ')

    user_longitude = float(input('Введите долготу(например - 34.345345): '))
    user_latitude = float(input('Введите широту(например - 36.345565): '))

    content = load_data(input_file_name)

    print('Самый большой бар: %s, количество мест: %s' % (
        get_biggest_bar(content)['properties']['Attributes']['Name'],
        get_biggest_bar(content)['properties']['Attributes']['SeatsCount']))

    print('Самый маленький бар: %s, количество мест: %s' % (
        get_smallest_bar(content)['properties']['Attributes']['Name'],
        get_smallest_bar(content)['properties']['Attributes']['SeatsCount']))

    closest_bar = get_closest_bar(content, user_longitude, user_latitude)

    print('Ближайший бар называется:  %s, находится по адресу: %s' % (
        closest_bar['properties']['Attributes']['Name'],
        closest_bar['properties']['Attributes']['Address']))
