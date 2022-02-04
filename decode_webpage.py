"""
program to print article title of a webpage
"""

import BeautifulSoup
import requests

# makes a request to webpage. the URL of the NY Times website we want to parse
url = 'https://www.nytimes.com/'

# the syntax (according to the documentation) for how to
# "load" a webpage through Python
get_url = requests.get(url)
get_html = get_url.text

# how to decode the text of the HTML of the NY Times homepage
# website. r comes from the requests request above
soup = BeautifulSoup(get_html, features="html.parser")
titles = soup.find_all(class_='story-heading')


# find and loop through all elements on the page with the
# class name "story-heading"

print()
for title in titles:
    print(title.text)

'''for heading in soup.find_all(class_='story-heading'):
    if heading.a:
        print(heading.a.text.replace("\n", " ").strip())
    else:
        print(heading.contents[0].strip())'''


