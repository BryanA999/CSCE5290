import urllib.request
from bs4 import BeautifulSoup
import nltk
from nltk.corpus import stopwords
nltk.download('stopwords')

#read article at url
response = urllib.request.urlopen('https://www.newscientist.com/article/2275587-astronauts-ride-reused-spacex-capsule-and-rocket-for-the-first-time/')
html = response.read()

#tokenize
soup = BeautifulSoup(html,"html.parser")
text = soup.get_text(strip=True)
tokens = [t for t in text.split()]

#clean tokens of stopwords
freq = nltk.FreqDist(tokens)
clean_tokens = tokens[:]
sr = stopwords.words('english')
for token in tokens:
    if token in stopwords.words('english'):
        clean_tokens.remove(token)
    elif tokens.count(token) < 5: # ignore tokens that appear less than 5 times
        clean_tokens.remove(token)

#Plot frequency distribution
freq = nltk.FreqDist(clean_tokens)
freq.plot(10, cumulative = False)

#Create different visualization
import matplotlib.pyplot as plt

# create values for bar chart
x = range(1, len(freq.items()) + 1)
labels = [tup[0] for tup in freq.items()]
y = [tup[1] for tup in freq.items()]

# plot and rotate ticks,
plt.bar(x, y, tick_label=labels)
plt.xticks(rotation=45)
