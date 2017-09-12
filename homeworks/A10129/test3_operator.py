#!/usr/bin/python
# -*- coding: utf-8 -*-
# @author: 冰糖葫芦

def main():
#01 int
	apple_number = 2
	apple_price = 2.5
	banana_number = 3
	banana_price = 1.8
	orange_total_price = 7
	orange_number = 4
	watermelon_total_money = 40.0
	watermelon_number = 3
#02 * / // %
	apple_total_price = apple_price * apple_number
	banana_total_price = banana_price * banana_number
	orange_price = orange_total_price / orange_number
	watermelon_price = watermelon_total_money // watermelon_number
	watermelon_change = watermelon_total_money % watermelon_number
#03 float
	print 'apple cost %d' %(apple_total_price)
	print 'apple cost %g' %(apple_total_price)
	print 'apple cost %0.2f' %(apple_total_price)
	print "orange's price is %3.3f" %(orange_price)
	print  watermelon_price
	print "watermelon's change is: %d" %(watermelon_change)
#04 **
	number = 2 ** 3
	print 'number: %d' %number
#05 logic
	if apple_total_price == banana_total_price:
		print 'buy both apple and banana'
	elif apple_total_price < banana_total_price:
		print 'buy apple'
	else:
		print 'buy banana'

	if number:
		print number
	else:
		print '0'

if __name__ == '__main__':
	main()