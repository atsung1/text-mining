from imdbpie import Imdb
from nltk.sentiment.vader import SentimentIntensityAnalyzer

#code from professor
imdb = Imdb()
print(imdb.search_for_title("Frozen")[0])
reviews = imdb.get_title_user_reviews("tt2294629")

# import pprint
# pprint.pprint(reviews)

'''The following is the 1st review'''
# #check
# print(reviews['reviews'][0]['author']['displayName'])
# print(reviews['reviews'][0]['reviewText'])

a = imdb.search_for_title("Frozen")[0]['title']
b = reviews['reviews'][0]['author']['displayName']
c = reviews['reviews'][0]['reviewText']
sentence = str(c)
score = SentimentIntensityAnalyzer().polarity_scores(sentence)
# print(score)

d = 'Movie Title:' + str(a) + '\n' + 'Username:' + str(b) + '\n' + 'Review:' + str(c) + '\n\n\n' + 'Natural Language Processing:' + '\n' + str(score)

'''Saving the file for the 1st review'''
file = open('movie_text1', 'w')
file.write(d)
file.close()

'''The following is the 2nd review'''
reviews2 = imdb.get_title_user_reviews("tt2294629")
w = imdb.search_for_title("Frozen")[0]['title']
x = reviews2['reviews'][1]['author']['displayName']
y = reviews2['reviews'][1]['reviewText']
sentence2 = str(y)
score2 = SentimentIntensityAnalyzer().polarity_scores(sentence2)
# print(score)

z = 'Movie Title:' + str(w) + '\n' + 'Username:' + str(x) + '\n' + 'Review:' + str(y) + '\n\n\n' + 'Natural Language Processing:' + '\n' + str(score2)

'''Saving the file for the 2nd review'''
file = open('movie_text2', 'w')
file.write(z)
file.close()
