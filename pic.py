class Picture:
    def __init__(self, description, framecolor, height, width):
        self.__Description = description  # string
        self.__FrameColour = framecolor # string
        self.__Height = height  # integer
        self.__Width = width  # integer

    def GetDescription(self):
        return self.__Description

    def GetColour(self):
        return self.__FrameColour

    def GetHeight(self):
        return self.__Height

    def GetWidth(self):
        return self.__Width

    def SetDescription(self, newdesc):
        self.__Description = newdesc


PictureArray = []
for i in range(100):
    PictureArray.append(Picture("","",0,0))


def ReadData(PictureArray):
    file = "Pictures.txt"
    count = 0
    try:

