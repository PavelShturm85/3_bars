import sys
import json
from math import sqrt


def load_data(enter_file):
    with open(enter_file) as json_file:
        json_content = json.load(json_file)['features']
    return json_content


def get_biggest_bar(input_bars):
    biggest_bar = max(input_bars, key=lambda bar: bar['properties']
                                                     ['Attributes']
                                                     ['SeatsCount'])

    attributes_bar = biggest_bar['properties']['Attributes']
    return attributes_bar['Name'], attributes_bar['SeatsCount']


def get_smallest_bar(input_bars):
    smallest_bar = min(input_bars, key=lambda bar: bar['properties']
                                                      ['Attributes']
                                                      ['SeatsCount'])

    attributes_bar = smallest_bar['properties']['Attributes']
    return attributes_bar['Name'], attributes_bar['SeatsCount']


def get_closest_bar(input_bars, longitude, latitude):
    closest_bar = min(input_bars,
                      key=lambda point: get_distance(latitude,
                                                     longitude,
                                                     point['geometry']
                                                          ['coordinates']))

    attributes_bar = closest_bar['properties']['Attributes']
    return attributes_bar['Name'], attributes_bar['Address']


def get_distance(latitude, longitude, user_point):
    return sqrt((latitude - user_point[0])**2 + (longitude - user_point[1])**2)


if __name__ == '__main__':
    if len(sys.argv) > 1:
        input_file_name = sys.argv[1]
    else:
        input_file_name = input('Введите путь к файлу: ')

    user_longitude = float(input('Введите долготу(например - 34.345345): '))
    user_latitude = float(input('Введите широту(например - 36.345565): '))

    bars = load_data(input_file_name)

    print('Самый большой бар: {}, количество мест: {}'.format(
        *get_biggest_bar(bars)))

    print('Самый большой бар: {}, количество мест: {}'.format(
        *get_smallest_bar(bars)))

    closest_bar = get_closest_bar(bars, user_longitude, user_latitude)
    print('Ближайший бар называется:  {}, находится по адресу: {}'.format(
        *closest_bar))
