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

carobjs1 = (Car["",0] for i in range(5))
carobjs2 = []
car1 = Car("Abcd", 2222)
for i in range(2):
    carattr1 = input("Please enter vehicle ID:")
    carattr2 = input("Please enter engine size: ")
    carobjs2.append(carattr1,carattr2)
for i in range(len(carobjs1)):
    print("Please enter the purchase price: ", carobjs1[i].GetPurchasePrice())
    pprice = input()
    carobjs1[i].SetPurchasePrice(pprice)
    print("Please enter the reg no for: ", carobjs[i].GetRegistrationNo())
