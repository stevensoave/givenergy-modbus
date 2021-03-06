holding_register_LUT = {
    0: ["Device Type Code", "unsigned", 1],
    1: ["Registers Module (high)", "unsigned", 1],
    2: ["Registers Module (low)", "unsigned", 1],
    3: ["Input tracker num and output phase num", "unsigned", 1],
    4: ["unknown", "unsigned", 1],
    5: ["unknown", "unsigned", 1],
    6: ["unknown", "unsigned", 1],
    7: ["unknown", "unsigned", 1],
    8: ["BAT Serial number 5", "ascii", 1],
    9: ["BAT Serial number 4", "ascii", 1],
    10: ["BAT Serial number 3", "ascii", 1],
    11: ["BAT Serial number 2", "ascii", 1],
    12: ["BAT Serial number 1", "ascii", 1],
    13: ["INV Serial number 5", "ascii", 1],
    14: ["INV Serial number 4", "ascii", 1],
    15: ["INV Serial number 3", "ascii", 1],
    16: ["INV Serial number 2", "ascii", 1],
    17: ["INV Serial number 1", "ascii", 1],
    18: ["Batt f/w version", "unsigned", 1],
    19: ["DSP f/w version", "unsigned", 1],
    20: ["Winter Mode On Off", "unsigned", 1],
    21: ["ARM f/w version", "unsigned", 1],
    22: ["Wifi or U disk ", "unsigned", 1],
    23: ["Selet dsp or ARM", "unsigned", 1],
    24: ["Set Variable address", "unsigned", 1],
    25: ["Set Variable Value", "unsigned", 1],
    26: ["GridPortMaxOutPutPower", "unsigned", 1],
    27: ["BatPowerMode", "boolean", 1],
    28: ["FreMode", "unsigned", 1],
    29: ["SOC_ForceAdjust", "unsigned", 1],
    30: ["Communicate  address", "unsigned", 1],
    31: ["Slot 2 charge time start", "time", 1],
    32: ["Slot 2 charge time stop", "time", 1],
    33: ["User code", "unsigned", 1],
    34: ["Modbus Version", "unsigned", 0.01],
    35: ["System time-year", "unsigned", 1],
    36: ["System time- Month", "unsigned", 1],
    37: ["System time- Day", "unsigned", 1],
    38: ["System time- Hour", "unsigned", 1],
    39: ["System time- Min", "unsigned", 1],
    40: ["System time- Second", "unsigned", 1],
    41: ["DRM enable", "unsigned", 1],
    42: ["CT Adjust", "unsigned", 1],
    43: ["Chg and dischg Soc", "unsigned", 1],
    44: ["Discharge start time slot2", "time", 1],
    45: ["Discharge end time slot2", "time", 1],
    46: ["BMSVersion", "unsigned", 1],
    47: ["bMeterType", "unsigned", 1],
    48: ["b115MeterDirect", "unsigned", 1],
    49: ["b418MeterDirect", "unsigned", 1],
    50: ["Active P rate", "unsigned", 1],
    51: ["Reactive P rate", "unsigned", 1],
    52: ["Power Factor", "unsigned", 1],
    53: ["Registers State", "unsigned", 1],
    54: ["Battery type", "unsigned", 1],
    55: ["Battery norminal capacity", "unsigned", 1],
    56: ["Discharge start time slot1", "time", 1],
    57: ["Discharge end time slot1", "time", 1],
    58: ["AutoJudgeBatteryTypeEnable", "unsigned", 1],
    59: ["Discharge Enable", "boolean", 1],
    60: ["Input start voltage ", "unsigned", 1],
    61: ["Start time", "unsigned", 1],
    62: ["RestartDelayTime", "unsigned", 1],
    63: ["Vac low OUT", "unsigned", 1],
    64: ["Vac high OUT", "unsigned", 1],
    65: ["Fac low OUT", "unsigned", 1],
    66: ["Fac high OUT", "unsigned", 1],
    67: ["Vac low OUT  time", "unsigned", 1],
    68: ["Vac high OUT  time", "unsigned", 1],
    69: ["Fac low OUT time", "unsigned", 1],
    70: ["Fac high OUT time", "unsigned", 1],
    71: ["Vac low IN", "unsigned", 1],
    72: ["Vac high IN", "unsigned", 1],
    73: ["Fac low IN", "unsigned", 1],
    74: ["Fac high IN", "unsigned", 1],
    75: ["Vac low IN time", "unsigned", 1],
    76: ["Vac high IN time", "unsigned", 1],
    77: ["Fac low time IN", "unsigned", 1],
    78: ["Fac high time IN", "unsigned", 1],
    79: ["Vac low C", "unsigned", 1],
    80: ["Vac high C", "unsigned", 1],
    81: ["Fac low C", "unsigned", 1],
    82: ["Fac high C", "unsigned", 1],
    83: ["U10min", "unsigned", 1],
    84: ["ISO1", "unsigned", 1],
    85: ["ISO2", "unsigned", 1],
    86: ["GFCI_I 1", "unsigned", 1],
    87: ["GFCI_time 1 ", "unsigned", 1],
    88: ["GFCI_I 2", "unsigned", 1],
    89: ["GFCI_time 2 ", "unsigned", 1],
    90: ["DCI_I 1", "unsigned", 1],
    91: ["DCI_time 1 ", "unsigned", 1],
    92: ["DCI_I 2", "unsigned", 1],
    93: ["DCI_time 2", "unsigned", 1],
    94: ["Charge start time slot1", "time", 1],
    95: ["Charge end time slot1", "time", 1],
    96: ["Battery Smart Charge", "boolean", 1],
    97: ["Discharger Low  limit", "unsigned", 1],
    98: ["Charger High limit", "unsigned", 1],
    99: ["Pv1 volt adjust", "unsigned", 1],
    100: ["Pv2 volt adjust", "unsigned", 1],
    101: ["Grid R volt adjust", "unsigned", 1],
    102: ["Grid S volt adjust", "unsigned", 1],
    103: ["Grid T volt adjust", "unsigned", 1],
    104: ["Grid Power adjust", "unsigned", 1],
    105: ["Bat volt adjust", "unsigned", 1],
    106: ["PV1 Power adjust", "unsigned", 1],
    107: ["PV2 Power adjust", "unsigned", 1],
    108: ["BatLowForceChgTime", "unsigned", 1],
    109: ["bBMSType", "unsigned", 1],
    110: ["Shallow Charge", "unsigned", 1],
    111: ["bBatChgLimit", "unsigned", 1],
    112: ["bBatDisLimit", "unsigned", 1],
    113: ["Buzzer_sw", "unsigned", 1],
    114: ["Battery Power Reserve", "unsigned", 1],
    115: ["IsLanChkContiue", "unsigned", 1],
    116: ["Target SOC", "unsigned", 1],
    117: ["Chg_soc stop2", "unsigned", 1],
    118: ["dischg_soc stop2", "unsigned", 1],
    119: ["Chg_soc stop", "unsigned", 1],
    120: ["dischg_soc stop", "unsigned", 1],
}

