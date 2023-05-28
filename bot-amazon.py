from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
# import pause
from selenium.webdriver.support.ui import Select
import csv
import datetime
import pause

def checkbsr():
    global ffg
    try:
        element = driver.find_element(By.CSS_SELECTOR, "h3.d-flex.align-items-center.py-0")

        # Extract the value
        ffg = element.text.split()[-1]

        return ffg

    except:
        pause.seconds(3)
        checkbsr()
        return ffg


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


print(f"""{bcolors.HEADER}
  _  __              _                ____              
 | |/ /___ _   _  __| | ___  ___ _ __/ ___| _ __  _   _ 
 | ' // _ \ | | |/ _` |/ _ \/ _ \ '_ \___ \| '_ \| | | |
 | . \  __/ |_| | (_| |  __/  __/ |_) |__) | |_) | |_| |
 |_|\_\___|\__, |\__,_|\___|\___| .__/____/| .__/ \__, |
           |___/                |_|        |_|    |___/ 
{bcolors.ENDC}
{bcolors.BOLD}BY MR.ZOX47{bcolors.ENDC}
""")


# Get the current date and time
current_datetime = datetime.datetime.now()

# Format the date and time
formatted_datetime = current_datetime.strftime("%Y-%m-%d")

# Print the formatted date and time


# Specify the path to your CSV file


download_directory = (r"C:\Users\viiru\Desktop\bot amazon")
options = webdriver.ChromeOptions()
# options.add_argument("--disable-extensions")  # Disable browser extensions
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
options.add_extension('bsr.crx')

options.add_experimental_option('prefs', {
    'download.default_directory': download_directory,
    'download.prompt_for_download': False,
    'download.directory_upgrade': True,
    'safebrowsing.enabled': True
})

# options.add_argument('--headless')

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



driver.switch_to.window(driver.window_handles[0])

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
# pause.sleep(2)

# all_dropdown = driver.find_element("name", "searchDropdownBox").click()


driver.refresh()

driver.find_element("id", 'nav-search-dropdown-card').click()
# driver.select_by_value('search-alias=stripbooks-intl-ship').click()

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

mainkeyword = input(f"{bcolors.OKGREEN}+{bcolors.ENDC} {bcolors.BOLD}Enter The Main Keywword: {bcolors.ENDC}")
query = (
    'chrome-extension://hbapdpeemoojbophdfndmlgdhppljgmp/html/page.html?page=autocomplete&query={0}&service=amazon').format(
    mainkeyword)
driver.get(query)

listk = []
input(f'{bcolors.OKGREEN}+{bcolors.ENDC} {bcolors.BOLD}Are the keywords downloaded! | Press Enter{bcolors.ENDC} \n')

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
count = 0
for i in listk:
    count += 1
    try:
        driver.find_element("id", 'twotabsearchtextbox').clear()
    except:
        pass
    driver.find_element("id", 'twotabsearchtextbox').send_keys(i)
    driver.find_element("id", 'nav-search-submit-button').click()
    res = driver.find_element(By.XPATH, '//*[@id="search"]/span/div/h1/div/div[1]/div/div/span[1]').text
    bsr = checkbsr()



    if "over" in str(res):
        results = res.partition('over ')[2]
    elif "of" in str(res):
        results = res.partition('of ')[2]
    else:
        results = res
    ress = results.partition(' results for')[0]
    # print (i+'------> '+ress)
    print(
        f"{bcolors.OKGREEN}[{count}]{bcolors.ENDC} " + i + f'{bcolors.OKGREEN} |----> {bcolors.ENDC}' + ress + f"{bcolors.OKGREEN} | {bcolors.ENDC}BSR {bcolors.OKGREEN}|---->{bcolors.ENDC} {bsr}" +"\n")
