class Person:
    def __init__(self, name, dd, mm, yyyy):
        print('Person object is created.')
        self.name = name
        self.dob = self.Dob(dd, mm, yyyy)

    def info(self):
        print('Name:', self.name)
        self.dob.display()

    class Dob:
        def __init__(self, dd, mm, yyyy):
            print('Dob object is created.')
            self.dd = dd
            self.mm = mm
            self.yyyy = yyyy

        def display(self):
            print('Date of birth is: {}/{}/{}'.format(self.dd, self.mm, self.yyyy))


p = Person('Abhinav', 1, 12, 1950)
p.info()
