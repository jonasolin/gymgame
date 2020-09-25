import win32com.client
speaker = win32com.client.Dispatch("SAPI.SpVoice")


def entrance():
    s = "You are in the lobby of a big gym. \nWhere do you want to go?"
    o = ['crossfit', 'weights']
    printspeak(s, o)


def crossfit():
    s = "You are walking out on the crossfit area and everyone is staring at you. \nWhat do you want to do?"
    o = ['run', 'showthefinger']
    printspeak(s, o)


def weights():
    s = "You enter a room with lots of weights such as barbells and dumbbells. \nYou see a huge guy who probably takes steroids doing bicep curls with weights that should be used between lanes on the highway. \nWhat do you want to do now?"
    o = ['bicepcurl']
    printspeak(s, o)


def run():
    s = "You run out from the area screaming like a little girl and end up back in the lobby."
    printspeak(s)
    return 'entrance'


def showthefinger():
    s = "You show everyone the finger and go to the room with weights instead."
    printspeak(s)
    return 'weights'


def bicepcurl():
    s = "You pickup a normal weight and curl it like you mean it.\nYou are now exhausted and decide to go home."
    printspeak(s)
    return 'exit'


def printspeak(s, o=None):
    print("")
    if o is None:
        print(s)
    else:
        print(s, "({options})".format(options="/".join(o)))
    speaker.Speak(s.replace("\n",""))


def play():
    position = 'entrance'

    while position:

        locations = {
            'entrance': entrance,
            'crossfit': crossfit,
            'weights': weights
        }

        try:
            location_action = locations[position]
        except KeyError:
            print("There is nothing here.")
        else: 
            location_action()

        command = input("? ")

        actions = {
            'run': run,
            'showthefinger': showthefinger,
            'bicepcurl': bicepcurl,
            'entrance': lambda: 'entrance',
            'crossfit': lambda: 'crossfit',
            'weights': lambda: 'weights',
            'machines': lambda: 'machines'
        }

        try:
            command_action = actions[command]
        except KeyError:
            print("I don't understand")
        else:
            position = command_action()

        if position == 'exit':
            s = "Game over! \nThank you for playing Gym Game!"
            printspeak(s)
            break


if __name__ == '__main__':
    play()