#!/usr/bin/python
# -*- coding: utf-8 -*-
# @author: Guoshushu

# 今日的作业
# 有十种菜
#   白菜、萝卜、西红柿、甲鱼、龙虾、生姜、白芍、西柚、牛肉、水饺
# 
# 1. 老妈来到了菜市场，从下标 0 开始买菜，遇到偶数的下标就买
#    遇到奇数的下标就不买，买的数量为下标 + 1 斤
#    （请写程序模拟整个过程）
#    （注意单一职责原则）
#    （注意灵活使用 def 函数（代码块））
#    
# 【提示】：
#   输出结果可能为
#   ‘老妈来到菜市场
#    老妈看到白菜，买了 1 斤
#    老妈继续逛
#    老妈看到xxx, 不买
#    老妈继续逛
#    ...
#   '
#  2. 完成后，用今天的学到的列表知识，加 3 个菜
#  3. 完成后，用今天的学到的列表知识，让老妈只逛第 5~9 个菜
def homework():
	#下标：    0     1       2      3      4     5      6     7      8      9
	lst = ['白菜','萝卜','西红柿','甲鱼','龙虾','生姜','白芍','西柚','牛肉','水饺']
	print '老妈来到菜市场'
	index = 0
	
	for lst_item in lst :
		if index%2 == 0:
			index2 = index +1
			print '老妈看到了%s,买了%d斤' % (lst_item,index2)
			print '老妈继续逛'
		else:
			print '老妈看到%s,不买'%(lst_item)
			if (index2+1==10):
				print '老妈终于心满意足地走出了菜市场'
			else:
				print '老妈继续逛'
		index = index+1
	return index2

if __name__ == '__main__':
  homework()

#-----------------------------------------------------------------------------------------------------------------

def print_list(lst):
  for lst_item in lst:  #遍历
    print '老妈看到了 %s '% (lst_item)

def homework():
	#下标：    0     1       2      3      4     5      6     7      8      9
	lst = ['白菜','萝卜','西红柿','甲鱼','龙虾','生姜','白芍','西柚','牛肉','水饺']
	print '老妈来到菜市场'
	index = 0
	for lst_item in lst :
		index = index +1
	lst.append('土豆')
	lst.append('大豆')
	lst.append('白芍')
	print_list(lst)
	
if __name__ == '__main__':
  homework()


#-----------------------------------------------------------------------------------------------------------------------
def main2(lst2):
	for lst2_item in lst2 :
		print '但老妈只逛了%s'%(lst2_item)

def main():
	#下标：    0     1       2      3      4     5      6     7      8      9
	lst = ['白菜','萝卜','西红柿','甲鱼','龙虾','生姜','白芍','西柚','牛肉','水饺']
	for lst_item in lst :
		print '老妈今天去菜市场,看到了%s'%(lst_item)
	lst2 = lst[4:9]
	main2(lst2)

if __name__ == '__main__':
  main()

		





