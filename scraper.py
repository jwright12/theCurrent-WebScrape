from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
from pprint import pprint
import pandas as pd


class webScrapeTheCurrent:

    def __init__(self, URL):
        """Pass the URL to server and download HTML"""

        try:
            self.URL = URL
            self.connectClient = uReq(self.URL)
            self.readHTML = self.connectClient.read()
            self.closeConnection = self.connectClient.close()
        except:
            pprint("Failed to connect and download HTML")

    def musicHTMLParser(self):
        """Read HTML and parse out desired data"""

        html_unparsed = self.readHTML
        page_soup = soup(html_unparsed, "html.parser")

        # Parse out all articles into a list
        song_containers = page_soup.find_all("article", {"class": "row song"})

        # Will need to loop through each article to parse out desired info
        song_container = song_containers[0]

        # Get todays date
        today = pd.Timestamp("today").strftime("%Y/%m/%d")

        # Blank dictionary, fill with parsed data and pass back to main.py
        todays_songs = []

        for song_container in song_containers:

            # extract time stamp
            time = song_container.time.text

            # extract album name from img alt text.
            album = song_container.img["alt"]

            # not all songs have an album
            if album == 'default album cover image':
                album = 'N/A'

            # Song & Artist are contained in a nested h5.
            artistContainer = song_container.findAll("h5", {"class": "artist"})
            artist = artistContainer[0].text.strip()

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

            # attach dictionary to todays_songs
            todays_songs.append(song)

        return todays_songs
