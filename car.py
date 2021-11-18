class Car(object):
    def __init__(self, model, color, wheelSize, company, speedLimit):
        self.model = model
        self.color = color
        self.wheelSize = wheelSize
        self.company = company
        self.speedLimit = speedLimit
        
    def start(self):
        print("Started")
    
    def stop(self):
        print("Stopped")
        
toyota = Car("A6B6", "Red", 20, "Toyota", 100)
toyota.start()
print(toyota.color)