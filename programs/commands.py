from functions import *
name = ""

mcmeta = name + '/pack.mcmeta'
repeat = name + '/data/pack/functions/repeat.mcfunction'
startup = name + '/data/pack/functions/startup.mcfunction'
tick = name + '/data/minecraft/tags/functions/tick.json'
load = name + '/data/minecraft/tags/functions/load.json'

clear()
open1 = True
while open1:
  name = ask('Please type the name of your command:')
  line = ask('Please type a basic line to start off your command:')
  selection = select('Who can run this command?', ['All players', 'Admins'])
  if selection == 0:
    players = ''

  else:
    players = '[tag=admin]'

  write_(startup, f'scoreboard objectives add {name} trigger\n', 'a')
  write_(repeat, f'scoreboard players enable @a{players} {name}\nexecute as @a[scores=' + '{' + name + '=1..}' + f'] run {line}\nscoreboard players set @a {name} 0', 'a')
  clear()