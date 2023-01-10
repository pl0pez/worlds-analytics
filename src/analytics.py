import pandas as pd

def load_data(path='./data/worlds-1218.csv'):
    return pd.read_csv(path, sep=',', header=0)

def main():
    data = load_data()
    print(data.head())
    
    


if __name__ == "__main__":
    main()
