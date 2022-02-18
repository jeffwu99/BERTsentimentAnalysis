import nltk
from nltk.corpus import stopwords
nltk.download('stopwords')
from nltk.tokenize import word_tokenize
nltk.download('punkt')

stop_words = set(stopwords.words('english'))

FILENAME = "data/reviewTexts.txt"
OUTPUT = "data/reviewTextsWithoutStops.txt"

try:
  f = open(FILENAME, "r")
  w = open(OUTPUT, "w")

  count = 0
  list_of_strings = f.readlines()
  for line in list_of_strings:
    word_tokens = word_tokenize(line)
    without_sw = [word for word in word_tokens if not word in stop_words]
    str = ""
    for element in without_sw:
      str = str + element + " "
    w.write(str + '\n')
except FileNotFoundError:
  print("reviewTexts.txt cannot be found")