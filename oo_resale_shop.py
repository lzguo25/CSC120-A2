from os import remove
from procedural_resale_shop import refurbish, buy, update_price, sell, print_inventory
from typing import Dict, Union, Optional
from computer import *

#Resale methods init(), buy(), update_price(),sell(), print_inventory(), refurbish()
class ResaleShop:
    
    # What attributes will it need?
    def __init__(self):
        self.inventory : Dict[int, Dict[str, Union[str, int, bool]]] = {} 
        self.itemID = 0
  

    #The method buy() is when a computer is bought by the store and an itemID is added to the inventory.
    def buy(self, computer: Dict[str, Union[str, int, bool]]):
        # global itemID
        self.itemID += 1 # increment itemID
        self.inventory[self.itemID] = computer

        print("Buying", computer.get_attribute("description"))
        print("Adding to inventory...")
        print("Done.\n") 

        #returns itemID
        return self.itemID

    #sell() takes in an item_id and removes it from the inventory if it's there. It will print an error message if the item is not in the inventory.
    def sell(self, item_ID: int):
        print("Selling Item ID:", item_ID)
        if item_ID in self.inventory:
            del self.inventory[item_ID]
            print("Item", item_ID, "sold!")
        else: 
            print("Item", item_ID, "not found. Please select a different item.")


    #update_price() takes the item_id of a computer and a new price and updates the price of the item if it's in the inventory. It will print an error message otherwise.
    def update_price(self, item_ID: int, new_price: int):
        if item_ID in self.inventory:
            self.inventory[item_ID]["price"] = new_price
        else:
            print("Item", item_ID, "not found. Updating price failed.")

    
    

   #This method prints out the entire inventory. If there is nothing then it will print that the inventory is empty.
    def print_inventory(self):
        # If the inventory is not empty
        print("Checking inventory...")
        if self.inventory:
            # For each item
            for item_ID in self.inventory:
                # Prints out attributes and details about computer
                print(f'Item ID: {item_ID} : {self.inventory[item_ID].get_attribute("all attributes")}')
        else:
            print("The inventory is empty.")
        print("Done.\n")


    #This method takes in the item_ID of a computer and assigns a price for how much it can be sold for. It also updates the OS. Only works for items in inventory.
    def refurbish(self, item_ID: int, new_os: Optional[str] = None):
        if item_ID in self.inventory:
            computer = self.inventory[item_ID] # identifies the computer in the inventory
            if int(computer.get_attribute("year_made")) < 2000:
                computer.update_attribute("price", 0) # too old to sell, donation only
            elif int(computer.get_attribute("year_made")) < 2012:
                computer.update_attribute("price", 250) # heavily-discounted price on machines 10+ years old
            elif int(computer.get_attribute("year_made")) < 2018:
                computer.update_attribute("price", 550) # discounted price on machines 4-to-10 year old machines
            else:
                computer.update_attribute("price", 1000) # recent stuff

            if new_os is not None:
                computer.update_attribute("operating_system", new_os) # update details after installing new OS
        else:
            print("Item", item_ID, "not found. Please select another item to refurbish.")
        print("Done.\n")