# INSTALL PACKAGE
import os
try:
    from selenium import webdriver
    from selenium.webdriver.common.by import By
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.support import expected_conditions as EC
    from selenium.webdriver.support.ui import Select
    from selenium.webdriver.chrome.service import Service

except ImportError:
    os.system('pip install selenium')
try:
    import csv
except ImportError:
    os.system('pip install python-csv')
    os.system('pip install csv')
try:
    from webdriver_manager.chrome import ChromeDriverManager
except ImportError:
    os.system('pip install webdriver-manager')

try:
    import datetime
except ImportError:
    os.system('pip install datetime')

try:
    import pause
except ImportError:
    os.system('pip install pause')
try:
    import pandas as pd
except ImportError:
    os.system('pip install pandas')
try:
    from tabulate import tabulate
except ImportError:
    os.system('pip install tabulate')


def extractkey():
    dirs = input(f"{bcolors.OKGREEN}+{bcolors.ENDC} {bcolors.BOLD}Enter Location Of Your File Keyword:{bcolors.ENDC} ")
    for key in open(f'keywords\{dirs}', 'r').read().split('\n'):
        co = key.split(':', 3)
        print(co[0])
def checkbsr(driver):
    global ffg
    try:
        #print(driver.find_element(By.CSS_SELECTOR, "div.text-sm.text-dark.font-weight-bold").text)
        if driver.find_element(By.CSS_SELECTOR, "div.text-sm.text-dark.font-weight-bold").text != "Preparing the results...":
            driver.refresh()
            checkbsr(driver)
        else:
            pass
    except:
        pass


    try:
        element = driver.find_element(By.CSS_SELECTOR, "h3.d-flex.align-items-center.py-0")

        # Extract the value
        ffg = element.text.split()[-1]

        return ffg

    except:
        pause.seconds(3)
        checkbsr(driver)
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



