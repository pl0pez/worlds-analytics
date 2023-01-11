import pandas as pd
from collections import Counter
import itertools

def load_data(path='./data/worlds-1218.csv'):
    return pd.read_csv(path, sep=',', header=0)

def count_bans(data, bans_columns, top=3):
    aux_list = []
    for column in bans_columns: 
        aux_list.append(data[column].values.tolist())
    
    aux_list = list(itertools.chain.from_iterable(aux_list)) #joining the list of lists into unique list!

    return list(sorted(Counter(aux_list).items(),reverse=True, key=lambda x:x[1]))[0:top]

def main():
    data = load_data()
    print(data.head())
    
    # Columns info
    print(data.columns)
    
    #Times blue team wins vs times red team wins
    bv = len(data[data['Winner']==1])
    rv = len(data[data['Winner']==2])
    
    print("Percentage blue victories: {}".format(bv/len(data)))
    print("Percentage red victories: {}".format(rv/len(data)))
    
    
    bans_columns= ['BB1',  'BB2', 'BB3', 'BB4', 'BB5', 'RB1', 'RB2', 'RB3', 'RB4', 'RB5']
    blue_bans = ['BB1',  'BB2', 'BB3', 'BB4', 'BB5']
    red_bans = ['RB1', 'RB2', 'RB3', 'RB4', 'RB5']
    
    # Three most banned champions in general
    print(count_bans(data, bans_columns))
    
    # Three most banned champions by blue side
    print(count_bans(data, blue_bans))
    
    # Three most banned champions by red side
    print(count_bans(data, red_bans))
    
    # Three most picked champions in general
    
    # Three most picked champions by blue side
    
    # Three most picked champions by red side

if __name__ == "__main__":
    main()
