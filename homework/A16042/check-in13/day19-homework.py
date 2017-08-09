#!/usr/bin/python
# -*- coding: utf-8 -*

class Fairy():
	def __init__(self,name,location):
		self.name = name
		self.location = location
	def descend(self):
		print ' 来自%s的%s偷偷下凡,遇到了驸马爷 '%(self.location,self.name)
	def work_hard(self):
		print '%s想尽办法成功蛊惑驸马爷和公主分手'%(self.name)
	def marry(self):
		print '%s从此和公主过上了幸福的生活'%(self.name)
def function():
	a_bad_bad_girl = Fairy('a_bad_bad_girl','天庭')
	a_bad_bad_girl.descend()
	a_bad_bad_girl.work_hard()
	a_bad_bad_girl.marry()
if __name__ == '__main__':
  function()

	

