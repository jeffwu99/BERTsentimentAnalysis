import re


raw_filename = input("Raw data file: ")
print("Entered: " + raw_filename)
#raw_filename = "amazonReviewData/Home_and_Kitchen_5.json"
#review_filename = "data/reviewTexts.txt"
#rating_filename = "data/ratings.txt"
outfile = "data/bruhwtf.txt"




try:
  f = open(raw_filename, "r")
  rev = open(outfile, "w")
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
    rev.write(rating + '\n')
except FileNotFoundError:
  print("raw data file name does not exist")
