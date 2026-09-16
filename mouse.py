from pynput import mouse
from rich.live import Live
from rich.panel import Panel
from rich.text import Text
import menu as p
import pydirectinput
import pyautogui
import time
from data import AppState



DELAY = 1.0



# prints coordinates of mouse continuously
def reportMousePosition(seconds=10):
    for i in range(seconds):
        print(pyautogui.position())
        time.sleep(DELAY)


# return point object and color object        
def getMouseColor(state: AppState, console):
    enabled = True
    def on_click(x, y, button, pressed):
        nonlocal enabled
        if pressed:
            state.mousePos = (x, y)
            state.color = pyautogui.pixel(x, y)
            enabled = False
            return False
        
    with (
        Live("", console=console, refresh_per_second=45) as live,
        mouse.Listener(on_click=on_click) as listener,
    ):
        while enabled:
            pos = pyautogui.position()
            rgb = pyautogui.pixel(pos.x, pos.y)
            live.update(p.printMousePos(pos, rgb))
            time.sleep(0.2)
        listener.join()


# listens for mouse, tracks position, returns list of tuples
def getPoints(state: AppState, console):
    state.points = []  
    # callback function to record coordinates
    def on_click(x, y, button, pressed):
        if pressed:
            state.points.append((x, y))
            console.print(Panel.fit(
                f"x: {x} y: {y}  recorded.",
                border_style="cyan",
                padding=(1,2),
                )
            )
        if len(state.points) == 2:
            return False
        
    with (
        Live("", console=console, refresh_per_second=24) as live,
        mouse.Listener(on_click=on_click) as listener,
    ):
        while len(state.points) < 2:
            pos = pyautogui.position()
            if not state.points:
                live.update("Click to add a point.")
            else:
                live.update("Click to record another point.")
            live.update(p.printMousePos(pos))
            #print(f"\r-----  x: {pos.x}  y: {pos.y}  -----", end="", flush=True)
            time.sleep(0.2)
        listener.join()


# send left mouse down and mouse up events
def useMouseButton(seconds=0.10):
    pydirectinput.mouseDown()
    time.sleep(seconds)
    pydirectinput.mouseUp()
