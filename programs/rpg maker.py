from functions import *
name = ""

mcmeta = name + '/pack.mcmeta'
repeat = name + '/data/pack/functions/repeat.mcfunction'
startup = name + '/data/pack/functions/startup.mcfunction'
tick = name + '/data/minecraft/tags/functions/tick.json'
load = name + '/data/minecraft/tags/functions/load.json'
triggers = name + '/data/pack/functions/triggers.mcfunction'
animations = name + '/data/minecraft/tags/functions/animations.mcfunction'

open1 = True
while open1:
  selection = select('What would you like to do?', ['Add feature', 'Add trigger'])
  clear()
  if selection == 0:
    open2 = True
    while open2:
      selection = select('What feature would you like to add?', ['Animations/Cutscenes', 'Fight zones', 'Gear', 'Shops'])
      clear()
      
      if selection == 0:
        open3 = True
        while open3: 
          clear()
          tag = ask('Please tag your animation/cutscene')
          selection = select('What would you like to do?', ['Animations', 'Cutscenes'])
          if selection == 0:
            lines = []
            open4 = True
            while open4:
              selection = select('What would you like to do?', ['Add keyframe', 'Add Dialouge', 'View', 'Complete'])

              frame = check('int', {})

              if selection == 0:
                keyName = ask('What is the name of this keyframe?')
                event = selection('What is the keyframe using?', ['Summon', 'Fill', 'Sound', '', '', 'Custom'])

              elif selection == 1:
                selection = select('Do you want to use audio with this?', ['Yes', 'No'])
                if not selection == 2:
                  if selection == 0:
                    sound = ask('What is the audio you would like to use?')
                  
                  text = ask('Type the text that will be sent')
                  selection = select('How would you like the dialouge to be sent?', ['Chat', 'Actionbar', 'Title', 'Subtitle'])
                  if selection == 0:
                    line = f'execute if score {tag} Animations matches {frame} run tellraw @s "{text}"'
              
                    




              elif selection == 2:
                print('\n'.join(lines))
                
                input('Press enter/return to continue')

              else:
                open4 = False

          
          elif selection == 1:
            print('asfafsdasd')

          else:  
            open3 = False

      else:
        open2 = False

  elif selection == 1:
    open2 = True
    while open2:
      selection = select('How would you like your trigger to be activated?', ['Activate when you enter an area', 'Activates when a certain score is reached', 'Custom'])
      clear()
      if selection == 3:
        open2 = False
      
      else:
        tag = ask('Enter the trigger tag here:')
        if selection == 0:
          x = check('int', {}, 'X: ')
          y = check('int', {}, 'Y: ')
          z = check('int', {}, 'Z: ')
          line = f'execute positioned {x} {y} {z} as @a[distance=..{check("int", {}, "Distance: ")}] run tag @s add {tag}'
        
        elif selection == 1:
          line = 'execute as @a[score={' + input('Scoreboard name: ') + '=' + input('Score value (can include ..): ') + '}] run tag @s add ' + tag
        
        elif selection == 2:
          line = f'execute {input("Execute statment: ")} run tag @s add {tag}'
        
        if select(f'{line}\nWould you like to keep this line?', ['Keep']) == 0:
          write_(triggers, line + '\n', 'a')

  else:
    open1 = False