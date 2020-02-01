import pandas as pd 
import os

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

  print(train.head())

  return train, test

def main():
  load_data()

if __name__ == '__main__':
  main()