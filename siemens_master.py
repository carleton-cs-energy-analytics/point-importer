"""
    siemens_master.py
    Ethan Cassel-Mace and Chris Tordi, 4 November 2018
    Edited and revamped by Silas Monahan, Spring 2021

    Helps importer.py import points
"""

import json

from decoders.point import Point
from decoders.point_decoder import PointDecoder

from decoders.boliou_point_decoder import BoliouPointDecoder
from decoders.cassat_point_decoder import CassatPointDecoder
from decoders.evans_point_decoder import EvansPointDecoder
from decoders.hulings_point_decoder import HulingsPointDecoder
from decoders.townhouses_point_decoder import TownhousesPointDecoder
from decoders.weitz_point_decoder import WeitzPointDecoder

from decoders.override_point_decoder import OverridePointDecoder


def get_point_object(name, point_attributes):
    '''
    :param name: point name
    :param point_attributes: attribute dictionary for point
    :return: Point object
    '''
    building_decoder_class = CassatPointDecoder  # class that corresponds to building mapping
    print(building_decoder_class)
    return Point(point_attributes, building_decoder_class)


def get_points():
    """
    :return: List of all the decoded points. Put your json file for the building you would like to upload after "open("
    """
    with open('json/testPointJson_Cassat.json') as f:
        points = json.loads(f.read())  # read point dictionary from points.json

    points_list = [get_point_object(name, point) for name, point in points.items()]  # list of point objects
    
    decoded_points_list = [point for point in points_list if point.building_name]
    return decoded_points_list
