###################################################################
# File Name: Save_and_remove_last_files.py
# Author: CoffreLv
# mail: coffrelv@163.com
# Created Time: 2018年07月30日 星期一 16时01分46秒
#=================================================================
#-*- coding:utf-8 -*
import time
import shutil
import os

#保存并移除上次运行的数据文件
def Save_and_remove_last_files(Time,iteration):
    Save_last_files(Time,iteration)
    Remove_last_files()

#保存上次运行的数据文件到指定目录
def Save_last_files(Time,iteration):
    logfile = '../log/'+Time
    if not os.path.exists(logfile):
        os.mkdir(logfile)
    itera_logfile = '../log/'+Time+'/'+str(iteration)
    if not os.path.exists(itera_logfile):
        os.mkdir(itera_logfile)
    Need_copy_files = ['exp','mfcc','data/train','data/test','data/dev','data/lang','data/lang_test_bg']
    for files in Need_copy_files:
        if os.path.exists('../../'+files):
            shutil.copytree('../../'+files,itera_logfile+'/'+files)

#移除上次运行的数据文件
def Remove_last_files():
    #Need_copy_files = ['../../exp','../../mfcc','../../data/train','../../data/test','../../data/lang','../../data/lang_test_bg']
    Need_remove_files = ['../../exp','../../mfcc','../../data/lang','../../data/dev','../../data/train/','../../data/test/','../../data/lang_test_bg']
    for files in Need_remove_files:
        if os.path.exists(files):
            shutil.rmtree(files)

#本脚本主函数
def Main_self(Time,Iteration):
    Save_and_remove_last_files(Time,Iteration)

if __name__ == '__main__':
    Time = str(time.strftime('%y-%m-%d_%H_%M_%S',time.localtime()))
    Iteration = input("请输入本次迭代次数：")
    Main_self(Time,Iteration)
    exit()
