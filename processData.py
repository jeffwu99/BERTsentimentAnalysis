import re
import matplotlib.pyplot as plt
import numpy as np

unprocFILENAME = "amazonReviewData/Home_and_Kitchen_5.json"
TEXTFILENAME = "amazonReviewData/reviewTexts.txt"
RATFILENAME = "amazonReviewData/ratings.txt"

f = open(unprocFILENAME, "r")
rev = open(TEXTFILENAME, "w")
rat = open(RATFILENAME, "w")

# dict = {
#   "\!" : None,
#   "\@" : None,
#   "\#" : None,
#   "\$" : None,
#   "\%" : None,
#   "\^" : None,
#   "\&" : None,
#   "\*" : None,
#   "\(" : None,
#   "\)" : None,
#   "\_" : None,
#   "\+" : None,
#   "\-" : None,
#   "\=" : None,
#   "\{" : None,
#   "\}" : None,
#   "\[" : None,
#   "\]" : None,
#   "\\" : None,
#   "\:" : None,
#   "\;" : None,
#   "\'" : None,
#   "\," : None,
#   "\." : None,
#   "\/" : None,
#   "\<" : None,
#   "\>" : None,
#   "\?" : None,
#   "\~" : None,
#   "\`" : None
# }



listOfLines = f.readlines()
for line in listOfLines: 
  #adding 14 since there are 15 chars until actual review
  reviewStart = line.find("reviewText") + 14 
  # 4 chars after review text is the token "overall"
  reviewEnd = line.find("\"overall\"") - 3 
  str = line[reviewStart:reviewEnd]
  # filter out special characters and numbers
  cleanstring = re.sub('[^A-Za-z ]+','', str) 

  #10 chars until rating appears, adding 14 to offset -4 from reviewEnd
  ratingStart = reviewEnd + 14
  ratingEnd = ratingStart + 3 
  rating = line[ratingStart:ratingEnd]
  rev.write(cleanstring + '\n')
  rat.write(rating + '\n')


#todo:  start using keras tokenizer

