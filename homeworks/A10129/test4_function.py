#!/usr/bin/python
# -*- coding: utf-8 -*-
# @author: 冰糖葫芦

# 1. 对照锅蜀黍视频里的过程自己打一遍，自己体会一下
# 2. 解释一遍自己眼中的单一职责原则是什么？
# 3. [选做]加一个记账函数'record_account'，打印：'老妈在小本子记了买菜花销xx元'（xx要计算返回哦）
import time

def buybuybuy():
    who = '冰糖葫芦的老妈'
    good_price = int(raw_input ('小贩的价格:'))#小贩的价格
    good_description = '西双版纳大白菜' #小贩的招牌

    is_cheap = False #是否便宜
    reasonalable_price = 5 #老妈能接受的最高价格
    buy_intend = 2 #准备买2斤

    print (('%s上街看到了%s， 卖 %d 元／斤')  %( who, good_description, good_price ))

    if good_price <= reasonalable_price:
        print '她认为便宜,',
        is_cheap = True
        buy_amount = buy_intend + reasonalable_price - good_price
        if buy_amount > 4:
            buy_amount = 4
        total_price = buy_amount * good_price
        print '买了 %d 斤,花了 %d 元' %(buy_amount,total_price)
    else:
        print '她认为贵了',
        is_cheap = False
        print '没有买，扬长而去'

    return good_description, is_cheap, good_price, buy_amount, total_price

def talk_with_daddy(is_cheap3,good_price3,buy_amount3):
	if is_cheap3:
		print '\n今天白菜好便宜啊，%d元一斤，我买了%d斤' %(good_price3,buy_amount3)
	else:
		print '\n最近白菜也太贵了吧，啥也没买'

def record_account(is_cheap4,good_description4,total_price4):
	if is_cheap4:
		print '\n\033[0;36;40m冰糖葫芦老妈的账簿\033[0m'
		print time.strftime('%Y-%m-%d',time.localtime(time.time())),
		print '：\t%s（%d元）' %(good_description4,total_price4)

def main():
	good_description2, is_cheap2, good_price2, buy_amount2, total_price2 = buybuybuy()
	talk_with_daddy(is_cheap2,good_price2,buy_amount2)
	record_account(is_cheap2,good_description2,total_price2)

if __name__ == '__main__':
	main()