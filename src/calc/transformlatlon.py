from pyproj import Proj, transform


class TransformLatLong(object):

    def __init__(self):
        self.inProj = Proj(init='epsg:3857')
        self.outProj = Proj(init='epsg:4326')


    def do_transform(self, lat, long):
        x2, y2 = transform(self.inProj, self.outProj, lat, long)
        return x2, y2

if __name__ == "__main__":
    t = TransformLatLong()
    x, y = t.do_transform(lat=-11705274.6374,long=4826473.6922)
    print(x,y)