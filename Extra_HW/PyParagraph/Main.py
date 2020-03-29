# First we'll import the os module
# This will allow us to create file paths across operating systems
import os

# Module re
import re

#variable declaration
word_count=0
sentence_count = 0
letter_count = 0

choose_para=input("Which paragraph do you want to analyze: paragraph_1.txt or paragraph_2.txt? ")

file_path="raw_data\\"+choose_para.lower()
# Open a file: file
file = open(file_path,mode='r')
 
# read all lines at once
read_file = file.read()

#word count
word_count = len(re.findall(r'\w+', read_file)) 

#sentence count
sentence_count = len(re.findall(r'[!?]+|(?<!\.)\.(?!\.)', read_file)) 

#Approximate letter count (per word)
for i in read_file:
    if(i!=' '):
        letter_count += 1

approx_letter_count=round(letter_count/len(read_file.split()),1)

#Average sentence length (in words)
sentence_length_avg=round(len(read_file.split())/sentence_count,1)

print("Paragraph Analysis")
print("-----------------")
print("Approximate Word Count: "+str(word_count))
print("Approximate Sentence Count: "+str(sentence_count))
print("Average Letter Count: "+str(approx_letter_count))
print("Average Sentence Length: "+str(sentence_length_avg))

file.close()
