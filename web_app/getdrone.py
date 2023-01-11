import urllib3
import xmltodict

URL = 'https://assignments.reaktor.com/birdnest/drones'


# Get XML containing drone information
def get_drone():
    http = urllib3.PoolManager()
    response = http.request('GET', URL)
    dict_response = xmltodict.parse(response.data)
    return dict_response

