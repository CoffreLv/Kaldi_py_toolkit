###################################################################
# File Name: build_data_set.py
# Author: CoffreLv
# mail: coffrelv@163.com
# Created Time: 2018年07月30日 星期一 10时03分47秒
#=================================================================
#-*- coding:utf-8 -*
#本文件中包含所有与数据集构建相关的函数

import random
import re
import os
import codecs
import wave

import prepare_dataset


#单语料数据集函数############################################################
#获取整个数据集存入列表all_text并返回
def Get_text_list():
    all_text = []
    with open('../doc/trainall_text.txt', mode = 'r', encoding = 'utf-8') as f_all:
        for alltext in f_all:
            all_text.append(alltext.split(' '))
    return all_text

#从整个数据集分别获取训练集，测试集和验证集三个数据集
def Build_every_dataset(Num_Of_Sentence,Train_scale,Test_scale,Dev_scale):
    All_data_list = Get_text_list()
    Num_of_train_sentence = int(Num_Of_Sentence/10*Train_scale)
    Num_of_test_sentence = int (Num_Of_Sentence/10*Test_scale)
    Num_of_dev_sentence = int (Num_Of_Sentence/10*Dev_scale)

    #构建train数据集
    Train_sentence = []
    Train_count = []
    Train_count = Random_without_same(Num_Of_Sentence, Num_of_train_sentence)
    for j in Train_count:
        Train_sentence.append(All_data_list[j-1])
    for w in Train_sentence:
        All_data_list.remove(w)
    All_text = Train_sentence
    if not os.path.exists('../../data/train'):
        os.mkdir('../../data/train')
    with open('../../data/train/wav.scp', mode = 'w', encoding = 'utf-8') as f_wav:
        for wav_text in All_text:
            f_wav.write(' '.join(wav_text[:2])+'\n')
        f_wav.close()
    with open('../../data/train/text', mode = 'w', encoding = 'utf-8') as f_text:
        for text in All_text:
            f_text.write(text[0]+' '+' '.join(text[3:]))
        f_text.close()
    with open('../../data/train/utt2spk', mode = 'w', encoding = 'utf-8') as f_u2s:
        for u2s_text in All_text:
            f_u2s.write(u2s_text[0]+' '+u2s_text[1][-13:-4]+'\n')
        f_u2s.close()
    Refresh_the_num('train')
    #将text复制为data/local/data/train.text
    os.system("cp ../../data/train/text ../../data/local/data/train.text")

    #构建test数据集
    Test_sentence = []
    Test_count = []
    Test_count = Random_without_same(Num_Of_Sentence-Num_of_train_sentence, Num_of_test_sentence)
    for j in Test_count:
        Test_sentence.append(All_data_list[j-1])
    for w in Test_sentence:
        All_data_list.remove(w)
    All_text = Test_sentence
    if not os.path.exists('../../data/test'):
        os.mkdir('../../data/test')
    with open('../../data/test/wav.scp', mode = 'w', encoding = 'utf-8') as f_wav:
        for wav_text in All_text:
            f_wav.write(' '.join(wav_text[:2])+'\n')
        f_wav.close()
    with open('../../data/test/text', mode = 'w', encoding = 'utf-8') as f_text:
        for text in All_text:
            f_text.write(text[0]+' '+' '.join(text[3:]))
        f_text.close()
    with open('../../data/test/utt2spk', mode = 'w', encoding = 'utf-8') as f_u2s:
        for u2s_text in All_text:
            f_u2s.write(u2s_text[0]+' '+u2s_text[1][-13:-4]+'\n')
        f_u2s.close()
    Refresh_the_num('test')
'''
    #构建dev数据集
    Dev_sentence = []
    Dev_count = []
    Dev_count = Random_without_same(Num_Of_Sentence-Num_of_train_sentence-Num_of_test_sentence,Num_of_dev_sentence)
    for j in Dev_count:
        Dev_sentence.append(All_data_list[j-1])
    for w in Dev_sentence:
        All_data_list.remove(w)
    All_text = Dev_sentence
    if not os.path.exists('../../data/dev'):
        os.mkdir('../../data/dev')
    with open('../../data/dev/wav.scp', mode = 'w', encoding = 'utf-8') as f_wav:
        for wav_text in All_text:
            f_wav.write(' '.join(wav_text[:2])+'\n')
        f_wav.close()
    with open('../../data/dev/text', mode = 'w', encoding = 'utf-8') as f_text:
        for text in All_text:
            f_text.write(text[0]+' '+' '.join(text[3:]))
        f_text.close()
    with open('../../data/dev/utt2spk', mode = 'w', encoding = 'utf-8') as f_u2s:
        for u2s_text in All_text:
            f_u2s.write(u2s_text[0]+' '+u2s_text[1][-13:-4]+'\n')
        f_u2s.close()
    Refresh_the_num('dev')
'''

