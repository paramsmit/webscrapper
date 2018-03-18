from bs4 import BeautifulSoup
from flask import render_template
    
def parse_results(html):
    soup = BeautifulSoup(html, 'html.parser')
    soup.prettify()
    found_results = []
    rank = 1
    result_block = soup.find_all('div', attrs={'class': 'g'})
    for result in result_block:
 
        link = result.find('a', href=True)
        title = result.find('h3', attrs={'class': 'r'})
        description = result.find('span', attrs={'class': 'st'})
        if link and title:
            link = link['href']
            title = title.get_text()
            if description:
                description = description.get_text()
            if link != '#':
                found_results.append({ 'rank': rank, 'title': title, 'description': description})
                rank += 1
    return render_template('scrappedlinks.html',found_results=found_results)