from datetime import datetime

class Device:
    def __init__(self, name):
        self.name = name
        self.is_on = False
    
    def turn_on(self):
        self.is_on = True
        print(f"{self.name} is now ON.")
    
    def turn_off(self):
        if self.is_on:
            self.is_on = False
            print(f"{self.name} is now OFF. Turned off at {datetime.now()}.")
        else:
            print(f"{self.name} is already OFF.")

# Example usage
device = Device("Lamp")
device.turn_on()   # Lamp is now ON.
device.turn_off()  # Lamp is now OFF. Turned off at YYYY-MM-DD HH:MM:SS.
