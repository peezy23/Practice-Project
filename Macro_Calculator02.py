''' PROJECT 1 REMAKE (CLASS VERSION): MACRO CALCULATOR '''

# SECOND DRAFT:

# TURN The first version of Macro Calculator into a class


class Macro:
    ''' Represent a calulator to calculate a person macro '''

    def __init__(self, gender, age, height, weight, active):
        ''' Initializing attributes '''

        self.gender = gender
        self.age = age
        self.height = height
        self.weight = weight
        self.active = active
        self.macro = 0

        self.active_level = {'Sedentary': 1.2, 'Lightly Active': 1.375,
                            'Moderate Active': 1.55, 'Very Active': 1.725,
                            'Extremely Active': 1.9}

    def calculate(self):
        global active_level

        if self.gender == 'male':
            macro = (10*self.weight) + (6.25*self.height) - (5*self.age) + 5

        elif self.gender == 'female':
            macro = (10*self.weight) + (6.25*self.height) - (5*self.age) - 161

        if self.active in self.active_level:
            self.macro = macro * self.active_level[self.active]

        return self.macro

    def show_result(self):
        print(self.macro)
