

##import requests
##import os
##import json
##from fake_useragent import UserAgent
##pyload = {"email":"abdellahmoutassad.eq392@gmail.com"}
##
##ua = UserAgent()
##
##
###title = input("Enter keyword you want: ")
##
##
##useragent = ua.random
##s = requests.Session()
##headers = {
## "Content-Type": "application/json",
## "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36",
##}
##
##response = requests.post("https://lexica.art/api/pre-signup", json=json.dumps(pyload), headers=headers)
##
###change = s.get("https://www.amazon.com/portal-migration/hz/glow/get-location-label?storeContext=books&pageType=Search&actionSource=desktop-modal", headers=headers)
##
##
##print (response.text)



##
##
##import requests
##import os
##import json
##from fake_useragent import UserAgent
##from bs4 import BeautifulSoup
##
##ua = UserAgent()
##useragent = ua.random
##
##pyload = {
##  "locationType": "LOCATION_INPUT",
##  "zipCode": "10001",
##  "storeContext": "generic",
##  "deviceType": "web",
##  "pageType": "Gateway",
##  "actionSource": "glow",
##  
##}
##
##ua = UserAgent()
##
##
###title = input("Enter keyword you want: ")
##
##
##useragent = ua.random
##s = requests.Session()
##headers = {
## "Content-Type": "application/json",
## "User-Agent": useragent}
##
##premier = s.get('https://www.amazon.com/', headers=headers)
##
##from bs4 import BeautifulSoup
##soup = BeautifulSoup(premier.text, 'html.parser')
##span = soup.find("span", id="nav-global-location-data-modal-action")
##
##attr = span["data-a-modal"]
##
##json_data = json.loads(attr)
##
### Extract the value of the "anti-csrftoken-a2z" key
##anti_csrftoken_a2z = json_data['ajaxHeaders']['anti-csrftoken-a2z']
##
###print(anti_csrftoken_a2z)
##
##
##
##headerss = {
## "Content-Type": "application/json",
## "User-Agent": ,
## "Accept": "text/html,*/*",
## "Accept-Encoding": "gzip, deflate, br",
## "Accept-Language": "en-US,en;q=0.9",
## "Anti-Csrftoken-A2z": anti_csrftoken_a2z,
## "Content-Length": "138",
## "Device-Memory": "8",
## "Downlink": "3.2",
## "Dpr": "1.25",
## "Ect": "3g",
## "Origin": "https://www.amazon.com",
## "Referer": "https://www.amazon.com/",
## "Rtt": "250",
## "Sec-Ch-Device-Memory": "8",
## "Sec-Ch-Dpr": "1.25",
## "Sec-Ch-Ua": '"Google Chrome";v="113", "Chromium";v="113", "Not-A.Brand";v="24"',
## "Sec-Ch-Ua-Mobile": "?0",
## "Sec-Ch-Ua-Platform": "Windows",
## "Sec-Ch-Ua-Platform-Version": "10.0.0",
## "Sec-Ch-Viewport-Width": "730",
## "Sec-Fetch-Dest": "empty",
## "Sec-Fetch-Mode": "cors",
## "Sec-Fetch-Site": "same-origin",
##
##}
##response = s.post("https://www.amazon.com/portal-migration/hz/glow/address-change?actionSource=glow", json=pyload, headers=headerss)
##responses = s.get("https://www.amazon.com", headers=headerss)
##print (response.text)
##
##
##soups = BeautifulSoup(responses.text, 'html.parser')
##spanx = soup.find("span", id="nav-global-location-data-modal-action")
##print (spanx)
##
###print (response.text)

























##from selenium import webdriver
##from webdriver_manager.chrome import ChromeDriverManager
##from selenium.webdriver.chrome.options import Options
##import pause
##
##options = Options()
##options.add_experimental_option('detach', True)
##driver = webdriver.Chrome(options=options)
##
##
##driver.get("https://www.amazon.com/")
##driver.find_element("id", "nav-global-location-popover-link").click()
##pause.seconds(3)
##driver.find_element("id", "GLUXZipUpdateInput").send_keys(10001)
##pause.seconds(3)
##
##driver.find_element("name", "GLUXZipUpdate").click()
##
##driver.find_element("name", "glowDoneButton").click()
##pause.seconds(3)
##driver.find_element("name", "searchDropdownBox").click()
##pause.seconds(3)
##driver.find_element("xpath", '//*[@id="searchDropdownBox"]/option[6]').click()
##


<<<<<<< HEAD

=======
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

print (f"""{bcolors.HEADER}
  _  __              _                ____              
 | |/ /___ _   _  __| | ___  ___ _ __/ ___| _ __  _   _ 
 | ' // _ \ | | |/ _` |/ _ \/ _ \ '_ \___ \| '_ \| | | |
 | . \  __/ |_| | (_| |  __/  __/ |_) |__) | |_) | |_| |
 |_|\_\___|\__, |\__,_|\___|\___| .__/____/| .__/ \__, |
           |___/                |_|        |_|    |___/ 
{bcolors.ENDC}
{bcolors.BOLD}BY MR.ZOX47{bcolors.ENDC}
""")
>>>>>>> 13971e0 (This is a new commit for what I originally planned to be amended)
        

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pause
from selenium.webdriver.support.ui import Select
import csv
import datetime

<<<<<<< HEAD
=======


>>>>>>> 13971e0 (This is a new commit for what I originally planned to be amended)
# Get the current date and time
current_datetime = datetime.datetime.now()

# Format the date and time
formatted_datetime = current_datetime.strftime("%Y-%m-%d")

# Print the formatted date and time



# Specify the path to your CSV file










