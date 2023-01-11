import urllib3
from urllib.error import HTTPError
from droneinfo import serial_numbers
from droneposition import calculate_position
import json

URL = 'https://assignments.reaktor.com/birdnest/pilots/'


# First checks if NDZ was breached by comparing the positions given by calculate_postition() to the radius.
# If position is smaller than radius, NDZ has been breached and the information of the pilot is collected
def get_pilots():

    radius = 100000
    serial_n = serial_numbers()
    pilot_list = []
    http = urllib3.PoolManager()
    positions = calculate_position()
    positions_under_radius = []

    for i in range(len(serial_n)):
        if positions[i] < radius:
            try:
                response = http.request('GET', URL+serial_n[i]).data
                # Response is byte data. Simply decoding it so it becomes dictionary data type.
                response = json.loads(response.decode('utf-8'))
                pilot_list.append(response)
                positions_under_radius.append(positions[i])
            except HTTPError as e:
                if e.code == 404:
                    continue

    if not pilot_list:
        return None, None
    else:
        return pilot_list, positions_under_radius
