import pickle

favorite_color = pickle.load( open( "save.p", "rb" ) )
print(favorite_color)