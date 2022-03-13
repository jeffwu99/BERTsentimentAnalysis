import csv



writeFile = open("tweetData/dataFULL.csv", 'w')

#writeFile.write("Tweet,sentiment" + "\n")

count = 0
with open("tweetData/training.processed.noemoticon.csv") as inFile: 
  reader = csv.reader(inFile, delimiter=',')
  for row in reader:
    count += 1
    #row[0] is sentiment: 0 for negative, 2 for neutral, 4 for positive
    #row[1] is (?tweet ID?)
    #row[2] is date
    #row[3] "NO_QUERY"``
    #row[4] is user handle
    #row[5] is tweet content

    #removing @tags
    raw_tweet = row[5]
    tag_flag = raw_tweet.find('@') #removing any @ tags to other users
    while(tag_flag != -1):
      end_index_tag = raw_tweet.find(' ', tag_flag)
      if (end_index_tag == -1): #tag was the end of the tweet
        raw_tweet = raw_tweet[:tag_flag]
        tag_flag = -1
      else:
        raw_tweet = raw_tweet[:tag_flag] + raw_tweet[end_index_tag + 1:]
        tag_flag = raw_tweet.find("@")
    link_flag = raw_tweet.find("http") #removing any hyperlinks
    while(link_flag != -1):
      end_index_link = raw_tweet.find(' ', link_flag)
      if (end_index_link == -1): #link was the end of the tweet
        raw_tweet = raw_tweet[:link_flag]
        link_flag = -1
      else:
        raw_tweet = raw_tweet[:link_flag] + raw_tweet[end_index_link + 1:]
        link_flag = raw_tweet.find("http")
    hash_flag = raw_tweet.find("#") #removing hashtags
    while(hash_flag != -1):
      end_index_hash = raw_tweet.find(' ', hash_flag)
      if (end_index_hash == -1): #at end of tweet
        raw_tweet = raw_tweet[:hash_flag]
        hash_flag = -1
      else:
        raw_tweet = raw_tweet[:hash_flag] + raw_tweet[end_index_hash + 1:]
        hash_flag = raw_tweet.find('#')
    writeFile.write("\"" + raw_tweet + "\"" + ',' +  row[0] + '\n')
inFile.close()
writeFile.close()
