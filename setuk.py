def calc():
  lines = []
  print("To end typing, type 'end'.")
  while True:
    line = input()
    if line == 'end':
      break
    lines.append(line)

  text = '\n'.join(lines)  # insert \n between index of lines
  numFullStr = len(text)  # the number of text
  space = text.count(' ')
  enter = text.count('\n')
  period = text.count('.')

  print((numFullStr - space - enter - period) * 3 + space + period + enter * 2,
        "byte")

calc()

while True:
  print('press ', '\033[32m', '1', '\033[0m', ' to exit or ', '\033[32m', '2', '\033[0m', ' using calculate again')
  exiter = input()
  if exiter == '1':
    break
  elif exiter == '2':
    calc()
  else:
    continue 
    
