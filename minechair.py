# -*- coding: utf-8 -*-
import minecraft.minecraft as minecraft
import minecraft.block as block
import time
from ledlib import LedLib

DEBUGLEVEL = 3
TIMELEN = 120

def log(msg, level):
    if (level <= DEBUGLEVEL):
        print msg

print 'hello chair'

class MineCraftChair:
    # instance vars
    myBlockType = block.AIR
    dict = {}
    LED = LedLib()
    # constructor
    def __init__(self):
        # color, fanStrength, heatStrength, description
        self.dict[block.AIR.id] = (self.LED.CYAN, 10, -3, "Air")
        self.dict[block.STONE.id] = (LedLib.CYAN, 0, 0, "Stone")
        self.dict[block.GRASS.id] = (LedLib.GREEN, 0, 0, "Grass")
        self.dict[block.DIRT.id] = (LedLib.RED, 0, -2, "Dirt")
        self.dict[block.COBBLESTONE.id] = (LedLib.CYAN, 0, 0, "Cobblestone")
        self.dict[block.BEDROCK.id] = (LedLib.RED, 0, 0, "Bedrock")
        self.dict[block.WATER.id] = (LedLib.BLUE, 0, -5, "Water")
        self.dict[block.WATER_STATIONARY.id] = (LedLib.BLUE, 0, -5, "Water Stationary")
        self.dict[block.LAVA.id] = (LedLib.RED, 0 , 10, "Lava")
        self.dict[block.LAVA_STATIONARY.id] = (LedLib.RED, 0 , 10, "Lava Stationary")
        self.dict[block.SAND.id] = (LedLib.YELLOW, 0, 0, "Sand")
        self.dict[block.GRAVEL.id] = (LedLib.RED, 0, 0, "Gravel")
        self.dict[block.WOOD.id] = (LedLib.RED, 0, 0, "Wood")
        self.dict[block.LEAVES.id] = (LedLib.GREEN, 0, 0, "Leaves")
        self.dict[block.GLASS.id] = (LedLib.WHITE, 0, 0, "Glass")
        self.dict[block.SANDSTONE.id] = (LedLib.YELLOW, 0, 0, "Sandstone")
        self.dict[block.BED.id] = (LedLib.RED, 0, 0, "Bed")
        self.dict[block.FLOWER_YELLOW.id] = (LedLib.YELLOW, 0, 0, "Flower Yellow")
        self.dict[block.GOLD_BLOCK.id] = (LedLib.YELLOW, 0, 0, "Gold")
        self.dict[block.IRON_BLOCK.id] = (LedLib.CYAN, 0, 0, "Iron")
        self.dict[block.BRICK_BLOCK.id] = (LedLib.RED, 0, 0, "Brick")
        self.dict[block.SNOW.id] = (LedLib.WHITE, 0, -10, "Snow")
        self.dict[block.ICE.id] = (LedLib.CYAN, 0, -10, "Ice")
        self.dict[block.SNOW_BLOCK.id] = (LedLib.WHITE, 0, -10, "Snow block")
        self.dict[block.GLOWSTONE_BLOCK.id] = (LedLib.RED, 0, 10, "Glowstone")
        self.dict[block.STONE_BRICK.id] = (LedLib.RED, 0, 0, "Stone Brick")
        self.dict[block.GLOWING_OBSIDIAN] = (LedLib.RED, 0, 0, "Glowing Obsidian")
        


        # init LED Library
        self.LED.led_setup()
        self.LED.led_clear() 
    
    def update(self, blockType):
        if (self.myBlockType != blockType):
            self.myBlockType = blockType
            log("Chair's block updated: " + str(self.myBlockType),2)
            if (self.dict.has_key(self.myBlockType)):
                log("Chair's value updated: " + str(self.dict[self.myBlockType]),2)
                
                # set LED color
                value = self.dict[self.myBlockType]
                log("Setting chair's color to: " + str(value[0]), 2)
                self.LED.led_clear()
                self.LED.led_activate_all(value[0])

                # TODO: Set fan strength
                # TODO: Set heat strength
                # TODO: Set scent


            else:
                log("Unknown block type: " + str(self.myBlockType), 1)
                log("Setting chair's color to none", 3)
                self.LED.led_clear()


    def cleanup(self):
        self.LED.led_clear()
        self.LED.cleanup()

# test post
mc = minecraft.Minecraft.create()
mc.postToChat("Hello Minecraft Chair. And hello there Tobin!")
time.sleep(2)

# test player
#playerPos = mc.player.getPos()
#mc.player.setPos(playerPos.x,playerPos.y + 80,playerPos.z)
#mc.postToChat("You're flying! Don't look down")
#time.sleep(5)

# chair
myChair = MineCraftChair()

# blocks

for x in range(0,TIMELEN):
    playerTilePos = mc.player.getTilePos()
    blockBelowPlayer = mc.getBlock(playerTilePos.x, playerTilePos.y - 1, playerTilePos.z)
    log("You are standing on: " + str(blockBelowPlayer),4)
    myChair.update(blockBelowPlayer)
    time.sleep(1)


# cleanup
myChair.cleanup()

