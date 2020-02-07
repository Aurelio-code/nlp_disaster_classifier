import string
import re
import pandas as pd 
import os

def url_strip(document):
  '''
    removes the urls from the tokens
    Args:
      document : string 
        word(s) document

    Returns:
      document : string
        document without urls
  '''
  url = re.compile(r'https?://\S+|www\.\S+') # reegular expression for an url
  return url.sub('', document)

def remove_html(document):
  '''
    Removes html strings
  '''
  html = re.compile(r'<.*?>')
  
  return html.sub('', document)

def remove_emoji(document):
  emoji_pattern = re.compile("["
                          u"\U0001F600-\U0001F64F"  # emoticons
                          u"\U0001F300-\U0001F5FF"  # symbols & pictographs
                          u"\U0001F680-\U0001F6FF"  # transport & map symbols
                          u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
                          u"\U00002702-\U000027B0"
                          u"\U000024C2-\U0001F251"
                          "]+", flags=re.UNICODE)
  
  return emoji_pattern.sub(r'', document)

def remove_punct(document):
  '''
    Removes puntuation #, @ etc
  '''
  return document.translate(str.maketrans('', '', string.punctuation))

def clean_document(document):
  document = remove_html(url_strip(document)).lower() # remove urls
  document = remove_html(document) # remove htmls
  document = remove_emoji(document) # remove emojis <- this can be handled in spacy directly
  document = remove_punct(document) # remove punctuation
  document = document.strip().rstrip() # remove front and end whitespace
  document = re.sub(' +', ' ',document) # remove multiple whitespace
  return document
  
def load_data():
  '''
    Loads the data located in the (root of theproject)/data folder

    Returns:
      train : pd dataframe 
      test : pd dataframe
  '''
  # walk the data folder
  file_paths = []
  for dirname, _, filenames in os.walk('./data'):
    for filename in filenames:
        name = str(os.path.join(dirname, filename))
        file_paths.append(name)

  train = pd.read_csv(file_paths[1])
  test = pd.read_csv(file_paths[2])

  return train, test

def main():
  load_data()

if __name__ == '__main__':
  main()