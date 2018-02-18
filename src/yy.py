import attr


@attr.s
class Empty(object):
    pass

x = Empty()
y = Empty()

print("{}".format(x == y))

Empty() is Empty()

print('k')c