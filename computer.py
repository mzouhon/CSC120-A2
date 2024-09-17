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

    ##prints all info about computer
    def printAllInfo(self):
        print("Description:",self.description)
        print("Processor Type:",self.processorType)
        print("Hard Drive Capacity:",self.hardDriveCapacity)
        print("Memory:",self.memory)
        print("Operating System:",self.operatingSystem)
        print("Year Made:",self.yearMade)
        print("Price:",self.price)
   

##tester object
danielComputer= Computer(
        description="Dell XPS 13",
        processorType="Intel Core i7",
        hardDriveCapacity="512GB SSD",
        memory=16,  # memory in GB
        operatingSystem="Windows 11",
        yearMade=2023,
        price=1299
    )

moyaComputer=Computer(
   description="Dell XPS 15",
        processorType="Intel Core i8",
        hardDriveCapacity="64GB SSD",
        memory=32,  # memory in GB
        operatingSystem="Windows 12",
        yearMade=2024,
        price=1399 
)

danielComputer.printAllInfo()
moyaComputer.printAllInfo()

# What attributes will it need?

    # How will you set up your constructor?
    # Remember: in python, all constructors have the same name (__init__)
    
    # What methods will you need?
    ##method that allows for printing of all atributes of a computer instance