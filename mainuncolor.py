# define func

def calc():
  lines = []
  print("To end typing, type 'end'.")
  while True:
    line = input()
    if line == 'end': # break sequence: str(end)
      break
    lines.append(line)
  # join lineend(line)
  text = '\n'.join(lines)  # insert \n between index of lines
  # integer  
  numFullStr = len(text)  # the number of text
  space = text.count(' ') # the number of space
  enter = text.count('\n') # the number of EOL (CRLF, \n)
  period = text.count('.') # the number of period
  print((numFullStr - space - enter - period) * 3 + space + period + enter * 2, "byte") #normal Charecter is 3 byte, space, period, and EOL(CRLF, \n) is 2 byte


# operate func

calc()

while True:
  print('press ', '', '1', '', ' to exit or ', '', '2', '', ' using calculate again')
  exiter = input()
  if exiter == '1':
    break
  elif exiter == '2':
    calc()
  else:
    continue 

