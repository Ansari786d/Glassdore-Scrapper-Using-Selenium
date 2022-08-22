# -*- coding: utf-8 -*-
"""
Created on Wed Aug 17 19:30:07 2022

@author: ansari
"""

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, ElementClickInterceptedException
import requests
from bs4 import BeautifulSoup
import pandas as pd 
import numpy as np 


# options = webdriver.ChromeOptions()
# driver = webdriver.Chrome(r"C:\Users\ansar\chromedriver\chromedriver.exe",options=options)
# driver.set_window_size(1920, 1080)

# keyword = 'Data Scientist'


# # https://www.glassdoor.co.in/Job/+keyword+-jobs-SRCH_KO0,14.htm?suggestCount=0&suggestChosen=false&clickSource=searchBtn&typedKeyword=&typedLocation=&context=Jobs&dropdown=0
# print(url)
# driver.get(url)
# # driver.get("https://www.glassdoor.com/Job/jobs.htm?sc.keyword=\"' + 'Data Scientist' + '\"&locT=C&locId=1147401&locKeyword=San%20Francisco,%20CA&jobType=all&fromAge=-1&minSalary=0&includeNoSalaryJobs=true&radius=100&cityId=-1&minRating=0.0&industryId=-1&sgocId=-1&seniorityType=all&companyId=-1&employerSizes=0&applicationType=0&remoteWorkType=0'\n")


def extract(page):
    # headers = {'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36'}
    url = f"https://www.glassdoor.co.in/Job/india-python-developer-jobs-SRCH_IL.0,5_IN115_KO6,22_IP{8}.htm?includeNoSalaryJobs=true"
    print(url)
    result = requests.get(url)
    soup = BeautifulSoup(result.content, 'html.parser')
    return soup

def transform(soup):
    # try:
    #     soup.find('span',class_ ="SVGInline modal_closeIcon")
    
    jobsd = soup.find_all('div',class_ = "d-flex flex-column pl-sm css-1buaf54 job-search-key-1mn3dn8 e1rrn5ka0")   
    for jobs in jobsd:
        
        company = jobs.find('div', class_="d-flex justify-content-between align-items-start").span.text
        
        
        title = jobs.find('a',class_ = "jobLink job-search-key-1rd3saf eigr9kq1").span.text
        
        
        try:
            salary = jobs.find('div', class_="css-1buaf54 pr-xxsm").text
            
        except:
            salary =''
            pass
        
        location = jobs.find('span', class_="css-1buaf54 pr-xxsm job-search-key-iii9i8 e1rrn5ka4").text
        
        
        data = {
            'Job Title':title,
            'Company': company,
            'Location':location,
            'Salary': salary,
            }
        all_data.append(data)
    return 
        


if __name__ == "__main__":
    all_data = []
    for i in range(1,40,10):
        c = extract(i)
        transform(c)
        print("hello")
    print(len(all_data))
    
    df = pd.DataFrame(all_data)
    # df.drop_duplicates(subset ="",
    #                  keep = False, inplace = True)
 
    # df.to_csv('glasdoor_dataset.csv')
    print(df)



# for i in range(1,10):
    
#     url = f"https://www.glassdoor.co.in/Job/data-scientist-jobs-SRCH_KO0,14_IP.htm?includeNoSalaryJobs=true&pgc=AB4AAoEAPAAAAAAAAAAAAAAAAeGqQfMAagEBARAKCjc5BWhB4mv6hgkDY3ZrxZr5b6S4OeEDEy4B9OeHIxdpCexxurZXgbqIHZMgfv44fDeHBkUwc%2FHyAr9NBURAHA%2BO2LYN8tw6JqKr8atqcLpfoyzbfWkvVjAoVnFDrL6IsI7FtgAAAA%3D%3D"
#     print(url)
#     result = requests.get(url)
#     # result = requests.get('https://www.linkedin.com/jobs/search/?distance=25&f_E=2%2C3&f_JT=F&f_LF=f_AL&geoId=102250832&keywords=software%20engineer&location=Mountain%20View%2C%20California%2C%20United%20States')
    
#     soup = BeautifulSoup(result.content, 'html.parser')
#     print(len(soup))
#     jobs = soup.find_all('div',class_ = "d-flex flex-column pl-sm css-1buaf54 job-search-key-1mn3dn8 e1rrn5ka0")
    
#     Company = []
#     Title = []
#     Salary = []
#     Location = []
    
    
    
#     jobsd = soup.find_all('div',class_ = "d-flex flex-column pl-sm css-1buaf54 job-search-key-1mn3dn8 e1rrn5ka0")
    
#     for jobs in jobsd:
        
#         company = jobs.find('div', class_="d-flex justify-content-between align-items-start")
#         Company.append(company.text)
        
#         title = jobs.find('a',class_ = "jobLink job-search-key-1rd3saf eigr9kq1").span.text
#         Title.append(title)
        
#         try:
#             salary = jobs.find('div', class_="css-1buaf54 pr-xxsm").text
#             Salary.append(salary)
#         except:
#             Salary.append(np.nan)
#             pass
        
        
#         location = jobs.find('div', class_="d-flex flex-wrap job-search-key-1m2z0go e1rrn5ka2").span.text
#         Location.append(location)
        
    # df = pd.DataFrame({
    #     'Job Title':Title,
    #     'Company': Company,
    #     'Location':Location,
    #     'Salary': Salary,
    #     })

    # # print(df)
    # df.to_csv("C:\\Users\\ansar\\Desktop\\MyDesk\\WebScrapping\\glassdoor.csv")
    


# print(len(Company))
# print(len(Salary))
# print(len(Title))
# print(len(Location))

# print(Company)
# print(Salary)
# print(Title)
# print(Location)

# df = pd.DataFrame({
#     'Job Title':Title,
#     'Company': Company,
#     'Location':Location,
#     'Salary': Salary,
#     })

# print(df)
# df.to_csv("C:\\Users\\ansar\\Desktop\\MyDesk\\WebScrapping\\glassdoor.csv")





