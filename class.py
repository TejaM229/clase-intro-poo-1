#--------Class,methods,atributes, objects--------------------------------
class Vehicle:
    def __init__(self, make, model, color):
        self.make = make
        self.model = model
        self.color = color
        self.is_running = False
    
    def start_engine(self):
        self.is_running = True
        print("The vehicle has started.")
    
    def stop_engine(self):
        self.is_running = False
        print("The vehicle has stopped.")
    
    def change_color(self, new_color):
        self.color = new_color
        print(f"The vehicle is now {self.color}.")

vehicle1 = Vehicle("peugeot","301","Blanco")
print (vehicle1.make, vehicle1.color, vehicle1.model)

vehicle1.start_engine()
vehicle1.change_color("Red")

