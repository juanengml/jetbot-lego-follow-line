from jtop import jtop


def jtop_sensors():
    with jtop() as jetson:
        # jetson.ok() will provide the proper update frequency
        if jetson.ok():
            # Read tegra stats
            data = jetson.stats
    return data
