Webscraping using Beautiful Soup 

This is a simple webscraper that makes use of the pandas module in python, requests and Beautiful soup. 
In the code below, I make use of lists, loops and pandas dataframe to save the data I have scraped in a readable .csv table
The code currently picks data from one page in the Jumia website 

# In[ ]:


# import libraries
import pandas as pd
import requests
from bs4 import BeautifulSoup
import time
import datetime

# define the free_delivery function
def free_delivery ():

    # Make a request to the webpage
    url = 'https://www.jumia.co.ke/mlp-free-delivery/?source=STB_FDY_GEN'
    response = requests.get(url)

    # Parse the HTML content using BeautifulSoup
    soup = BeautifulSoup(response.content, 'html.parser')

    # Find the elements containing the data you want to scrape
    product_names = soup.find_all('div', {'class': 'name'})
    prices = soup.find_all('div', {'class': 'prc'})

    # Create a variable and assign it to the datetime module
    today = datetime.date.today()


    # Initialize an empty list to store the scraped data
    data = []

    # Loop through the product_names and prices lists and add the data to the data list
    for i in range(len(product_names)):
        name = product_names[i].get_text().strip()
        price = prices[i].get_text().strip()
        data.append([name, price,today])

    # Create a pandas DataFrame from the data list
    df = pd.DataFrame(data, columns=['Product_name', 'Price', "Date"])

    # Save the DataFrame to a CSV file
    df.to_csv('Jumia_Dataset.csv', index=False)

while (True):
    free_delivery()
    time.sleep(86400)

