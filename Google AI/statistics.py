import os
import numpy as np
import sys
from collections import Counter
import string
import pandas as pd
import matplotlib.pyplot as plt

translator = str.maketrans('', '', string.punctuation)
text_list = os.listdir("article/")
total_length = len(text_list)
total_list = []
count_list = []
most_list = []
for article in text_list:
	file_name = "article/" + str(article)
	file_read = open(file_name, 'r')
	temp = []
	for line in file_read:
		if line == "\n":
			continue
		line = line.translate(translator)
		temp.append(line.strip("\n").strip('"').split(' '))
	tokens = []
	for i in range(len(temp)):
		tokens += temp[i]
	total_list += tokens
	count = Counter(tokens)
	count_list.append(count)
	most_list.append(count.most_common(50))
	# print(article)
	file_read.close()

total_count = Counter(total_list)
# print(len(total_count))
# print(most_list[0])
total_most = total_count.most_common(50)
# print(total_most)

file1 = open("file1_count.csv", 'w')
file1.write('word,count\n')
for i in range(len(most_list[0])):
	file1.write(str(most_list[0][i][0])+','+str(most_list[0][i][1])+'\n')
file1.close()

plt.rcParams['font.family']='SimHei'
plt.style.use('ggplot')
df1=pd.read_csv("file1_count.csv",encoding="big5")
df1.plot(x = 'word', y = 'count', kind='bar')
plt.show()

file = open("total_count.csv", 'w')
file.write('word,count\n')
for i in range(len(total_most)):
	# print(total_most[i][0])
	file.write(str(total_most[i][0])+','+str(total_most[i][1])+'\n')
file.close()

plt.rcParams['font.family']='SimHei'
plt.style.use('ggplot')
df1=pd.read_csv("total_count.csv",encoding="big5")
df1.plot(x = 'word', y = 'count', kind='bar')
plt.show()