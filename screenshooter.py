import mss
import keyboard
import time
import os

# Create a directory to store screenshots (if it doesn't exist)
screenshot_dir = "osu_taiko_screenshots"
os.makedirs(screenshot_dir, exist_ok=True)

# Define the region of the screen to capture (left, top, width, height)
screenshot_region = {'left': 0, 'top': 912, 'width': 640, 'height': 480}  # Adjust as needed

def take_screenshot(key):
    """Takes a screenshot of a specific region and saves it."""
    timestamp = time.strftime("%Y%m%d-%H%M%S")
    filename = f"{screenshot_dir}/{key}_{timestamp}.png"
    
    with mss.mss() as sct:
        screenshot = sct.grab(screenshot_region)
        mss.tools.to_png(screenshot.rgb, screenshot.size, output=filename)
    
    print(f"Screenshot saved: {filename}")

def on_key_press(event):
    """Handles key press events."""
    if event.name in ['d', 'f', 'k', 'j']:
        take_screenshot(event.name)

# Register the key press event listener
keyboard.on_press(on_key_press)

print("Press 'd', 'f', 'k', or 'j' to take screenshots. Press 'esc' to exit.")

# Keep the program running until 'esc' is pressed
keyboard.wait('esc')

print("Exiting...")
keyboard.unhook_all()
