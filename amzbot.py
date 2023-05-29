from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
import csv
import datetime
import pause


def extractkey():
    dirs = input("Enter Dir Of Your File Keyword: ")
    for key in open(dirs, 'r').read().split('\n'):
        co = key.split(':', 3)
        print(co[0])


def checkbsr():
    global ffg
    max_retries = 10
    retries = 0
    while retries < max_retries:
        try:
            element = driver.find_element(By.CSS_SELECTOR, "h3.d-flex.align-items-center.py-0")
            ffg = element.text.split()[-1]
            return ffg
        except:
            pause.seconds(3)
            retries += 1
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
--------------------------------|
{bcolors.OKGREEN}[1]{bcolors.ENDC} - {bcolors.BOLD}Extract Keyword From File{bcolors.ENDC} |
{bcolors.OKGREEN}[2]{bcolors.ENDC} - {bcolors.BOLD}Extract Keyword From Web{bcolors.ENDC}  |
--------------------------------|
""")

choice = int(input(f"{bcolors.OKGREEN}+{bcolors.ENDC} {bcolors.BOLD}Enter Your Choice: {bcolors.ENDC}"))
if choice == 1:
    extractkey()

    complt = input(
        f'{bcolors.OKGREEN}+{bcolors.ENDC} {bcolors.BOLD}You want continues{bcolors.ENDC} {bcolors.OKGREEN}Y{bcolors.ENDC} | {bcolors.FAIL}N{bcolors.ENDC} : ')
    if complt == 'y':
        pass
    else:
        exit()

# Get the current date and time
current_datetime = datetime.datetime.now()
formatted_datetime = current_datetime.strftime("%Y-%m-%d")

download_directory = r"C:\Users\viiru\Desktop\bot amazon"

options = webdriver.ChromeOptions()
options.add_argument("--disable-gpu")
options.add_argument("--disable-infobars")
options.add_argument("--disable-notifications")
options.add_argument("--disable-dev-shm-usage")
options.add_argument("--disable-browser-side-navigation")
options.add_argument("--disable-features=VizDisplayCompositor")
options.add_argument("--disable-features=NetworkService")
options.add_argument("--no-sandbox")
options.add_argument("--dns-prefetch-disable")
options.add_experimental_option("detach", True)
options.add_argument("--fast-start")
options.add_argument("--ignore-certificate-errors")
options.add_argument("--disable-popup-blocking")
options.add_extension('getkeyword.crx')
options.add_extension('bsr.crx')

options.add_experimental_option('prefs', {
    'download.default_directory': download_directory,
    'download.prompt_for_download': False,
    'download.directory_upgrade': True,
    'safebrowsing.enabled': True
})

driver = webdriver.Chrome(options=options)
print(f"{bcolors.HEADER}{bcolors.BOLD}----------------------------------{bcolors.ENDC}")

print(f"{bcolors.HEADER}{bcolors.BOLD}BY MR.ZOX47{bcolors.ENDC}")

driver.get('https://www.amazon.com/')

driver.switch_to.window(driver.window_handles[1])
driver.switch_to.window(driver.window_handles[0])
driver.close()
driver.switch_to.window(driver.window_handles[0])

location_element = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.ID, 'nav-global-location-data-modal-action'))
)
location_element.click()

postal_code_input = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.ID, 'GLUXZipUpdateInput'))
)
postal_code_input.clear()
postal_code_input.send_keys('10001')

apply_button = driver.find_element(By.XPATH, '//*[@id="GLUXZipUpdate"]/span/input')
apply_button.click()

apply_buttons = driver.find_element(By.XPATH, '//*[@id="a-popover-1"]/div/div[2]/span/span/span/button')
apply_buttons.click()

driver.refresh()

driver.find_element("id", 'nav-search-dropdown-card').click()

dropdown_element = driver.find_element("id", "searchDropdownBox")
dropdown = Select(dropdown_element)
desired_value = "search-alias=stripbooks"
dropdown.select_by_value(desired_value)

driver.find_element("id", 'twotabsearchtextbox').click()

driver.execute_script("window.open();")
driver.switch_to.window(driver.window_handles[1])

mainkeyword = input(f"{bcolors.OKGREEN}+{bcolors.ENDC} {bcolors.BOLD}Enter The Main Keyword: {bcolors.ENDC}")
query = f'chrome-extension://hbapdpeemoojbophdfndmlgdhppljgmp/html/page.html?page=autocomplete&query={mainkeyword}&service=amazon'
driver.get(query)

listk = []
input(f'{bcolors.OKGREEN}+{bcolors.ENDC} {bcolors.BOLD}Are the keywords downloaded! | Press Enter{bcolors.ENDC} \n')

til = mainkeyword.replace(' ', '-')
csv_file_path = f'amazon-keywords-{til}--{formatted_datetime}.csv'

with open(csv_file_path, 'r') as file:
    csv_reader = csv.reader(file)
    first_column = [row[0] for row in csv_reader]
    for value in first_column:
        if str(value) != 'Keyword':
            listk.append(value)

driver.close()
driver.switch_to.window(driver.window_handles[0])

count = 0
ll = []
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
    ll.append(f'{i}:{ress}:{bsr}')
    print(
        f"{bcolors.OKGREEN}[{count}]{bcolors.ENDC} " + i + f'{bcolors.OKGREEN} |----> {bcolors.ENDC}' + ress + f"{bcolors.OKGREEN} | {bcolors.ENDC}BSR {bcolors.OKGREEN}|---->{bcolors.ENDC} {bsr}" + "\n")

save = input(
    f"{bcolors.OKGREEN}+{bcolors.ENDC} Save this keyword in File {bcolors.OKGREEN}Y{bcolors.ENDC} | {bcolors.FAIL}N{bcolors.ENDC} :")
if save == "y":
    file = open(f'keyword-{til}.txt', 'w')
    sorted_list = sorted(ll, key=lambda item: int(item.split(':')[2].replace(',', '')))
    for i in sorted_list:
        file.write(i + "\n")
    file.close()
else:
    driver.close()
