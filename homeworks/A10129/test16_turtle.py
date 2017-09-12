#!/usr/bin/python
# -*- coding: utf-8 -*-
# @冰糖葫芦
import turtle

def main():
	windows = turtle.Screen()
	#设置背景
	windows.bgcolor('yellow')
	#生成一个乌龟
	bran = turtle.Turtle()
	bran.shape('turtle')
	bran.color('red')
	bran.speed(1)
	for i in range(1,3):
		bran.left(45)
		bran.forward(80)
		bran.right(90)
		bran.forward(80)
		bran.right(90)
		bran.forward(160)
		bran.right(90)
		bran.forward(160)
		bran.right(90)
		bran.forward(80)
		bran.right(90)
		bran.forward(80)
		bran.left(45)


if __name__ == '__main__':
	main()
