# -*- coding: utf-8 -*-
"""
Created on Thu Nov  5 13:08:45 2020

@author: Administrator
"""

from pymysql import *
class Mysqlpython:
    def __init__(self, database="pythondb", host="localhost", user="root",
                 password="zxcvbnm1999", port=3306, charset="utf8"):
        self.host = host
        self.user = user
        self.password = password
        self.port = port
        self.database = database #可修改，根据文件所在位置修改
        self.charset = charset

    # 数据库连接方法:
    def open(self):
        self.db = connect(host=self.host, user=self.user,
                          password=self.password, port=self.port,
                          database=self.database,
                          charset=self.charset)
        # 游标对象
        self.cur = self.db.cursor()

    # 数据库关闭方法:
    def close(self):
        self.cur.close()
        self.db.close()

    # 数据库执行操作方法:
    def Operation(self, sql):
        try:
            self.open()
            self.cur.execute(sql)
            self.db.commit()
            print("ok")
        except Exception as e:
            self.db.rollback()
            print("Failed", e)
        self.close()

    # 数据库查询所有操作方法:
    def Search(self, sql):
        try:
            self.open()
            self.cur.execute(sql)
            result = self.cur.fetchall()
            return result
        except Exception as e:
            print("Failed", e)
        self.close()


def Insert():#如何从外面将数据录入到sql语句中
    id_num = int(input("请输入学校的序号："))
    sch_name = input("请输入参赛学校的名字：")
    run_score = int(input("请输入男生跑步的成绩："))
    lift_score = int(input("请输入男生举重的成绩："))
    swim_score = int(input("请输入女生游泳的成绩："))
    dance_score = int(input("请输入女生跳舞的成绩："))
    boy_score = run_score + lift_score
    girl_score = swim_score + dance_score
    group_score = boy_score + girl_score
    sql_insert = "insert into sports(id,schname,running,lifting,swimming,dancing,boy_total,girl_total,all_total) values(%d,'%s',%d,%d,%d,%d,%d,%d,%d)"%(id_num, sch_name, run_score,lift_score,swim_score,dance_score, boy_score, girl_score, group_score)
    print(id_num)
    return  sql_insert

def Project():
    print("所有比赛项目有：")
    list=['举重','跑步','游泳','跳舞']
    print(list)


def Exit():
    print("欢迎下次使用!!!")
    exit()

def Search_choice(num):
    date = Mysqlpython()
    date.open()
    if num=="2":
        # 1.增加操作
        sql_insert = Insert()
        date.Operation(sql_insert)
        print("添加成功！")
        Start()
    elif num=="1":
        # 2.查找数据,其中order by 是为了按什么顺序输出，asc 是升序输出，desc降序输出
        input_date=input("请选择您想要以什么格式输出：默认升序排列1.学校编号，2.女子团体，3.男子团体，4.团体总分")
        if input_date=="1":
            sql_search = "select * from sports order by id asc"
        elif input_date=="2":
            sql_search = "select * from sports order by girl_total asc"
        elif input_date=="3":
            sql_search = "select * from sports order by boy_total asc"
        elif input_date=="4":
            sql_search = "select * from sports order by all_total asc"
        else:
            print("请重新输入，输入越界或者有误！")
        result = date.Search(sql_search)
        print("id 学校 跑步 举重 游泳 跳舞 男团 女团 总团")
        for str in result:
            print(str)
        Start()
    elif num=="3":
        Project()
        Start()

    elif num=="4":
        del_num=input("请输入您要删除学校的序号：")
        sql_delete="delete from sports where id=%s"%del_num
        date.Operation(sql_delete)
        print("删除成功！")
        Start()
    elif num=="5":
        Exit()
    else:
        print("输入有误，请重新输入！")

def Start():
    print("********************************************************")
    print("*              欢迎来到校运会评分系统                  *")
    print("*1.查看参赛信息                        2.参赛信息录入  *")
    print("*3.参赛项目                            4.删除信息      *")
    print("*5.退出系统                                            *")

    print("********************************************************")
    choice = input("请输入您的选择：")
    Search_choice(choice)

if __name__=="__main__":
    Start()


