# -*- coding: utf-8 -*-	


import codecs
import os
import csv
# 读取文件~~~~~~~~
def word_split(words):#分割使用 -
	new_list=[]
	for word in words:
		if '-' not in word:
			new_list.append(word)
		else:
			lst=word.split('-')
			new_list.extend(lst)
	return new_list

def read_file(file_path):#读取单文件的单词
	f=codecs.open(file_path,'r',"utf-8")
	lines=f.readlines()
	word_list=[]
	for line in lines:
		line=line.strip()
		words=line.split(' ')
		words=word_split(words)
		word_list.extend(words)		
	return word_list
def read_files(file_paths):#读取多文件里的单词
	final_words=[]
	for path in file_paths:
		final_words.extend(read_file(path))
	return final_words
def get_file_from_folder(folder_path):#读取文件夹里的所有单词
	file_paths=[]
	for root,dirs,files in os.walk(folder_path):
		for file in files:
			file_path=os.path.join(root,file)
			file_paths.append(file_path)
	return file_path
# 清洗文本~~~~~~~~取得格式化的单词	
def format_word(word):
	fmt='abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ-'
	for char in word:
		if char not in fmt:
			word=word.replace(char,' ')
	return word.lower()
def format_words(words):
	word_list=[]
	for word in words:
		wd=format_word(word)
		if wd:
			word_list.append(wd)
	return word_list
#统计单词数目~~~~~~~~~
def statictcs_words(words):
	s_word_dict={}
	for word in words:
		if s_word_dict.has_key(word):
			s_word_dict[word]=s_word_dict[word]+1
		else:
			s_word_dict[word]=1
	return s_word_dict
#输出成csv
'''def createListCSV(vocaulay_map,to_file_path):
	nfile=open(to_file_path,'w+')
    with open(fileName, "wb") as csvFile:
        csvWriter = csv.writer(csvFile)
        for data in dataList:
            csvWriter.writerow(data)
        csvFile.close
	sorted(word_dict.items(),key=lambda item:item[1],reverse=0)'''

def print_to_csv(vocaulay_map,to_file_path):
	nfile=open(to_file_path,'w+')

	for key in vocaulay_map.keys():
		values=vocaulay_map[key]
		nfile.write("%s,%s\n"%(key,values))
	nfile.close()


def main():
	words=read_file(get_file_from_folder('data2'))#未经格式化的单词
	print'未经格式化的单词%d个'%(len(words))
	f_words=format_words(words)#已经格式化的单词
	print'已经格式化的单词%d个'%(len(f_words))
	word_dict=statictcs_words(f_words)
	sorted(word_dict.items(),key=lambda word_dict:word_dict[1],reverse=1)#这句对排序然并卵，不知道怎么改。
	print_to_csv(word_dict,'output/test.csv') 

if __name__ == '__main__':
	main()