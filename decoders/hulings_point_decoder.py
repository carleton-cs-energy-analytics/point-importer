'''
    Silas Monahan, Last Updated April 11, 2021
    Decodes point data in the Hulings
'''

from decoders.point_decoder import PointDecoder
from decoders.point import Point

import re


class HulingsPointDecoder(PointDecoder):
    """
    Decoder for Hulings points.
    @TODO Not currently in use.
    """
    @staticmethod
    def decode_building_name(attr_dict):
        return "Hulings"

    @staticmethod
    def decode_device_name(attr_dict):
        return None

    @staticmethod
    def decode_device_desc(attr_dict):
        return None

    @staticmethod
    def decode_room_name(attr_dict):
        sub_names = attr_dict["Point Name"].split('.')
        if len(sub_names) == 1:
            nums = re.findall(r'\d+', sub_names[0])
            return nums[0]
        split1 = sub_names[1]
        if "R" in split1 and len(re.findall(r'\d+',split1)) > 0:
            return re.findall(r'\d+', split1)[0]
        return None

    @staticmethod
    def decode_room_floor(attr_dict):
        sub_names = attr_dict["Point Name"].split('.')
        if len(sub_names) == 1:
            nums = re.findall(r'\d+', sub_names[0])
            return int(str(nums[0])[0])
        split1 = sub_names[1]
        if "R" in split1 and len(re.findall(r'\d+',split1)) > 0:
            return re.findall(r'(?<=\D)\d', split1)[0]
        return None

    @staticmethod
    def decode_building_type(attr_dict):
        return "Academic"

    @staticmethod
    def decode_point_type(attr_dict):
        sub_names = attr_dict["Point Name"].split('.')
        split2 = ""
        if len(sub_names) < 3:
            split2 = sub_names[-1]
            #split2 = re.split('\d+', sub_names[-1])[1]
        else:
            split2 = sub_names[2]
        if "DSET" in split2:
            return "Differential Set"
        elif "EDMP" in split2:
            return "Exhaust Damper"
        elif "ESET" in split2:
            return "Exhaust Set"
        elif "EXCFM" in split2:
            return "Exhaust Cubic Feet per Minute"
        elif "EXSET" in split2:
            return "Exhaust Set"
        elif "FCFM" in split2:
            return "Fume Cubic Feet per Minute"
        elif "FDIFF" in split2:
            return "Flow Diff"
        elif "RM" in split2:
            return "Room Temperature"
        elif "RSET" in split2:
            return "Room Set Point"
        elif split2 == "A":
            return "Alarm"
        elif "BLAST" in attr_dict["Point Name"]:
            return "Blast Freeze Alarm"
        elif "OSUP" in split2:
            return "Other Supply"
        elif "TSUP" in split2:
            return "Total Supply"
        elif "OCC" in split2:
            return "Occupied"
        elif "ECFM" in split2:
            return "Exhaust Cubic Feet per Minute"
        elif "MSAIR" in split2:
            return "Max Air Supply"
        elif "SDMP" in split2:
            return "Supply Damper"
        elif "SSET" in split2:
            return "Supply Set"
        elif "SASET" in split2:
            return "Supply Set"
        elif "SCFM" in split2:
            return "Supply Cubic Feet per Minute"
        elif "SACFM" in split2:
            return "Supply Cubic Feet per Minute"
        '''
        elif "CO2" in split2:
            return None
        elif "TFH" in split2:
            return None
        elif "RMT" in split2:
            return
        elif "TEXH" in split2:
            return
        elif "SVPRS" in split2:
            return
        elif "RHV" in split2:
            return
        elif "MCFM" in split2:
            return
        elif "SREQ" in split2:
            return
        elif "ESET" in split2:
            return
        elif "FDIFF" in split2:
            return
        elif "LOCKOUT" in split2:
            return
        elif "EVPRS" in split2:
            return
        elif "CONSUMP" in split2:
            return
        elif "CONSU" in split2:
            return
        elif "CONSUM" in split2:
            return
        elif "SBIAS" in split2:
            return
        elif "HOLDER" in split2:
            return
        elif "SCAL" in split2:
            return
        elif "INTENSITY" in split2:
            return
        elif "ENA" in split2:
            return
        elif "DELAY" in split2:
            return
        elif "TCFM" in split2:
            return
        elif "SS" in split2:
            return
        elif "DEMAND" in split2:
            return
        elif "NACDMP" in split2:
            return
        elif "MXSA" in split2:
            return
        elif "LOC13" in split2:
            return
        elif "TUNNEL" in split2:
            return
        elif "HWSP" in split2:
            return
        elif "SHADES" in split2:
            return
        elif "LPACI" in split2:
            return
        elif "SACDMP" in split2:
            return
        elif "ECAL" in split2:
            return
        elif "LOOPOUT" in split2:
            return
        elif "RMS" in split2:
            return
        elif "FICFM" in split2:
            return
        elif "NACSWT" in split2:
            return
        elif "ISODMP" in split2:
            return
            '''













