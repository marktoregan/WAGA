from src.calc import transformlatlon as tran
class Normalize(object):

    def __init__(self, longitude, latitude):
        t = tran.TransformLatLong()
        tx, ty = t.do_transform(lat=latitude, long=longitude)
        self.x = self.normalize_longitude(tx)
        self.y = self.normalize_latitude(ty)

    def normalize_longitude(self, xi):
        min_x = 0.0004624949021336246
        max_x = 0.0004963315732606508
        a = xi - min_x
        b = max_x - min_x
        ans_longitude = a / b
        return round(ans_longitude * 100, ndigits=2)

    def normalize_latitude(self, yi):
        min_y = -9.233595057399676e-05
        max_y = -4.9834938709674104e-05
        a = yi - min_y
        b = max_y - min_y
        ans_latitude = a / b
        return round(ans_latitude * 100, ndigits=2)