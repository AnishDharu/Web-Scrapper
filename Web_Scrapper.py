#Develop a web scraper that extracts specific data from websites using libraries like BeautifulSoup or Scrapy. 
# This task will improve their knowledge of web scraping techniques and handling HTML/XML data.

import requests
from bs4 import BeautifulSoup

def scrape_titles(url):
    try:
        response = requests.get(url)
        response.raise_for_status()  

        soup = BeautifulSoup(response.text, 'html.parser')

      
        titles = soup.find_all('p')  

        print("\nExtracted Article Titles:")
        for idx, title in enumerate(titles, start=1):
            print(f"{idx}. {title.get_text(strip=True)}")

    except requests.exceptions.RequestException as e:
        print(f"An error occurred while making the request: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")

url = input("Enter the URL of the website to scrape: ")
scrape_titles(url)
