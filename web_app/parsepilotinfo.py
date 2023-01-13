from getpilot import get_pilots
from gettime import current_time


def parse_pilot_info():

    pilots, positions, snapshot = get_pilots()
    pilot_dict_list = []

    if pilots:
        for pilot in range(len(pilots)):
            temp_dict = {}
            full_name = (pilots[pilot]['firstName']) + ' ' + (pilots[pilot]['lastName'])
            email = (pilots[pilot]['email'])
            phone = (pilots[pilot]['phoneNumber'])
            temp_dict['Name'] = full_name
            temp_dict['Email'] = email
            temp_dict['Phone'] = phone
            temp_dict['Position'] = positions[pilot]
            temp_dict['Time'] = [snapshot]
            pilot_dict_list.append(temp_dict)

    return pilot_dict_list
