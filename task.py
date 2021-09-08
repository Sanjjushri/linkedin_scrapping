import requests, time, random
from bs4 import BeautifulSoup
from selenium import webdriver

browser = webdriver.Chrome('/home/sanjju/chromedriver')
browser.get('https://www.linkedin.com/login')
file = open('config.txt')
lines = file.readlines()
username = lines[0]
password = lines[1]

elementID = browser.find_element_by_id('username')
elementID.send_keys(username)

elementID = browser.find_element_by_id('password')
elementID.send_keys(password)

elementID.submit()

link = 'https://www.linkedin.com/in/sanjjushri-varshini-r-aa33551ba/'
browser.get(link)

SCROLL_PAUSE_TIME = 5

#get scroll input
last_height = browser.execute_script("return document.body.scrollHeight")

for i in range(5):
    #scroll down to bottom
    browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    #wait to load page
    time.sleep(SCROLL_PAUSE_TIME)

    #claculate new scroll height and compare the last scroll height
    new_height = browser.execute_script("return document.body.scrollHeight")
    if new_height == last_height:
        break
    last_height = new_height

src = browser.page_source
#print(src)
soup = BeautifulSoup(src, 'lxml')

name_location = soup.find('div', {'class' : 'pv-text-details__left-panel mr5'})
#print(name_div)
name_loc = name_location.find('h1', {'class' : 'text-heading-xlarge inline t-24 v-align-middle break-words'})
name = name_loc.get_text().strip()

location_div = name_location.find('span', {'class' : 'text-body-small inline t-black--light break-words'})
location = location_div.get_text().strip()

about_loc = soup.find('div', {'class':"inline-show-more-text inline-show-more-text--is-collapsed mt4 t-14"})
about = about_loc.get_text().strip()

connections_num = soup.find('span', {'class' : 't-bold'})
connections = connections_num.get_text().strip()

job_title_div = soup.find('h3', {'class' : 't-16 t-black t-bold'})
job_title = job_title_div.get_text()

duration_loc = soup.find('h4', {'class' : 'pv-entity__date-range t-14 t-black--light t-normal'})
duration = duration_loc.get_text().strip()
#print(duration)

edu_loc = soup.find('h3', {'class' : 'pv-entity__school-name t-16 t-black t-bold'})
insti_name = edu_loc.get_text()

degree_loc = soup.find('span', {'class' : 'pv-entity__comma-item'})
degree = degree_loc.get_text()

# field = soup.find('span', {'class' : 'pv-entity__comma-item'})
# field_of_study = field.get_text()

try:
   course_tit = soup.find('h3', {'class' : 't-16 t-bold'})
   course = course_tit.get_text()
except Exception as e:
    course = None

try:
    vol_exp = soup.find('h3', {'class' : 't-16 t-black t-bold'})
    volunteer_experience = vol_exp.get_text()
except Exception as e:
    volunteer_experience = None



info = []
info.append(link)
info.append(name)
info.append(location)
info.append(about)
info.append(connections)
info.append(job_title)
info.append(duration)
info.append(insti_name)
info.append(degree)
#info.append(field_of_study)
info.append(course)
print(info)

