from functions import *
name = ""

mcmeta = name + '/pack.mcmeta'
repeat = name + '/data/pack/functions/repeat.mcfunction'
startup = name + '/data/pack/functions/startup.mcfunction'
tick = name + '/data/minecraft/tags/functions/tick.json'
load = name + '/data/minecraft/tags/functions/load.json'
#Do not delete the lines above

open1 = True
while open1:
  selection = select('', [''])
  clear()

  if selection == 0:
    pass

  else:
    open1 = False