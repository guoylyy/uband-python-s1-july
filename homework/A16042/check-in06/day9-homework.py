#!/usr/bin/python
# -*- coding: utf-8 -*-
# @author: xxx

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
def homework1():
	dictionary = {'good':'of a favourable character on tendenc','none':'not any such thing or person','nice':'very beautiful'}
	#长度
	print len(dictionary)
  	#获得keys列表
  	print dictionary.keys()
  	#获得values列表
  	print dictionary.values()
  	#有
  	print dictionary.has_key('good')
  	#没有
  	print dictionary.has_key('bad')
  	#add
  	dictionary ['bad'] = 'not very good'
  	print dictionary
  	#modify
  	dictionary ['bad'] = 'failing to reach an acceptable standard'
  	print dictionary
  	#delete
  	del dictionary ['bad']
  	print dictionary
  	#get value
  	print dictionary ['good']
  	if dictionary.has_key('bad'):
  		print dictionary ['bad']
  	else:
  		print '没有这个单词'
  	#iterator
  	for keys in dictionary.keys():
  		print keys
  		print dictionary[keys]
def homework2(): 
	print '老爸正在看一本英语书,他旁边有一本字典,但是只有三个单词的解释'
	dictionary = {'abandon':'to give up to the control or influence of another person or agent','abase':'to lower in rank, office, prestige, or esteem','abash':'to destroy the self-possession or self-confidence of'}
	if dictionary.has_key('etiquette'):
		print dictionary['etiquette']
	else:
		print '老爸先查了一个单词"etiquette",没有查到'
		del dictionary ['abandon']
		print '老爸怒了，把"abandon"这一页撕掉了'
	if dictionary.has_key('abase'):
		print '老爸又查了一个单词"abase",得到了解释'
		print dictionary['abase']
		dictionary ['abandon'] = 'to give up to the control or influence of another person or agent'
		print '老爸很开心,又把"abandon"加到了字典里'



if __name__ == '__main__':
  homework2()