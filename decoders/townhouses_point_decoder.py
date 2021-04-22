'''
    Silas Monahan, Last Updated April 11, 2021
    Decodes point data in the Student Townhouses
'''

from decoders.point_decoder import PointDecoder
from decoders.point import Point

import re


class TownhousesPointDecoder(PointDecoder):
    """
    Decoder for Hulings points.
    @TODO Not currently in use.
    """
    @staticmethod
    def decode_building_name(attr_dict):
        return "Townhouses"

    @staticmethod
    def decode_device_name(attr_dict):
        return None

    @staticmethod
    def decode_device_desc(attr_dict):
        return None

    @staticmethod
    def decode_room_name(attr_dict):
        sub_names = attr_dict["Point Name"][0].split('.')
        mid = str(sub_names[1])
        if mid[1] == '0':
            floor = str(mid[2])
            house_code = mid[0]
            if house_code == 'A':
                return "Hunt House " + floor
            elif house_code == 'B':
                return "Colwell House " + floor
            elif house_code == 'C':
                return "Dixon House " + floor
            elif house_code == 'D': # there is no building labeled as "D"
                return "Townhouse D " + floor
            elif house_code == 'E':
                return "Collier House " + floor
            elif house_code == 'F':
                return "Owens House " + floor
            elif house_code == 'G':
                return "Brooks House " + floor
            elif house_code == 'H':
                return "Nason House " + floor
            elif house_code == 'I':
                return "Scott House " + floor
            elif house_code == 'J':
                return "Eugster House " + floor
        else:
            return "All Townhouses"

    @staticmethod
    def decode_room_floor(attr_dict):
        sub_names = attr_dict["Point Name"][0].split('.')
        if(len(sub_names) > 1):
            mid = str(sub_names[1])
            if mid[1] == '0':
                floor = str(mid[2])
                return floor
        return None


    @staticmethod
    def decode_building_type(attr_dict):
        return "Residential"

    @staticmethod
    def decode_point_type(attr_dict):
        sub_names = attr_dict["Point Name"][0].split(':')
        device = ""
        if len(sub_names) == 2:
            device = sub_names[1]
            if "MODE" in device:
                return "Vacancy"
            elif "AUX TEMP" in device:
                return "Aux Temperature"
            elif "CLG LOOPOUT" in device:
                return "Cooling Loopout"
            elif "CTL STPT" in device:
                return "Controller Setpoint"
            elif "CTL TEMP" in device:
                return "Controller Temperature"
            elif "DAY CLG STPT" in device:
                return "Day Cooling Setpoint"
            elif "DAY HTG STPT" in device:
                return "Day Heating Setpoint"
            elif "DAY.NGT" in device:
                return "Day/Night"
            elif "DI 2" in device:
                return "Radiator DI 2"
            elif "DI 3" in device:
                return "Radiator DI 3"
            elif "FAN" in device:
                return "Radiator Fan"
            elif "HEAT.COOL" in device:
                return "Heating/Cooling"
            elif "HTG LOOPOUT" in device:
                return "Heating Loopout"
            elif "NGT CLG STPT" in device:
                return "Night Cooling Setpoint"
            elif "NGT HTG STPT" in device:
                return "Night Heating Setpoint"
            elif "RM STPT DIAL" in device:
                return "Room Setpoint Dial"
            elif "ROOM TEMP" in device:
                return "Room Temperature"
            elif "VLV 1 COMD" in device:
                return "Valve One Command"
            elif "VLV 1 POS" in device:
                return "Value One Command"
            elif "VLV 2 COMD" in device:
                return "Valve Two Command"
            elif "VLV 2 POS" in device:
                return "Value Two Position"
        else:
            device = attr_dict["Point Name"][0][5:]
            return_str = ""

            if "LAST" in device:
                return_str += "Last "
            
            if "TODAY" in device:
                return_str += "Today's "
            elif "YEST" in device:
                return_str += "Yesterday's "
            elif "WEEK" in device:
                if "LAST" not in device:
                    return_str += "This "
                return_str += "Week's "
            elif "MONTH" in device:
                if "LAST" not in device:
                    return_str += "This "
                return_str += "Month's "

            if "WATER" in device or "H2O" in device:
                return_str += "Water "
            elif "STEAM" in device:
                return_str += "Steam "
            elif "ELEC" in device:
                return_str += "Electricity "

            if "CONSUMP" in device:
                return_str += "Consumption"
            elif "DEMAND" in device:
                return_str += "Demand"
            elif "METER" in device:
                return_str += "Meter Reading"

            if "CHW" in device:
                return_str += "Chilled Water "
            elif "HW" in device:
                return_str += "Hot Water "
            elif "DH2O" in device or "DW" in device[0:2]:
                return_str += "Domestic Water "
            elif "DHW" in device:
                return_str += "Domestic Hot Water "

            if "ST" in device[0:5]:
                return_str += "Supply"
            elif "RT" in device[0:3]:
                return_str += "Return"
            elif "FLO" in device:
                return_str += "Flow"
            elif "ALM" in device:
                return_str += "Alarm"
            elif "HIGH" in device:
                return_str += "Highest Flow"
            elif "LOW" in device:
                return_str += "Lowest Flow"
            elif "HI" in device:
                return_str += "High Point"
            elif "LO" in device:
                return_str += "Low Point"

            if "TRSUMP" in device:
                return "Sump Pump"
            elif "TRENCH" in device:
                return "Trench Alarm"


            return return_str
