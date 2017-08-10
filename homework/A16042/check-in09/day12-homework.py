#!/usr/bin/python
# -*- coding: utf-8 -*-
# @author: xxx

def main():
  tup = (1,2,3,4)

  #取值
  print tup[1]
  # 切片
  print tup
  print tup[0:2]
  # 是否存在某值
  print (2 in tup)
  
  # 赋值
  a,b,c,d = (1,2,3,4)
  print b
  print c
  # 遍历
  #number1
  for item in tup:
    print item
  #number2
  print 'number2'
  for index,item in enumerate(tup):
    print index
    print item
  # 花式报错
  # 不支持 1)插入 2)修改 3) 删除
  try:
    tup.append(5)
    del tup[0]
    tup[0] = 'hhhhh'
    pass
  except Exception, e:
    print e
  
if __name__ == '__main__':
  main()


