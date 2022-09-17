from procedural_resale_shop import print_inventory, refurbish, sell, update_price


class Computer:

    # What attributes will it need?
    class Computer:

    #All information about a computer is stored here
        def __init__(self, description: str,
                        processor_type: str,
                        hard_drive_capacity: int,
                        memory: int,
                        operating_system: str,
                        year_made: int,
                        price: int
                        ):
            self.computer = {'description': description,
            'processor_type': processor_type,
            'hard_drive_capacity': hard_drive_capacity,
            'memory': memory,
            'operating_system': operating_system,
            'year_made': year_made,
            'price': price}
        
        #This method will return the attributes of a computer when called.
        def get_attribute(self, attribute):
            if attribute == "all attributes":
                # return all existing information of the computer
                return self.computer
            else:
                # only returns the specific attribute being called
                return self.computer[attribute]
        
        #This method updates the attribute of a computer
        def update_attribute(self, attribute, updated_value):
            self.computer[attribute] = updated_value
        

    
        