#生成一个具有num个取值在0-maxnum之间的元素的列表并返回这个列表
def Random_without_same(maxnum, num):
    temp = []
    while maxnum:
        temp.append(maxnum)
        maxnum -= 1
    result = []
    while num:
        tmp = random.choice(temp)
        result.append(tmp)
        temp.remove(tmp)
        num -= 1
    return result

#抽取完数据集后更新重新排序后的编号
def Refresh_the_num(signal):
    Del_num("../../data/"+signal+"/text")
    Add_num("../../data/"+signal+"/text")
    Del_num("../../data/"+signal+"/wav.scp")
    Del_num("../../data/"+signal+"/utt2spk")
    Add_num("../../data/"+signal+"/wav.scp")
    Add_num("../../data/"+signal+"/utt2spk")

#按行删除编号
def Del_num(Filepath):
    charnum = 11
    tmp = []
    f = open(Filepath , mode = 'r' ,encoding = 'utf-8')
    for line in f:
        tmp.append(line[charnum:])
    f.close()
    outf = open(Filepath, mode = 'w' ,encoding = 'utf-8')
    for line in tmp:
        outf.write(line)
    outf.close()

#为每一行添加编号
def Add_num(Filepath):
    f = open(Filepath ,mode = 'r' ,encoding = 'utf-8')
    Head = "voice_"
    tmp = []
    i = 1
    for line in f:
        tmp.append(Head+"%04d"%i+' '+line)
        i += 1
    f.close()
    nf = open(Filepath ,mode = 'w' ,encoding = 'utf-8')
    for line in tmp:
        nf.writelines(line)
        i += 1
    nf.close()

#多语料数据集函数############################################################
#根据（sign）all_text.txt获得（sign）目录下所有text、utt2spk、wav.scp三个文档
def Get_every_text(sign):
    All_text = []
    f_all =  open('../doc/'+sign+'all_text.txt', mode = 'r', encoding = 'utf-8')
    for alltext in f_all:
        if alltext[:3]==codecs.BOM_UTF8:
            alltext = alltext[3:]
        All_text.append(alltext.split(' '))
    if not os.path.exists('../../data/'+sign):
        os.mkdir('../../data/'+sign)
    with open('../../data/'+sign+'/wav.scp', mode = 'w', encoding = 'utf-8') as f_wav:
        for wav_text in All_text:
            f_wav.write(' '.join(wav_text[:2])+'\n')
        f_wav.close()
    with open('../../data/'+sign+'/text', mode = 'w', encoding = 'utf-8') as f_text:
        for text in All_text:
            f_text.write(text[0]+' '+' '.join(text[2:]))
        f_text.close()
    with open('../../data/'+sign+'/utt2spk', mode = 'w', encoding = 'utf-8') as f_u2s:
        for u2s_text in All_text:
            f_u2s.write(u2s_text[0]+' '+u2s_text[1][-13:-4]+'\n')
            #f_u2s.write(u2s_text[0]+' voice'+'\n')
        f_u2s.close()
    #将text复制为data/local/data/train.text
    os.system("cp ../../data/train/text ../../data/local/data/train.text")

#公共函数####################################################################
#测试数据集中音频文件格式是否复合Kaldi所需格式
def Get_and_test_the_wav_params(Wav_path):
    filenames = os.listdir(Wav_path)
    for filename in filenames:
        filepath = Wav_path+filename
        if filename.endswith('.WAV'):
            f = wave.open(filepath,'rb')
            params = f.getparams()
            nchannels, sampwidth, framerate, nframes = params[:4]
            if not nchannels == 1:
                print('ERROR:The wavefile'+filepath+'nchannels not 1!')
                exit()
            if not framerate == 16000:
                print('ERROR:The wavefile'+filepath+'framerate not 16000!')
                exit()
        if filename.endswith('.wav'):
            f = wave.open(filepath,'rb')
            params = f.getparams()
            nchannels, sampwidth, framerate, nframes = params[:4]
            if not nchannels == 1:
                print('ERROR:The wavefile'+filepath+'nchannels not 1!')
                exit()
            if not framerate == 16000:
                print('ERROR:The wavefile'+filepath+'framerate not 16000!')
                exit()
    return nchannels,framerate
#############################################################################

def Main_self():
    Choice = int(input("请选择单（1）或多（0）语料集："))
    if Choice == 1:
        Num_Of_Sentence = int(input("请输入语聊句子数目："))
        Train_scale = int(input("请输入训练集所占比例（0-10）："))
        Test_scale = int(input("请输入测试集所占比例（0-10）："))
        Build_every_dataset(Num_Of_Sentence, Train_scale, Test_scale, 10-Train_scale-Test_scale)
    elif Choice == 0:
        Get_every_text('train')
        Get_every_text('test')
        #Get_every_text('dev')
    else:
        print("ERROR:选择错误请重新运行！")

if __name__ == '__main__':
    Main_self()
    exit()
