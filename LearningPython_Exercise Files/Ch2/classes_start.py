#
# Example file for working with classes
#
class Someclass():
    def somemethod(self):
        print('somemethod')

    def somemethod2(self, somestring):
        print(f'{somestring} added')

class Inheritingclass(Someclass):
    def newmethod(self):
        Someclass.somemethod2(self, 'John')
        print('Howdy?')


def main():
    c = Someclass()
    c.somemethod()
    c.somemethod2('hello')
    c2 = Inheritingclass()
    c2.newmethod()


if __name__ == "__main__":
    main()