download_directory = (r"C:\Users\viiru\Desktop\bot amazon")
options = webdriver.ChromeOptions()
#options.add_argument("--disable-extensions")  # Disable browser extensions
options.add_argument("--disable-gpu")  # Disable GPU usage
options.add_argument("--disable-infobars")  # Disable info bars
options.add_argument("--disable-notifications")  # Disable notifications
options.add_argument("--disable-dev-shm-usage")  # Disable /dev/shm usage
options.add_argument("--disable-browser-side-navigation")  # Disable browser side navigation
options.add_argument("--disable-features=VizDisplayCompositor")  # Disable VizDisplayCompositor feature
options.add_argument("--disable-features=NetworkService")  # Disable NetworkService feature
options.add_argument("--no-sandbox")  # Disable sandbox mode
options.add_argument("--dns-prefetch-disable")  # Disable DNS prefetching
options.add_experimental_option("detach", True)
# Set additional options for performance
options.add_argument("--fast-start")  # Enable fast start
options.add_argument("--ignore-certificate-errors")  # Ignore certificate errors
options.add_argument("--disable-popup-blocking")
options.add_extension('getkeyword.crx')
options.add_experimental_option('prefs', {
    'download.default_directory': download_directory,
    'download.prompt_for_download': False,
    'download.directory_upgrade': True,
    'safebrowsing.enabled': True
})

#options.add_argument('--headless')

# Create a new instance of the Chrome driver
driver = webdriver.Chrome(options=options)



##def checknow():
##    
##    driver.switch_to.window(driver.window_handles[1])
##    input('ok')
##    driver.find_element(By.XPATH, '//*[@id="table-control-buttons"]/div/button[3]')
##           

    




# Open Amazon's website
driver.get('https://www.amazon.com/')


driver.switch_to.window(driver.window_handles[1])

driver.close()
driver.switch_to.window(driver.window_handles[0])


# Wait for the page to load and find the location element
location_element = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.ID, 'nav-global-location-data-modal-action'))
)

# Click on the location element to open the location modal
location_element.click()

# Wait for the location modal to load and find the postal code input field
postal_code_input = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.ID, 'GLUXZipUpdateInput'))
)

# Clear the current postal code
postal_code_input.clear()

# Enter the new postal code
postal_code_input.send_keys('10001')






# Find and click the apply button
apply_button = driver.find_element(By.XPATH, '//*[@id="GLUXZipUpdate"]/span/input')
apply_button.click()

apply_buttons = driver.find_element(By.XPATH, '//*[@id="a-popover-1"]/div/div[2]/span/span/span/button')
apply_buttons.click()
#pause.sleep(2)

#all_dropdown = driver.find_element("name", "searchDropdownBox").click()


driver.refresh()

driver.find_element("id", 'nav-search-dropdown-card').click()
#driver.select_by_value('search-alias=stripbooks-intl-ship').click()

dropdown_element = driver.find_element("id", "searchDropdownBox")  # Replace with the actual ID of the dropdown element

# Create a Select object
dropdown = Select(dropdown_element)

# Select option by value
desired_value = "search-alias=stripbooks"  # Replace with the value of the option you want to select
dropdown.select_by_value(desired_value)

driver.find_element("id", 'twotabsearchtextbox').click()

########GET KEYWRDS
driver.execute_script("window.open();")

# Switch to the new tab
driver.switch_to.window(driver.window_handles[1])

<<<<<<< HEAD
mainkeyword = 'fairy coloring book for adult'
=======
mainkeyword = input(f"{bcolors.OKGREEN}+{bcolors.ENDC} {bcolors.BOLD}Enter The Main Keywword: {bcolors.ENDC}")
>>>>>>> 13971e0 (This is a new commit for what I originally planned to be amended)
query = ('chrome-extension://hbapdpeemoojbophdfndmlgdhppljgmp/html/page.html?page=autocomplete&query={0}&service=amazon').format(mainkeyword)
driver.get(query)

listk = []
<<<<<<< HEAD
input('are the keywords downloaded!: ')
=======
input(f'{bcolors.OKGREEN}+{bcolors.ENDC} {bcolors.BOLD}Are the keywords downloaded! | Press Enter{bcolors.ENDC} \n')
>>>>>>> 13971e0 (This is a new commit for what I originally planned to be amended)

til = mainkeyword.replace(' ', '-')
csv_file_path = (r'amazon-keywords-{0}--{1}.csv').format(til, formatted_datetime)

# Open the CSV file
with open(csv_file_path, 'r') as file:
    # Create a CSV reader object
    csv_reader = csv.reader(file)

    # Extract the first column values
    first_column = [row[0] for row in csv_reader]

    # Print the extracted values
    
    for value in first_column:
        
        if str(value) == 'Keyword':
            pass
        else:
            listk.append(value)

driver.close()
driver.switch_to.window(driver.window_handles[0])

for i in listk:
    try:
        driver.find_element("id", 'twotabsearchtextbox').clear()
    except:
        pass
    driver.find_element("id", 'twotabsearchtextbox').send_keys(i)
    driver.find_element("id", 'nav-search-submit-button').click()
    res = driver.find_element(By.XPATH, '//*[@id="search"]/span/div/h1/div/div[1]/div/div/span[1]').text
    try:
        results = res.partition('over ')[2]
    except:
        results = res.partition('of ')[2]
    ress = results.partition(' results for')[0]  
<<<<<<< HEAD
    print (i+'------> '+ress)
=======
    print (i+f'{bcolors.OKGREEN}--------->{bcolors.ENDC}'+ress)
>>>>>>> 13971e0 (This is a new commit for what I originally planned to be amended)










