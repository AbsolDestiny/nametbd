class Weapon:
    '''Weapon class is used to set a weapons characteristics.'''
    def __init__(self, name, level=1, damage=0, speed='fast'):
        self.name = name
        self.level = level
        self.damage = damage
        self.speed = speed
    
    def damage_modifier_2h(self):
        '''Damage modifier for 2H Weapons'''
        return (self.damage*(strength/55+1))
    
    def damage_modifier_1h(self):
        '''Damage modifier for 1H Weapons'''
        return (self.damage*(strength/80+0.9))
    
    def damage_modifier_off_hand(self):
        '''Damage modifier for off-hand weapons'''
        return (self.damage*(strength/80+0.75))

