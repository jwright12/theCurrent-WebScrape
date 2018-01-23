import psycopg2
from pprint import pprint


class DataBaseConnection:

    def __init__(self):
        try:
            self.connection = psycopg2.connect(
                "dbname=test user=joe")
            self.connection.autocommit = True
            self.cursor = self.connection.cursor()
        except:
            pprint("Failed to connect to database")
# Add the scraped data to the database

    def insertDB(self, list):
        """Insert todays songs into database"""
        # List to unpack
        self.mySongs = list
        # get cursor object from database constructor
        cur = self.cursor
        # iterate through list of song dictionaries
        for song in self.mySongs:
            day = song['Day']
            time = song['Time']
            song_title = song['Song']
            artist = song['Artist']
            album = song['Album']
            # Write variables to a row in our database
            SQL = "INSERT INTO thecurrent (day, hour, song, artist,\
             album) VALUES (%s, %s, %s, %s, %s);"
            values = (day, time, song_title, artist, album)
            cur.execute(SQL, values)
