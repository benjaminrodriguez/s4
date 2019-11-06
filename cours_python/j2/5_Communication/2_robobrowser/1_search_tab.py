# pip3 install robobrowser
# pip3 install html5lib
# https://github.com/jmcarp/robobrowser
# Doc: https://robobrowser.readthedocs.io/en/latest/readme.html

import re
from robobrowser import RoboBrowser

# Browse
browser = RoboBrowser(history=True, parser='html5lib')
browser.open('https://www.tabs4acoustic.com/')

# On recherche le formulaire de recherche
form = browser.get_form(action=re.compile('recherche'))
form                # <RoboForm q=>

# On spécifie la valeur de formulaire, puis on soumet le formulaire
form['FindMe'].value = 'creep'
browser.submit_form(form)

# Dans la réponse, on extrait la section qui contient un résultat
div_resultat = browser.find('div', id='page_content')

# On clique sur le premier lien retourné
browser.follow_link(div_resultat.find('a'))

# Dans la réponse, on sélectionne la section qui contient le texte à afficher
tab = browser.find('div', id='tab_zone')
print(tab.find('pre').text)

