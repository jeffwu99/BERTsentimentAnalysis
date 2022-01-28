# import pandas as pd


# with open('amazonReviewData/Home_and_Kitchen_5.json', encoding='utf-8') as inputfile:
#     df = pd.read_json(inputfile, lines=True)

# df.to_csv('rawReviews.csv', encoding='utf-8', index=True)

import re
import json


#for max, each rating will have 24313 reviews

MAX = 24313

new = open("amazonReviewData/data.json", "w")
count_one = 0
count_two = 0
count_three = 0
count_four = 0
count_five = 0
with open('amazonReviewData/Home_and_kitchen_5 - Copy.json', 'r') as data_file:
  for obj in data_file:
    reviewStart = obj.find("\"reviewText") + 14
    reviewEnd = obj.find("\"overall\"") - 2
    str = obj[reviewStart:reviewEnd]
    cleanstr = re.sub('[^A-Za-z ]+','', str)
    
    ratingStart = reviewEnd
    ratingEnd = ratingStart + 3 + 13
    rat = obj[ratingStart:ratingEnd]
    if rat[13] == "1":
      count_one += 1
      if count_one > MAX:
        continue
    elif rat[13] == "2":
      count_two += 1
      if count_two > MAX:
        continue
    elif rat[13] == "3":
      count_three += 1
      if count_three > MAX:
        continue
    elif rat[13] == "4":
      count_four += 1
      if count_four > MAX:
        continue
    elif rat[13] == "5":
      count_five += 1
      if count_five > MAX:
        continue

    new.write( "{\"reviewText\":" + "\"" + cleanstr + "\"" + rat + "}" + '\n')


print("One stars: ", count_one)
print("two stars: ", count_two)
print("three stars: ", count_three)
print("four stars: ", count_four)
print("five stars: ", count_five)





    


