#this scraper works with an array with the headlines or can use a txt file to work on the data

# imports
from bs4 import BeautifulSoup
import requests                         # for connection
import re                               # for reading the data
from collections import Counter         # for counting words

# this function returns a soup page object
def getPage(url):
    r = requests.get(url)
    data = r.text
    spobj = BeautifulSoup(data, 'html.parser')
    return spobj

# scraper website: heise
def main():

    webpage = "https://www.heise.de/thema/https"   # get website with topic from heise
    file = open('parsedTitles.txt', 'wb')          # file we will save the data
    results = open('results.txt', 'wb')          # file we will save the results

    #get content from website
    content = getPage(webpage).find('div', {'class' : 'keywordliste'})
    i = 0
    array = []
    for title in content.find_all('header'):
        # print title.text
        word = title.text
        array.extend([word])
        file.write( title.text.encode('utf8') + '\n' )
        results.write(str(i) + '. Headline: ' + title.text.encode('utf8') + '\n' )
        i += 1
    file.flush()
    file.close()

    # Read words from txt file
    # with open('parsedTitles.txt') as f:
    #     passage = f.read()
    # words = re.findall(r'\w+', passage.decode('utf8'), re.UNICODE)

    # change array to string for re to find words in string
    arrayToString = ''.join(array)
    # get all words from String
    words = re.findall(r'\w+', arrayToString, re.UNICODE)
    # capitalize words and count them
    cap_words = [word.upper() for word in words]
    word_counts = Counter(cap_words)
    # terminal output and most_common Count from collections
    results.write('Most common words:\n')
    print 'Most common:\n'
    for word, count in word_counts.most_common(3):
    	results.write('%s: \t%7d' % (word, count) + '\n')
        print '%s: \t%7d' % (word, count)

    results.flush()
    results.close()

    print("\nDONE !\n\n\nheise is scraped.\n")

# main program

if __name__ == '__main__':
    main()
