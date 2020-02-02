import pandas as pd
import sys
import spacy

from src.util.utils import load_data, clean_document

def lematize(document):
  '''
    Lematizes the document (tweet)
    Args:
      document : doc
        document object from the spacy library
    Returns:
      tokens : list<doc>
        list of lematized tokens
  '''
  tokens = []
  for token in document:
    # append only if the token is not a stop word
    if not token.is_stop:
      if token.lemma_ != '-PRON-':
        tokens.append(token.lemma_) # if the lemma is not a pronoun then append
      else:
        tokens.append(token)

  return tokens
   
def spacy_tokenization(corpus):
  '''
    tokenizes a corpus using spacy, cleans text, lematizes
    and removes stop words

    Args:
      corpus : list
        list of the different documents to tokenize
    Returns:
      tokenized_corpus : list
        list of tokenized and clean documents
  '''
  nlp = spacy.load('en_core_web_sm', disable=['parser', 'ner']) # for now disable parser and named entity recog
  en_stop_words = list(spacy.lang.en.stop_words.STOP_WORDS) # define english stop words
  
  corpus = [clean_document(document) for document in corpus] # clean the corpus
  # corpus = [nlp(document) for document in corpus] # call spacy
  # corpus = [lematize(document) for document in corpus] # lemmatize 
  
  # ---- test funcs
  corpus_generator = (nlp(document) for document in corpus) # define generator
  g5 = [next(corpus_generator) for _ in range(5)] # just 2 first tweets from the generator
  tokenized_corpus = [lematize(doc) for doc in g5]
  
  
  return tokenized_corpus

def main():
  train, test = load_data()
  
  train_corpus = [_ for _ in train['text']] # convert pandas column into a list
  tknzd_corpus = spacy_tokenization(train_corpus)
  

if __name__ == '__main__':
  for path in sys.path:
    print(path)

  main()
