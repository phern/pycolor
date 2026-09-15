import pywinctl as pwc
import time
import sys

# get status of window
def windowStatus():
    nms_window = pwc.getWindowsWithTitle("No Man's Sky")
    return bool(nms_window)

# move target window 
# accepts window object
def moveWindow(window):
    window.activate()
    window.moveTo(0 ,0)


# wait for target window
# accepts string
def waitForWindow(window_name):
    timeout = 0
    window = None
    print("Waiting for game window...")
    while not window:
        
        timeout += 1
        if timeout == 1000:
            print("Game window not found. Exiting...")
            sys.exit()
            
        time.sleep(0.2)
        
        windows = pwc.getWindowsWithTitle(window_name)
        if windows:
            print(f"{window} window found.")
            window = windows[0]
            moveWindow(window)
   
