# Scrape list of YA authors from wikipedia and save to CSV file
# Author list is broken into sections alphabetically
# 
# Key HTML Structure:
# <section class="collapsible-block">
#   <li>
#       <a href="..." title="{Author's Name}">: <i>List of books...</i></a>
#   </li>
# </section>
#
# Note: The "section" with a class="mf-section-26" has list items we don't want 
#       to capture.

import requests
from bs4 import BeautifulSoup
import pandas as pd

url = 'https://en.m.wikipedia.org/wiki/List_of_young_adult_fiction_writers'
output_file = "data/raw/authors.csv"

data = requests.get(url)
soup = BeautifulSoup(data.content, "html.parser")
sections = soup.find_all("section", {"class":"collapsible-block"})

authors = []
author_index = []
index_val = 1

for section in sections:
    if "mf-section-26" not in section["class"]: # don't capture the last block
        author_list = section.find_all("li")
        for author in author_list:
            authors.append(author.find_next("a").get("title"))
            author_index.append(index_val)
            index_val += 1


df = pd.DataFrame(authors, index= author_index, columns=['Name'])

remove_list = [
    '(author)',
    '(writer)',
    '(novelist)',
    '(author, born 1954)',
    '(TV producer)',
    '(Irish author)',
    '(young adult author)',
    '(historian)']

for item in remove_list:
    df['Name'] = df['Name'].str.replace(item, '', regex= False)

df.to_csv(output_file)
