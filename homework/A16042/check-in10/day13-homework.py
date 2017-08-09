#!/usr/bin/python
# -*- coding: utf-8 -*-

def main():
	week_overnight =[False,False,True,False,False]
	for index,is_overnight in enumerate(week_overnight):
		print '今天是星期%d'%(index + 1)
		try:
			overnight_check(is_overnight)
		except Exception,e:
			print '发生错误:%s'%(e)
			print '老妈骂了老爸一顿,然后原谅了他'
		else:
			print '附带脚本'
		finally:
			pass
	pass

def overnight_check(is_overnight):
	if is_overnight:
		raise Exception('离婚')
	else:
		print '正常'

if __name__ == '__main__':
  main()




def homework2():
  book = {"abandon": 'to give up to the control or influence of another person or agent',"abase": "to lower in rank, office, prestige, or esteem","abash" : "to destroy the self-possession or self-confidence of"}
  who = '老妈'
  tear_word = 'abase' #可能会被撕毁的页的key

  print '%s在看一本英文书' % (who)
  if not search('etiquette', book, who):
    tear_mean = book[tear_word]

    del book[tear_word]
    print '%s撕毁了 %s 的页面' % (who, tear_word)
    
    for key in book.keys():
        print key
        print book[key]
    print book.has_key('abase')
    	
def search(key, dictionary, who):
  if dictionary.has_key(key):
    print '%s 查询到了 %s:%s' % (who, key, dictionary[key])
    return True
  else:
    print '%s 没有查询到 %s 的意思' %(who, key)
    return False


def item_check(is_short):
	if not search ('abase',book,who):
		raise Exception('END')
	else:
		print '正常'



if __name__ == '__main__':
  homework2()