import re
from robobrowser import RoboBrowser

browser = RoboBrowser(history=True, parser='html5lib')

# Mettre son user-agent ici !
browser.session.headers['User-Agent'] = 'xxxxxxxx'

browser.open("https://en.wikipedia.org/wiki/Main_Page")

form = browser.get_form(id="searchform")

form["search"].value = "TCP-IP"
# browser.submit_form(form) -> stack trace
browser.submit_form(form, submit=form.submit_fields['go'])

print(browser.parsed.get_text()) # puis ajouter à un dictionnaire..
