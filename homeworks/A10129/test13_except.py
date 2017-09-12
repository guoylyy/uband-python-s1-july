#!/usr/bin/python
# -*- coding: utf-8 -*-
#author:冰糖葫芦

def main():
  week_overnight = [False, True, False, False, False] #周一到周五的情况
  for index,is_overnight in enumerate(week_overnight):
    print '今天星期%d' % (index + 1)
    
    try:
      overnight_check(is_overnight)
    except Exception,e:
      #发生错误的情况
      print '发生错误：%s' % (e)
      print '洋葱暴打大葱，但最后原谅了他'
    else:
      #没有发生错误的情况
      print '继续'

def overnight_check(is_overnight):
  if is_overnight:
    raise Exception('分手') #强行中断程序的语法
  else:
    print '正常'

if __name__ == '__main__':
  main()