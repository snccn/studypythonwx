#!/usr/bin/env python 
#-*- coding: utf-8 -*-
#date 2015 10 11
#author snccn
#filename :sender.py
#sqlite connction script when the Save bar actived
#connect
#@version alpha 0.02

from os import *
import sqlite3

class sender():
	def __init__(self):
		self.database=sqlite3.connect("./store.db")
		self.cur=self.database.cursor()
	def create_table(self):
		try:
			self.cur.execute('CREATE TABLE data0 (id integar PRIMARY KEY,client varchar(255))  ')
			self.cur.execute('CREATE TABLE details (dates varchar(255) PRIMARY KEY ,comment varchar(255))' )
			print "execute complete"
		except:
			print "table had already created"
	def insert_data(self,data):
		self.cur.execute('INSERT INTO data0 VALUES'+data)
		self.database.commit()
	def select_data(self,contorl):
		self.cur.execute('select* from data0 where id ='+contorl)
		return self.cur.fetchall()
	def __doc__(self):
		print "do not open the string input command to normal users"
		print "it will cause some troble here"
	def insertNorData(self,data):
		self.cur.execute('INSERT INTO details VALUES'+data)
		self.database.commit()
# debug options
# if __name__ == '__main__':
# 	save=sender()
# 	save.create_table()
# 	# save.insert_data()
# 	save.select_data("0 or 1=1")
