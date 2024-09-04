from selenium import webdriver

# Initialize Chrome WebDriver
options = webdriver.ChromeOptions()
options.add_argument("--headless")  # Optional: run in headless mode
driver = webdriver.Chrome(options=options)

url = 'https://main.un.org/securitycouncil/en/content/list-updates-unsc-consolidated-list'
url = 'https://scsanctions.un.org/resources/xml/en/consolidated.xml'

# Load the page
driver.get(url)

# Use JavaScript to get the page dimensions
page_width = driver.execute_script("return document.documentElement.scrollWidth;")
page_height = driver.execute_script("return document.documentElement.scrollHeight;")

# Set the window size to the page dimensions
driver.set_window_size(page_width, page_height)

# Capture the full-page screenshot
driver.get_screenshot_as_file('full_page_screenshot_chrome-2.png')

# Close the browser
driver.quit()

print("Full-page screenshot saved as 'full_page_screenshot_chrome.png'")
