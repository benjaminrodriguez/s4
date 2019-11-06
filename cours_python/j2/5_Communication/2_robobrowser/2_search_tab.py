# pip3 install robobrowser
# https://github.com/jmcarp/robobrowser

import re
import argparse
from robobrowser import RoboBrowser

def gettab(keyword):
    browser = RoboBrowser(history=True, parser='html5lib')
    browser.open('https://www.tabs4acoustic.com/')

    form = browser.get_form(action=re.compile('recherche'))

    form['FindMe'].value = keyword
    browser.submit_form(form)
    div_resultat = browser.find('div', id='page_content')
    browser.follow_link(div_resultat.find('a'))
    tab = browser.find('div', id='tab_zone')
    return tab.find('pre').text

parser = argparse.ArgumentParser()
parser.add_argument('-k', '--keyword', help='tab you want to find', required=True)
args = parser.parse_args()

print(gettab(args.keyword))

