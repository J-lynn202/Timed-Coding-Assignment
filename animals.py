class Dog():
    def _init_(self,breed, color, age):
        self._breed = breed
        self._color = color
        self._age = age

    def breed(self):
        return self._breed

    def color(self):
        return self._color

    def age(self):
        return self._age

    def __eq__(self, other):
         if not isinstance(other):
             return False
         return(self._breed == other .self._breed and
                self._color == other .self._color and
                self._age == other .self._age)
   