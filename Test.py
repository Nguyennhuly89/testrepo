import pandas as pd
import numpy as np

path = 'D:\DSP301\ASM\Data Files'
file = input('Enter a class file to grade (i.e. class1 for class1.txt):')
df = pd.read_csv(path + '\\' + file + '.txt', sep=',', header=None)



