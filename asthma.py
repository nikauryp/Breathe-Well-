#  ^X^S is to save ^X^C is to quit use arrow keys and delete key to edit
# ^A begin line ^E end line  ^PNFB  ^K kill rest of line ^Y yanks it back
print("Asthma Crisis Helper")

# ask questions and then give answers to user
def helper():
    reply = input("Is the person struggling with breathing?")
    if (reply == 'no'):
        print("Call 911 right away!")
        return
        if (reply == 'yes'):
        print("Great, you are healthy!")
        return
    reply = input("Do you hear the person wheezing (yes or no)?")
    if (reply=='yes'):
        print("If they have an inhaler, have them use it.")
    else:
        print("They should be fine, avoid physical activity and remain seated calmy")
    reply = input("Do they have an inhalor?")
        if (reply == 'yes'):
        print("Follow the instructions, and proceed to use")
        return
    reply = input("Are there any nearby hospitals?")
        if (reply=='yes'):
        print("Hop in that Uber or call an ambulance")
    else:
        print("Attempt to treat at home for 30 minutes more, if symptoms increase, find the closest hospital")
    reply = input("Are you aware of what could have triggered the asthma attack?")
        if (reply == 'yes'):
        print("Remove yourself from that area or enviroment")
    else:
        print("Find a nearby or the closest hospital.")
