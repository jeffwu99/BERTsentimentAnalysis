from gensim.parsing.preprocessing import remove_stopwords

FILENAME = "data/dataFinal.json"
OUTPUT = "data/reviewTextsWithoutStops.json"

try:
  f = open(FILENAME, "r")
  w = open(OUTPUT, "w")

  list_of_strings = f.readlines()
  for line in list_of_strings:
    str = remove_stopwords(line)
    w.write(str + '\n')
except FileNotFoundError:
  print("reviewTexts.txt cannot be found")