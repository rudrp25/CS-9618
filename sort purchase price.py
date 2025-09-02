class Car: # this is the object
    def __init__(self, n, e):  #constructor, self is not a parameter, n and e are parameters
         self.__VehicleID = n
         self.__Registration = ""      # two underscores to indicate that attribute is private. the attributes cant be used outside the class
         # (__Registration is an attribute for example)
         self.__DateOfRegistration = None
         self.__EngineSize = e
         self.__PurchasePrice = 0.00

    def SetPurchasePrice(self,p): # this is called a method (subroutine) (methods are usually public for accessibility outside the class)
        self.__PurchasePrice = p

    def SetRegistration(self,r):
        self.__Registration = r

    def SetDateOfRegistration(self,d):
        self.__DateOfRegistration = d

    def GetVehicleID (self):
        return(self.__VehicleID)

    def GetRegistration(self):
        return(self.__Registration)

    def GetDateOfRegistration(self):
        return(self.__DateOfRegistration)

    def GetEngineSize(self):
        return(self.__EngineSize)

    def GetPurchasePrice(self):
        return(self.__PurchasePrice)
    # end of class

    def PrintDetails(self):
        print("---------")
        print("The vehicle ID is : ", self.__VehicleID)
        print("The vehicle registration is: ", self.__Registration)
        print("The date of registration is: " , self.__DateOfRegistration)
        print("The engine size of the vehicle is: ", self.__EngineSize)
        print("The purchase price of the vehicle is: ", self.__PurchasePrice)

maxp = 0

import random
carobjs1 = [Car(random.randint(1000,9999), 0) for i in range(3)]
carobjs2 = []
newarr = []


for i in range(2):
    eng = int(input("Enter engine size: "))
    vehicle = input("Enter vehicle ID: ")
    carobjs2.append(Car(vehicle, eng))

for car in carjobs1:
    pp = int(input("Enter purchase price of the car: "))
    reg = int(input("Enter registration number: "))
    regdate = input("Enter date of registration: ")

    car.SetPurchasePrice(pp)
    car.SetRegistration(reg)
    car.SetDateOfRegistration(regdate)

for i in carobjs2:
    swap = False
    if carobjs2.GetPurchasePrice(i) > carobjs2.GetPurchasePrice(i+1):





