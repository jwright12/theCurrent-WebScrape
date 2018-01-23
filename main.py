from database_manager import DataBaseConnection
import scraper

URL = 'https://www.thecurrent.org/playlist'
# Scrape todays playlist by running at 11:59pm at URL below
webScrape = scraper.webScrapeTheCurrent(URL)

# Call method that cleans the web scrape and packs it in a list of dictionaries
song_dictionaries = webScrape.musicHTMLParser()

# Instantiate DB connection
db_connect = DataBaseConnection()

# Pass dictionary to unpack and load into DB
db_connect.insertDB(song_dictionaries)
