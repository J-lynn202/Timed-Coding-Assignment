class Rescue():
    def __init__(self):
        self.capatiy = 0
        self.dog = []

    def capacity(self):
        return self._capacity

    def capacity(self,value):
        self._capacity = value

    def dogs(self):
        return self._dogs
    def add_dog(self,dog):
        if len(self._dog)< self._capacity:
            self._dogs. append(dog)