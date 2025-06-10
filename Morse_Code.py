from time import sleep, perf_counter
from gpiozero import Button

def start():
    val = perf_counter()
    return val
def end(val):
    return float(perf_counter()-val)

button = Button(23) #Button is initialized as being at Gpio pin 23, change this depending on your setup

End = -1
Morse = ""
space = False
text = ""
Code = {"_":" ",
        ".-":"A",
        "-...":"B",
        "-.-.":"C",
        "-..":"D",
        ".":"E",
        "..-.":"F",
        "--.":"G",
        "....":"H",
        "..":"I",
        ".--":"J",
        "-.-":"K",
        ".-..":"L",
        "--":"M",
        "-.":"N",
        "---":"O",
        ".--.":"P",
        "--.-":"Q",
        ".-.":"R",
        "...":"S",
        "-":"T",
        "..-":"U",
        "...-":"V",
        ".--":"W",
        "-..-":"X",
        "-.--":"Y",
        "..--":"Z"}
while End <= 5:
    active = False
    Start = start()
    
    if button.is_active:
        space = False
            
    elif not button.is_active:
        space = True

    state = button.is_active
    while button.is_active == state and End <5.1:
        End = end(Start)
        sleep(0.005)
        
    if End>=5 and space == True:
        break
    
    elif End <=0.3 and space == False:
        Morse += "."
        #print(Morse)
        
    elif End > 2 and space == True:
        if Code.get(Morse):
            text += Code.get(Morse) + " "
            Morse += "_"
            #print(Morse)
            print(text)
            Morse = ""
    elif End > 0.3 and space == False:
        Morse += "-"
        #print(Morse)
        
    elif End >=0.5 and space == True:
        if Code.get(Morse):
            text += Code.get(Morse)
            print(text)
            Morse = ""
#print(Morse)
if Code.get(Morse):
            text += Code.get(Morse)
            print(text)
print(text)
