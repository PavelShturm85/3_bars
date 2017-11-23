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
    return biggest_bar


def get_smallest_bar(input_bars):
    smallest_bar = min(input_bars, key=lambda bar: bar['properties']
                                                      ['Attributes']
                                                      ['SeatsCount'])
    return smallest_bar


def get_closest_bar(input_bars, longitude, latitude):
    closest_bar = min(input_bars,
                      key=lambda point: get_distance(latitude,
                                                     longitude,
                                                     point['geometry']
                                                          ['coordinates']))
    return closest_bar


def get_distance(latitude, longitude, bars_point):
    return sqrt((latitude - bars_point[0])**2 + (longitude - bars_point[1])**2)


def print_bar(attributes_bar, info):
    print(info, 'бар: {}, количество мест: {}, адрес: {}'.format(
        attributes_bar['Name'],
        attributes_bar['SeatsCount'],
        attributes_bar['Address']))


if __name__ == '__main__':
    if len(sys.argv) > 1:
        input_file_name = sys.argv[1]
    else:
        input_file_name = input('Введите путь к файлу: ')

    user_longitude = float(input('Введите долготу(например - 34.345345): '))
    user_latitude = float(input('Введите широту(например - 36.345565): '))

    bars = load_data(input_file_name)

    attributes_closest_bar = get_closest_bar(
        bars, user_longitude, user_latitude)['properties']['Attributes']

    attributes_smallest_bar = get_smallest_bar(
        bars)['properties']['Attributes']

    attributes_biggest_bar = get_biggest_bar(
        bars)['properties']['Attributes']

    print_bar(attributes_biggest_bar, 'Крупнейний')
    print_bar(attributes_smallest_bar, 'Наименьший')
    print_bar(attributes_closest_bar, 'Ближайший')
