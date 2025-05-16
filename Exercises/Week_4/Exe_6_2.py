from Exe_6_1 import Car

class Main :
    def run (self) :
        car1 = Car("Toyota", 2023)
        car2 = Car(color="Red", brand="Ford", year=2018)
        print(car1.description()) # Toyota (2023)
        print(car2.description()) # Ford (2018)
        print(car1.is_new()) # True
        print(car2.is_new()) # False

if __name__ == "__main__":
    main = Main()
    main.run()

