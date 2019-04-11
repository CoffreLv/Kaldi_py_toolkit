###################################################################
# File Name: prepare_dataset.py
# Author: CoffreLv
# mail: coffrelv@163.com
# Created Time: 2018年07月30日 星期一 10时45分11秒
#=================================================================
#-*- coding:utf-8 -*

import sys
import os
import re
import shutil
import codecs

import read_config

#将所有训练所需语料相关数据收集并存储至doc/*_all_text.txt
def Get_all_text_data(Sign,iteration):
    Wav_path = read_config.Read_config('../doc/config.cfg', 'section'+str(iteration), Sign+'_wav_path')
    f = open('../doc/'+Sign+'all_text.txt' , mode = 'w' , encoding = 'utf-8')
    Filenamelist = []
    for parent, dirname , filenames in os.walk(Wav_path, topdown = True):
        for filename in filenames:
            if not filename.endswith('.wav'):
                continue
            else:
                file_path = os.path.join(parent, filename)
                Filenamelist.append(file_path)
        Filenamelist.sort()
        num = 1
        for i in Filenamelist:
            f_txt = open(i[:-4]+'.txt', mode = 'r', encoding = 'utf-8')
            wav_txt = f_txt.readline()
            wav_txt = re.sub('[a-zA-Z]','',wav_txt)
            wav_txt = wav_txt.strip()
            #wav_txt = re.sub("[\xE2\x8D]",'\x18\x24',wav_txt)
            #f.write("voice_%1d%1d%1d%1d"%(num%10000/1000,num%1000/100,num%100/10,num%10)+' '+i+' '+wav_txt+"\n")
            f.write(i[-13:-4]+'_'+i[-22:-14]+' '+i+' '+wav_txt+"\n")
            num += 1
    f.close()

#准备数据字典相关文档
def Prepare_dict():
    tmp = []
    phones = []
    f = open("../../data/local/dict/lexicon.txt", mode = 'r', encoding = 'utf-8')
    for line in f:
        line = re.sub('\n','',line)
        if line.startswith('sil'):
            continue
        temp = []
        temp = line.split()
        temp.pop(0)
        for w in temp:
            tmp.append(w)
    for w in tmp:
        if not w in phones:
            phones.append(w)
    extra_f = open("../../data/local/dict/extra_questions.txt", mode = 'w', encoding = 'utf-8')
    non_f = open("../../data/local/dict/nonsilence_phones.txt", mode = 'w', encoding = 'utf-8')
    sil_f = open("../../data/local/dict/silence_phones.txt", mode = 'w', encoding = 'utf-8')
    op_f = open("../../data/local/dict/optional_silence.txt", mode = 'w', encoding = 'utf-8')
    op_f.write('sil')
    sil_f.write('sil\n')
    extra_f.write('sil\n')
    for w in phones:
        extra_f.write(w+' ')
        non_f.write(w+'\n')
    extra_f.write('\n')
    print("The dict is prepared.\n")
    f.close()
    extra_f.close()
    non_f.close()
    sil_f.close()
    op_f.close()

#本脚本主函数
def Main_self(Train_signal,Test_signal):
    Prepare_dict()
    iteration = int(input("请输入迭代轮数："))
    Get_all_text_data(Train_signal,iteration)
    Get_all_text_data(Test_signal,iteration)

if __name__ == '__main__':
    Train_signal = 'train'
    Test_signal = 'test'
    Main_self(Train_signal, Test_signal)
    exit()
