import glob 
import re
import pandas as pd

# location of data
file_path = './data'

def process_file(file):
    name = re.split('[/_]', file)[2]
    mean, acc, std_dev = {'HIGH':0, 'LOW':0, 'NONWORD':0}, {'HIGH':0, 'LOW':0, 'NONWORD':0}, {'HIGH':0, 'LOW':0, 'NONWORD':0}
    dataframe = pd.read_csv(file, usecols=['response.rt', 'response.corr', 'condition'], dtype = {'condition':str, 'response.rt':float, 'response.corr':float})
    for cond in ['HIGH', 'LOW', 'NONWORD']:
        rows = dataframe.loc[dataframe['condition'] == cond]
        mean[cond] = rows.sum()['response.rt']*1000/len(rows)
        acc[cond] = rows.sum()['response.corr']/len(rows)
        std_dev[cond] = rows['response.rt'].std()*1000
        print(name + " " + cond)
        print('mean = ', mean[cond])
        print('std dev = ', std_dev[cond])
        print('acc = ', acc[cond]) 
    return (name, mean, acc, std_dev)

total_participants = 0
avg_acc, avg_mean, avg_std = {'HIGH':0, 'LOW':0, 'NONWORD':0}, {'HIGH':0, 'LOW':0, 'NONWORD':0}, {'HIGH':0, 'LOW':0, 'NONWORD':0}
for file in glob.glob(file_path+"/*.csv"):
    total_participants += 1
    name, mean, acc, std = process_file(file)
    for cond in ['HIGH', 'LOW', 'NONWORD']:
        avg_acc[cond] += acc[cond]
        avg_mean[cond] += mean[cond]
        avg_std[cond] += std[cond]
for cond in ['HIGH', 'LOW', 'NONWORD']:
    print('average '+cond)
    print('mean = ', avg_mean[cond]/total_participants)
    print('std = ', avg_std[cond]/total_participants)
    print('acc = ', avg_acc[cond]/total_participants)