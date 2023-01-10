from functions import *
name = ""

mcmeta = name + '/pack.mcmeta'
repeat = name + '/data/pack/functions/repeat.mcfunction'
startup = name + '/data/pack/functions/startup.mcfunction'
main = name + '/data/main/advancements'
side = name + '/data/side/advancements'
structures = name + '/data/pack/structures'
worldgen = name + '/data/pack/worldgen'
tick = name + '/data/minecraft/tags/functions/tick.json'
load = name + '/data/minecraft/tags/functions/load.json'

addFile(main, 'root.json', '{"display": {"title": {"text": "' + name + ' main questline"},"description": {"text": "This will show the main questline of ' + name + '"},"icon": {"item": "minecraft:map"},"frame": "task","show_toast": false,"announce_to_chat": false,"hidden": false,"background": "minecraft:textures/gui/advancements/backgrounds/stone.png"},"criteria": {"quest": {"trigger": "minecraft:tick"}}}')
addFile(side, 'root.json', '{"display": {"title": {"text": "' + name + ' side quests"},"description": {"text": "This will show the side quests of ' + name + '"},"icon": {"item": "minecraft:map"},"frame": "task","show_toast": false,"announce_to_chat": false,"hidden": false,"background": "minecraft:textures/gui/advancements/backgrounds/stone.png"},"criteria": {"quest": {"trigger": "minecraft:tick"}}}')

clear()
open1 = True
while open1:
  selection = select('What do you want to add?', ['Quest', 'Structure'])

  if selection == 0:
    selection = select('What type of quest is this?', ['Side', 'Main'])
    if selection == 0:
      questName = ask('What is the name of the quest?')
      simpleName = ask('What will the simple name of this quest be?')
      description = ask('Discribe how to get to the quest?')
      icon = ask('What item would you like to be displayed as the icon of the quest?')

      advancement = '{ "display": { "title": { "text": "' + questName + '" }, "description": { "text": "' + description + '" }, "icon": { "item": "minecraft:' + icon + '" }, "frame": "task", "show_toast": true, "announce_to_chat": false, "hidden": false }, "criteria": { "quest": {"trigger": "minecraft:impossible"}},"parent": "side:root"}'
      write_(f'{side}/{simpleName}.json', advancement + '\n', 'a')

    if selection == 1:
      questName = ask('What is the name of the quest?')
      simpleName = ask('What will the simple name of this quest be?')
      description = ask('Discribe how to get to the quest?')
      icon = ask('What item would you like to be displayed as the icon of the quest?')
      last = ask('What was the last quest before this one?')

      advancement = '{ "display": { "title": { "text": "' + questName + '" }, "description": { "text": "' + description + '" }, "icon": { "item": "minecraft:' + icon + '" }, "frame": "task", "show_toast": true, "announce_to_chat": false, "hidden": false }, "criteria": { "quest": {"trigger": "minecraft:impossible"}},"parent": "main:' + last + '"}'
      write_(f'{main}/{simpleName}.json', advancement + '\n', 'a')
    
  if selection == 1:
    structureName = ask('What is the name of your structure?')
    write_('paste.txt', '', 'w')
    ask('Paste the nbt data for your structure in the "paste.txt" file')
    data = read_('paste.txt', False)
    remove('paste.txt')

    addFile(structures + '/' + structureName, 'main.nbt', data)
    data = '{"name":"pack:' + structureName + '/main","fallback":"minecraft:empty","elements":[{"weight":1,"element":{"projection":"rigid","element_type":"single_pool_element","location":"pack:' + structureName + '/main","processors":"minecraft:empty"}}]}'
    addFile(worldgen + '/' + structureName, 'main.json', data)
    data = '{"config":{"start_pool": "pack:' + structureName + '/main","size":7},"type":"minecraft:village"}'
    addFile(worldgen + '/configured_structure_feature', structureName + '.json', data)
    # data = '{"config":{"start_pool": "pack:' + structureName + '/main","size":7},"type":"minecraft:village"}'
    # addFile(worldgen + '/biome', 'plains.json', data)

  else:
    open1 = False

  clear()