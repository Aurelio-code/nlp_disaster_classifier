import pandas as pd
import sys
from src.util.utils import load_data

def main():
  train, test = load_data()
  
  print(train.head())

if __name__ == '__main__':
  for path in sys.path:
    print(path)

  main()
