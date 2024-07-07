from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup

# Replace with your desired path to Chrome webdriver
driver_path = "https://developer.chrome.com/docs/chromedriver/downloads#chromedriver_1110556341"

# Open Chrome webdriver
driver = webdriver.Chrome(executable_path=driver_path)

# Visit Yahoo Finance homepage
driver.get("https://finance.yahoo.com/")

# Wait for page to load (adjust wait time as needed)
driver.implicitly_wait(10)

# Get the HTML content
html_content = driver.page_source

# Close the browser window
driver.quit()

# Parse the HTML content
soup = BeautifulSoup(html_content, "html.parser")

# Find all news headlines
news_headlines = soup.find_all("h3", class_="headline")

# Extract and store headlines
scraped_news = []
for headline in news_headlines:
  scraped_news.append(headline.text.strip())

# Print scraped headlines
print("Scraped US Stock Market News Headlines:")
for headline in scraped_news:
  print(headline)
