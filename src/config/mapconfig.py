import yaml
import sys


class MapConfig(object):

    def __init__(self):
        self.legend_distance = self._get_legend_distance()

    def read(self):
        try:
            with open("../src/config/config.yaml", 'r') as f:
                return yaml.load(f)
        except FileNotFoundError:
            # logger.error("Config file {0} not found".format(filename))
            #print("Config file {0} not found".format(filename), file=sys.stderr)
            sys.exit(1)

    def _get_legend_distance(self):
        cfg = self.read()
        leg_dist = cfg['journeymap']['legend_distance']
        return leg_dist