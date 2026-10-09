
class GameSettings:
    def __init__(self):
        self.volume = 50


settings1 = GameSettings()
settings2 = GameSettings()

settings1.volume = 80

print(settings1.volume)
print(settings2.volume)
print(settings1 is settings2)

