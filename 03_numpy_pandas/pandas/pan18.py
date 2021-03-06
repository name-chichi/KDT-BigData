import pandas as pd

x = {'subj': ['math', 'comp', 'phys', 'chem', 'biol'], 'score': [100, 95, 85, 75, 80], 'avg': [95.2, 66.1, 69.5, 86.8, 91.2]}
df1 = pd.DataFrame(x, index=list('abcde'))
df2 = df1.reindex(list('abcdef'))
print('#1', df2, '\n')

df2.to_csv('./df2.csv', sep=',', na_rep='NaN')
df2.to_csv('./df2_ind.csv', sep=',', na_rep='NaN', index=False, header=None)

rdf1 = pd.read_csv('./df2_ind.csv', header=None, names=list('ABC'))
print('#2', rdf1,'\n')

tdf1 = rdf1.T
print('#3', tdf1)