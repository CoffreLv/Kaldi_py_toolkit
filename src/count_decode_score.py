###################################################################
# File Name: Count_decode_score.py
# Author: CoffreLv
# mail: coffrelv@163.com
# Created Time: 2018年09月04日 星期二 08时28分28秒
#=================================================================
#-*- coding:utf-8 -*

import os
import json

#读取训练集和测试集单音素及三音素不同语言模型比重的打分分数
def Get_and_save_the_all_score(Time,iteration):
    all_score = {}
    all_score['Train_Wer_mono'],all_score['Train_Ser_mono'] = Get_the_train_score_mono()
    all_score['Train_Wer_tri'],all_score['Train_Ser_tri'] = Get_the_train_score_tri()
    all_score['Test_Wer_mono'],all_score['Test_Ser_mono'] = Get_the_test_score_mono()
    all_score['Test_Wer_tri'],all_score['Test_Ser_tri'] = Get_the_test_score_tri()
    json_file = json.dumps(all_score,indent = 4)
    with open('../log/'+Time+'/'+str(iteration)+'/score.json', mode = 'w', encoding = 'utf-8') as f:
        f.write(json_file)
        f.close()
        return all_score

#从文件读取存储的全部打分分数
def Get_the_all_score_from_file(Time,iteration):
    filename = '../log/'+Time+'/'+str(iteration)+'/score.json'
    if not os.path.exists(filename):
        print("ERROR: 不存在此文件！   /"+Time+"/"+str(iteration)+'/score.json')
        exit()
    f = open(filename, mode = 'r', encoding = 'utf-8')
    json_file = f.read()
    all_score = json.loads(json_file)
    f.close()
    return all_score

#读取训练集单音素不同语言模型比重的打分分数
def Get_the_train_score_mono():
    Train_score_path = '../../exp/mono/decode_train/'
    Train_score_wer = {}
    Train_score_ser = {}
    for parent, dirnames, filenames in os.walk(Train_score_path):
        for filename in filenames:
            if filename.startswith('wer_'):
                f = open(Train_score_path+filename, mode = 'r', encoding = 'utf-8')
                for line in f:
                    if line.startswith('%WER'):
                        tmp = filename[4:]
                        Train_score_wer[tmp] = float(line[5:10])
                    if line.startswith('%SER'):
                        tmp = filename[4:]
                        Train_score_ser[tmp] = float(line[5:10])
                f.close()
    return Train_score_wer,Train_score_ser

#读取训练集三音素不同语言模型比重的打分分数
def Get_the_train_score_tri():
    Train_score_path = '../../exp/tri1/decode_train/'
    Train_score_wer = {}
    Train_score_ser = {}
    for parent, dirnames, filenames in os.walk(Train_score_path):
        for filename in filenames:
            if filename.startswith('wer_'):
                f = open(Train_score_path+filename, mode = 'r', encoding = 'utf-8')
                for line in f:
                    if line.startswith('%WER'):
                        tmp = filename[4:]
                        Train_score_wer[tmp] = float(line[5:10])
                    if line.startswith('%SER'):
                        tmp = filename[4:]
                        Train_score_ser[tmp] = float(line[5:10])
                f.close()
    return Train_score_wer,Train_score_ser

#读取测试集单音素不同语言模型比重的打分分数
def Get_the_test_score_mono():
    Test_score_path = '../../exp/mono/decode_test/'
    Test_score_wer = {}
    Test_score_ser = {}
    for parent, dirnames, filenames in os.walk(Test_score_path):
        for filename in filenames:
            if filename.startswith('wer_'):
                f = open(Test_score_path+filename, mode = 'r', encoding = 'utf-8')
                for line in f:
                    if line.startswith('%WER'):
                        tmp = filename[4:]
                        Test_score_wer[tmp] = float(line[5:10])
                    if line.startswith('%SER'):
                        tmp = filename[4:]
                        Test_score_ser[tmp] = float(line[5:10])
                f.close()
    return Test_score_wer,Test_score_ser

#读取测试集三音素不同语言模型比重的打分分数
def Get_the_test_score_tri():
    Test_score_path = '../../exp/tri1/decode_test/'
    Test_score_wer = {}
    Test_score_ser = {}
    for parent, dirnames, filenames in os.walk(Test_score_path):
        for filename in filenames:
            if filename.startswith('wer_'):
                f = open(Test_score_path+filename, mode = 'r', encoding = 'utf-8')
                for line in f:
                    if line.startswith('%WER'):
                        tmp = filename[4:]
                        Test_score_wer[tmp] = float(line[5:10])
                    if line.startswith('%SER'):
                        tmp = filename[4:]
                        Test_score_ser[tmp] = float(line[5:10])
                f.close()
    return Test_score_wer,Test_score_ser

#本脚本主函数
def Main_self():
    Time = input("请输入打分数据所在总文件夹（例：18-10-22_18_25_18）：")
    Itera = input("请输入打分数据所在迭代次数文件夹（例：1）：")
    Get_and_save_the_all_score(Time ,Itera)

if __name__ == '__main__':
    Main_self()
    exit()
