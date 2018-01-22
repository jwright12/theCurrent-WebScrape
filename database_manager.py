import pandas as pd
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
from pprint import pprint
import datetime


class webScrapeTheCurrent:

    def __init__(self):
        """Pass the URL to establish connection with the web server and download the HTML for parsing"""

        try:
            self.URL = 'https://www.thecurrent.org/playlist'
            self.connectClient = uReq(self.URL)
            self.readHTML = self.connectClient.read()
            self.closeConnection = self.connectClient.close()
        except:
            pprint("Failed to connect to client address and download HTML")

    def musicHTMLParser(self):
        """Read the object's (blueprint of theCurrent.org's HTML) HTML assigned in the contructor using Beautiful Soup and parse out desired data"""

        html_unparsed = self.readHTML
        page_soup = soup(html_unparsed, "html.parser")

        # Parse out all articles into a list
        song_containers = page_soup.find_all("article", {"class": "row song"})

        # Will need to loop through each article to parse out desired info
        song_container = song_containers[0]

        # Get todays date
        today = pd.Timestamp("today").strftime("%m/%d/%Y")

        # Blank dictionary, which we will fill with parsed data and pass back to main.py
        todays_songs = []

        for song_container in song_containers:

            # extract time stamp - SQL is expecting a time datatype. It will be easier in the future to convert the time stamp to time data type here
            time = song_container.time.text

            # extract album name from img alt text.
            album = song_container.img["alt"]

            # not all songs have an album
            if album == 'default album cover image':
                album = 'N/A'

            # Song & Artist are contained in a nested h5. Create container before parsing them.
            artist_Container = song_container.findAll("h5", {"class": "artist"})
            artist = artist_Container[0].text.strip()

           # song title, nested in h5s
            title_container = song_container.findAll("h5", {"class": "title"})
            h5_text = title_container[0].text.split('\n')
            title = ''.join(h5_text[0])

            song = {'Day': today,
                    'Time': time,
                    'Song': title,
                    'Artist': artist,
                    'Album': album
                    }

            todays_songs.append(song)

        return todays_songs

        # Calculate the time in between timestamps. row.time()-row.time()-1
        # return a data structure that we can read into postgres
