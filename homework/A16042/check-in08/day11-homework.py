#!/usr/bin/python
# -*- coding: utf-8 -*-
# @author: xxx

# 实现了和 homework01 一样的功能
# 供你分析和对比
def print_list(lst):
  for lst_item in lst :
    print '%s'%(lst_item)

def homework2():
  book = {
          "abandon": 'to give up to the control or influence of another person or agent',
          "abase": "to lower in rank, office, prestige, or esteem",
          "abash" : "to destroy the self-possession or self-confidence of"
          }
  who = ' 老妈 '
  tear_word = 'abase' #可能会被撕毁的页的key

  print '%s 在看一本英文书 ' % (who)
  if not search('etiquette', book, who):
    tear_mean = book[tear_word]

    del book[tear_word]
    print '%s撕毁了 %s 的页面' % (who, tear_word)

    if search('abase', book, who):
      print '%s查到了%s:%s'%(who,'abase',book['abase'])
    else:
       #老爸黏贴了代码
      book[tear_word] = tear_mean
      print '%s把 %s 的字典页又贴上了' % (who, tear_word)
  
  lst = ['abandon','abase','abash' ]
  for lst_item in lst :
    if search(lst_item,book,who):
      print '可把我牛逼坏了,叉会腰'
    else:
      print 'there is some bugs'

    
  
def search(key,book,who):
    if book.has_key(key):
      print '%s 查询到了 %s:%s' % (who, key, book[key])
      return True
    else:
      print '%s 没有查询到 %s 的意思' %(who, key)
      return False
      
if __name__ == '__main__':
  homework2()



  #问题二：
  加上key='abase'，key被重新定义，只含有abase，查询etiquette时，调用search函数，查询不到继续执行，
  查询到abase，即直接输出老爸查询到了abase，结束运行。