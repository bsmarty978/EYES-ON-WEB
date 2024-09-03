import undetected_chromedriver as uc

from PIL import Image, ImageChops
import time
import os

# driver = uc.Chrome(headless=True,use_subprocess=False)
# driver.get('https://nowsecure.nl')
# driver.save_screenshot('nowsecure.png')
# Setup WebDriver (e.g., Chrome)


def capture_screenshot(path):
    driver.get(url)
    driver.save_screenshot(path)

def compare_images(image1_path, image2_path):
    image1 = Image.open(image1_path)
    image2 = Image.open(image2_path)
    
    # Compare the images
    diff = ImageChops.difference(image1, image2)
    
    return diff.getbbox() is not None  # True if there's a difference


if __name__ == '__main__':

    driver = uc.Chrome(headless=True,use_subprocess=False)

    # Define URL and screenshot paths
    url = 'https://main.un.org/securitycouncil/en/content/list-updates-unsc-consolidated-list'
    old_screenshot_path = 'screenshot_old.png'
    new_screenshot_path = 'screenshot_new.png'

    # Capture new screenshot
    capture_screenshot(new_screenshot_path)

    # Compare with old screenshot
    if os.path.exists(old_screenshot_path):
        if compare_images(old_screenshot_path, new_screenshot_path):
            print("Page updated.")
            # Update old screenshot to the new one for the next check
            os.replace(new_screenshot_path, old_screenshot_path)
        else:
            print("No update detected.")
            os.remove(new_screenshot_path)  # Clean up
    else:
        # If there's no previous screenshot, just store the current one for future comparison
        os.rename(new_screenshot_path, old_screenshot_path)
        print("First check completed. Stored initial screenshot.")

    # Clean up and close the driver
    driver.quit()
