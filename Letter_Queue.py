# 1 star solution

def letter_queue(commands):
    queue = ""
    stack = []
    for command in commands:
        if (command == "POP"):
            try:
                queue = queue[1:]
            except Exception:
                queue = ""
        elif (command.split(" ")[0] == "PUSH"):
            queue += command.split(" ")[1]
    print(queue)
    return queue

# 2 stars solution

def golf(cs):
 u=0
 t=[]
 for c in cs:
  c=c.split(" ")
  if "O" in c[0]:
   try:u+=int(t[-1])
   except Exception:u=+u
   if t:t.pop(-1)
  elif("U" in c[0]):t+=c[1]
  else:
   try:u+=int(t[-1])
   except Exception:u=+u
 return u

# 3 stars solution

def golf(d):
 q=[];s=0
 for c in d:
  if "U" in c:
   q+=[int(c[-1])]
  elif len(q):
   if "O" in c:
    s+=q.pop()
   else:
    s+=q[-1]
return s

# letter_queue(("POP", "POP"))

#if __name__ == '__main__':
#    # These "asserts" using only for self-checking and not necessary for auto-testing
#    assert letter_queue(("PUSH A", "POP", "POP", "PUSH Z", "PUSH D", "PUSH O", "POP", "PUSH T")) == "DOT", "dot example"
#    assert letter_queue(("POP", "POP")) == "", "Pop, Pop, empty"
#    assert letter_queue(("PUSH H", "PUSH I")) == "HI", "Hi!"
#    assert letter_queue(()) == "", "Nothing"

#    print("All done? Earn rewards by using the 'Check' button!")

# | Command | Queue | Note
# -------------------------------------------------
# | PUSH A  | A     | Added "A" in the empty queue
# | POP     |       | Removed "A"
# | POP     |       | The queue is empty already
# | PUSH Z  | Z     |
# | PUSH D  | ZD    |
# | PUSH O  | ZDO   |
# | POP     | DO    |
# | PUSH T  | DOT   | The result
