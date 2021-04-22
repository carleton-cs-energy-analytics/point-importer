'''
    Silas Monahan, Last Updated April 13, 2021
    Decodes point data in the Cassat
'''

from decoders.point_decoder import PointDecoder
from decoders.point import Point

import re


class CassatPointDecoder(PointDecoder):
    """
    Decoder for Cassat points
    """
    @staticmethod
    def decode_building_name(attr_dict):
        return "Cassat"

    @staticmethod
    def decode_device_name(attr_dict):
        return None

    @staticmethod
    def decode_device_desc(attr_dict):
        return None

    @staticmethod
    def decode_room_name(attr_dict):
        split = attr_dict["Point Name"][0].split(".")
        if(len(split)==4):
            whole = split[2]
            if(whole[1].isdigit()):
                return whole[1:]
        if(len(split) == 3):
            whole = split[1]
            if(len(whole)>3):
                if(whole[1].isdigit() and whole[2].isdigit() and whole[3].isdigit()):
                    return whole[1:]
        if(split[1][0:2]=="RM"):
            return split[1][2:]
        weird_rooms = ["FC", "EF", "CU"]
        if split[1][0:2] in weird_rooms:
            return split[1].split(":")[0]

        return None

    @staticmethod
    def decode_room_floor(attr_dict):
        split = attr_dict["Point Name"][0].split(".")
        if(len(split)==4):
            whole = split[2]
            if(whole[1].isdigit()):
                return whole[1]
        if(len(split) == 3):
            whole = split[1]
            if(len(whole)>3):
                if(whole[1].isdigit() and whole[2].isdigit() and whole[3].isdigit()):
                    return whole[1]
        if(split[1][0].isdigit() or split[1] == "BASEMENT"):
            if(split[1] == "BASEMENT"):
                return 0
            else:
                return split[1][0]
        if(split[1][0:2]=="RM"):
            return split[1][2]
        return None

    @staticmethod
    def decode_building_type(attr_dict):
        return "Residential"

    @staticmethod
    def decode_point_type(attr_dict):
        split = attr_dict["Point Name"][0].split('.')
        device = attr_dict["Point Name"][0]
        
        room = False # if this point is part of a specific room
        if(len(split) == 3):
            whole = split[1]
            if(len(whole)>3):
                if(whole[1].isdigit() and whole[2].isdigit() and whole[3].isdigit()):
                    room = True
        if(split[1][0].isdigit() or split[1] == "BASEMENT"):
            if(split[1] == "BASEMENT"):
                room = True
            else:
                room = True
        if(split[1][0:2]=="RM"):
            room = True
        if(room == True):
            last = split[len(split)-1]
            if last == "RMT":
                return "Room Temperature"
            elif last == "RMS":
                return "Room Temperature Setpoint"
            elif last == "MAX":
                return "Maximum Setpoint"
            elif last == "MIN":
                return "Minimum Setpoint"
            elif last == "CO2":
                return "CO2 Monitor"
            elif last == "HCV":
                return "Heating Value"
            elif last == "CALL":
                return "DB"
            elif last == "FLT":
                return "Floor Temperature"
            elif last == "FLTD":
                return "Floor Temperature Disable"
            elif last == "STP":
                return "Setpoint"
            elif last == "VLV":
                return "Floor Heating Valve"
            elif last == "STPA":
                return "Setpoint Actual"
            elif last == "STPH":
                return "Setpoint High Limit"
            elif last == "STPL":
                return "Setpoint Low Limit"
            elif last =="STPT":
                return "Setpoint"
            elif last == "PAN":
                return "Drain Pan"
        elif ":" in device:
            device = device.split(":")[1]
            return_str = ""

            if "CONSUMPTN HI" in device:
                return "DEM Consumption High"
            elif "CONSUMPTN LO" in device:
                return "DEM Consumption Low"
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
            

            return return_str
        else:
            return_str = ""
            
            if "LAST" in device:
                return_str += "Last "
            
            if "HALL.LIGHTS" in device:
                return "Hall Lights"
            
            if "HEAT.TAPE" in device:
                if "CNTRL" in device:
                    return "Central Heat Tape"
                if "EAST" in device:
                    return "East Heat Tape"
                if "WEST" in device:
                    return "West Heat Tape"
                else:
                    return "Heat Tape"
            
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
            
            if "AVG" in device:
                return_str+= "Average "

            if ".DOM" in device:
                return_str += "Domestic "
            elif ".HWR" in device:
                return_str += "Hot Water Return Temp "
            elif ".HWS" in device:
                return_str += "Hot Water Supply Temp "
            elif "DH2O" in device or "DW" in device[0:2]:
                return_str += "Domestic Water "
            elif "DHW" in device:
                return_str += "Domestic Hot Water "

            if "WATER" in device or "H2O" in device:
                return_str += "Water "
            elif "STM" in device or "STEAM" in device:
                return_str += "Steam "
            elif "ELEC" in device or ".EL." in device:
                return_str += "Electricity "
            
            if "IRRIGATION" in device:
                return_str += "Irrigation "
            if "MTR" in device:
                return_str += "Meter"

            if "CONS" in device:
                return_str += "Consumption "
            elif "DEMAND" in device:
                return_str += "Demand "

            if " HI" in device:
                return_str += "High"
            elif " LO" in device:
                return_str += "Low"

            if ".HV" in device:
                return "Steam Valve"

            if ".HCV" in device:
                return_str+= "Heating Valve"

            if ".HTG" in device:
                return_str+= "Heating Value Open"
            
            if ".VC" in device:
                return_str+= "Valve Output"
            elif ".SC" in device:
                return_str+= "Speed Output"

            if "STPT" in device:
                return_str += "Setpoint"

            if "RMS" in device:
                return_str+= "Room Temperature Setpoint "
            elif "RMT" in device:
                return_str+= "Room Temperature Setpoint "
            
            if ".LOC" in device:
                return "Local Point"
            
            if "ALARM" in device:
                return_str += "Alarm"
            
            return return_str
        
        return None












