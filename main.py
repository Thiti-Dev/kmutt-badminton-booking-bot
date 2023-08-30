##https://docs.google.com/forms/d/e/1FAIpQLSe204X8BO3IpMk0uiytzF1Z7hgMri4tO9_k9FtOdi6pPI0vSw/viewform?usp=sf_link

from selenium import webdriver
from selenium.common.exceptions import *
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import datetime
import threading


target_form_url = "https://docs.google.com/forms/d/e/1FAIpQLSeZNL6JI8ZkG9xjYLQiCnW5MjDS2xKRoGTBaP0nnWupzzdoZQ/viewform"

def first_reservation():
    print("Starting first_reservation process")

    driver = webdriver.Chrome()
    driver.get(target_form_url)

    wait = WebDriverWait(driver, 10, poll_frequency=1, ignored_exceptions=[ElementNotVisibleException, ElementNotSelectableException])
    elem = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')))

    name_field = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
    name_field.click()
    name_field.clear()
    name_field.send_keys('ธิติ มหาวรรณกิจ')


    name_field = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
    name_field.click()
    name_field.clear()
    name_field.send_keys('0931398015')

    phone_field = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
    phone_field.click()
    phone_field.clear()
    phone_field.send_keys('thiti.mwk.main@gmail.com')

    type_of_client = driver.find_element(By.XPATH, '//*[@id="i20"]')
    type_of_client.click()

    next_button = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div')
    next_button.click()

    time.sleep(0.5)
    elem = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')))
    student_code_field = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
    student_code_field.click()
    student_code_field.clear()
    student_code_field.send_keys('60090500410')

    department_field = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
    department_field.click()
    department_field.clear()
    department_field.send_keys('คณิตศาสตร์')

    faculty_field = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[4]/div/div/div[2]/div/div[1]/div/div[1]/input')
    faculty_field.click()
    faculty_field.clear()
    faculty_field.send_keys('วิทยาศาสตร์')

    degree_field = driver.find_element(By.XPATH, '//*[@id="i17"]')
    degree_field.click()

    year_of_study_field = driver.find_element(By.XPATH, '//*[@id="i39"]')
    year_of_study_field.click()

    next_button2 = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div[2]')
    next_button2.click()

    time.sleep(0.5)
    elem = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="i11"]')))
    court_2_radio = driver.find_element(By.XPATH, '//*[@id="i11"]')
    court_2_radio.click()

    next_button3 = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div[2]')
    next_button3.click()

    time.sleep(0.5)
    elem = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')))

    P1_field = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
    P1_field.click()
    P1_field.clear()
    P1_field.send_keys('จิราพร แย้มกลีบ')

    P2_field = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
    P2_field.click()
    P2_field.clear()
    P2_field.send_keys('ปพิชญา มหาวรรณกิจ')

    P3_field = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[4]/div/div/div[2]/div/div[1]/div/div[1]/input')
    P3_field.click()
    P3_field.clear()
    P3_field.send_keys('Aung Phone Htet')

    while True:
        current_time = datetime.datetime.now()
        current_hour = current_time.hour
        current_minute = current_time.minute
        
        if current_hour == 13 and current_minute == 0:  # 13 represents 1 PM
            print("[First Reservation] Pressing Submit btn")
            submit_btn = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div[2]')
            submit_btn.click()
            time.sleep(10)
            break
        
        print("[First Reservation] Waiting for 1:00 PM...")
        time.sleep(0.5)

    time.sleep(3)

def second_reservation():
    print("Starting second_reservation process")

    driver = webdriver.Chrome()
    driver.get(target_form_url)

    driver.set_window_position(4000, 0)

    wait = WebDriverWait(driver, 10, poll_frequency=1, ignored_exceptions=[ElementNotVisibleException, ElementNotSelectableException])
    elem = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')))

    name_field = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
    name_field.click()
    name_field.clear()
    name_field.send_keys('ธิติ มหาวรรณกิจ')


    name_field = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
    name_field.click()
    name_field.clear()
    name_field.send_keys('0931398015')

    phone_field = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
    phone_field.click()
    phone_field.clear()
    phone_field.send_keys('thiti.mwk.main@gmail.com')

    type_of_client = driver.find_element(By.XPATH, '//*[@id="i20"]')
    type_of_client.click()

    next_button = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div')
    next_button.click()

    time.sleep(0.5)
    elem = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')))
    student_code_field = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
    student_code_field.click()
    student_code_field.clear()
    student_code_field.send_keys('60090500410')

    department_field = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
    department_field.click()
    department_field.clear()
    department_field.send_keys('คณิตศาสตร์')

    faculty_field = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[4]/div/div/div[2]/div/div[1]/div/div[1]/input')
    faculty_field.click()
    faculty_field.clear()
    faculty_field.send_keys('วิทยาศาสตร์')

    degree_field = driver.find_element(By.XPATH, '//*[@id="i17"]')
    degree_field.click()

    year_of_study_field = driver.find_element(By.XPATH, '//*[@id="i39"]')
    year_of_study_field.click()

    next_button2 = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div[2]')
    next_button2.click()

    time.sleep(0.5)
    elem = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="i14"]')))
    court_2_radio = driver.find_element(By.XPATH, '//*[@id="i14"]')
    court_2_radio.click()

    next_button3 = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div[2]')
    next_button3.click()

    time.sleep(0.5)
    elem = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')))

    P1_field = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
    P1_field.click()
    P1_field.clear()
    P1_field.send_keys('จิราพร แย้มกลีบ')

    P2_field = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
    P2_field.click()
    P2_field.clear()
    P2_field.send_keys('ปพิชญา มหาวรรณกิจ')

    P3_field = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[4]/div/div/div[2]/div/div[1]/div/div[1]/input')
    P3_field.click()
    P3_field.clear()
    P3_field.send_keys('Aung Phone Htet')


    while True:
        current_time = datetime.datetime.now()
        current_hour = current_time.hour
        current_minute = current_time.minute
        
        if current_hour == 13 and current_minute == 0:  # 13 represents 1 PM
            print("[Second Reservation] Pressing Submit btn")
            submit_btn = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div[2]')
            submit_btn.click()
            time.sleep(10)
            break
        
        print("[Second Reservation] Waiting for 1:00 PM...")
        time.sleep(0.5)

    time.sleep(3)

thread = threading.Thread(target=first_reservation)
thread2 = threading.Thread(target=second_reservation)
thread.start()
thread2.start()