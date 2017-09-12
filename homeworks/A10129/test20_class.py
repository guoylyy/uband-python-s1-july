#!/usr/bin/python
# -*- coding: utf-8 -*-
# author:冰糖葫芦


#需求
# - 老妈的交通工具有两个，电动车和自行车
# - 家里离菜场共 20 公里
# - 周一的时候骑电动车去买菜，骑了 0.5 小时
# - 周二的时候骑自行车去卖菜，骑了 2 小时
# - 周三的时候骑电动车去卖菜，骑了 0.6 小时
# - 分别输出三天骑行的平均速度
class dailylife():
  """this is my mom's dailylife"""
  def __init__(self, week_day, transportion, time):
    self.week_day = week_day
    self.transportion = transportion
    self.time = time

  def momslife(self):
    speed = 20/self.time
    print 'mom %s 骑 %s 平均时速 %0.2f km/h' %(self.week_day,self.transportion, speed)


def main():
  day1 = dailylife('周一', '电动车', 0.5)
  day1.momslife()
  day2 = dailylife('周二', '自行车', 2)
  day2.momslife()
  day3 = dailylife('周三', '电动车', 0.6)
  day3.momslife()
  distance = 20

if __name__ == '__main__':
  main()
