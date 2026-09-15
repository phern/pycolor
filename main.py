import pyautogui
# import pydirectinput
import time
import prints


DELAY = 1.00

def main():
    initPyAutoGUI()
    
    
        
    
# init pyautogui and enable the failsafe
def initPyAutoGUI():
    pyautogui.FAILSAFE = True


# countdown timer 
def countdownTimer(seconds): 
    print("Starting", end="")
    for i in range(seconds):
        print(".", end="")
        time.sleep(DELAY)
    print("Started")

# screenshot a region and
# iterate over pixels for color_to_find
def searchScreenAreaForColor(x, y, width, height, color_to_find):
    region = (x, y, width, height)  # Define the region of interest
    screenshot = pyautogui.screenshot(region=region)
    try:
        for row in range(screenshot.width):
            for col in range(screenshot.height):
                pixel_rgb = screenshot.getpixel(row, col)
                if pixel_rgb == color_to_find:
                    print("Pixel found")
                    return True
    except ValueError:
        print("ValueError exception caught while searching for pixel color")
        return False
    
    
if __name__ == "__main__":
    main()