#  ^X^S is to save ^X^C is to quit use arrow keys and delete key to edit
# ^A begin line ^E end line  ^PNFB  ^K kill rest of line ^Y yanks it back
print("Asthma Crisis Helper")

# ask questions and then give answers to user
def helper():
    reply = input("Can the person breathe at all? (yes or no)")
    if (reply == 'no'):
        print("Call 911 right away!")
        return
    reply = input("Do they have an inhaler? (yes or no)")
    if (reply=='yes'):
        print("Have them use the inhaler.")
    else:
        print("sit up right and try to take deep breaths")

def noncritical():
  print("call your doctor")

def emergencyvisit():
    tobring= input("what to bring to hospital")

helper()
 