def keyextra(market,mainkeyword):
    # Get the current date and time
    current_datetime = datetime.datetime.now()
    formatted_datetime = current_datetime.strftime("%Y-%m-%d")


    # get the current working directory
    download_directory = f'{os.getcwd()}\sugesstion'


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

    # options.add_argument("--disable-popup-blocking")

    options.add_experimental_option('prefs', {
        'download.default_directory': download_directory,
        'download.prompt_for_download': False,
        'download.directory_upgrade': True,
        'safebrowsing.enabled': True
    })


    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

    if market == "com" or market == "uk":
        if market == "uk":
            driver.get('https://www.amazon.co.uk/')
        else:
            driver.get('https://www.amazon.com/')
        try:
            acceptc = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.ID, 'sp-cc-accept'))
            )
            acceptc.click()
        except:
            pass

        main_window_handle = driver.current_window_handle

        # Loop through all window handles and close any tabs except the main driver tab
        for handle in driver.window_handles:
            if handle != main_window_handle:
                driver.switch_to.window(handle)
                driver.close()

        # Switch back to the main driver tab
        driver.switch_to.window(main_window_handle)

        try:
            location_element = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.ID, 'nav-global-location-data-modal-action'))
            )
            location_element.click()
        except:
            driver.refresh()
            location_element = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.ID, 'nav-global-location-data-modal-action'))
            )
            location_element.click()

        postal_code_input = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, 'GLUXZipUpdateInput'))
        )
        postal_code_input.clear()

        if market == "com" or market == "COM":
            postal_code_input.send_keys('10001')
            apply_button = driver.find_element(By.XPATH, '//*[@id="GLUXZipUpdate"]/span/input')
            apply_button.click()

            apply_buttons = driver.find_element(By.XPATH, '//*[@id="a-popover-1"]/div/div[2]/span/span/span/button')
            apply_buttons.click()

        else:
            postal_code_input.send_keys('AL3 8QE')
            apply_button = driver.find_element(By.XPATH, '//*[@id="GLUXZipUpdate"]/span/input')
            apply_button.click()
            pause.seconds(1)

        driver.refresh()

        driver.find_element("id", 'nav-search-dropdown-card').click()

        dropdown_element = driver.find_element("id", "searchDropdownBox")
        dropdown = Select(dropdown_element)
        desired_value = "search-alias=stripbooks"
        dropdown.select_by_value(desired_value)

        driver.find_element("id", 'twotabsearchtextbox').click()
    elif market == "fr" or market == "FR":
        driver.get('https://www.amazon.fr/')
        try:
            acceptc = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.ID, 'sp-cc-accept'))
            )
            acceptc.click()
        except:
            pass

        main_window_handle = driver.current_window_handle

        # Loop through all window handles and close any tabs except the main driver tab
        for handle in driver.window_handles:
            if handle != main_window_handle:
                driver.switch_to.window(handle)
                driver.close()

        # Switch back to the main driver tab
        driver.switch_to.window(main_window_handle)


        try:
            location_element = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.ID, 'nav-global-location-data-modal-action'))
            )
            location_element.click()
        except:
            driver.refresh()
            location_element = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.ID, 'nav-global-location-data-modal-action'))
            )
            location_element.click()

        postal_code_input = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, 'GLUXZipUpdateInput'))
        )
        postal_code_input.clear()
        postal_code_input.send_keys('75001')

        apply_button = driver.find_element(By.XPATH, '//*[@id="GLUXZipUpdate"]/span/input')
        apply_button.click()

        driver.refresh()

        driver.find_element("id", 'nav-search-dropdown-card').click()

        dropdown_element = driver.find_element("id", "searchDropdownBox")
        dropdown = Select(dropdown_element)
        desired_value = "search-alias=stripbooks"
        dropdown.select_by_value(desired_value)

        driver.find_element("id", 'twotabsearchtextbox').click()




    driver.execute_script("window.open();")
    driver.switch_to.window(driver.window_handles[1])

    query = f'chrome-extension://hbapdpeemoojbophdfndmlgdhppljgmp/html/page.html?page=autocomplete&query={mainkeyword}&service=amazon'
    driver.get(query)

    listk = []
    input(f'{bcolors.OKGREEN}+{bcolors.ENDC} {bcolors.BOLD}Are the keywords downloaded! | Press Enter{bcolors.ENDC} \n')


    til = mainkeyword.replace(' ', '-')
    csv_file_path = f'{os.getcwd()}\sugesstion\\amazon-keywords-{til}--{formatted_datetime}.csv'
    print(
        f"{bcolors.OKGREEN}+{bcolors.ENDC} {bcolors.BOLD}Total Keyword Find{bcolors.ENDC} ===> {len(open(csv_file_path, 'r').read().splitlines())}")


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
    if market == "fr" or market == "FR":
        for i in listk:
            count += 1
            try:
                driver.find_element("id", 'twotabsearchtextbox').clear()
            except:
                pass
            driver.find_element("id", 'twotabsearchtextbox').send_keys(i)
            driver.find_element("id", 'nav-search-submit-button').click()
            res = driver.find_element(By.XPATH, '//*[@id="search"]/span/div/h1/div/div[1]/div/div/span[1]').text
            bsr = checkbsr(driver)

            if "plus de" in str(res):
                results = res.partition('plus de ')[2]
            else:
                results = res
            ress = results.partition(' résultats pour')[0]
            ll.append(f'{i}:{ress}:{bsr}')
            print(
                f"{bcolors.OKGREEN}[{count}]{bcolors.ENDC} " + i + f' {bcolors.OKGREEN}|{bcolors.ENDC} RESULTS {bcolors.OKGREEN}|----> {bcolors.ENDC}' + ress + f"{bcolors.OKGREEN} | {bcolors.ENDC}BSR {bcolors.OKGREEN}|---->{bcolors.ENDC} {bsr}" + "\n")
    elif market == "com" or market == "COM" or market == "uk" or market == "UK":
        for i in listk:
            count += 1
            try:
                driver.find_element("id", 'twotabsearchtextbox').clear()
            except:
                pass
            driver.find_element("id", 'twotabsearchtextbox').send_keys(i)
            driver.find_element("id", 'nav-search-submit-button').click()
            res = driver.find_element(By.XPATH, '//*[@id="search"]/span/div/h1/div/div[1]/div/div/span[1]').text
            bsr = checkbsr(driver)

            if "over" in str(res):
                results = res.partition('over ')[2]
            elif "of" in str(res):
                results = res.partition('of ')[2]
            else:
                results = res
            ress = results.partition(' results for')[0]
            ll.append(f'{i}:{ress}:{bsr}')
            print(
                f"{bcolors.OKGREEN}[{count}]{bcolors.ENDC} " + i + f' {bcolors.OKGREEN}|{bcolors.ENDC} RESULTS {bcolors.OKGREEN}|----> {bcolors.ENDC}' + ress + f"{bcolors.OKGREEN} | {bcolors.ENDC}BSR {bcolors.OKGREEN}|---->{bcolors.ENDC} {bsr}" + "\n")


    save = input(
        f"{bcolors.OKGREEN}+{bcolors.ENDC} Save this keyword in File {bcolors.OKGREEN}Y{bcolors.ENDC} | {bcolors.FAIL}N{bcolors.ENDC} :")
    if save == "y" or  save == "Y":
        file = open(f'keywords\keyword-{til}.txt', 'w')
        sorted_list = sorted(ll, key=lambda item: int(item.split(':')[2].replace(',', '')))
        for i in sorted_list:
            file.write(i + "\n")
        file.close()

        data = []
        for item in sorted_list:
            keyword, count, value = item.split(':')
            data.append([keyword, count, value])

        df = pd.DataFrame(data, columns=['Keyword', 'Results', 'Bsr'])

        # Display DataFrame as ASCII table
        print(tabulate(df, headers='keys', tablefmt='psql'))

        again = input(
            f"{bcolors.OKGREEN}+{bcolors.ENDC} Start New Session: {bcolors.OKGREEN}Y{bcolors.ENDC} | {bcolors.FAIL}N{bcolors.ENDC} :")
        if again == "y" or again == "Y":
            driver.close()
            keyextra()
    else:
        driver.close()

def sortbsr():
    sorted_list = []
    data = []
    dirs = input(f"{bcolors.OKGREEN}+{bcolors.ENDC} {bcolors.BOLD}Enter Dir Of Your File Keyword:{bcolors.ENDC} ")
    for key in open(f'keywords\{dirs}', 'r').read().split('\n'):
        sorted_list.append(key)

    clean = [item for item in sorted_list if item]

    sorted_lists = sorted(clean, key=lambda item: int(item.split(':')[2].replace(',', '')))

    for item in sorted_lists:
        if item:
            keyword, count, value = item.split(':')
            data.append([keyword, count, value])

    df = pd.DataFrame(data, columns=['Keyword', 'Results', 'Bsr'])
    print(tabulate(df, headers='keys', tablefmt='psql'))



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
{bcolors.OKGREEN}[3]{bcolors.ENDC} - {bcolors.BOLD}Sort Keyword By Bsr{bcolors.ENDC}       |
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
elif choice == 2:
    market = input(f"{bcolors.OKGREEN}+{bcolors.ENDC} {bcolors.BOLD}Enter Market | com | fr | uk |:{bcolors.ENDC} ")
    mainkeyword = input(f"{bcolors.OKGREEN}+{bcolors.ENDC} {bcolors.BOLD}Enter The Main Keyword: {bcolors.ENDC}")

    keyextra(market,mainkeyword)
elif choice == 3:
    sortbsr()


