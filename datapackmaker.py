print('Loading...')
from os import makedirs, listdir, remove, removedirs, system
known_versions = ['1.19']


# try:
#   cache = 'programs/__pycache__'
#   for i in listdir(cache):
#     remove(cache + '/' + i)
#   removedirs(cache)

# except:
#   pass

try:
  remove('update.py')

except:
  pass

try:
  remove('newFunctions.py')

except:
  pass

with open('newFunctions.py', 'w') as file:
  with open('functions.py', 'r') as file2:
    file.write(file2.read())

from newFunctions import *
remove('newFunctions.py')

engines = []
x = 0
write_('updater.py', 'from functions import *\ndef run(program, name):', 'w')
for i in listdir('programs'):
  if i[-3:] == '.py':
    path = 'programs/' + i
    name = i[:-3]
    engines.append(name)
    lines = read_(path, True)
    lines.remove('from functions import *\n')
    lines.remove('name = ""\n')
    write_('updater.py', f'\n  if program == {x}:\n    {"    ".join(lines)}', 'a')
    print(f'Updated and loaded {name} for using')

    x += 1

engines.append('Create engine')
import updater
remove('updater.py')

clear()
while True:
  print('What is the name of your datapack?')
  name = input('')

  mcmeta = name + '/pack.mcmeta'
  repeat = name + '/data/pack/functions/repeat.mcfunction'
  startup = name + '/data/pack/functions/startup.mcfunction'
  tick = name + '/data/minecraft/tags/functions/tick.json'
  load = name + '/data/minecraft/tags/functions/load.json'

  try:
    description = eval(read_(mcmeta, False))['pack']['description']
    version = '1.1' + str(eval(read_(mcmeta, False))['pack']['pack_format'])

  except:
    makedirs(name + '/data/pack/functions')
    makedirs(name + '/data/minecraft/tags/functions')
    write_(repeat, '', 'w')
    write_(startup, '', 'w')
    write_(tick, '{"values":["pack:repeat"]}', 'w')
    write_(load, '{"values":["pack:startup"]}', 'w')

    print('Please write a description for your pack: ')
    description = input('')
    print('Please select a version for your pack:')
    version = str(check(['int'], {}))
    write_(mcmeta, '{"pack":{"description":"' + description + '","pack_format":' + version + '}}', 'w')
    version = '1.1' + version


  open_ = True
  while open_:
    selection = select('What engine would you like to run?', engines)
    clear()
    if selection == len(engines) - 1:
      name = ask('What is the name of your engine?')
      write_('programs/' + name + '.py', read_('basecode.txt', False),'w')
      print('New file created in "programs/%s.py"' + name)
      ask('Press enter/return to continue')
      
    if selection == len(engines):
      open_ = False

    else:
      updater.run(selection, name)