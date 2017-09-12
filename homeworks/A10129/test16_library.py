#!/usr/bin/python
# -*- coding: utf-8 -*-
# @author: 冰糖葫芦

import time
import calendar

def main():
	now = time.time()
	print now
	localtime = time.localtime(time.time())
	print localtime
	localtime1 = time.asctime(localtime)
	print localtime1
	localtime2 = time.strftime('%Y-%m-%d', localtime)
	print localtime2

	cal1 = calendar.month(2017,3)
	print cal1
	isleap = calendar.isleap(2016)
	print isleap

if __name__ == '__main__':
	main()