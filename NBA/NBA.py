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
def matchup_extraction(soup):
    ''' find all sections with 'GameCard_gcMain' in their class string
        sections.children has a-tag html element we can extract matchups and time for later
    '''
    sects = soup.find_all('section')
    gamecard_sects = []
    for items in sects:
        if 'GameCard_gcMain' in items.get('class')[0]: 
            gamecard_sects.append(items)
    teams = []
    for i in gamecard_sects:
        a_kids = list(i.children) # tag a and tag ul 
        teams.append(a_kids[0])
    return teams

    
#*Might needt selenium header to fully load webpage prior to souping it
def sel_soup(url):  
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

def versus_data(versus):
    #versus is list of Tag.a objects we pull href out first
    team_vs_string = []

    for a_items in versus:
        a_items.get('href') #grabs string x vs y 
        p_items = a_items.find_all('p')
        for text in p_items:
            if 'GameCardMatchupStatusText' in text.get('class')[0]:
                print(text.string)
def main():
    url = "https://www.nba.com/games?date=2024-02-23" 
    selenium_soup = sel_soup(url)
    versus = matchup_extraction(selenium_soup)
    line_up = versus_data(versus)
    #_div = matchup_div(BeautifulSoup(urllib.request.urlopen(baseURL+path_nba_games_today), 'lxml'))
    #tmp = nbaSoup.find_all('data-text')
    #print(tmp)
"""
open nba ->  hard code "/games" but we can also check for tags where data-text is "SEE ALL GAMES" to confirm path


"""
if __name__ == "__main__":
    main()
