import csv
import pandas as pd
from bs4 import BeautifulSoup
import requests
from time import sleep
import numpy as np
from selenium import webdriver

phone_links=[]
phone_names=[]
phone_weights=[]
screen_sizes=[]
screen_resolutions=[]
screen_types=[]
processors=[]
phone_cameras=[]
on_phone_cameras=[]
batteries=[]
rams=[]
genel=[]

url='https://www.hepsiburada.com/android-telefonlar-c-60005201?sayfa=2'
driver = webdriver.Chrome()
driver.get(url)
sleep(4)
r = requests.get(url)
soup = BeautifulSoup(driver.page_source,"html.parser")
table=driver.find_element_by_xpath("//ul[@class='productListContent-wrapper productListContent-grid-0']")
a_tags=table.find_elements_by_tag_name("a")
for i in a_tags:
    bur=i.get_attribute('href')
    phone_links.append(bur)

counter=0

for i in range(0,(len(phone_links))):
    sleep(2)
    driver.get(phone_links[counter])
    counter+=1
    tbody=driver.find_element_by_xpath('//*[@id="productTechSpecContainer"]/table[2]/tbody')
    phone_name=driver.find_element_by_xpath('//*[@id="detail-container"]/div/header/span').text
    phone_weight=driver.find_elements_by_xpath('//*[@id="productTechSpecContainer"]/table[2]/tbody/tr[1]')[0].text
    screen_size=driver.find_elements_by_xpath('//*[@id="productTechSpecContainer"]/table[2]/tbody/tr[13]')[0].text
    screen_resolution=driver.find_elements_by_xpath('//*[@id="productTechSpecContainer"]/table[2]/tbody/tr[14]')[0].text
    screen_type=driver.find_elements_by_xpath('//*[@id="productTechSpecContainer"]/table[2]/tbody/tr[16]')[0].text
    processor=driver.find_elements_by_xpath('//*[@id="productTechSpecContainer"]/table[2]/tbody/tr[25]')[0].text
    camera=driver.find_elements_by_xpath('//*[@id="productTechSpecContainer"]/table[2]/tbody/tr[30]')[0].text
    on_camera=driver.find_elements_by_xpath('//*[@id="productTechSpecContainer"]/table[2]/tbody/tr[38]')[0].text
    battery=driver.find_elements_by_xpath('//*[@id="productTechSpecContainer"]/table[2]/tbody/tr[41]')[0].text
    ram=driver.find_elements_by_xpath('//*[@id="productTechSpecContainer"]/table[2]/tbody/tr[44]')[0].text
    print(phone_name,phone_weight,screen_size,screen_type,processor,camera,on_camera,battery,ram)
    phone_names.append(phone_name)
    phone_weights.append(phone_weight)
    screen_sizes.append(screen_size)
    screen_resolutions.append(screen_resolution)
    screen_types.append(screen_type)
    processors.append(processor)
    phone_cameras.append(camera)
    on_phone_cameras.append(on_camera)
    batteries.append(battery)
    rams.append(ram)
    sleep(2)
driver.close()
genel.append([phone_names,phone_weights,screen_sizes,screen_types,processors,phone_cameras,on_phone_cameras,batteries,rams])
a=np.array(phone_names)
b=np.array(phone_weights)
c=np.array(screen_sizes)
d=np.array(screen_resolutions)
e=np.array(screen_types)
g=np.array(processors)
h=np.array(phone_cameras)
j=np.array(on_phone_cameras)
k=np.array(batteries)
l=np.array(rams)

df = pd.DataFrame({"Telefon Adı" : a, "\t\t\t\t\t\t\t\t\t\t\tAğırlık" : b, "\tEkran Boyutu" : c, "Çözünürlük" : d, "Ekran Tipi" : e, "İşlemci" : g, "Kamera" : h, "Ön Kamera" : j, "Pil" : k, "Ram" : l})
df.to_csv("genelbilgiler.csv", encoding='UTF-8', index=False)
"""
csvfile = open("bilgiler.csv", "a", newline='', encoding='UTF-8')
writer = csv.writer(csvfile, delimiter=" ")
for c in genel:
    for x in c:
        writer.writerow(x)
csvfile.close()
print("Ürünün bilgileri dosyaya işlendi.")
"""
