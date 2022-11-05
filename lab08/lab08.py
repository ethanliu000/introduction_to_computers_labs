# -*- coding: utf-8 -*-

import os

now_path=(os.path.abspath(os.getcwd()))
now_path_split=now_path.split("/")
now_path_split_len=len(now_path_split)
print(now_path_split)
for i in range(1,now_path_split_len):
  path = 'e94116059.txt'
  f = open(path, 'a')
  f.write(now_path_split[i])
  f.write("\n")
  f.close()

dir_path = r"/home/E94116059"
result = os.listdir(dir_path)
result_len = len(result)
print(result)
for i in range(0,result_len):
  path = 'e94116059.txt'
  f = open(path, 'a')
  if i==0:
      f.write("\n")
      f.write(result[i])
      f.write("\n")
  else:
      f.write(result[i])
      f.write("\n")
  f.close()
