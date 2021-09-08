import requests
from bs4 import BeautifulSoup
import pandas as pd
import csv 
url = "https://www.linkedin.com/in/aishwarya-kapoor-6019a51a2/"

linkedin=[]
def get_soup(url):
    response=requests.get(url)
    soup= BeautifulSoup(response.text,'html.parser')
    return soup

def get_reviews(soup): 
    profiles = soup.find('id',{'class':'scaffold-layout__main'})
    try:
        #for item in profiles:
        details = {
        'name':profiles.find_all('h1', {'class':'text-heading-xlarge inline t-24 v-align-middle break-words'}).text,
        'location ':profiles.find('span',{'class':'text-body-small inline t-black--light break-words'}).text
        # 'about':item.find('i',{'data-hook':'review-star-rating'}).text,
        # 'experience': item.find('span',{'data-hook':'review-body'}).text.strip(),
        # 'education': item.find('span',{'data-hook':'review-body'}).text.strip(),
        # 'Licenses&certificates': item.find('span',{'data-hook':'review-body'}).text.strip(),
        # 'volunter-experience': item.find('span',{'data-hook':'review-body'}).text.strip(),
        # 'skills': item.find('span',{'data-hook':'review-body'}).text.strip(),
        # 'Accomplishments': item.find('span',{'data-hook':'review-body'}).text.strip()
        }
        linkedin.append(details)
        print("hello")
    except:
        pass

soup = get_soup('https://www.linkedin.com/in/aishwarya-kapoor-6019a51a2/')
get_reviews(soup)

df = pd.DataFrame(linkedin)
df.to_csv('profile.csv')
print('End')


import requests
from bs4 import BeautifulSoup
import pandas as pd

#url = "https://www.amazon.in/Solimo-Plastic-Container-White-SOPLA186/product-reviews/B07P94VK1Q/ref=cm_cr_dp_d_show_all_btm?ie=UTF8&reviewerType=all_reviews"

reviewlist=[]
def get_soup(url):
    response=requests.get(url)
    soup= BeautifulSoup(response.text,'html.parser')
    return soup

def get_reviews(soup): 
    reviews = soup.find_all('main',{'class':'scaffold-layout__main'})
    try:
        for item in reviews:
            review = {
             'name':item.find('h1', {'class':'text-heading-xlarge inline t-24 v-align-middle break-words'}).text,
             'location ':item.find('span',{'class':'text-body-small inline t-black--light break-words'}).text
            }
            reviewlist.append(review)
    except:
        pass
for x in range(1,10):
    soup = get_soup('https://www.linkedin.com/in/aishwarya-kapoor-6019a51a2/')
    #print(f'Getting page:{x}')
    get_reviews(soup) 
    print(len(reviewlist))
    if  soup.find('main',{'class':'scaffold-layout__main'}):
        pass
    else:
        break

df = pd.DataFrame(reviewlist)
df.to_csv('reviews.csv')
print('End')