##Computer class that allows for the creation of computer instances and controls actions that each instance can perform
class Computer:
    ##attributes of each computer
    description:str
    processorType:str
    hardDriveCapacity:str
    memory:int
    operatingSystem:str
    yearMade=int
    price=int


    ##computer constructor that creates instance when called
    def __init__(self,description,processorType,hardDriveCapacity, memory,operatingSystem,yearMade,price):
    
        self.description=description
        self.processorType=processorType
        self.hardDriveCapacity=hardDriveCapacity
        self.memory=memory
        self.operatingSystem=operatingSystem
        self.yearMade=yearMade
        self.price=price

    ##prints all info about computer that calls this method
    def printAllInfo(self):
        print("Description:",self.description)
        print("Processor Type:",self.processorType)
        print("Hard Drive Capacity:",self.hardDriveCapacity)
        print("Memory:",self.memory)
        print("Operating System:",self.operatingSystem)
        print("Year Made:",self.yearMade)
        print("Price:",self.price)
        