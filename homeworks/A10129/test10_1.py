#!/usr/bin/python
# -*- coding: utf-8 -*-
# @author: 冰糖葫芦

def homework2():
  book = {
          "abandon": 'to give up to the control or influence of another person or agent',
          "abase": "to lower in rank, office, prestige, or esteem",
          "abash" : "to destroy the self-possession or self-confidence of"
          }
  print '老妈在看一本英文书'
  if not book.has_key('etiquette'): #没有查到
    print '老妈没有查到 %s 的意思' % ('etiquette')

    #撕毁了abandon
    del book['abase']
    print '老妈撕毁了 %s 的页面' % ('abase')

    if book.has_key('abash'):
      print '老妈查到了 %s : %s' % ('abash', book['abash'])

      #老妈黏贴了代码
      book['abase'] = "to lower in rank, office, prestige, or esteem"
      print '老妈把 %s 的字典页又贴上了' % ('abase')

    else:
      print '老妈没有查到 %s ' % (abash) 
  else:
    print '老妈查到了 %s '% ('etiquette')


if __name__ == '__main__':
  homework2()