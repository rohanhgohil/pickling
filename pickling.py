import pickle

# cars = ["Thar", "Scorpio", "Fortuner", "G-Wagon", "zl1 Camaro"]
# file = "cars.pkl"
# fileobj = open(file,'wb')
# pickle.dump(cars,fileobj)
# fileobj.close()

file = "cars.pkl"
fileobj = open(file,'rb')
my_car = pickle.load(fileobj)
print(my_car)