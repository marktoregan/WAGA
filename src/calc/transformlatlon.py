from pyproj import Proj, transform
from src.calc import normalize as nl
import csv
import numpy as np


class TransformLatLong(object):

    def __init__(self):
        self.inProj = Proj(init='epsg:3857')
        self.outProj = Proj(init='epsg:4326')


    def do_transform(self, lat, long):
        x2, y2 = transform(self.inProj, self.outProj, lat, long)
        return x2, y2

    def load_csv(self):
        rows =[]
        with open('/home/mark/projects/WAGA/src/db/towns.txt', 'r') as f:
            next(f)
            reader = csv.reader(f, delimiter='\t')
            for r in reader:
                rows.append(r)
        return rows


    def process_all_towns(self, towns):
        #print(towns)
        towns_processed = []
        for t in towns:
            name = t[0]
            latitude = t[1]
            longitude = t[2]
            normal = nl.Normalize(latitude=latitude, longitude=longitude)
            new_twn = [name, normal.x, normal.y]
            towns_processed.append(new_twn)
        return towns_processed

    def filter_out_duplicate_names(self,seq):
        # order preserving
        checked = []
        for e in seq:
            names = [x[0] for x in checked]
            if e[0] not in names:
                checked.append(e)
        return checked

if __name__ == "__main__":
    t = TransformLatLong()
    #x, y = t.do_transform(lat=-11705274.6374,long=4826473.6922)
    rr = t.load_csv()
    pp = t.process_all_towns(rr)
    #header=["name","latitude","longitude"]
    #np.savetxt("/home/mark/projects/WAGA/src/db/file_name.csv", pp, delimiter="\t", fmt='%s', header=header)
    p = t.filter_out_duplicate_names(pp)
    print(p)
    print(len(p))
    #print(x,y)