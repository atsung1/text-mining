#Assignment2:
Angela Tsung
MIS 3640

##1. Project Overview
For this assignment, I used IMDB as a data source. I used IMDBpie, a Python IMDB client using the IMDB JSON web service in order to conduct a search for a particular movie title, and then to get a user review. I then used the NLTK package to conduct basic natural language processing, scoring whether the language in the review was positive, negative, or neutral. I wanted to learn how to scrape data from a webpage, how to use packages that are new to me, and how natural language processing works at a very basic level.

##2. Implementation
I first had to choose what data source I wanted to learn to scrape and analyze. I chose to use IMDB as a data source because the IMDBpie package made it much easier for me to learn to scrape data from the website. This package scrapes the data on IMDB movies and reviews into a dictionary format, so thus it’s much easier to find and access information. The package scrapes every single review of a movie and saves it into a dictionary format, thus, in order to switch the review, all we need to do is change the index which we are accessing. For simplicity and for my own understanding, I chose to compare the first and second review, but the index can easily be altered into a for loop in order to repeat the process and use other reviews for comparison.
Among the information on the IMDB website, I chose to compare reviews, as it was the component on the website with the largest block of “natural language” from users, and the structured list of reviews made it easier to access using Python. Lastly, I chose to save the processed information in a text file, as all of the processing was already done within the script I wrote, and it was only the results that I wanted to save.

##3. Results
Through this project, I was able to learn how to scrape data from webpages and use natural language processing to dissect the positivity/negativity of a group of words. After selecting a movie, I scraped the first two reviews, performed natural language processing, and compared the how positive or negative the reviews were. I learned that language can really be interpreted in many different ways, as the results from the natural language processing didn't always match the sentiments of the rating score that the users provided. For instance, both outputs from natural language processing indicated that the reviews contained more positive words than negative, however, once I read the reviews, it seemed that both users wanted to rate the movie as low as possible, and when checked against the real rating the users gave, it was indeed the case.
Here's a sample of the results that were output by my script:
{'neg': 0.076, 'neu': 0.801, 'pos': 0.123, 'compound': 0.9951}
Although the negative words held the least value, the user actually rated 1/10.
I believe this is due to the fact that many of the movie reviewers use language to describe the plot of the movie, which are normally not the same words that are associated with typical positive or negative connotations.


##4. Reflection
From a process point of view, I do not think I scoped the project correctly. I think I had originally intended for the project to be more complex, but later realized that my coding capabilities and understanding of webscraping was limited, and so I simplified the project in order to still accomplish the goal of scraping and processing data. My plan for unit testing was writing script to print out the correct output in terminal in order to test whether my code was working, which correctly phased the steps I had to take for the project into scraping, processing, and saving results.

Since I worked on the project alone, I was not able to delegate tasks to others, however, if i were able to work with a partner, I would have delegated the data scraping to one person, and the data processing to another. In this way, we would be able to work together to find more complex ways of analyzing the data we choose to collect.
