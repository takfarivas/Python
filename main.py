# importing stuff for web scraping
import pandas as pd
import requests
from bs4 import BeautifulSoup

# requesting to the page
page = requests.get(
    'https://forecast.weather.gov/MapClick.php?lat=41.8843&lon=-87.6324#.YFCEzrRKhQI'
)
soup = BeautifulSoup(page.content, 'html.parser')
week = soup.find(id='seven-day-forecast-body')

# searching into items in the div
items = week.find_all(class_='tombstone-container')

# searching for items in items
period = [item.find(class_='period-name').get_text() for item in items]
small_desc = [item.find(class_='short-desc').get_text() for item in items]
temp = [item.find(class_='temp').get_text() for item in items]

# transforming into a DataFrame (with pandas)
weather = pd.DataFrame({
    'Period': period,
    'Little description': small_desc,
    'Temperature': temp,
})

# printing the weather
print(weather)

# transforming the DataFrame into csv file
weather.to_csv('result.csv')
