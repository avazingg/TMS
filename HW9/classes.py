from abc import ABC, abstractmethod

class Device(ABC):

    def __init__(self, brand:str, year_of_production: int, color:str):
        self._brand = brand
        self._year_of_production = year_of_production
        self._color = color
        self._is_power_on = False

    def switch_device(self):
        if self._is_power_on:
            self._is_power_on = False
        else:
            self._is_power_on = True

    # @abstractmethod
    # def __str__(self):
    #    pass

class Mobile(Device):

    def __init__(self, brand, year_of_production, color, model, memory):
        super().__init__(brand, year_of_production, color)
        self.__model = model
        self.__memory = memory

    def set_phone_model(self, mod: str):
        self.__model = mod

    def set_phone_memory(self, mem: str):
        self.__memory = mem

    def get_phone_model(self):
        return self.__model

    def get_phone_memory(self):
        return self.__memory

    def __str__(self):
        return (f"Brand: {self._brand};"
                f" Release date: {self._year_of_production};"
                f" Color: {self._color};"
                f" Power: {'Turned on' if self._is_power_on else 'Turned off'};"
                f" Model: {self.__model}; Memory: {self.__memory}.")


class Laptop(Device):

    def __init__(self, brand, year_of_production, color, battery, memory):
        super().__init__(brand, year_of_production, color)
        self.__battery = battery
        self.__memory = memory

    def __str__(self):
        return (f"Brand: {self._brand};"
                f" Release date: {self._year_of_production};"
                f" Color: {self._color};"
                f" Power: {'Turned on' if self._is_power_on else 'Turned off'};"
                f" Model: {self.__battery}; Memory: {self.__memory}.")

    def set_laptop_battery(self, bat:str):
        self.__battery = bat

    def set_laptop_memory(self, mem:str):
        self.__memory = mem

    def get_laptop_battery(self):
        return self.__memory

    def get_laptop_memory(self):
        return self.__battery


class Computer(Device):

    def __init__(self, brand, year_of_production, color, is_for_gaming:bool, memory:str):
        super().__init__(brand, year_of_production, color)
        self.__is_for_gaming = is_for_gaming
        self.__memory = memory

    def __str__(self):
        return (f"Brand: {self._brand};"
                f" Release date: {self._year_of_production};"
                f" Color: {self._color};"
                f" Power: {'Turned on' if self._is_power_on else 'Turned off'};"
                f" Model: {self.__is_for_gaming};"
                f" Memory: {self.__memory}.")


    def set_computer_gaming_status(self, gaming:bool):
        self.__is_for_gaming = gaming

    def set_computer_memory(self, mem:str):
        self.__memory = mem

    def get_computer_gaming_status(self):
        return self.__is_for_gaming

    def get_computer_memory(self):
        return self.__memory

if __name__ == "__main__":

    # init devices
    iphone = Mobile(brand = "Iphone", year_of_production=2024, color="Midnight blue", model="15 Pro", memory="256GB")
    lenovo_laptop = Laptop(brand="Lenovo", year_of_production=2021, color="black", battery="10000 mah", memory="1TB")
    gaming_pc = Computer(brand="super-puper", year_of_production=2024, color="red", is_for_gaming= True, memory="8TB")

    # print devices
    print(iphone.__str__())
    print(lenovo_laptop.__str__())
    print(gaming_pc.__str__())

    # print brand of Mobile, change power status and print the instance again
    print(iphone._brand)
    iphone.switch_device()
    print("We turned the phone on")
    print(iphone.__str__())


    lenovo_laptop.set_laptop_battery("12000 mah")
    lenovo_laptop.set_laptop_memory("2TB")
    print("We changed laptop: memory and battery")
    print(lenovo_laptop.get_laptop_battery(), lenovo_laptop.get_laptop_memory())
    print(lenovo_laptop.__str__())

    print("We changed computer:  gaming status and memory")
    gaming_pc.set_computer_gaming_status(False)
    gaming_pc.set_computer_memory("6TB")
    print("Is for gaming:", gaming_pc.get_computer_gaming_status(),"New memory:", gaming_pc.get_computer_memory())
    print(gaming_pc.__str__())


