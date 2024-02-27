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
#TODO: Expand on data scraped, and organize it prior to sending off to flask for rendering



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

#*Function : matchup_div()
#@param : versus is list of html elements with Tag.a related to "dates" games
def versus_data(versus):
    #versus is list of Tag.a objects we pull href out first
    team_vs_string = []

    for a_items in versus:
        vs_text = a_items.get('href') #grabs string x vs y 
        p_items = a_items.find_all('p')
        time_text = ""
        for text in p_items:
            if 'GameCardMatchupStatusText' in text.get('class')[0]:
               time_text = text.string
               break
        team_vs_string.append((vs_text, time_text))
    
    return team_vs_string
def ui_processing(teams):
    #teams list  of data pairs ( teams , times)
    #string format : '/game/XXX-vs-YYY-randomdata'
    #time string can be kept as is
    #can probably "hardcode" specific text string location anchors  // use ReGex down the line if things change
    finalized = []
    for data in teams:
        lineup, times = data
        #find vs go forward and back 1 to eliminate '-' get 3 letters of text
        vs = lineup.rfind('vs')
        teamOne = lineup[vs-4:vs-1]
        teamTwo = lineup[vs+3:vs+6]
        finalized.append([teamOne, teamTwo, times])
    return finalized
def data_scrape():
    url = "https://www.nba.com/games" 
    selenium_soup = sel_soup(url)
    versus = matchup_extraction(selenium_soup)
    line_up = versus_data(versus)
    temp_text = ui_processing(line_up)
    return temp_text
    #_div = matchup_div(BeautifulSoup(urllib.request.urlopen(baseURL+path_nba_games_today), 'lxml'))
    #tmp = nbaSoup.find_all('data-text')
    #print(tmp)
"""
open nba ->  hard code "/games" but we can also check for tags where data-text is "SEE ALL GAMES" to confirm path


"""
if __name__ == "__main__":
    data_scrape()
