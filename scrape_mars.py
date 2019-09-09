# To add a new cell, type '#%%'
# To add a new markdown cell, type '#%% [markdown]'

#%%
from splinter import browser
from bs4 import BeautifulSoup
import pandas as pd
import requests
import pymongo
import time


#%%
def init_browser(): 
    executable_path = {'executable_path': 'chromedriver.exe'}
    return browser('chrome', **executable_path, headless=False)


#%%
def scrape(): 

    browser = init_browser() 


    url = 'https://mars.nasa.gov/news/'
    browser.visit(url)
    time.sleep(2)


#%% [markdown]
# # NASA Mars News

#%%



#%%



#%%


#%% [markdown]
# # JPL Mars Space Images - Featured Image

#%%
    featured_image_url= 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
    browser.visit(featured_image_url)
    time.sleep(1)
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')


#%%
    featured_image = soup.find ('article')['style'].replace('background-image: url(','').replace(');', '')


#%%
#Slice the url to only include the text inside the hyphens 
    featured_image = featured_image[1:-1]


#%%
    parent_url = 'https://www.jpl.nasa.gov'


#%%
    image_url= parent_url + featured_image 


#%% [markdown]
# # Mars Weather

#%%
    mars_weather_url = 'https://twitter.com/marswxreport?lang=en'
    browser.visit(mars_weather_url)
    time.sleep(2)

    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')


#%%
    current_tweet = soup.find_all('div', class_='js-tweet-text-container')


#%%
for tweet in current_tweet: 
    mars_weather_tweet= tweet.find('p').text
    if 'sol' and 'pressure' in mars_weather_tweet: 
        print(mars_weather_tweet)
        print('-------------')

#%% [markdown]
# # Mars Facts

#%%
    mars_facts_url= 'https://space-facts.com/mars/'
    browser.visit(mars_facts_url)
    time.sleep(1)
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')


#%%
    mars_facts_second_table = pd.read_html(mars_facts_url)[1]
    mars_facts_second_table = mars_facts_second_table.rename(index=str, columns = {0: "Description", 1: "Value"})
    mars_facts_second_tablehtml = mars_facts_second_table.to_html(index= 'False')

#%% [markdown]
# # Mars Hemispheres

#%%
    mars_hemispheres_url= 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
    browser.visit(mars_hemispheres_url)
    time.sleep(1)
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')


#%%
#gather all of the links 
    parent_url = 'https://astrogeology.usgs.gov/'
    hemisphere_image_title = []
    hem_name = soup.find_all('h3')

for link in hem_name:
    hemisphere_image_title.append(link.text)




#%%
    hemisphere_image_url = []

for hem in hemisphere_image_title: 
    hem_dict = {
        'title': [],
        'img_url': []
    }
    
    #find your image
    browser.click_link_by_partial_text(hem)
    
    url = browser.find_by_text('Sample')['href']
    
    hem_dict['img_url']= url
    
    hem_dict['title'] = hem 
    
    hemisphere_image_url.append(hem_dict)
    
    browser.visit(mars_hemispheres_url)
    
    


#%%
    mars = { 
        "featured_image": image_url, 
        "mars_weather": mars_weather_tweet,
        "mars_facts": mars_facts_second_tablehtml, 
        "mars_hemispheres": mars_hemispheres_url
        }


    return mars 

#%% [markdown]
# # Establish MongoDB Connection

#%%
# Initialize PyMongo to work with MongoDBs



#%%
# Define database and collection


#%%



#%%


#%%
# Insert dictionary into MongoDB as a document



#%%



#%%



