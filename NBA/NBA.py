import urllib
from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

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
    sects = soup.find_all('section')
    gamecard_sects = []
    #html skeleton
    #sects -> get team abbreviation from href /teama_vs_teamb
    #traverse children to get game time
    for items in sects:
        #print(items.get('class')[0])
        if 'GameCard_gcMain' in items.get('class')[0]: 
            gamecard_sects.append(items)
    
    #children in sect_gc has 2 1) a and 2) ul we can skip the UL and extract the a tag
    teams = []
    for i in gamecard_sects:
        a_kids = list(i.children) # tag a and tag ul 
        teams.append(a_kids[0])
    return
    try:
        divs = soup.find_all('div')
    except  urllib.error.URLError as e:
        print(e)
    tmp = []
    for items in divs:
        if 'class' in items.attrs and items.attrs['class'] : tmp.append(items.get('class'))
    
    return
            
        #from our divs find extract all the div's classes and find if "Games" word is in the class descriptions
        #GamesView ________gameCard#
        #if 'class' in items.attrs and len(items.attrs['class']) > 0 and items.attrs['class'][0].find('Games') >= 0 :
         #   if re.search('^(.*GameCard.*)$',items.attrs['class'][0]): print(items)

    
#*Might needt selenium header to fully load webpage prior to souping it
def sel_soup():
    url = "https://www.nba.com/games"    
    #headless
    chrome_opts = Options()
    chrome_opts.add_argument('--headless')
    chrome_opts.add_argument('executable_path=E:\chromeweb\chromedriver.exe')
    chrome_opts.add_argument('--disable-cache')

    #driver
    driver = webdriver.Chrome(options = chrome_opts)

    #opening website

    driver.get(url)
    driver.refresh()
    WebDriverWait(driver , 10)
    final_html = driver.page_source
    driver.quit()

    soup = BeautifulSoup(final_html, 'lxml')
    return soup

def main():
    baseURL = "https://www.nba.com/"
    path_nba_games_today = "games/"
    nbaSoup = make_nba_soup(baseURL)
    score_board = nba_game_path(nbaSoup , path_nba_games_today) # returns /path 
    _div = matchup_div(sel_soup())
    #_div = matchup_div(BeautifulSoup(urllib.request.urlopen(baseURL+path_nba_games_today), 'lxml'))
    #tmp = nbaSoup.find_all('data-text')
    #print(tmp)
"""
open nba ->  hard code "/games" but we can also check for tags where data-text is "SEE ALL GAMES" to confirm path


"""
if __name__ == "__main__":
    main()
