#-- BITBOT All moves python test 
#-- BITBOT is based on OttoDIY Python Project, 2023

import bot as bot, time

#Left leg 13
#Right leg 12    
#Left Foot 14
#Right Foot 27

# -- Constants
FORWARD  = const(1)
BACKWARD = const(-1)
LEFT     = const(1)
RIGHT    = const(-1)
SMALL    = const(5)
MEDIUM   = const(15)
BIG      = const(30)

BitBot = bot.Bitbot()
BitBot.init(13, 12, 14, 27, True, 0)
BitBot.home()

BitBot.walk(2, 1000, FORWARD)         #-- 2 steps, "TIME". IF HIGHER THE VALUE THEN SLOWER (from 600 to 1400), 1 FORWARD
BitBot.walk(2, 1000, BACKWARD)        #-- 2 steps, T, -1 BACKWARD 
BitBot.turn(2, 1000, LEFT)            #-- 3 steps turning LEFT
BitBot.home()
time.sleep_ms(100)  
BitBot.turn(2, 1000, RIGHT)           #-- 3 steps turning RIGHT 
BitBot.bend(1, 500, LEFT)             #-- usually steps =1, T=2000
BitBot.bend(1, 2000, RIGHT)     
BitBot.shakeLeg(1, 1500, LEFT)
BitBot.home()
time.sleep_ms(100)
BitBot.shakeLeg(1, 2000, RIGHT)
BitBot.moonwalker(3, 1000, 25, LEFT)  #-- LEFT
BitBot.moonwalker(3, 1000, 25, RIGHT) #-- RIGHT  
BitBot.crusaito(2, 1000, 20, LEFT)
BitBot.crusaito(2, 1000, 20, RIGHT)
time.sleep_ms(100)
BitBot.flapping(2, 1000, 20, LEFT)
BitBot.flapping(2, 1000, 20, RIGHT)
time.sleep_ms(100)
BitBot.swing(2, 1000, 20)
BitBot.tiptoeSwing(2, 1000, 20)
BitBot.jitter(2, 1000, 20)            #-- (small T)
BitBot.updown(2, 1500, 20)            #-- 20 = H "HEIGHT of movement"T 
BitBot.ascendingTurn(2, 1000, 50)
BitBot.jump(1, 2000)

BitBot.home()

#end
