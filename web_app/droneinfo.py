from parsedronedata import parse_drone


def serial_numbers():
    serials = parse_drone('serialNumber')
    return serials


def x_coordinate():
    x = parse_drone('positionX')
    return x


def y_coordinate():
    y = parse_drone('positionY')
    return y


def snapshot_time():
    snapshot = parse_drone('@snapshotTimestamp')
    return snapshot

