from random import randint


class Weapon:
    '''Weapon class is used to set a weapons characteristics.'''
    def __init__(self, name, level=1, damage=0):
        self.name = name
        self.level = level
        self.damage = damage
    
    def damage_modifier_2h(self):
        return (self.damage*(strength/10+1))
    
    def damage_modifier_1h(self):
        return (self.damage*(strength/20+0.75))

strength = 10

steel_dagger = Weapon("steel_dagger", damage=100)
steel_sword_2h = Weapon("2H Steel Sword", damage=100).damage_modifier_2h()

print(steel_dagger.damage_modifier_1h())
print(steel_sword_2h)
