from selenium import webdriver
import time
import json

# Initialize WebDriver
driver = webdriver.Chrome()

# Load the desired URL
driver.get('https://main.un.org/securitycouncil/en/content/list-updates-unsc-consolidated-list')

# Inject the JavaScript for selecting a region
with open('ss_js.js', 'r') as js_file:
    js_code = js_file.read()
driver.execute_script(js_code)

# Wait for the user to select the region (you can add time.sleep or another waiting mechanism)
time.sleep(30)  # Adjust this to give the user time to select the region

# Retrieve the coordinates from the page's global variable
coordinates = driver.execute_script("return window.selectedRegion;")

if coordinates:
    print("Selected Region Coordinates:", coordinates)
    startX = coordinates['startX']
    startY = coordinates['startY']
    endX = coordinates['endX']
    endY = coordinates['endY']
    
    # Save the coordinates for future use
    with open("region_coordinates.json", "w") as f:
        json.dump(coordinates, f)
else:
    print("No region was selected")

# Close the browser
driver.quit()
