# This mapping maps substrings of point names to what type of point it is
# Watch out; there are some names that are included in others, are not deliminated in their names, or have other warnings
# Pretty much, many of the point names are named in weird and not conventional ways, and you should check the points
#   you are trying to decode before taking any of this document as fact. This is meant to help decode, not do the decoding
# Silas Monahan 4/2021


mapping = {
    'DMPR COMD': "Damper Command",
    'ROOM TEMP': "Room Temperature",
    'RT': "Room Temperature",
    'RMT': "Room Temperature",
    'NACRMT': "Room Temperature",
    'RMTP': "Room Temperature",
    'RSET': "Room Temperature Setpoint",
    'STP': "Room Temperature Setpoint",
    'STPA': "Room Temperature Setpoint",
    'STPT DIAL': "Room Temperature Setpoint",
    'RMS': "Room Temperature Setpoint",
    'RM STPT DIAL': "Room Temperature Setpoint",
    'SP': "Room Temperature Setpoint", # IMORTANT: Not always deliminated
    'V': "Valve",
    'VC': "Valve",
    'NGT OVRD': "Night Override",
    'NGT CLG STPT': "Night Cooling Setpoint",
    'AUX TEMP': "Aux Temperature",
    'CTL STPT': "Controller Setpoint",
    'DAY CLG STPT': "Day Cooling Setpoint",
    'HTG LOOPOUT': "Heating Loopout",
    'HTG FLOW MIN': "Flow",
    'HTG FLOW MAX': "Flow",
    'Flow': "Flow",
    'VLV2 POS': "Valve Two Position",
    'VLV 2 POS': "Valve Two Position",
    'VLV2 COMD': "Valve Two Command",
    'VLV 2 COMD': "Valve Two Command",
    'DMPR POS': "Damper Position", 
    'DUCT AREA': "Duct Area", 
    'VLV1 COMD': "Valve One Command",
    'VLV 1 COMD': "Valve One Command",
    'DAY HTG STPT': "Day Heating Setpoint", 
    'CTL FLOW MIN': "Controller Minimum Flow", 
    'FLOW STPT': "Flow Setpoint", 
    'DAY.NGT': "Day/Night", # IMPORTANT: see that the name is deliminated by a '.'
    'VALVE COUNT': "Valve Count",
    'VLV1 POS': "Valve One Position",
    'VLV 1 POS': "Valve One Position",
    'CTL TEMP': "Controller Temperature", 
    'NGT HTG STPT': "Night Heating Setpoint", 
    'CLG FLOW MIN': "Cooling Minimum Flow", 
    'CLG FLOW MAX': "Cooling Maximum Flow", 
    'HEAT.COOL': "Heating/Cooling", # IMPORTANT: see that the name is deliminated by a '.'
    'MTR SETUP': "Meter Setup",
    'AIR VOLUME': "Air Volume",
    'HWRT': "Hot Water Terurn Temp", # IMORTANT: Not always deliminated
    'HWR': "Hot Water Terurn Temp",
    'FLOW COEFF': "Flow Coefficient",
    'CTL FLOW MAX': "Controller Maximum Flow",
    'CLG LOOPOUT': "Cooling Loopout",
    'FLT': "Floor Temperature",
    'FLTD': "Floor Temperature Disable",
    'HWST': "Hot Water Supply Temp", # IMORTANT: Not always deliminated
    'HWS': "Hot Water Supply Temp", # Important: Not always at end of point name
    'EXSET': "Exhaust Set",
    'ESET': "Exhauset Set",
    'EXCFM': "Exhaust Air Flow Sensor",
    'ECFM': "Exhaust Air Flow Sensor",
    'EDMP': "Exhaust Damper",
    'DSET': "Differential Set",
    'FDIFF': "Flow Differential",
    'FCFM': "Fume Flow Sensor",
    'ALARM': "Alarm", # IMPORTANT: Other alarms also have this ending
    'OSUM': "Other Supply",
    'BLAST.FRZ.ALARM': "Blast Freeze Alarm", # IMPORTANT: see that the name is deliminated by a '.'
    'BLAST.FRZ': "Blast Freeze Alarm", # IMPORTANT: Not always at the end AND see that the name is deliminated by a '.'
    'TSUP': "Total Supply",
    'OCC': "Occupied",
    'MSAIR': "Max Air Supply",
    'SDMP': "Supply Damper",
    'SSET': "Supply Set",
    'SASET': "Supply Set",
    'SCFM': "Supply Air Flow Sensor",
    'SACFM': "Supply Air Flow Sensor",
    'MODE': "Vacancy",
    'DI 2': "Radiator DI 2",
    'DI 3': "Radiator DI 3",
    'FAN': "Fan",
    'CHW': "Chilled Water", # IMPORTANT: Not at the end of the point name AND other point names contain 'CHW'
    'CHW.FLO': "Chilled Water Flow", # IMPORTANT: see that the name is deliminated by a '.'
    'DWRT': "Domestic Water Supply Temperature Sensor",
    'HW.FLO': "Hot Water Flow", # IMPORTANT: see that the name is deliminated by a '.'
    'DOM': "Domestic Water", # IMPORTANT: Not at the end of the point name
    'DH2O': "Domestic Water", # IMPORTANT: Not at the end of the point name
    'DOMESTIC': "Domestic Water", # IMPORTANT: Not at the end of the point name
    'DW': "Domestic Water", # IMPORTANT: IN OTHER NAMES AND Not at the end of the point name
    'DWST': "Domestic Water Supply Temperature Sensor",
    'ELEC': "Electricity Use", # IMPORTANT: IN OTHER NAMES
    'ELEC.DEMAND': "Electricity Demand",
    'ELEC.METER.READING': "Electricity Meter Reading",
    'H2O.METER.READING': "Water Meter Reading",
    'HW.SP2ALM': "Hot Water Alarm", # IMPORTANT: see that the name is deliminated by a '.'
    'HW': "Hot Water", # IMPORTANT: IN OTHER NAMES
    'LAST.MONTH.EL.CONS': "Last Months Electricity Consumption", # IMPORTANT: see that the name is deliminated by a '.'
    'LAST.MONTH.ELEC.CONSUM': "Last Months Electricity Consumption", # IMPORTANT: see that the name is deliminated by a '.'
    'LAST.MONTH.H2O.CONSUMP': "Last Months Water Consumption", # IMPORTANT: see that the name is deliminated by a '.'
    'LAST.MONTH.STEAM.CONSU': "Last Months Steam Consumption", # IMPORTANT: see that the name is deliminated by a '.'
    'LAST.MONTH.CONSUM': "Last Months Steam Consumption", # IMPORTANT: see that the name is deliminated by a '.'
    'LAST.WEEK.ELEC.CONSUMP': "Last Weeks Electricity Consumption", # IMPORTANT: see that the name is deliminated by a '.'
    'LAST.WEEK.EL.CONS': "Last Weeks Electricity Consumption", # IMPORTANT: see that the name is deliminated by a '.'
    'LAST.WEEK.H2O.CONSUMP': "Last Weeks Water Consumption", # IMPORTANT: see that the name is deliminated by a '.'
    'LAST.WEEK.STEAM.CONSU': "Last Weeks Steam Consumption", # IMPORTANT: see that the name is deliminated by a '.'
    'STM.MTR.LAST.WEEK.CONSUMP': "Last Weeks Steam Consumption", # IMPORTANT: see that the name is deliminated by a '.'
    'MONTH.ELEC.CONSUMP': "This Months Electricity Consumption", # IMPORTANT: see that the name is deliminated by a '.'
    'MONTH.EL.CONS': "This Months Electricity Consumption", # IMPORTANT: see that the name is deliminated by a '.'
    'MONTH.H2O.CONSUMP': "This Months Water Consumption", # IMPORTANT: see that the name is deliminated by a '.'
    'MONTH.STEAM.CONSUMP': "This Months Steam Consumption", # IMPORTANT: see that the name is deliminated by a '.'
    'STM.MTR.MONTH.CONSUMP': "This Months Steam Consumption", # IMPORTANT: see that the name is deliminated by a '.'
    'STM.MTR': "Steam", # IMPORTANT: IN OTHER NAMES IMPORTANT: see that the name is deliminated by a '.'
    'STEAM': "Steam", # IMPORTANT: IN OTHER NAMES
    'TODAY.ELEC.CONSUMP': "Todays Electricity Consumption", # IMPORTANT: see that the name is deliminated by a '.'
    'TODAY.EL.CONS': "Todays Electricity Consumption", # IMPORTANT: see that the name is deliminated by a '.'
    'TODAY.H2O.CONSUMP': "Todays Water Consumption", # IMPORTANT: see that the name is deliminated by a '.'
    'TODAY.STEAM.CONSUMP': "Todays Steam Consumption", # IMPORTANT: see that the name is deliminated by a '.'
    'STEAM.TODAY': "Todays Steam Consumption", # IMPORTANT: see that the name is deliminated by a '.'
    'STM.MTR.TODAY.CONSUMP': "Todays Steam Consumption", # IMPORTANT: see that the name is deliminated by a '.'
    'TRSUMP': "Sump Pump",
    'WATER.DEMAND': "Water Demand", # IMPORTANT: see that the name is deliminated by a '.'
    'WATER.HI': "Water High Point", # IMPORTANT: see that the name is deliminated by a '.'
    'WATER.HIGH': "Water Highest Flow", # IMPORTANT: see that the name is deliminated by a '.'
    'WATER.LO': "Water Lowest Point", # IMPORTANT: see that the name is deliminated by a '.'
    'WATER.LOW': "Water Lowest Flow", # IMPORTANT: see that the name is deliminated by a '.'
    'WEEK.ELEC.CONSUMP': "This Weeks Electricity Consumption", # IMPORTANT: absence of "LAST." means that it is this week
    'WEEK.EL.CONS': "This Weeks Electricity Consumption", # IMPORTANT: absence of "LAST." means that it is this week
    'WEEK.H2O.CONSUMP': "This Weeks Water Consumption", # IMPORTANT: absence of "LAST." means that it is this week
    'WEEK.STEAM.CONSUMP': "This Weeks Steam Consumption", # IMPORTANT: absence of "LAST." means that it is this week
    'STM.MTR.WEEK.CONSUMP': "This Weeks Steam Consumption", # IMPORTANT: see that the name is deliminated by a '.'
    'YEST.ELEC.CONSUMP': "Yesterdays Electricity Consumption", # IMPORTANT: see that the name is deliminated by a '.'
    'YEST.EL.CONS': "Yesterdays Electricity Consumption", # IMPORTANT: see that the name is deliminated by a '.'
    'YEST.H2O.CONSUMP': "Yesterdays Water Consumption", # IMPORTANT: see that the name is deliminated by a '.'
    'YEST.STEAM.CONSUMP': "Yesterdays Steam Consumption", # IMPORTANT: see that the name is deliminated by a '.'
    'STEAM.YEST.CONSUMP': "Yesterdays Steam Consumption", # IMPORTANT: see that the name is deliminated by a '.'
    'STM.MTR.YEST.CONSUMP': "Yesterdays Steam Consumption", # IMPORTANT: see that the name is deliminated by a '.'
    'STPT.MAX': "Maximum Temperature Setpoint", # IMPORTANT: see that the name is deliminated by a '.'
    'STPT MAX': "Maximum Temperature Setpoint",
    'STPH': "Maximum Temperature Setpoint",
    'STPT.MIN': "Minimum Temperature Setpoint", # IMPORTANT: see that the name is deliminated by a '.'
    'STPT': "Setpoint",
    'HTG': "Heating Valve", # IMPORTANT: IN OTHER NAMES
    'HCV': "Heating Valve",
    'DOM.MTR.LAST.MONTH.CONSUM': "Last Months Domestic Water Consumption", # IMPORTANT: see that the name is deliminated by a '.'
    'DOM.MTR.LAST.WEEK.CONSUMP': "Last Weeks Domestic Water Consumption", # IMPORTANT: see that the name is deliminated by a '.'
    'LOC': "Local Point",
    'DOM.MTR.MONTH.CONSUMP': "This Months Domestic Water Consumption", # IMPORTANT: see that the name is deliminated by a '.'
    'DOM.MTR.TODAY.CONSUMP': "Todays Domestic Water Consumption", # IMPORTANT: see that the name is deliminated by a '.'
    'DOM.MTR.WEEK.CONSUMP': "This Weeks Domestic Water Consumption", # IMPORTANT: see that the name is deliminated by a '.'
    'DOM.MTR.YEST.CONSUMP': "Yesterdays Domestic Water Consumption", # IMPORTANT: see that the name is deliminated by a '.'
    'DOMESTIC.CONSUMPTION': "Domestic Water Consumption", # IMPORTANT: see that the name is deliminated by a '.'
    'CO2': "CO2 Monitor",
    'HALL.LIGHTS': "Hall Lights", # IMPORTANT: see that the name is deliminated by a '.'
    'HWS.STPT': "Hot Water Supply Temp Setpoint", # IMPORTANT: see that the name is deliminated by a '.'
    'HEAT.TAPE': "Heat Tape", # IMPORTANT: Not at the end of the point name IMPORTANT: see that the name is deliminated by a '.'
    'HWS.AVG': "Average Hot Water Supply Temp", # IMPORTANT: see that the name is deliminated by a '.'
    'SC': "Speed Output",
    'IRRIGATION.MTR': "Irrigation Meter", # IMPORTANT: see that the name is deliminated by a '.'
    'CONSUMPTION': "Consumption", # IMPORTANT: IN OTHER NAMES
    'CONSUMPTN HI': "DEM Consumption High",
    'CONSUMPTN LO': "DEM Consumption Low",
    'DRAIN.PAN': "Drain Pan", # IMPORTANT: see that the name is deliminated by a '.'
    'STEAM.AVG': "Average Steam", # IMPORTANT: see that the name is deliminated by a '.'
    'HV': "Steam Valve",
    }
