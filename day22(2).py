# Scrape a website and store the data into DB.
import requests
import MySQLdb
from bs4 import BeautifulSoup
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="My_sqlprofile@123"

)

mydb = mysql.connector.connect(
  host="localhost",
 user="root",
  password="My_sqlprofile@123",
  database="New"
)

dbse = mydb.cursor()
url_to_scrape = 'https://news.ycombinator.com/news'
plain_html_text = requests.get(url_to_scrape)
soup = BeautifulSoup(plain_html_text.text, "html.parser")
print(soup.prettify())