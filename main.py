from db_mgmt import DataBaseConnection
import webScraper

# Submit the URL for web scrape and parsing
    webScrape = webScraper.webScrapeTheCurrent()

    # Call method that cleans the web scrape and packs it in a list of dictionaries
    song_dictionaries = webScrape.musicHTMLParser()

    # Instantiate DB connection
    db_connect = DataBaseConnection()

    # Pass dictionary to unpack and load into DB
    db_connect.insertDB(song_dictionaries)

    # Create cursor object from DB instantiation
    # Verify DB connection
