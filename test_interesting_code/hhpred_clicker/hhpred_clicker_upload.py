import time
import pyautogui
import pyperclip

import pandas as pd

from config import *
from utils import submit

# Отправка данных на сервер
user_answer = pyautogui.confirm('Run the clicker for uploads?')
if user_answer == 'OK':
    submit('Astrophysics is the best')
    for item in table.aa_sequence:
        submit(item)