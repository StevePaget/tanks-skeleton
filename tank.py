# Tank game
from pygame_functions import *
import math


screenSize(1000,700)
setBackgroundImage("battlefield.png")
wall=makeSprite("wall.png")
moveSprite(wall,480,400)
showSprite(wall)


tankSprites = [None, makeSprite("redtank.png"), makeSprite("bluetank.png")]
keys = [None,  ("w", "s", "a", "d", "space") , ("up","down","left", "right", "return") ]
startPositions = [None, 100,800]
startAngles = [None, -45, -145]
rotationAngles = [None, -5, 5]

class Tank():
    def __init__(self, playerNumber):
        self.playerNumber = playerNumber
        self.keys = keys[playerNumber]
        self.sprite = tankSprites[playerNumber]
        addSpriteImage(self.sprite, "explosion.png")
        showSprite(self.sprite)
        self.x = startPositions[playerNumber]
        self.y = 600
        self.angle = startAngles[playerNumber]
        self.rotationAngle = rotationAngles[playerNumber]
        self.barrel = makeSprite("barrel.png")
        showSprite(self.barrel)
        self.firing = False
        self.power = 20
        self.powerText = makeLabel("Power: 0", 20, self.x, self.y - 100)
        showLabel(self.powerText)
        self.alive=True
        self.draw()
        
        
    def draw(self):
        moveSprite(self.sprite, self.x, self.y, centre=True)
        moveSprite(self.barrel, self.x, self.y, centre=True)
        moveLabel(self.powerText, self.x, self.y - 100)
        transformSprite(self.barrel, self.angle, 1)
                
    def update(self):
        self.draw()
        return True


players = [Tank(1), Tank(2)]

gameOn = True
while gameOn:
    for p in players:
            p.update()
    tick(60)

gameOverText = makeLabel("Game Over", 90,10,10)
showLabel(gameOverText)
print("end")
endWait()


