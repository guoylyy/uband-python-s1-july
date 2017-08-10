#!/usr/bin/python
# -*- coding: utf-8 -*-
# @author: zj

import turtle
def main():
	windows = turtle.Screen()#设置画面
	windows.bgcolor('blue')#设置背景
	bran = turtle.Turtle()#生成乌龟
	bran.shape('turtle')
	bran.color('yellow')
	bran.speed(2)#设置速度
	for i in range(1,5):#设置路径
		bran.forward(100)
		bran.right(45)
		bran.forward(100)
		bran.right(45)
		bran.forward(100)
		bran.right(45)
		bran.forward(100)
		bran.right(45)

if __name__ == '__main__':
	main()

	pass



def main2():
#time
	#函数time.time()用于获取当前时间戳,最适于做日期计算，1970-2038
	import time;
	ticks = time.time()
	print '当前时间戳为:',ticks
#时间元祖：用一个元件装起来的9组数字处理时间
#获取当前时间：从返回浮点数的时间缀方式向时间元祖转换。localtime
	print'----------------------'
	import time
	localtime = time.localtime(time.time())
	print '本地时间为:',localtime
# 获取格式化的时间，asctime()
	print '--------------------'
	import time
	localtime = time.asctime(time.localtime(time.time()))
	print '本地时间为:',localtime
#格式化日期：time-strftime
	print'-----------------------'
	import time
	#格式化成2017-07-25 21:14:19形式
	print time.strftime('%Y-%m-%d %H:%M:%S',time.localtime())
	#格式化成Tue Jul 25 21:14:19 2017形式
	print time.strftime('%a %b %d %H:%M:%S %Y',time.localtime())
	#将时间字符串转换为时间戳
	a = 'Tue Jul 25 21:08:49 2017'
	print time.mktime(time.strptime(a,'%a %b %d %H:%M:%S %Y'))
#calendar处理年历和月历
	import calendar
	cal = calendar.month(2017,7)
	print '以下输出2017年7月份的日历:'
	print cal;
if __name__ == '__main__':
	main2()