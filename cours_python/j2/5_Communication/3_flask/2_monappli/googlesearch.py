import sys
import re
from robobrowser import RoboBrowser

# Voir la documentation de beautifulSoup
# https://www.crummy.com/software/BeautifulSoup/bs4/doc/

def get_google_result(keyword):
    browser = RoboBrowser(history=True, parser='html5lib')
    # Mettre un user-agent ici !
    browser.session.headers['User-Agent'] = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.119 Safari/537.36'
    browser.open("https://google.com")
    form = browser.get_form()
    form['q'] = keyword
    browser.submit_form(form, submit=form.submit_fields['btnK'])
    # On récupère les liens réponse
    html = browser.parsed   # beautifulSoup object
    return [
        {
            'url':link.a['href'],
            'description':link.get_text()
        } for link in html.find_all('h3', attrs={'class':'r'})
    ]

