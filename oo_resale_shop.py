from typing import Dict 
from typing import Optional
from computer import Computer

##resale shop that allows for resale shop intances to be created and controls what each shop is able to do in relation to the computer class

class ResaleShop:

    ##initializes inventory list of computers and ID number count
    def __init__(self):
        self.inventory: Dict[int, Computer]= {}
        self.itemID: int=0
        
    ##allows for the buying of computers and addition to inventory
    def buy(self,computer:Computer):
        self.itemID += 1 # increment itemID
        self.inventory[self.itemID] = computer
        return self.itemID
   
    ##allows for price of a computer to be updated from resale shop class
    def updatePrice(self, itemID:int, newPrice:int):
     if itemID in self.inventory:
        computer=self.inventory[itemID]
        computer.price=newPrice
     else:
        print("Item", itemID, "not found. Cannot update price.")
        
    ## sells computer and rids inventory of that computer
    def sell(self,itemID: int):
     if itemID in self.inventory:
        del self.inventory[itemID]
        print("Item", itemID, "sold!")
     else: 
        print("Item", itemID, "not found. Please select another item to sell.") 
    
    ##prints item id of each computer on inventory   
    def printInventory(self):
     if self.inventory:
        # For each item
        for itemID in self.inventory:
            # Print its details
            print(f'Item ID: {itemID} : {self.inventory[itemID]}')
     else:
        print("No inventory to display.")
   
    ##refurbishes computers, allows price to be updated based on year made and allows for the updating of the OS variable
    def refurbish(self, itemID: int, newOS: Optional[str] = None):
     if itemID in self.inventory:
        computer = self.inventory[itemID] # locate the computer
        if computer.yearMade < 2000:
            computer.price = 0 # too old to sell, donation only
        elif computer.yearMade < 2012:
            computer.price = 250 # heavily-discounted price on machines 10+ years old
        elif computer.yearMade < 2018:
            computer.price = 550 # discounted price on machines 4-to-10 year old machines
        else:
            computer.price = 1000 # recent stuff

        if newOS is not None:
            computer.operatingSystem = newOS # update details after installing new OS
     else:
         print("Item", itemID, "not found. Please select another item to refurbish.")


##tester objects
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

acerComputer = Computer(
    description="Acer Swift 3",
    processorType="Intel Core i5",
    hardDriveCapacity="256GB SSD",
    memory=8,  # memory in GB
    operatingSystem="Windows 10",
    yearMade=2020,
    price=699
)

hpComputer = Computer(
    description="HP Spectre x360",
    processorType="Intel Core i7",
    hardDriveCapacity="512GB SSD",
    memory=16,  # memory in GB
    operatingSystem="Windows 11",
    yearMade=2021,
    price=1199
)

lenovoComputer = Computer(
    description="Lenovo ThinkPad X1 Carbon",
    processorType="Intel Core i7",
    hardDriveCapacity="1TB SSD",
    memory=16,  # memory in GB
    operatingSystem="Windows 11",
    yearMade=2022,
    price=1399
)

macBookComputer = Computer(
    description="Apple MacBook Pro 14",
    processorType="Apple M1 Pro",
    hardDriveCapacity="512GB SSD",
    memory=16,  # memory in GB
    operatingSystem="macOS Monterey",
    yearMade=2021,
    price=1999
)

asusComputer = Computer(
    description="ASUS ROG Zephyrus G14",
    processorType="AMD Ryzen 9",
    hardDriveCapacity="1TB SSD",
    memory=32,  # memory in GB
    operatingSystem="Windows 11",
    yearMade=2023,
    price=2299
)

def main():
    myComputerShop=ResaleShop()
    myComputerShop.printInventory()
    myComputerShop.buy(moyaComputer)
    myComputerShop.buy(danielComputer)
    myComputerShop.buy(acerComputer)
    myComputerShop.buy(hpComputer)
    myComputerShop.buy(lenovoComputer)
    myComputerShop.buy(macBookComputer)
    myComputerShop.buy(asusComputer)
    myComputerShop.printInventory()
    myComputerShop.sell(8)
    print()
    print()
    moyaComputer.printAllInfo()
    myComputerShop.refurbish(1,"Windows 13")
    print()
    moyaComputer.printAllInfo()
    print()
    print()
    myComputerShop.sell(2)
    myComputerShop.sell(2)
    myComputerShop.sell(5)
    myComputerShop.printInventory()
    print()
    print()
    acerComputer.printAllInfo()
    myComputerShop.updatePrice(3,200)
    print()
    acerComputer.printAllInfo()

main()