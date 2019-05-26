# -*- coding: utf-8 -*-
"""
Created on Sun May  5 15:06:06 2019

@author: AlbertVillarOrtiz
"""

from selenium import webdriver 
from selenium.webdriver.common.by import By 
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC 
from selenium.common.exceptions import TimeoutException
import numpy as np
import time
from datetime import datetime  
from datetime import timedelta
import constants as c
from bs4 import BeautifulSoup
import pandas as pd

def setYears(years):
    yearsUrl = []
    for i in range(3, len(years)-1):
        yearsUrl.append(years[i]+'-'+years[i+1])
    
    return(yearsUrl)
    
def setPages(driver):
    pagination = driver.find_element_by_xpath('//*[@id="pagination"]')
    listPages = pagination.find_elements_by_tag_name('a')

    return(int(listPages[-1].get_attribute("x-page"))+1)

def getData(driver, year):
    html = driver.page_source
    html = BeautifulSoup(html, "html.parser")
    html.prettify
    
    return(setDataset(html, year))

def setDataset(html, year):
    dataset = []
    hour = html.find_all(attrs={'class': 'table-time'})
    match = html.find_all(attrs={'class': 'table-participant'})
    pts = html.find_all(attrs={'class': 'table-score'})
    odds = html.find_all(attrs={'class': 'odds-nowrp'})
    
    for i in range(len(hour)):
        h, m, p, o1, o2 = formData(hour, match, pts, odds, i)
        
        if m[0] in c.TEAMS.values() and m[1] in c.TEAMS.values() and (o1 != '-' or o2 != '-'):
            if len(p) == 2:
                p[1] = p[1].replace('OT','')
                dataset.append([year,h,m[0],m[1],p[0],p[1],o1,o2])
            else:
                dataset.append([year,h,m[0],m[1],p,p,o1,o2])
    
    return(dataset)

def saveDataset(dataset, year):
    df = pd.DataFrame(dataset)
    df.to_excel('dataInit/odds/odds-'+year+'.xlsx', index=False)
    print('Datos de los partidos del '+year+' actualizados correctamente.') 

def formData(hour, match, pts, odds, i):
    index = 2*i
    h = hour[i].get_text()
    m = match[i].get_text().split('-')
    p = pts[i].get_text().split(':')
    o1 = odds[index].get_text()
    o2 = odds[index+1].get_text()
    m[0] = m[0].replace(' ','').replace(u'\xa0', u'')
    m[1] = m[1].replace(' ','').replace(u'\xa0', u'')
    if m[0] in c.TEAMS: m[0] = c.TEAMS[m[0]]
    if m[1] in c.TEAMS: m[1] = c.TEAMS[m[1]]
    
    return(h, m, p, o1, o2)
    
option = webdriver.ChromeOptions()
#option.add_argument(“ — incognito”)
driver = webdriver.Chrome(executable_path= c.DRIVERPATH)

yearsFormat = setYears(c.YEARSH2H)
datasetGlobal = []

for i in range(len(yearsFormat)):
    dataset = []
    driver.get(c.URLBASE.format(yearsFormat[i], 1))
    pages = setPages(driver)   
    
    for page in range(2, pages):
        driver.get(c.URLBASE.format(yearsFormat[i], page))
        driver.implicitly_wait(5)
        dataset.extend(getData(driver, c.YEARSH2H[i+3]))
    
    datasetGlobal.extend(dataset)
    saveDataset(dataset, c.YEARSH2H[i+3])

df = pd.DataFrame(datasetGlobal)
df.to_excel('dataInit/odds/odds.xlsx', index=False)
print('Datos de los partidos actualizados correctamente.')

    