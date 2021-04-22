'''
    Silas Monahan, Last Updated April 11, 2021
    Decodes point data in the Weitz
'''

import re

from decoders.point_decoder import PointDecoder
from decoders.point import Point

class WeitzPointDecoder(PointDecoder):
    """
    Decoder for Weitz points
    """

    @staticmethod
    def decode_building_name(attr_dict):
        return "Weitz"

    @staticmethod
    def decode_device_name(attr_dict):
        return None

    @staticmethod
    def decode_device_desc(attr_dict):
        return None

    @staticmethod
    def decode_room_name(attr_dict):
        location_name = ""
        if ":" in attr_dict["Point Name"][0]:
            sub_names = attr_dict["Point Name"][0].split(':')
            location_name = sub_names[0]
        location_units = location_name.split('.')
        if len(location_units) == 3:
            room_name = location_units[2]
            if "V" in room_name:
                room_name_list = re.findall(r'\d+', room_name)
                return room_name_list[0] if room_name_list else None
        return None

    @staticmethod
    def decode_room_floor(attr_dict):
        location_name = ""
        floor = 0
        if ":" in attr_dict["Point Name"][0]:
            sub_names = attr_dict["Point Name"][0].split(':')
            location_name = sub_names[0]
        location_units = location_name.split('.')
        if len(location_units) == 3:
            room_name = location_units[2]
            if "V" in room_name:
                room_name_list = re.findall(r'\d+', room_name)
                floor = int(str(room_name_list[0])[0])
        return floor

    @staticmethod
    def decode_building_type(attr_dict):
        return "Academic"

    @staticmethod
    def decode_point_type(attr_dict):
        split1 = ""
        if ":" in attr_dict["Point Name"][0]:
            sub_names = attr_dict["Point Name"][0].split(':')
            split1 = sub_names[1]
        if "ROOM TEMP" in split1:
            return "Room Temperature"
        return None
