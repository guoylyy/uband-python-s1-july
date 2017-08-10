#!/usr/bin/python
# -*- coding: utf-8 -*-
# @author: zhangjing

def main():
	#01.int
	apple_number = 5
	apple_price = 4.8
	pie_number = 6
	pie_price = 6.7

	#02. * /
	apple_total_price = apple_number * apple_price
	pie_total_price = pie_number * pie_price

	#03.float
	print 'pie cost %d' % ( pie_total_price )
	print 'pie_cost %g' % ( pie_total_price )
	print 'pie_cost %0.2f' % ( pie_total_price )

	#04. **
	number = 2**3
	print 'number = %d' % ( number )

	#05.   // %
	print 'number = %d' % ( 8/3 )
	print 'number = %d' % ( 8//3 )

	#06. & |
	print 'number = %d' % ( 5&3 )
	print 'number = %d' % ( 5|3 )

	#07. 
	print 'test: %d' % (4 >= 2)
	print 'test: %d' % (4 != 2)
	if 1:
		print 'yes'
	if 0:
		print 'no'

if __name__ == '__main__':
  main()
