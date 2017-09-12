#!/usr/bin/python
# -*- coding: utf-8 -*-
# @author: 冰糖葫芦
import turtle

def main():
  #设置一个画面
  windows = turtle.Screen()
  #设置背景
  windows.bgcolor('blue')
  turtle.register_shape('love',((0,0),(16,0),(16,8),(8,8),(8,16),(0,16)))
  turtle.title('welcome to the turtle zoo')
  #生成一个黄色乌龟
  bran = turtle.Turtle()
  #poly = ((0,0),(10,-5),(0.10),(-10,-5))
  #s = turtle.Shape("compound")
  #s.addcomponent(poly,'red','blue')
  #bran.shape(s)
  bran.color('yellow')
  #开始你的表演

  turtle_shape = turtle.getshapes()
  length = len(turtle_shape)
  for index,shapepart in enumerate(turtle_shape):
    bran.shape(shapepart)
    bran.speed(1)
    bran.forward(100)
    bran.right(90)
    bran.forward(100)
    bran.right(90)
    bran.forward(100)
    bran.right(90)
    bran.forward(100)
    bran.right(40)
    print index,shapepart


if __name__ == '__main__':
  main()