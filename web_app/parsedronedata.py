from getdrone import get_drone
from datetime import datetime

# A function that does some parsing on the XML returned as a list by get_drone()
# Returns a list containing specified information about the drone based on the given parameters


def parse_drone(drone_data_variable):

    requested_information = []
    data = get_drone()
    data = data['report']
    capture = data['capture']
    drone_data = capture['drone']
    drone_count = len(drone_data)

    # Get the time of the snapshot.
    if drone_data_variable == '@snapshotTimestamp':
        snapshot_timestamp = capture[drone_data_variable]
        # Remove last char from snapshot, it simply indicates that the time is in UTC and datetime doesn't like it.
        snapshot_timestamp = snapshot_timestamp[:-1]
        snapshot_timestamp = datetime.fromisoformat(snapshot_timestamp)
        snapshot_timestamp = datetime.strftime(snapshot_timestamp, '%d/%m/%Y %H:%M:%S')
        return snapshot_timestamp

    for i in range(drone_count):
        drone_data_ = drone_data[i][drone_data_variable]
        requested_information.append(drone_data_)

    return requested_information
