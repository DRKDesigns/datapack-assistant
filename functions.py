from os import system, makedirs, remove

def clear():
  system('clear')


def an(next):
  if next[0] in ['a','e','i','o','u','A','E','I','O','U']:
    return ' an '
  
  else:
    return ' a '


def check(checks, args):
  passed = False
  while not passed:
    answer = input('')
    
    if 'int' in checks:
      try:
        answer = int(answer)
        passed = True
      
      except:
        pass
    
    if 'number in range' in checks:
      if answer >= args['number in range'][0] and answer <= args['number in range'][1]:
        passed = True

    if not passed:
      print(f'Please make sure to enter{an(checks)}{"/".join(checks)}')
  
  return answer


def write_(path, data, letter):
  with open(path, letter) as file:
    file.write(data)


def read_(path, lines):
  with open(path, 'r') as file:
    if lines:
      return file.readlines()
    else:
      return file.read()


def select(question, options):
  list_ = []
  for i in range(len(options)):
    list_.append(f'{i}: {options[i]}')
  
  clear()
  if question == '':
    print("\n".join(list_) + '\n' + str(len(options)) + ': Exit')
  else:
    print(question + '\n' + "\n".join(list_) + '\n' + str(len(options)) + ': Exit')

  return check(['number in range', 'int'], {'number in range':[0, len(options)]})

def ask(question):
  print(question)
  return input('')

def split(data, seperators):
  final = []
  part = 0
  for i in data:
    if i in seperators:
      final.append()
      part += 1

    else:
      final[part] = final[part] + i  

  return final

def addFile(path, file, data):
  try:
    makedirs(path)

  except:
    pass
  
  try:
    open(path)
  
  except:
    write_(path + '/' + file, data, 'w')