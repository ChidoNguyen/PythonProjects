import urllib
from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

#!! All URL strings end with / but do not start with / in order to make appending for paths easier !!#
"""
Quick script to pull today's NBA matchups 
"""



''' 
#*Function : nba_game_path
#*param  : BeautifulSoup object
#*Purpose : create our BeautifulSoup object and find /games path
'''
def make_nba_soup(url):
    try:
        with urlopen(url) as nba:
            soup = BeautifulSoup(nba, 'lxml')
    except urllib.error.URLError as e:
        print(e)
    except urllib.error.HTTPError as e:
        print(e)
    return soup

#*Function : nba_game_path
#@param  : BeautifulSoup object , gPath (i.e /games/)
def nba_game_path(soup, gPath):
    tag_text = "SEE ALL GAMES"
    tag_label = 'a'
    # !! 2/21/204 data-id tag for scoreboard link is data-id="nba:game-tracker:link"
    for items in soup.find_all(tag_label):
        if items.get('data-id') == "nba:game-tracker:link":
            return items.get('href')
    return ""


#*Function : matchup_div()
#@param : 
def matchup_div(soup):
    try:
        divs = soup.find_all('div')
    except  urllib.error.URLError as e:
        print(e)
    for items in divs:
        #from our divs find extract all the div's classes and find if "Games" word is in the class descriptions
        #GamesView ________gameCard#
        if 'class' in items.attrs and len(items.attrs['class']) > 0 and items.attrs['class'][0].find('Games') >= 0 :
            if re.search('^(.*gameCard.*)$',items.attrs['class'][0]): print(items.name)

    
    

def main():
    baseURL = "https://www.nba.com/"
    path_nba_games_today = "games/"
    nbaSoup = make_nba_soup(baseURL)
    score_board = nba_game_path(nbaSoup , path_nba_games_today) # returns /path 
    _div = matchup_div(BeautifulSoup(urllib.request.urlopen(baseURL+path_nba_games_today), 'lxml'))
    #tmp = nbaSoup.find_all('data-text')
    #print(tmp)
"""
open nba ->  hard code "/games" but we can also check for tags where data-text is "SEE ALL GAMES" to confirm path


"""
if __name__ == "__main__":
    main()
