
import pyautogui
import mouse
import sys
from rich.console import Console
import menu
from data import AppState
import color
from rich.prompt import Prompt



DELAY = 1.00



def main():
    
    initPyAutoGUI()
    console = Console()
    menu.welcomeMessage(console)
    controlFlowLoop(console, initState())
    sys.exit()
    
    
def initState():
    return AppState([], (0,0), (0,0), 0, (0,0), 0.2)

    
def controlFlowLoop(console: Console, state):
    
    # init state object and start the loop
    enabled = True
    while enabled:
        selection = menu.mainMenu(console)
    
        # control flow for Select Screen Area tool
        if selection == "1":
            areaTool(console, state)

        # eyedropper section
        if selection == "2":
            eyeDropper(state, console)

        # exit program
        if selection == "3":
            enabled = False
    

def areaTool(console: Console, state):
    
    mouse.getPoints(state, console)
    state.calculateRegion()
    option = menu.areaSubMenu(console)
    
    
    # average rgb value in area
    if option == "1":
        rgb_average = color.averageRgbInRegion(state.region)
        menu.printColorValue(console, rgb_average)
        if menu.tryAgain(console):
            return


    # prints location of pixel with user input RGB value
    elif option == "2":
        state.color = Prompt.ask("RGB Value as tuple (0, 0, 0)")
        if isinstance(state.color, tuple):
            rgb_location = color.searchScreenAreaForColor(state.region, tuple(state.color))
            if rgb_location:
                print(f"RGB found at {rgb_location[0]}, {rgb_location[1]}.")
            else:
                print("RGB not found.")
                if menu.tryAgain(console):
                    return
        else:
            print("Not of type tuple.")
            if menu.tryAgain(console):
                return
    

def eyeDropper(state, console):
    mouse.getMouseColor(state, console)
    menu.printColorValue(console, state.color)
    if menu.tryAgain(console):
        return





        
    
# init pyautogui and enable the failsafe
def initPyAutoGUI():
    pyautogui.FAILSAFE = True



    
if __name__ == "__main__":
    main()