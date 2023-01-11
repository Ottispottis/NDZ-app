from getpilot import get_pilots
import datetime



def parse_pilot_info():

    pilots, positions = get_pilots()
    pilot_dict_list = []

    if pilots:
        for pilot in range(len(pilots)):
            current_time = datetime.datetime.now()
            hour = current_time.hour
            minute = current_time.minute
            hour_minute = '{}-{}'.format(hour, minute)
            temp_dict = {}
            full_name = (pilots[pilot]['firstName']) + ' ' + (pilots[pilot]['lastName'])
            email = (pilots[pilot]['email'])
            phone = (pilots[pilot]['phoneNumber'])
            temp_dict['Name'] = full_name
            temp_dict['Email'] = email
            temp_dict['Phone'] = phone
            temp_dict['Position'] = positions[pilot]
            temp_dict['Time'] = [hour_minute]

            pilot_dict_list.append(temp_dict)

    return (pilot_dict_list)
