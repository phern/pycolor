import pyautogui



# screenshot a region, iterate over each pixel for R, G and B values, combine, average, return
def averageRgbInRegion(region: tuple):
    screenshot =  pyautogui.screenshot(region=region)
    divisor = screenshot.height * screenshot.width
    rsum = 0
    gsum = 0
    bsum = 0
    for x in range(screenshot.width):
        for y in range(screenshot.height):
            this_pixel = screenshot.getpixel((x, y))
            rsum += this_pixel[0]
            gsum += this_pixel[1]
            bsum += this_pixel[2]
    rgb_average = (
        (round(rsum / divisor)),
        (round(gsum / divisor)),
        (round(bsum / divisor))
    )
    return rgb_average
            
                
    
    

# screenshot a region and
# iterate over pixels for color_to_find
def searchScreenAreaForColor(region: tuple, color_to_find: tuple):
    screenshot = pyautogui.screenshot(region=region)
    try:
        for row in range(screenshot.width):
            for col in range(screenshot.height):
                if color_to_find == screenshot.getpixel((row, col)):
                    abs_x = region[0] + row
                    abs_y = region[1] + col
                    #print(f"RGB found at {abs_x}, {abs_y}")
                    return (abs_x, abs_y)
        return False
    except ValueError:
        print("ValueError exception caught while searching for pixel color")
        return False
    
