#!/usr/bin/python
# -*- coding: utf-8 -*-
# @author: zhangjing

# 1. 对照锅蜀黍视频里的过程自己打一遍，自己体会一下
# 2. 解释一遍自己眼中的单一职责原则是什么？
# 3. [选做]加一个记账函数'record_account'，打印：'老妈在小本子记了买菜花销xx元'（xx要计算返回哦）
# task 01
def talk_with_daddy ( is_cheap3,buy_account3 ):
	if is_cheap3:
		print '老妈回到家里,跟老爸说:"今天去买菜，价格不贵，买了%d斤". ' % (buy_account3)
	else:
		print '老妈回到家里,跟老爸说:"今天去买菜，菜好贵啊,没买".'

def buy_buy_buy_():
	good_price = 4
	reasonable_price = 5
	buy_account = 2

	who = '我的老妈'
	good_description = '西双版纳大白菜'
	is_cheap = False

	print '%s上街看到了%s,卖%d元/斤' % (who,good_description,good_price)
	if good_price <= reasonable_price:
		print  '她认为便宜'
		is_cheap = True
		buy_account = 2 + (reasonable_price - good_price)
		if buy_account > 4:
			buy_account = 4
		print '她买了%d斤' % (buy_account)
	else:
		print '她认为贵了'
		is_cheap = False
		print '扬长而去'
	return is_cheap,buy_account

def main():
	is_cheap2,buy_account2 = buy_buy_buy_()
	talk_with_daddy(is_cheap2,buy_account2)
	
if __name__ == '__main__':
	main()

#task 02 单一职责原则：定义的一个代码块函数只能执行一个功能。

def talk_with_daddy ( is_cheap,buy_account ):
	if is_cheap:
		print '老妈回到家里,跟老爸说:"今天去买菜，价格不贵，买了%d斤". ' % (buy_account)
	else:
		print '老妈回到家里,跟老爸说:"今天去买菜，菜好贵啊,没买".'

def account(is_cheap,buy_account):
	if is_cheap:
		print '老妈今天买了%d斤菜,并记在了账单上'%(buy_account)
	else:
		print '因为菜价很贵，老妈今天没买菜'

def buy_buy_buy_():
	good_price = 4
	reasonable_price = 5
	buy_account = 2

	who = '我的老妈'
	good_description = '西双版纳大白菜'

	is_cheap = False

	print '%s上街看到了%s,卖%d元/斤' % (who,good_description,good_price)
	if good_price <= reasonable_price:
		print  '她认为便宜'
		is_cheap = True
		buy_account = 2 + (reasonable_price - good_price)
		if buy_account > 4:
			buy_account = 4
		print '她买了%d斤' % (buy_account)
	else:
		print '她认为贵了'
		is_cheap = False
		print '扬长而去'
	return is_cheap,buy_account

def main():
	is_cheap,buy_account = buy_buy_buy_()

	talk_with_daddy (is_cheap,buy_account)
	account(is_cheap,buy_account)

if __name__ == '__main__':
	main()
