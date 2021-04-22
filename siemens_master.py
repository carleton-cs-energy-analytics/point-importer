#!/usr/bin/env python3
"""
    siemens_master.py
    Ethan Cassel-Mace and Chris Tordi, 4 November 2018

    Controls decoding of Siemens points. Delegates which building subclass a point will be passed to. Outputs list
    of point objects.
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

# maps building prefixes to building subclass decoders
# NOT USING ANYMORE
BUILDING_PREFIX_MAP = {'EV': EvansPointDecoder,
                       'EVANS': EvansPointDecoder,
                       'BO': BoliouPointDecoder,
                       'HU': HulingsPointDecoder,
                       # 'BO': HulingsPointDecoder,
                       'HULINGS': HulingsPointDecoder,
                       'HULLINGS': HulingsPointDecoder,
                       'STHS': TownhousesPointDecoder,
                       'WC': WeitzPointDecoder,
                       'CH': CassatPointDecoder
                       }

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


def get_building_decoder(name):
    '''
    IMPORTANT: this does not work very well for other buildings with many different prefixes
        or prefixes that are not deliminated by a special character
    :param prefix: prefix of point name
    :return:  name of subclass that corresponds to the building of a given point prefix
    '''
    #print(name)
    if name in OVERRIDE_POINTNAME_SET:
        return OverridePointDecoder
    prefix = get_prefix(name)  # get prefix of point name
    return BUILDING_PREFIX_MAP.get(prefix, PointDecoder)


def get_prefix(point_name):
    '''
    IMPORTANT: does not work for prefixes that are not deliminated
    :param point_name: name of point
    :return: Prefix of point name. These are calculated as follows:
    if a point has a delimiter, the prefix is the name up to the delimiter. Else, it is
    the first two characters of the point name. '''
    delimiters = {'.', ':', ' ', '-'}

    # calculate index of first delimiter, else None
    first_delimiter_index = next((i for i, ch in enumerate(point_name) if ch in delimiters), None)
    return point_name[:first_delimiter_index] if first_delimiter_index else point_name[:2]


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
