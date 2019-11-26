import os
import sys
from pathlib import Path
from PIL import Image, ImageGrab, Image
from datetime import datetime

LOCAL_DIR = os.path.dirname(os.path.realpath(__file__))
SAVE_DIR = older = os.path.expanduser("~/Downloads")
FILE_PATHS = sys.argv[1:]


def generateUUID():
    return str(hash(datetime.now()))[1:10]


def getWallpaper():
    for path in FILE_PATHS:
        if "wallpaper" in path:
            return path
    # fallback
    return f"{LOCAL_DIR}/wallpaper.png"


for screenshot_path in FILE_PATHS:

    # open wallpaper
    wallpaper = Image.open(getWallpaper()).convert("RGBA")
    wallpaper_w, wallpaper_h = wallpaper.size

    # open the screenshot
    screenshot = Image.open(screenshot_path).convert("RGBA")
    screenshot_w, screenshot_h = screenshot.size

    # figure out where to position screenshot
    offset = ((wallpaper_w - screenshot_w) // 2, (wallpaper_h - screenshot_h) // 2)

    # paste it onto the wallpaper
    wallpaper.paste(screenshot, offset, screenshot)

    # save the wallpaper
    original_location = Path(screenshot_path).parent
    wallpaper.save(f"{original_location}/screenshot-{generateUUID()}.png", "PNG")
