#!/usr/bin/python
# -*- coding: utf-8 -*
#author:冰糖葫芦

class Car():
	"""please look at my car"""
	number = 0

	def __init__(self, brand, clour, speed, price):
		self.brand = brand
		self.clour = clour
		self.speed = speed
		self.price = price
		Car.number += 1

	def mycar(self):
		print "我的第%d辆车是%s，车速度是%d，花了%d万" %(Car.number, self.brand, self.speed, self.price)

def main():
	print Car.__doc__
	myfirstcar = Car('Benz', 'red', 120, 100)
	myfirstcar.mycar()
	mysecondcar = Car('JEEP', 'black', 160, 140)
	mysecondcar.mycar()


if __name__ == '__main__':
	main()
		