input_register_LUT = {
    0: ["Invertor Status", "unsigned", 1],
    1: ["PV1 voltage", "unsigned", 0.1],
    2: ["PV2 voltage", "unsigned", 0.1],
    3: ["P Bus inside  Voltage", "unsigned", 0.1],
    4: ["N Bus inside Voltage", "unsigned", 0.1],
    5: ["single phase grid voltage", "unsigned", 0.1],
    6: ["Battery Throughput_H", "hex", 0.1],
    7: ["Battery Throughput_L", "hex", 0.1],
    8: ["PV1 input current", "unsigned", 0.01],
    9: ["PV2 input current", "unsigned", 0.01],
    10: ["single phase grid output current", "unsigned", 0.01],
    11: ["PV Total generating capacity_H", "hex", 0.1],
    12: ["PV Total generating capacity_L", "hex", 0.1],
    13: ["Grid frequency of Three-single Phase", "unsigned", 0.01],
    14: ["Charge Status", "unsigned", 1],
    15: ["HighBrighBUS_Volt", "unsigned", 1],
    16: ["Registers output PF now", "unsigned", 1],
    17: ["PV1 Energy Today", "unsigned", 0.1],
    18: ["PV1 input watt", "unsigned", 1],
    19: ["PV2 Energy Today", "unsigned", 0.1],
    20: ["PV2 input watt", "unsigned", 1],
    21: ["Grid Energy Out totalH", "hex", 0.1],
    22: ["Grid Energy Out totalL", "hex", 0.11],
    23: ["PV mate", "unsigned", 0.1],
    24: ["Three-single phase grid output watt (low)", "signed", 1],
    25: ["Grid Energy Out Day", "unsigned", 0.1],
    26: ["Grid Energy IN Day", "unsigned", 0.1],
    27: ["INV Energy IN total H", "hex", 0.1],
    28: ["INV Energy IN total L", "hex", 0.1],
    29: ["YearDisChargeEnergyLow", "unsigned", 0.1],
    30: ["Grid Output Power", "signed", 1],
    31: ["PBackUp", "unsigned", 1],
    32: ["Grid Energy IN totalH", "hex", 0.1],
    33: ["Grid Energy IN totalL", "hex", 0.1],
    34: ["Unknown", "unsigned", 1],
    35: ["TotalLoad energy today", "unsigned", 0.1],
    36: ["Battery Charge Energy Today", "unsigned", 0.1],
    37: ["Battery Discharge Energy Today", "unsigned", 0.1],
    38: ["wCountdown", "unsigned", 1],
    39: ["fault Code High 16bits", "hex", 1],
    40: ["fault Code Low 16bits", "hex", 1],
    41: ["Registers temperature", "unsigned", 0.1],
    42: ["LoadTotal Power ", "unsigned", 1],
    43: ["Pgrid_Apparent", "unsigned", 1],
    44: ["Today generate energy today (low)", "unsigned", 0.1],
    45: ["Total generate energy (high)", "hex", 0.1],
    46: ["Total generate energy (low)", "hex", 0.1],
    47: ["Work time total (high)", "hex", 1],
    48: ["Work time total (low)", "hex", 1],
    49: ["System Mode", "unsigned", 1],
    50: ["Battery voltage", "unsigned", 0.01],
    51: ["Battery current", "signed", 0.01],
    52: ["Battery power", "signed", 1],
    53: ["Output voltage", "unsigned", 0.1],
    54: ["Output frequency", "unsigned", 0.01],
    55: ["Charger temperature", "unsigned", 0.1],
    56: ["Battery temperature", "unsigned", 0.1],
    57: ["Charger Warning code", "unsigned", 1],
    58: ["wGridPortCurr", "unsigned", 0.01],
    59: ["Battery percent", "unsigned", 1],
    60: ["Reg60", "unsigned", 1],
    105: ["Battery Discharge Energy Total AC", "unsigned", 0.1],
    106: ["Battery Charge Energy Total AC", "unsigned", 0.1],
    180: ["Battery Discharge Energy Total", "unsigned", 0.1],
    181: ["Battery Charge Energy Total", "unsigned", 0.1],
}
