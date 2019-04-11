###################################################################
# File Name: main.py
# Author: CoffreLv
# mail: coffrelv@163.com
# Created Time: 2018年10月16日 星期四 08时07分41秒
#=================================================================
#-*- coding:utf-8 -*

import os
import time

import read_config
import drawing_chart
import build_dataset
import prepare_dataset
import count_decode_score
import save_and_remove_last_files

#读取配置文件，配置所需配置
def Read_now_config(iteration):
    Num_Of_Sentence = int(read_config.Read_config('../doc/config.cfg', 'section'+str(iteration), 'num_of_sentence'))
    Train_wav_path = read_config.Read_config('../doc/config.cfg', 'section'+str(iteration), 'train_wav_path')
    Test_wav_path = read_config.Read_config('../doc/config.cfg', 'section'+str(iteration), 'test_wav_path')
    return Num_Of_Sentence,Train_wav_path,Test_wav_path

#调用shell脚本./run.sh进行训练
def Training(Time,itera):
    #training
    os.chdir("../../")
    os.system("./run.sh")
    os.chdir("Kaldi_py_toolkit/src/")
    return

def One_corpus(Time):
    Num_Of_Iterations = int(read_config.Read_config('../doc/config.cfg', 'section0', 'num_of_iterations'))
    i = 1;
    while i < Num_Of_Iterations+1:
        print("--------------------------------------------------------------------------------")
        print("-             Oh my goddess! This is the %d iterations !"%i+"                        -")
        print("--------------------------------------------------------------------------------")
        Train_signal = 'train'
        Num_Of_Sentence,Train_wav_path,Test_wav_path = Read_now_config(i)
        save_and_remove_last_files.Remove_last_files()
        prepare_dataset.Prepare_dict()
        prepare_dataset.Get_all_text_data(Train_signal,i)
        Train_scale = int(input("请输入训练集所占比例（1-10）："))
        Test_scale = int(input("请输入测试集所占比例（1-10）："))
        Dev_scale = 10 - Train_scale - Test_scale
        build_dataset.Build_every_dataset(Num_Of_Sentence,Train_scale,Test_scale,Dev_scale)
        build_dataset.Get_and_test_the_wav_params(Train_wav_path)
        build_dataset.Get_and_test_the_wav_params(Test_wav_path)
        #build_dataset.Get_and_test_the_wav_params(Dev_wav_path)
        Training(i,Time)
        save_and_remove_last_files.Save_last_files(Time,i)
        All_score = count_decode_score.Get_and_save_the_all_score(Time,i)
        drawing_chart.Get_the_Itera_chart(Time,i)
        i += 1
    drawing_chart.Get_the_Iterations_chart(Time)

def Many_corpus(Time):
    Num_Of_Iterations = int(read_config.Read_config('../doc/config.cfg', 'section0', 'num_of_iterations'))
    i = 1;
    while i < Num_Of_Iterations+1:
        print("--------------------------------------------------------------------------------")
        print("-             Oh my goddess! This is the %d iterations !"%i+"                        -")
        print("--------------------------------------------------------------------------------")
        Train_signal = 'train'
        Test_signal = 'test'
        #Dev_signal = 'dev'
        Num_Of_Sentence,Train_wav_path,Test_wav_path = Read_now_config(i)
        save_and_remove_last_files.Remove_last_files()
        prepare_dataset.Prepare_dict()
        prepare_dataset.Get_all_text_data(Train_signal,i)
        prepare_dataset.Get_all_text_data(Test_signal,i)
        #prepare_dataset.Get_all_text_data(dev_signal,i)
        build_dataset.Get_every_text(Train_signal)
        build_dataset.Get_every_text(Test_signal)
        #build_dataset.Get_every_text(Dev_signal)
        #build_dataset.Get_and_test_the_wav_params(Train_wav_path)
        #build_dataset.Get_and_test_the_wav_params(Test_wav_path)
        #build_dataset.Get_and_test_the_wav_params(Dev_wav_path)
        Training(Time,i)
        save_and_remove_last_files.Save_last_files(Time,i)
        All_score = count_decode_score.Get_and_save_the_all_score(Time,i)
        #drawing_chart.Get_the_Itera_chart(Time,i)
        i += 1
    #drawing_chart.Get_the_Iterations_chart(Time)

def Main_self():
    Time = str(time.strftime('%y-%m-%d_%H_%M_%S',time.localtime()))
    choice = int(input("请选择单（1）或多（0）语料集："))
    if choice == 1:
        One_corpus(Time)
    elif choice == 0:
        Many_corpus(Time)
    else:
        print("ERROR:输入错误请重新运行并选择！")

if __name__ == '__main__':
    Main_self()
    exit()
