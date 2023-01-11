from getdrone import get_drone


# A function that does some parsing on the XML returned as a list by get_drone()
# Returns a list containing specified information about the drone based on the given parameters

def parse_drone(drone_data_variable):

    requested_information = []
    data = get_drone()
    data = data['report']
    capture = data['capture']
    drone_data = capture['drone']
    drone_count = len(drone_data)

    for i in range(drone_count):
        drone_data_ = drone_data[i][drone_data_variable]
        requested_information.append(drone_data_)

    return requested_information
