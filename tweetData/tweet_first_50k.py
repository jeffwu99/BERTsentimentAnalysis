#puts only the first 50,000 positive and negative tweets in a csv file

import csv

MAX = 50000
low_count = 0
high_count = 0
writeFile = open("tweetData/dataINITIAL.csv", "w")
writeFile.write("Tweet,sentiment")

with open("tweetData/dataFULL.csv") as inFile:
  reader = csv.reader(inFile, delimiter=',')
  for row in reader:
    if (row[1] == "0"):
      low_count += 1
      if (low_count >= MAX):
        continue
      else:
        writeFile.write('\n' + "\"" + row[0] + "\"" + ',' +  row[1])
    if (row[1] == "4"):
      high_count += 1
      if (high_count >= MAX):
        continue
      else:
        writeFile.write('\n' + "\"" + row[0] + "\"" + ',' +  row[1])

print("Number of Low sentiment tweets is: " + str(low_count))
print("Number of high sentiment tweets is: " + str(high_count))

writeFile.close()