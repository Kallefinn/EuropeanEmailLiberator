import requests
from bs4 import BeautifulSoup as bs
import re

def getEmaillist(country,faction,weirdthing,name):


    URL = 'https://www.europarl.europa.eu/meps/de/full-list/all'

    req = requests.get(URL)
    soup = bs(req.text, 'html.parser')

    members = soup.find_all('a')

    members = [member for member in members if "class" in member.attrs]
    members = [member for member in members if "es_member-list-item-content" in member["class"]]


    if country:
        members = [member for member in members if country in str(member.contents)] 
    if faction:
        members = [member for member in members if faction in str(member.contents)]
    if weirdthing:
        members = [member for member in members if weirdthing in str(member.contents)]
    if name:
        members = [member for member in members if name in str(member.contents)]

    links = [link.attrs['href'] for link in members]

    emaillist = []

    for link in links:

        # function to extract html document from given url
        def getHTMLdocument(url):
        
        # request for HTML document of given url
            response = requests.get(url)
        
        # response will be provided in JSON format
            return response.text

    # create document
        html_document = getHTMLdocument(link)

    # create soap object
        soup = bs(html_document, 'html.parser')

        links_with_text = []

        for link in soup.find_all('a', href=re.compile("aporue")):
            if link.text:
                links_with_text.append(link['href'])
            
        list = " ".join(links_with_text)

        cleaned = list.replace('[dot]','.')
        cleaned2 = cleaned.replace('[at]','@')
        email = cleaned2[::-1]
        emaillist.append(email)
        print(email)
    return emaillist

