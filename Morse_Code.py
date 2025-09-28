from time import sleep, perf_counter
from gpiozero import Button

def start():
    val = perf_counter()
    return val
def end(val):
    return float(perf_counter()-val)

button = Button(17)

Code = {"_":" ",
        ".-":  "A",
        "-...":"B",
        "-.-.":"C",
        "-..": "D",
        ".":   "E",
        "..-.":"F",
        "--.": "G",
        "....":"H",
        "..":  "I",
        ".--": "J",
        "-.-": "K",
        ".-..":"L",
        "--":  "M",
        "-.":  "N",
        "---": "O",
        ".--.":"P",
        "--.-":"Q",
        ".-.": "R",
        "...": "S",
        "-":   "T",
        "..-": "U",
        "...-":"V",
        ".--": "W",
        "-..-":"X",
        "-.--":"Y",
        "..--":"Z"}
End = -1
Morse = ""
text = ""
pressed = False

while pressed == button.is_active:
    sleep(0.05)
pressed = True

while End<=5 or pressed == True:
    
    Start = start()
    pressed = button.is_active
    
    while pressed == button.is_active:
        sleep(0.05)
        End = end(Start)
        
        if End >= 5 and pressed == False:
            break
        
        elif End >= 2 and pressed == False:
            if text[-1] != " ":
                Morse += "_"
                print(Morse)
                text += " "
                print(text)
                Morse = ""
                break
            
        elif End >=0.5 and pressed == False:
            if Code.get(Morse):
                text += Code.get(Morse)
                print(text)
                Morse = ""

          
    if End > 0.3 and pressed == True:
        Morse += "-"
        print(Morse)
            
    elif End <=0.3 and pressed == True:
        Morse += "."
        print(Morse)
