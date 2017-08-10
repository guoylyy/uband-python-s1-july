#!/usr/bin/python
# -*- coding: utf-8 -*-
# @author: xxx
import turtle

def main():
  #设置一个画面
  windows = turtle.Screen()
  #设置背景
  windows.bgcolor('blue')
  #生成一个黄色乌龟
  bran = turtle.Turtle()
  bran.shape('turtle')
  bran.color('yellow')
  #开始你的表演
  for i in range(1,3):
    bran.setposition(300,300)
    bran.setheading(90)
    bran.setposition(300,0)
    bran.setheading(90)
    bran.setposition(0,0)
    bran.setheading(90)

    bran.dot(60,'red')

  bran.color('black')
  bran.stamp()
  bran.forward(-300)
  bran.right(90)
  bran.forward(300)
  bran.left(90)
  bran.forward(300)

  bran.clearstamps()

  for i in range(5):
    bran.undo()
    



if __name__ == '__main__':
  main()