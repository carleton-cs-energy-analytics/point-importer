#!/usr/bin/env python3
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

OVERRIDE_POINTNAME_SET = {}
#                       {'STHS.HWRT',
#                          'STHS.HWST',
#                          'SEV.HX1.HW',
#                          'MCHWRT',
#                          'EV.HX2.HWR',
#                          'SHHWRT',
#                          'SHHWST'}


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
    :return: List of all the decoded points. This is where to change which points are allowed to be
    imported, and which aren't.
    """
    with open('json/testPointJson_Cassat.json') as f:
        points = json.loads(f.read())  # read point dictionary from points.json

    points_list = [get_point_object(name, point) for name, point in points.items()]  # list of point objects
    # @TODO Only decodes points with building name decoded or in override set. Change if this isn't wanted!
    decoded_points_list = [point for point in points_list if
                           point.building_name or point.point_name in OVERRIDE_POINTNAME_SET]
    return decoded_points_list
