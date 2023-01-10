from functions import *
name = ""

mcmeta = name + '/pack.mcmeta'
repeat = name + '/data/pack/functions/repeat.mcfunction'
startup = name + '/data/pack/functions/startup.mcfunction'
tick = name + '/data/minecraft/tags/functions/tick.json'
load = name + '/data/minecraft/tags/functions/load.json'

if not 'scoreboard objectives add enabled dummy' in read_(startup, False):
  write_(startup, 'scoreboard objectives add enabled dummy\n','a')

clear()
open1 = True
while open1:
  name = ask('Please type the name of your qol feature:')
  line = ask('Please type a basic line to start off your feature:')
  write_(startup, f'scoreboard objectives add use_{name} trigger\n', 'a')
  write_(repeat, f'scoreboard players enable @a[tag=admin] use_{name}\nexecute as @a[scores=' + '{use_' + name + '=1..}' + f'] run scoreboard players add {name} enabled 1\nexecute if score {name} enabled matches 2.. run scoreboard players set {name} enabled 0\nscoreboard players set @a use_{name} 0\nexecute if score {name} enabled matches 1 run {line}\n', 'a')
  clear()
