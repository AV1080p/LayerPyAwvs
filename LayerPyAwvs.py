# -*- coding:utf-8 -*-
 import subprocess
 import os, time, shutil
 import sys

'''给子域名添加http前缀，并保存'''
 def addPrefix():
  url = []
  try:
  layerRead = open('layer.txt', 'r')
  layerWrite = open('results.txt', 'w')
  layer = layerRead.readlines()
  # print s,type(s)
  prefix = 'http://'
  for x in range(len(layer)):
  prefixLayer = prefix + layer[x]
  list(prefixLayer)
  url.append(prefixLayer)
  # print url
  layerWrite.writelines(url)
  layerRead.close()
  layerWrite.close()
  print "finish"
  except IOError, e:
  print "file open error"

'''使用wvs命令行进行批量扫描'''

def wvsScan():
  file = open('results.txt', 'r')
  for fileurl in file:
  url = fileurl.strip('\n')
  print u'开始扫描:'+url

#填入wvs的路径
  scan = r"C:\Acunetix\Web Vulnerability Scanner 10\wvs_console.exe /Scan " + url
  doscan = subprocess.Popen(scan)
  doscan.wait()

if __name__ == '__main__':
 addPrefix()
  print u'是否进行批量扫描，是 Y 否 N'
  inputs = raw_input()
  if inputs.upper()=='Y':
  wvsScan()
  else:
  sys.exit()