import yaml
import sys


class MapConfig(object):

    def __init__(self):
        self.legend_distance = self._get_legend_distance()

    def read(self):
        try:
            print('open')
            with open("../src/config.yaml", 'r') as f:
                print('success')
                return yaml.load(f)
        except FileNotFoundError:
            print('fail')
            # logger.error("Config file {0} not found".format(filename))
            #print("Config file {0} not found".format(filename), file=sys.stderr)
            sys.exit(1)

    def _get_legend_distance(self):
        cfg = self.read()
        leg_dist = cfg['journeymap']['legend_distance']
        return leg_dist