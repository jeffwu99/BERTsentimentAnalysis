import csv

START = 50000
MAX = 60000
low_count = 0
high_count = 0
writeFile = open("tweetData/data_middle.csv", "w")
writeFile.write("Tweet,sentiment")

with open("tweetData/dataFULL.csv") as inFile:
  reader = csv.reader(inFile, delimiter=',')
  for row in reader:
    if (row[1] == "0"):
      low_count += 1
      if (low_count <= START or low_count >= MAX):
        continue
      else:
        writeFile.write('\n' + "\"" + row[0] + "\"" + ',' +  row[1])
    if (row[1] == "4"):
      high_count += 1
      if (high_count <= START or high_count >= MAX):
        continue
      else:
        writeFile.write('\n' + "\"" + row[0] + "\"" + ',' +  row[1])

print("Number of Low sentiment tweets is: " + str(low_count))
print("Number of high sentiment tweets is: " + str(high_count))

writeFile.close()