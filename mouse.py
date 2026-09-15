from pynput import mouse
import pydirectinput
import pyautogui
import time


DELAY = 1.0



# prints coordinates of mouse continuously
def reportMousePosition(seconds=10):
    for i in range(seconds):
        print(pyautogui.position())
        time.sleep(DELAY)
        

# return point object        
def getPoint():
    return pyautogui.position()


# listens for mouse, tracks position, returns list of tuples
def getPoints():
    points = []  
    # callback function to record coordinates
    def on_click(x, y, button, pressed):
        if pressed:
            points.append(tuple(x, y))
            print(f"x: {x} y: {y}  recorded.")
        if len(points) == 2:
            return False
        
    with mouse.Listener(on_click=on_click) as listener:
        while len(points) < 2:
            pos = pyautogui.position()
            if not points:
                print("Click to add a point.")
            else:
                print("Click to record another point.")
            print(f"\r-----  x: {pos.x}  y: {pos.y}  -----", end="", flush=True)
            time.sleep(0.2)
        listener.join()
    return points


# send left mouse down and mouse up events
def useMouseButton(seconds=0.10):
    pydirectinput.mouseDown()
    time.sleep(seconds)
    pydirectinput.mouseUp()
