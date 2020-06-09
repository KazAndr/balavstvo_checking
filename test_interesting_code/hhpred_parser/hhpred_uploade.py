import time
import glob
import pyautogui
import pyperclip
import pandas as pd

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.keys import Keys 

from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import StaleElementReferenceException


def submit(message):
    pyperclip.copy(message)

    while driver.find_element_by_xpath(xpath_textbox).get_property("value") != message:
        driver.find_element_by_xpath(xpath_textbox).clear()
        driver.find_element_by_xpath(xpath_textbox).send_keys(Keys.CONTROL, "v")
    
    driver.find_element_by_xpath(xpath_submit).click()

    try:
        driver.implicitly_wait(3)
        driver.find_element_by_xpath(start_job_aw).click()
    except NoSuchElementException:
        driver.implicitly_wait(30)
        
    driver.find_element_by_xpath(xpath_input).click()
    time.sleep(2)
 

default_files = sorted(glob.glob('*.xls'))

if len(default_files) == 0:
    default_files.append('Enter a filename here!')
filename = pyautogui.prompt(
    text='Enter the name of a file for analisys:',
    title='File for analisys',
    default=f'{default_files[0]}'
)
table = pd.read_excel(filename, sheet_name='Sheet1')

driver = webdriver.Chrome()
driver.maximize_window() 
driver.implicitly_wait(30) # глобальное время ожидания для всех элементов
driver.wait = WebDriverWait(driver, 5)
# Захдим на сайт
driver.get("https://toolkit.tuebingen.mpg.de/tools/hhpred")

# Прописываем изначальные пути (полные)
xpath_cookie = '/html/body/div/div[5]/div[2]/button'
xpath_textbox = '/html/body/div/div[1]/div[3]/div[2]/div/form/div/div/div[2]/div[1]/div/div/div/div[1]/div/fieldset[1]/div/textarea'
xpath_submit = '/html/body/div/div[1]/div[3]/div[2]/div/form/div/div/div[2]/div[1]/fieldset/div/button'
xpath_input = '/html/body/div/div[1]/div[3]/div[2]/div/form/div/div/div[1]/ul/li[1]/a'
start_job_aw = '/html/body/div/div[1]/div[3]/div[2]/div/form/div/div/div[2]/div[3]/div/div/button[1]'

xpath_1 = '/html/body/div/div[1]/div[1]/div[2]/div/div[2]/a[1]'
# Жамкаем кнопку по поводу cookie-сов
time.sleep(1)
driver.find_element_by_xpath(xpath_cookie).click()
user_answer = pyautogui.confirm('Run the clicker for uploads?')
if user_answer == 'OK':
    submit('MMMMMMMMMMMMM')
    for item in table.aa_sequence:
        submit(item)
pyautogui.alert(
    text=(f'The program finished successfully!\n'
          f'A total of {table.aa_sequence.size} sequences were upload.'),
    title='Uploading completed')
