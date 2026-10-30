class Vehicle:
    def start(self):
        print("Vehicle Started")
    def stop(self):
        print("Vehicle Stopped")

class Car(Vehicle):
    def drive(self):
        print("Car Driving")

car1 = Car()
car1.start()
car1.drive()
car1.stop()
