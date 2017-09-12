#!/usr/bin/python
# -*- coding: utf-8 -*-
# @author: 冰糖葫芦

#作业1:对照 day9 sample-code 打一遍代码
#
#作业2: （选做）模拟下面的过程，用今天学到的知识
#【场景模拟】
#
# 老爸在看一本英文书，他旁边有一个词典，但是只有三个词的解释
# abandon “to give up to the control or influence of another person or agent”
# abase  “to lower in rank, office, prestige, or esteem ”
# abash  “to destroy the self-possession or self-confidence of ”
# 
# 老爸先查了一个单词 'etiquette' 没有查到
# 老爸怒了，把含有 'abandon' 一页的单词撕掉了
# 然后老爸又差了一个单词 'abase' 得到了解释
# 老爸很开心，有把 'abandon' 加入到了字典里
# 
def dictionary():
	dictionary = {'abandon': 'to give up to the control or influence of another person or agent',
				  'abase':  'to lower in rank, office, prestige, or esteem',
				  'abash': 'to destroy the self-possession or self-confidence of'
				}
	return dictionary

def homework1(dictionary):
	#获取长度
	len_dic = len(dictionary)
	print len_dic
	#获取key
	keys = dictionary.keys()
	print keys
	#获取value
	values = dictionary.values()
	print values
	#存在与否判断
	print dictionary.has_key('etiquette')
	print dictionary.has_key('abandon')
	#删除
	del dictionary['abandon']
	#添加
	dictionary['abandon'] = 'to give up to the control or influence of another person'
	print dictionary
	#修改
	dictionary['abandon'] = 'to give up to the control or influence of another person or agent'
	#遍历
	for key in keys:
		print '%-13s' %(key),dictionary[key]

def homework2(dictionary,tmp = {}):
	print '------------daddy is consulting the dictionary----------------'
	print '-----dictionary'
	keys = dictionary.keys()
	for key in keys:
		print '%-13s' %(key),dictionary[key]
	word1 = 'etiquette'
	word2 = 'abase'
	word_d = 'abandon'
	print ''
	print 'daddy wants to look %s up in dictionary' %(word1)
	is_exist_1= dictionary.has_key(word1)
	if is_exist_1:
		print word1,dictionary[word1]
	else:
		print "However %s doesnt exist in the dictionary" %(word1)
		#tmp.update({word_d:dictionary[word_d]})
		tmp[word_d] = dictionary[word_d]
		del dictionary[word_d] 
		print "daddy was angry, so he tore off the %s page" %(word_d)
	print '-----dictionary'
	keys = dictionary.keys()
	for key in keys:
		print '%-13s' %(key),dictionary[key]
	print ''
	print 'daddy wants to look %s up in dictionary' %(word2)	
	is_exist_2 = dictionary.has_key(word2)
	if is_exist_2:
		print '%s:' %(word2),dictionary[word2]
		dictionary[word_d] = tmp[word_d]
		print '' 
		print "daddy is glad to look %s up in the dictionary,and then paste \
the %s page to the dictionary" %(word2,word_d)
	print '-----dictionary'
	keys = dictionary.keys()
	for key in keys:
		print '%-13s' %(key),dictionary[key]

if __name__ == '__main__':
  dic1 = dictionary()
  homework1(dic1)
  homework2(dic1)