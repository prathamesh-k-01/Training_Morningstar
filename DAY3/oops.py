# class Car():                  WITHOUT CONSTRUCTOR
#     pass

# honda = Car()
# tata = Car()

# honda.model_name = "city"
# honda.price = 1000000
# honda.year = 2017

# tata.model_name = "bolt"
# honda.price = 500000
# honda.year = 2010


# print(honda.model_name)


# WITH CONSTRUCTOR

class Car():
    def __init__(self, modelname, price, year) -> None:
        self.modelname = modelname
        self.year = year
        self.price = price

    def price_inc(kuch):
        kuch.price =  kuch.price * 1.5

honda = Car('City', 100000, 2017)
tata = Car('bolt', 500000,2010)

d = honda.__dict__
# print(type(d))
honda.price_inc()
print(honda.price)
# print(honda.year)