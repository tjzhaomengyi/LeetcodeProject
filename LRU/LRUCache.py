# -*- coding: utf-8 -*-#

#-------------------------------------------------------------------------------
# Name:         LRUCache
# Description:  实现LRU,get如果关键字存在于缓存根据关键字返回；
# 插入：如果关键字存在变更数值，不存在插入键值。当容量达到上限时，在写入新数据之前删除最久未使用的数据值
# Author:       zhaomengyi
# Date:         2021/5/25
#-------------------------------------------------------------------------------
import collections


class LRUCache:

  def __init__(self, capacity: int):
    self.dic = collections.OrderedDict()#使用一个有序字典实现
    self.remain = capacity

  def get(self, key: int) -> int:
    if key not in self.dic:
      return -1
    v = self.dic.pop(key)
    self.dic[key] = v #表示当前取出来的元素是最新的元素
    return v


  def put(self, key: int, value: int) -> None:
    if key in self.dic:
      self.dic.pop(key)
    else:
      if self.remain > 0:
        self.remain = self.remain-1
      else:
        self.dic.popitem(last=False) #将最后一个弹出
    self.dic[key] = value

if __name__ == '__main__':
  lRUCache = LRUCache(2);
  lRUCache.put(1, 1);
  lRUCache.put(2, 2);
  a=lRUCache.get(1);
  print(a)
  lRUCache.put(3, 3);

  b=lRUCache.get(2);
  print(b)
  lRUCache.put(4, 4);
  c=lRUCache.get(1);
  print(c)
  d=lRUCache.get(3);
  print(d)
  e=lRUCache.get(4);
  print(e)
