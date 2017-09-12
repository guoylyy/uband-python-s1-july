#!/usr/bin/python
# -*- coding: utf-8 -*-
# @author: 冰糖葫芦

# 今日的作业
# 有十种菜
#   白菜、萝卜、西红柿、甲鱼、龙虾、生姜、白芍、西柚、牛肉、水饺
# 
# 1. 老妈来到了菜市场，从下标 0 开始买菜，遇到偶数的下标就买
#    遇到奇数的下标就不买，买的数量为下标 + 1 斤
#    （请写程序模拟整个过程）
#    （注意单一职责原则）
#    （注意灵活使用 def 函数（代码块））
#  2. 完成后，用今天的学到的列表知识，加 3 个菜
#  3. 完成后，用今天的学到的列表知识，让老妈只逛第 5~9 个菜
def commodity():
	commodity = ['白菜','萝卜','西红柿','甲鱼','龙虾','生姜','白芍','西柚','牛肉','水饺']
  	return commodity

#1.append()  向列表尾部追加一个新元素，列表只占一个索引位，在原有列表上增加，即无返回值，只改变原表
#2.extend() 向列表尾部追加一个列表，将列表中的每个元素都追加进来，在原有列表上增加
#3.+  直接用+号看上去与用extend()一样的效果，但是实际上是生成了一个新的列表存这两个列表的和，只能用在两个列表相加上
#4.+= 效果与extend()一样，向原列表追加一个新元素，在原有列表上增加
def commodity_add(commodity1):
	commodity1.append('西兰花') 
	commodity1.extend(['排骨','莲藕']) 
	return commodity1

def shopping_all(commodity3):
  	for index1, buy_item in enumerate(commodity3):
  	 	if is_even(index1):
  			buy_number = index1 + 1
  			print '老妈看到%s，买%d斤好了' %(buy_item, buy_number)
  			print '老妈继续逛'
  		else:
  			print '这里有%s啊，不买' %(buy_item)
  			print '老妈继续逛'

def shopping_part(commodity6):
	print_list(commodity6)

def  is_even(index):
	if index % 2 ==0:
		return True
	else:
		return False

def print_list(lst):
	for item in lst:
		print '老妈逛了%s' %(item)
	
def main():
	print '老妈来到菜市场'
	print '-----'
	commodity3 = commodity()
	len1 = len(commodity3)
	print '原商品种类数%d种' %(len1)
	shopping_all(commodity3)
	print '-----'
	commodity4 = commodity_add(commodity3)	
	len2 = len(commodity4)
	print '商品增加种类后为%d种' %(len2)
	print '老妈有点累，只逛第五种到第九种商品'
	commodity5 = commodity4[4:9]
	shopping_part(commodity5)

if __name__ == '__main__':
  	main()