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
import string as sr

#Getting and cleaning the song list
url = urlopen('http://www.azlyrics.com/s/springsteen.html').read()

text = bs4.BeautifulSoup(url, 'lxml')

song_list = text.find_all('a', {'target' : '_blank'})

songs = []
for song in song_list:
    songs.append(song.get_text())

# Making it into a series then change it into a list
boss_song_list = pd.Series(songs)
boss_song_list = boss_song_list[1:]
boss_song_list = boss_song_list.tolist()

#Now creating a loop that appends a list (or something) to collect all the lyrics
i = 0
while i < len(boss_song_list):
    boss = boss_song_list[i].lower().replace(' ', '')
    punct = set(sr.punctuation)
    boss = ''.join(x for x in boss if x not in punct)
    url_songs = 'http://www.azlyrics.com/lyrics/brucespringsteen/' + boss + '.html'
    print(url_songs)
    
    # Now that we have URLs, need to get html and clean text for lyrics
    #html = urlopen(url_songs).read()
    i += 1
    
