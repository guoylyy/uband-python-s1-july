#!/usr/bin/python
# -*- coding: utf-8 -*-
# @author: 冰糖葫芦
def word_lst():
  word_list = ['abandon','add','abash']
  return word_list

def dic_item():
  dictionary = {
        "abandon": 'to give up to the control or influence of another person or agent',
        "abase": "to lower in rank, office, prestige, or esteem",
        "abash" : "to destroy the self-possession or self-confidence of"
        }
  return dictionary

def homework2():
  who = '老妈'
  book = dic_item()
  word = word_lst()
  tear_word = 'abase' #可能会被撕毁的页的key
  tear_mean = book[tear_word]
  print '%s在看一本英文书' % (who)
  for item in word:
    if not search(item, book, who):
      if book.has_key(tear_word):
        del book[tear_word]
        print '%s撕毁了 %s 的页面' % (who, tear_word)
    else:
      if not book.has_key(tear_word):
        book[tear_word] = tear_mean
        print '%s把 %s 的字典页又贴上了' % (who, tear_word)

def search(key, dictionary, who):
  if dictionary.has_key(key):
    print '%s 查询到了 %s:%s' % (who, key, dictionary[key])
    return True
  else:
    print '%s 没有查询到 %s 的意思' %(who, key)
    return False


if __name__ == '__main__':
  homework2()