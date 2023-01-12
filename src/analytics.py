from collections import Counter
import itertools
import sys
import pandas as pd


# Bans columns
bans_columns= ['BB1',  'BB2', 'BB3', 'BB4', 'BB5', 'RB1', 'RB2', 'RB3', 'RB4', 'RB5']
blue_bans = ['BB1',  'BB2', 'BB3', 'BB4', 'BB5']
red_bans = ['RB1', 'RB2', 'RB3', 'RB4', 'RB5']

# Pick columns
pick_columns = ['BP1', 'BP2', 'BP3', 'BP4', 'BP5', 'RP1', 'RP2', 'RP3', 'RP4', 'RP5']
blue_picks = ['BP1', 'BP2', 'BP3', 'BP4', 'BP5']
red_picks = ['RP1', 'RP2', 'RP3', 'RP4', 'RP5']

def load_data(path='./data/worlds-1218.csv'):
    return pd.read_csv(path, sep=',', header=0)

def count_times(data, columns, top=3):
    aux_list = []
    for column in columns: 
        aux_list.append(data[column].values.tolist())
    
    aux_list = list(itertools.chain.from_iterable(aux_list)) #joining the list of lists into unique list!

    return list(sorted(Counter(aux_list).items(),reverse=True, key=lambda x:x[1]))[0:top]

def team_picks(data, name, side, top=5):
    if side == 'Blue':
        return count_times(data[data['Blue']==name], blue_picks, top)
    if side == 'Red':
        return count_times(data[data['Red']==name], red_picks, top)
    if side == '':
        return count_times(data[(data['Blue']==name) | (data['Red']==name)], pick_columns, top)

def main():
    # if sys.argv: 
    #     data = load_data(sys.argv[0])
    # else: 
    data = load_data()
    
    print(data.head())
    
    # Columns info
    print(data.columns)
    
    #Times blue team wins vs times red team wins
    bv = len(data[data['Winner']==1])
    rv = len(data[data['Winner']==2])
    
    print("Percentage blue victories: {}".format(bv/len(data)))
    print("Percentage red victories: {}".format(rv/len(data)))
    

    
    # Three most banned champions in general
    print(count_times(data, bans_columns))
    
    # Three most banned champions by blue side
    print(count_times(data, blue_bans))
    
    # Three most banned champions by red side
    print(count_times(data, red_bans))
    
    # Three most picked champions in general
    print(count_times(data, pick_columns,5))
    
    # Three most picked champions by blue side
    print(count_times(data, blue_picks,5))
    
    # Three most picked champions by red side
    print(count_times(data, red_picks,5))
    
    # Picks by team
    print(team_picks(data, 'T1', 'Blue', -1))
    print(team_picks(data, 'T1', 'Red', -1))
    print(team_picks(data, 'T1', '', -1))
          
if __name__ == "__main__":
    main()
