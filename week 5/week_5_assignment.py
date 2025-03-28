# Base class: Smartphone
class Smartphone:
    def __init__(self, brand, model, storage, battery_life):
        self.brand = brand
        self.model = model
        self.storage = storage
        self.battery_life = battery_life  # in hours
    
    def call(self, number):
        print(f"{self.brand} {self.model} is calling {number}...")
    
    def charge(self):
        print(f"{self.brand} {self.model} is charging...")

# Subclass 1: AndroidPhone
class AndroidPhone(Smartphone):
    def __init__(self, brand, model, storage, battery_life, android_version):
        super().__init__(brand, model, storage, battery_life)
        self.android_version = android_version
    
    def google_assistant(self):
        print(f"{self.brand} {self.model} is using Google Assistant!")

# Subclass 2: iPhone
class iPhone(Smartphone):
    def __init__(self, model, storage, battery_life, ios_version):
        super().__init__("Apple", model, storage, battery_life)
        self.ios_version = ios_version
    
    def siri(self):
        print(f"iPhone {self.model} is activating Siri!")

# Creating objects
samsung = AndroidPhone("Samsung", "Galaxy S22", "256GB", 24, "Android 12")
iphone = iPhone("iPhone 14", "128GB", 20, "iOS 16")

# Testing methods
samsung.call("0703-456-789")
samsung.google_assistant()
iphone.call("0707-654-321")
iphone.siri()
