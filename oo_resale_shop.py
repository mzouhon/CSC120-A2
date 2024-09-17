from typing import Dict 
from typing import Optional
from computer import Computer

##decided to use dictionary over lists in order to easily be able to access items by ID

class ResaleShop:

    ##initializes inventory list of computers and ID num
    def __init__(self):
        self.inventory: Dict[int, Computer]
        self.itemID: int=0
        
    ##allows for the buying of computer and addition to inventory
    def buy(self,computer:Computer):
        itemID += 1 # increment itemID
        self.inventory[itemID] = computer
        return itemID
   
    #allows for price of a computer to be updated from resale shop class
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
    
    ##prints item id and name of each computer on inventory   
    def printInventory(self):
     if self.inventory:
        # For each item
        for itemID in self.inventory:
            # Print its details
            print(f'Item ID: {itemID} : {self.inventory[itemID]}')
     else:
        print("No inventory to display.")
   
    ##refurbish
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