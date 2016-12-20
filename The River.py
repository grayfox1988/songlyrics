"""
    'Counting with Bruce Springsteen' is a program that takes the whole corpus
    of the Boss's work, cleans and filters the text, and creates an analysis
    based on the text to gather insights into themes in Springsteen's work.
    
"""

from urllib.request import urlopen
import bs4
import nltk
import pandas as pd
import re

#Getting and cleaning the song list
url = urlopen('http://www.azlyrics.com/s/springsteen.html').read()

text = bs4.BeautifulSoup(url, 'lxml')

song_list = text.find_all('a', {'target' : '_blank'})

songs = []
for song in song_list:
    songs.append(song.get_text())

boss_song_list = pd.Series(songs)
boss_song_list = boss_song_list[1:]

#Now creating a loop that appends a list (or something) to collect all the lyrics
for boss in boss_song_list:
    url_songs = 'http://www.azlyrics.com/lyrics/brucespringsteen/' + boss + '.html'
    html = urlopen(url_songs).read()
    