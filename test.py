import minecraft.minecraft as minecraft
import minecraft.block as block
import time
from enum import Enum

print 'hello chair'

class MineCraftChair:
    blockType = 0
    ledColor = 0
    fanOn = false
    heatOn = false
    

# test post
mc = minecraft.Minecraft.create()
mc.postToChat("Hello Minecraft Chair!")
time.sleep(5)

# test player
#playerPos = mc.player.getPos()
#mc.player.setPos(playerPos.x,playerPos.y + 80,playerPos.z)
#mc.postToChat("You're flying! Don't look down")
#time.sleep(5)

# blocks

for x in range(0,1):
    # get tile player is standing on
    playerTilePos = mc.player.getTilePos()
    blockBelowPlayer = mc.getBlock(playerTilePos.x, playerTilePos.y - 1, playerTilePos.z)
    # update chair status
    print("You are standing on: " + str(blockBelowPlayer))
    time.sleep(5)


