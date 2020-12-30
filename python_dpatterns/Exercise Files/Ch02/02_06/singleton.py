class Borg:
    """Borg clas making class attributes global"""
    _shared_state = {} #Attribute dictionary

    def __init__(self):
        self.__dict__ = self._shared_state #make it an attribute dictionary
        

class Singleton(Borg): 
    """This class now shares all its attributes among its various instances
    This essentially makes the singleton objects an object-oriented global variable"""
   
    def __init__(self, **kwargs):
        Borg.__init__(self)
       #Update the attribute dictionary by inserting a new key-value pair

        self._shared_state.update(kwargs)

    def __str__(self):
        #Returns the attribute dictionary for printing
        return str(self._shared_state)

x = Singleton(HTTP = "HyperText transfer Protocol")
print(x)

y = Singleton(SNMP = "Simple Network management protocol")
print(y)