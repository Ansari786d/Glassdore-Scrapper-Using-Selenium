# -*- coding: utf-8 -*-
"""
Created on Fri Aug 19 22:49:08 2022

@author: ansar

"""
from selenium import webdriver
import pandas as pd
import numpy as np
import time
from selenium.webdriver.common.by import By


options = webdriver.ChromeOptions()
driver = webdriver.Chrome(
    r"C:\Users\ansar\chromedriver\chromedriver.exe", options=options)
driver.set_window_size(1920, 1080)


all_data = []
for i in range(1, 3):
    driver.get(
        f"https://www.glassdoor.co.in/Job/python-developer-jobs-SRCH_KO0,16_IP{i}.htm?includeNoSalaryJobs=true&pgc=AB4AAYEAHgAAAAAAAAAAAAAAAeHxmucASwECAQcUBgIUzfp645Ayp3kspMvaOH%2FMjzErD09kJGX9r58QkDhdFa8FQ73WDFpLAAZllNzjuwhyNnAIJ54P0Lw%2Bd%2B5mnVG3mYnr2QAA")
    time.sleep(5)
    try:
        driver.find_element(
            By.XPATH, "//span[@class='SVGInline modal_closeIcon']").click()
    except Exception as e:
        print(e)
        pass

    time.sleep(1.8)

    try:
        driver.find_element(
            By.XPATH, '//*[@id="JAModal"]/div/div[2]/span/svg/path').click()
    except:
        pass

    try:

        elements = driver.find_elements(
            By.XPATH, "//div[@class='d-flex flex-column pl-sm css-1buaf54 job-search-key-1mn3dn8 e1rrn5ka0']")
        print(len(elements))

    except Exception as e:
        print(e)

    for item in elements:
        # print(item)
        title = item.find_element(
            By.XPATH, ".//a[@class='jobLink job-search-key-1rd3saf eigr9kq1']").text
        print(title)
        company = item.find_element(
            By.XPATH, ".//div[@class='d-flex justify-content-between align-items-start']").text
        print(company)
        location = item.find_element(
            By.XPATH, ".//span[@class='css-1buaf54 pr-xxsm job-search-key-iii9i8 e1rrn5ka4']").text
        print(location)
        try:
            salary = item.find_element(
                By.XPATH, ".//div[@class='css-1buaf54 pr-xxsm']").text
            print(salary)
        except:
            salary = np.nan
            print(salary)
        data = {
            'Job Title': title,
            'Company': company,
            'Location': location,
            'Salary': salary,
        }
        all_data.append(data)
    df = pd.DataFrame(all_data)
    df.to_csv('glasdoor_dataset.csv')
    if len(elements) == '30':
        continue
# quit the driver
driver.quit()
