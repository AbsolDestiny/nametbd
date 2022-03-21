class Character:
    '''Used to define characters'''
    def __init__(self, name, level=1, strength=0, defence=0, speed=0, hitpoints=20):
        self.name = name
        self.level = level
        self.strength = strength
        self.defence = defence
        self.speed = speed
        self.hitpoints = hitpoints
