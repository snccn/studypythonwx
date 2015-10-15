#!/usr/bin/env python 
#-*- coding:utf-8 -*-
#author snccn
#filename: flitter.py
#api to encode string 


from base64 import b64encode as b64enc
import hashlib
# from hashlib import *
class STRFliter():
	def __init__(self,target):
		self.target=target
		self.result='0'
		self.m=hashlib.md5()
	def b64en(self,STR):
		self.result=b64enc(STR)
		print self.result
	def Md5hash(self,STR):
		self.m.update(STR)
		self.result=self.m.hexdigest()
		print self.result
	def ASCII_hex(self,STR):
		for i in STR:
			self.result=self.result+((str(hex(ord(i))))[3:4])
		print self.result[2:]
	
a=STRFliter("Administartor")
# a.b64en(a.target)
# a.Md5hash(a.target)
a.ASCII_hex(a.target)
