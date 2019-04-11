#!/usr/bin/env python
import plotly.offline as pltoff
import plotly.graph_objs as go
import time
import os

import count_decode_score

def Train_data_gender_division(Time, Itera):
    male = 0
    famale = 0
    f = open('../log/'+Time+'/'+str(Itera)+'/data/train/utt2spk')
    for line in f:
        if line[-8:-7] == 'W':
            famale += 1
        if line[-8:-7] == 'M':
            male += 1
    f.close()
    values = [male,famale]
    labels = ['男','女']

    trace = go.Pie(labels = labels, values = values,
                   hoverinfo = 'label+percent', textinfo = 'value',
                   textfont = dict(size=20),
                   marker = dict(line = dict(color = '#000000', width = 3)))

    pltoff.plot([trace], filename='../log/'+Time+'/'+str(Itera)+'/训练集性别分布图.html')

def Test_data_gender_division(Time, Itera):
    male = 0
    famale = 0
    f = open('../log/'+Time+'/'+str(Itera)+'/data/test/utt2spk')
    for line in f:
        if line[-8:-7] == 'W':
            famale += 1
        if line[-8:-7] == 'M':
            male += 1
    f.close()
    values = [male,famale]
    labels = ['男','女']

    trace = go.Pie(labels = labels, values = values,
                   hoverinfo = 'label+percent', textinfo = 'value',
                   textfont = dict(size=20),
                   marker = dict(line = dict(color = '#000000', width = 3)))

    pltoff.plot([trace], filename='../log/'+Time+'/'+str(Itera)+'/测试集性别分布图.html')

def Train_data_age_division(Time, Itera):
    age_0 = 0
    age_1 = 0
    age_2 = 0
    age_3 = 0
    age_4 = 0
    age_5 = 0
    age_6 = 0
    age_7 = 0
    age_8 = 0
    age_9 = 0
    f = open('../log/'+Time+'/'+str(Itera)+'/data/train/utt2spk')
    for line in f:
        age = int(line[-6:-4])
        if 0 <= age < 10:
            age_1 += 1
        elif 10 <= age <20:
            age_2 += 1
        elif 20 <= age <30:
            age_3 += 1
        elif 30 <= age <40:
            age_4 += 1
        elif 40 <= age <50:
            age_5 += 1
        elif 50 <= age <60:
            age_6 += 1
        elif 60 <= age <70:
            age_7 += 1
        elif 70 <= age <80:
            age_8 += 1
        elif 80 <= age <90:
            age_9 += 1
        elif 90 <= age <100:
            age_0 += 1
        else:
            print("ERROR: 年龄超出范围！")
            exit()
    f.close()
    values = [age_1,age_2,age_3,age_4,age_5,age_6,age_7,age_8,age_9,age_0]
    labels = ['0-10','10-20','20-30','30-40','40-50','50-60','60-70','70-80','80-90','90-100']

    trace = go.Pie(labels = labels, values = values,
                   hoverinfo = 'label+percent', textinfo = 'value',
                   textfont = dict(size=20),
                   marker = dict(line = dict(color = '#000000', width = 3)))

    pltoff.plot([trace], filename='../log/'+Time+'/'+str(Itera)+'/训练集年龄分布图.html')

def Test_data_age_division(Time ,Itera):
    age_0 = 0
    age_1 = 0
    age_2 = 0
    age_3 = 0
    age_4 = 0
    age_5 = 0
    age_6 = 0
    age_7 = 0
    age_8 = 0
    age_9 = 0
    f = open('../log/'+Time+'/'+str(Itera)+'/data/train/utt2spk')
    for line in f:
        age = int(line[-6:-4])
        if 0 <= age < 10:
            age_1 += 1
        elif 10 <= age <20:
            age_2 += 1
        elif 20 <= age <30:
            age_3 += 1
        elif 30 <= age <40:
            age_4 += 1
        elif 40 <= age <50:
            age_5 += 1
        elif 50 <= age <60:
            age_6 += 1
        elif 60 <= age <70:
            age_7 += 1
        elif 70 <= age <80:
            age_8 += 1
        elif 80 <= age <90:
            age_9 += 1
        elif 90 <= age <100:
            age_0 += 1
        else:
            print("ERROR: 年龄超出范围！")
            exit()
    f.close()
    values = [age_1,age_2,age_3,age_4,age_5,age_6,age_7,age_8,age_9,age_0]
    labels = ['0-10','10-20','20-30','30-40','40-50','50-60','60-70','70-80','80-90','90-100']

    trace = go.Pie(labels = labels, values = values,
                   hoverinfo = 'label+percent', textinfo = 'value',
                   textfont = dict(size=20),
                   marker = dict(line = dict(color = '#000000', width = 3)))

    pltoff.plot([trace], filename='../log/'+Time+'/'+str(Itera)+'/测试集年龄分布图.html')

def Train_data_regional_division(Time, Itera):
    regional_A = 0
    regional_B = 0
    regional_C = 0
    regional_D = 0
    regional_E = 0
    regional_F = 0
    regional_G = 0
    regional_H = 0
    regional_J = 0
    regional_K = 0
    regional_L = 0
    regional_M = 0
    f = open('../log/'+Time+'/'+str(Itera)+'/data/train/utt2spk')
    for line in f:
        regional = line[-10:-9]
        if regional == 'A':
            regional_A += 1
        elif regional == 'B':
            regional_B += 1
        elif regional == 'C':
            regional_C += 1
        elif regional == 'D':
            regional_D += 1
        elif regional == 'E':
            regional_E += 1
        elif regional == 'F':
            regional_F += 1
        elif regional == 'G':
            regional_G += 1
        elif regional == 'H':
            regional_H += 1
        elif regional == 'J':
            regional_J += 1
        elif regional == 'K':
            regional_K += 1
        elif regional == 'L':
            regional_L += 1
        elif regional == 'M':
            regional_M += 1
        else:
            print("ERROR: 无此地区"+regional)
            exit()
    f.close()
    values = [regional_A,regional_B,regional_C,regional_D,regional_E,regional_F,regional_G,regional_H,regional_J,regional_K,regional_L,regional_M]
    labels = ['呼和浩特市','包头市','乌海市','赤峰市','呼伦贝尔市','兴安盟','通辽市','锡林郭勒盟','乌兰察布市','鄂尔多斯市','巴彦淖尔市','阿拉善盟']

    trace = go.Pie(labels = labels, values = values,
                   hoverinfo = 'label+percent', textinfo = 'value',
                   textfont = dict(size=20),
                   marker = dict(line = dict(color = '#000000', width = 3)))

    pltoff.plot([trace], filename='../log/'+Time+'/'+str(Itera)+'/训练集地区分布图.html')

def Test_data_regional_division(Time, Itera):
    regional_A = 0
    regional_B = 0
    regional_C = 0
    regional_D = 0
    regional_E = 0
    regional_F = 0
    regional_G = 0
    regional_H = 0
    regional_J = 0
    regional_K = 0
    regional_L = 0
    regional_M = 0
    f = open('../log/'+Time+'/'+str(Itera)+'/data/test/utt2spk')
    for line in f:
        regional = line[-10:-9]
        if regional == 'A':
            regional_A += 1
        elif regional == 'B':
            regional_B += 1
        elif regional == 'C':
            regional_C += 1
        elif regional == 'D':
            regional_D += 1
        elif regional == 'E':
            regional_E += 1
        elif regional == 'F':
            regional_F += 1
        elif regional == 'G':
            regional_G += 1
        elif regional == 'H':
            regional_H += 1
        elif regional == 'J':
            regional_J += 1
        elif regional == 'K':
            regional_K += 1
        elif regional == 'L':
            regional_L += 1
        elif regional == 'M':
            regional_M += 1
        else:
            print("ERROR: 无此地区"+regional)
            exit()
    f.close()
    values = [regional_A,regional_B,regional_C,regional_D,regional_E,regional_F,regional_G,regional_H,regional_J,regional_K,regional_L,regional_M]
    labels = ['呼和浩特市','包头市','乌海市','赤峰市','呼伦贝尔市','兴安盟','通辽市','锡林郭勒盟','乌兰察布市','鄂尔多斯市','巴彦淖尔市','阿拉善盟']

    trace = go.Pie(labels = labels, values = values,
                   hoverinfo = 'label+percent', textinfo = 'value',
                   textfont = dict(size=20),
                   marker = dict(line = dict(color = '#000000', width = 3)))

    pltoff.plot([trace], filename='../log/'+Time+'/'+str(Itera)+'/测试集地区分布图.html')

def Train_data_mono_WER_score_line(Time, Itera, score_dict):
    name = '../log/'+Time+'/'+str(Itera)+'/Line_train_WER_mono.html'
    dataset = {
        'Train_WER_mono' : [],
        'wer' : []
    }
    for key in score_dict:
        if key=='Train_Wer_mono':
            tmp = sorted(score_dict[key])
            for wer in tmp:
                dataset['Train_WER_mono'].append(score_dict[key][wer])
                dataset['wer'].append(wer)

    data_g = []
    # 构建数据关系，折线图
    Train_WER_mono = go.Scatter(
        x = dataset['wer'],
        y = dataset['Train_WER_mono'],
        name = 'Train_WER_mono')
    data_g.append(Train_WER_mono)

  # 设置图表布局
    layout = go.Layout(title="Line train WER mono",
        xaxis={'title':'wer(%)'}, yaxis={'title':'Train_WER_mono'})
    fig = go.Figure(data=data_g, layout=layout)
  # 生成离线html
    pltoff.plot(fig, filename=name)

def Train_data_mono_SER_score_line(Time, Itera, score_dict):
    name = '../log/'+Time+'/'+str(Itera)+'/Line_train_SER_mono.html'
    dataset = {
        'Train_SER_mono' : [],
        'wer' : []
    }
    for key in score_dict:
        if key=='Train_Ser_mono':
            tmp = sorted(score_dict[key])
            for wer in tmp:
                dataset['Train_SER_mono'].append(score_dict[key][wer])
                dataset['wer'].append(wer)

    data_g = []
    # 构建数据关系，折线图
    Train_SER_mono = go.Scatter(
        x = dataset['wer'],
        y = dataset['Train_SER_mono'],
        name = 'Train_SER_mono')
    data_g.append(Train_SER_mono)

  # 设置图表布局
    layout = go.Layout(title="Line train SER mono",
        xaxis={'title':'wer(%)'}, yaxis={'title':'Train_SER_mono'})
    fig = go.Figure(data=data_g, layout=layout)
  # 生成离线html
    pltoff.plot(fig, filename=name)

def Test_data_mono_WER_score_line(Time, Itera, score_dict):
    name = '../log/'+Time+'/'+str(Itera)+'/Line_test_WER_mono.html'
    dataset = {
        'Test_WER_mono' : [],
        'wer' : []
    }
    for key in score_dict:
        if key=='Test_Wer_mono':
            tmp = sorted(score_dict[key])
            for wer in tmp:
                dataset['Test_WER_mono'].append(score_dict[key][wer])
                dataset['wer'].append(wer)

    data_g = []
    # 构建数据关系，折线图
    Test_WER_mono = go.Scatter(
        x = dataset['wer'],
        y = dataset['Test_WER_mono'],
        name = 'Test_WER_mono')
    data_g.append(Test_WER_mono)

  # 设置图表布局
    layout = go.Layout(title="Line test WER mono",
        xaxis={'title':'wer(%)'}, yaxis={'title':'Test_WER_mono'})
    fig = go.Figure(data=data_g, layout=layout)
  # 生成离线html
    pltoff.plot(fig, filename=name)

def Test_data_mono_SER_score_line(Time, Itera, score_dict):
    name = '../log/'+Time+'/'+str(Itera)+'/Line_test_SER_mono.html'
    dataset = {
        'Test_SER_mono' : [],
        'wer' : []
    }
    for key in score_dict:
        if key=='Test_Ser_mono':
            tmp = sorted(score_dict[key])
            for wer in tmp:
                dataset['Test_SER_mono'].append(score_dict[key][wer])
                dataset['wer'].append(wer)

    data_g = []
    # 构建数据关系，折线图
    Test_SER_mono = go.Scatter(
        x = dataset['wer'],
        y = dataset['Test_SER_mono'],
        name = 'Test_SER_mono')
    data_g.append(Test_SER_mono)

  # 设置图表布局
    layout = go.Layout(title="Line test SER mono",
        xaxis={'title':'wer(%)'}, yaxis={'title':'Test_SER_mono'})
    fig = go.Figure(data=data_g, layout=layout)
  # 生成离线html
    pltoff.plot(fig, filename=name)

def Train_data_tri_WER_score_line(Time, Itera, score_dict):
    name = '../log/'+Time+'/'+str(Itera)+'/Line_train_WER_tri.html'
    dataset = {
        'Train_WER_tri' : [],
        'wer' : []
    }
    for key in score_dict:
        if key=='Train_Wer_tri':
            tmp = sorted(score_dict[key])
            for wer in tmp:
                dataset['Train_WER_tri'].append(score_dict[key][wer])
                dataset['wer'].append(wer)

    data_g = []
    # 构建数据关系，折线图
    Train_WER_tri = go.Scatter(
        x = dataset['wer'],
        y = dataset['Train_WER_tri'],
        name = 'Train_WER_tri')
    data_g.append(Train_WER_tri)

  # 设置图表布局
    layout = go.Layout(title="Line train WER tri",
        xaxis={'title':'wer(%)'}, yaxis={'title':'Train_WER_tri'})
    fig = go.Figure(data=data_g, layout=layout)
  # 生成离线html
    pltoff.plot(fig, filename=name)

def Train_data_tri_SER_score_line(Time, Itera, score_dict):
    name = '../log/'+Time+'/'+str(Itera)+'/Line_train_SER_tri.html'
    dataset = {
        'Train_SER_tri' : [],
        'wer' : []
    }
    for key in score_dict:
        if key=='Train_Ser_tri':
            tmp = sorted(score_dict[key])
            for wer in tmp:
                dataset['Train_SER_tri'].append(score_dict[key][wer])
                dataset['wer'].append(wer)

    data_g = []
    # 构建数据关系，折线图
    Train_SER_tri = go.Scatter(
        x = dataset['wer'],
        y = dataset['Train_SER_tri'],
        name = 'Train_SER_tri')
    data_g.append(Train_SER_tri)

  # 设置图表布局
    layout = go.Layout(title="Line train SER tri",
        xaxis={'title':'wer(%)'}, yaxis={'title':'Train_SER_tri'})
    fig = go.Figure(data=data_g, layout=layout)
  # 生成离线html
    pltoff.plot(fig, filename=name)

def Test_data_tri_WER_score_line(Time, Itera, score_dict):
    name = '../log/'+Time+'/'+str(Itera)+'/Line_test_WER_tri.html'
    dataset = {
        'Test_WER_tri' : [],
        'wer' : []
    }
    for key in score_dict:
        if key=='Test_Wer_tri':
            tmp = sorted(score_dict[key])
            for wer in tmp:
                dataset['Test_WER_tri'].append(score_dict[key][wer])
                dataset['wer'].append(wer)

    data_g = []
    # 构建数据关系，折线图
    Test_WER_tri = go.Scatter(
        x = dataset['wer'],
        y = dataset['Test_WER_tri'],
        name = 'Test_WER_tri')
    data_g.append(Test_WER_tri)

  # 设置图表布局
    layout = go.Layout(title="Line test WER tri",
        xaxis={'title':'wer(%)'}, yaxis={'title':'Test_WER_tri'})
    fig = go.Figure(data=data_g, layout=layout)
  # 生成离线html
    pltoff.plot(fig, filename=name)

def Test_data_tri_SER_score_line(Time, Itera, score_dict):
    name = '../log/'+Time+'/'+str(Itera)+'/Line_test_SER_tri.html'
    dataset = {
        'Test_SER_tri' : [],
        'wer' : []
    }
    for key in score_dict:
        if key=='Test_Ser_tri':
            tmp = sorted(score_dict[key])
            for wer in tmp:
                dataset['Test_SER_tri'].append(score_dict[key][wer])
                dataset['wer'].append(wer)

    data_g = []
    # 构建数据关系，折线图
    Test_SER_tri = go.Scatter(
        x = dataset['wer'],
        y = dataset['Test_SER_tri'],
        name = 'Test_SER_tri')
    data_g.append(Test_SER_tri)

  # 设置图表布局
    layout = go.Layout(title="Line test SER tri",
        xaxis={'title':'wer(%)'}, yaxis={'title':'Test_SER_tri'})
    fig = go.Figure(data=data_g, layout=layout)
  # 生成离线html
    pltoff.plot(fig, filename=name)

def Iteration_train_score_WER_mono_line(Time):
    name = '../log/'+Time+'/Line_iteration_train_WER_mono.html'
    Score_list = {}
    Itera_file_list = os.listdir('../log/'+Time)
    for filename in Itera_file_list:
        if not filename.endswith('.html'):
            Score_dict = count_decode_score.Get_the_all_score_from_file(Time, filename)
            for key in Score_dict:
                if key=='Train_Wer_mono':
                    tmp = min(Score_dict[key], key = Score_dict[key].get)
                    Score_list[filename] = Score_dict[key][tmp]
    dataset = {
        'Train_WER_mono' : [],
        'Iteration' : []
    }
    tmp = sorted(Score_list)
    for Itera in tmp:
        dataset['Train_WER_mono'].append(Score_list[Itera])
        dataset['Iteration'].append(Itera)
    data_g = []
    # 构建数据关系，折线图
    Train_WER_mono = go.Scatter(
        x = dataset['Iteration'],
        y = dataset['Train_WER_mono'],
        name = 'Train_WER_mono')
    data_g.append(Train_WER_mono)
  # 设置图表布局
    layout = go.Layout(title="Line iteration train WER mono",
        xaxis={'title':'Iteration'}, yaxis={'title':'Train_WER_mono'})
    fig = go.Figure(data=data_g, layout=layout)
  # 生成离线html
    pltoff.plot(fig, filename=name)

def Iteration_train_score_SER_mono_line(Time):
    name = '../log/'+Time+'/Line_iteration_train_SER_mono.html'
    Score_list = {}
    Itera_file_list = os.listdir('../log/'+Time)
    for filename in Itera_file_list:
        if not filename.endswith('.html'):
            Score_dict = count_decode_score.Get_the_all_score_from_file(Time, filename)
            for key in Score_dict:
                if key=='Train_Ser_mono':
                    tmp = min(Score_dict[key], key = Score_dict[key].get)
                    Score_list[filename] = Score_dict[key][tmp]
    dataset = {
        'Train_SER_mono' : [],
        'Iteration' : []
    }
    tmp = sorted(Score_list)
    for Itera in tmp:
        dataset['Train_SER_mono'].append(Score_list[Itera])
        dataset['Iteration'].append(Itera)
    data_g = []
    # 构建数据关系，折线图
    Train_SER_mono = go.Scatter(
        x = dataset['Iteration'],
        y = dataset['Train_SER_mono'],
        name = 'Train_SER_mono')
    data_g.append(Train_SER_mono)
  # 设置图表布局
    layout = go.Layout(title="Line iteration train SER mono",
        xaxis={'title':'Iteration'}, yaxis={'title':'Train_SER_mono'})
    fig = go.Figure(data=data_g, layout=layout)
  # 生成离线html
    pltoff.plot(fig, filename=name)

def Iteration_train_score_WER_tri_line(Time):
    name = '../log/'+Time+'/Line_iteration_train_WER_tri.html'
    Score_list = {}
    Itera_file_list = os.listdir('../log/'+Time)
    for filename in Itera_file_list:
        if not filename.endswith('.html'):
            Score_dict = count_decode_score.Get_the_all_score_from_file(Time, filename)
            for key in Score_dict:
                if key=='Train_Wer_tri':
                    tmp = min(Score_dict[key], key = Score_dict[key].get)
                    Score_list[filename] = Score_dict[key][tmp]
    dataset = {
        'Train_WER_tri' : [],
        'Iteration' : []
    }
    tmp = sorted(Score_list)
    for Itera in tmp:
        dataset['Train_WER_tri'].append(Score_list[Itera])
        dataset['Iteration'].append(Itera)
    data_g = []
    # 构建数据关系，折线图
    Train_WER_tri = go.Scatter(
        x = dataset['Iteration'],
        y = dataset['Train_WER_tri'],
        name = 'Train_WER_tri')
    data_g.append(Train_WER_tri)
  # 设置图表布局
    layout = go.Layout(title="Line iteration train WER tri",
        xaxis={'title':'Iteration'}, yaxis={'title':'Train_WER_tri'})
    fig = go.Figure(data=data_g, layout=layout)
  # 生成离线html
    pltoff.plot(fig, filename=name)

def Iteration_train_score_SER_tri_line(Time):
    name = '../log/'+Time+'/Line_iteration_train_SER_tri.html'
    Score_list = {}
    Itera_file_list = os.listdir('../log/'+Time)
    for filename in Itera_file_list:
        if not filename.endswith('.html'):
            Score_dict = count_decode_score.Get_the_all_score_from_file(Time, filename)
            for key in Score_dict:
                if key=='Train_Ser_tri':
                    tmp = min(Score_dict[key], key = Score_dict[key].get)
                    Score_list[filename] = Score_dict[key][tmp]
    dataset = {
        'Train_SER_tri' : [],
        'Iteration' : []
    }
    tmp = sorted(Score_list)
    for Itera in tmp:
        dataset['Train_SER_tri'].append(Score_list[Itera])
        dataset['Iteration'].append(Itera)
    data_g = []
    # 构建数据关系，折线图
    Train_SER_tri = go.Scatter(
        x = dataset['Iteration'],
        y = dataset['Train_SER_tri'],
        name = 'Train_SER_tri')
    data_g.append(Train_SER_tri)
  # 设置图表布局
    layout = go.Layout(title="Line iteration train SER tri",
        xaxis={'title':'Iteration'}, yaxis={'title':'Train_SER_tri'})
    fig = go.Figure(data=data_g, layout=layout)
  # 生成离线html
    pltoff.plot(fig, filename=name)

def Iteration_test_score_WER_mono_line(Time):
    name = '../log/'+Time+'/Line_iteration_test_WER_mono.html'
    Score_list = {}
    Itera_file_list = os.listdir('../log/'+Time)
    for filename in Itera_file_list:
        if not filename.endswith('.html'):
            Score_dict = count_decode_score.Get_the_all_score_from_file(Time, filename)
            for key in Score_dict:
                if key=='Test_Wer_mono':
                    tmp = min(Score_dict[key], key = Score_dict[key].get)
                    Score_list[filename] = Score_dict[key][tmp]
    dataset = {
        'Test_WER_mono' : [],
        'Iteration' : []
    }
    tmp = sorted(Score_list)
    for Itera in tmp:
        dataset['Test_WER_mono'].append(Score_list[Itera])
        dataset['Iteration'].append(Itera)
    data_g = []
    # 构建数据关系，折线图
    Test_WER_mono = go.Scatter(
        x = dataset['Iteration'],
        y = dataset['Test_WER_mono'],
        name = 'Test_WER_mono')
    data_g.append(Test_WER_mono)
  # 设置图表布局
    layout = go.Layout(title="Line iteration test WER mono",
        xaxis={'title':'Iteration'}, yaxis={'title':'Test_WER_mono'})
    fig = go.Figure(data=data_g, layout=layout)
  # 生成离线html
    pltoff.plot(fig, filename=name)

def Iteration_test_score_SER_mono_line(Time):
    name = '../log/'+Time+'/Line_iteration_test_SER_mono.html'
    Score_list = {}
    Itera_file_list = os.listdir('../log/'+Time)
    for filename in Itera_file_list:
        if not filename.endswith('.html'):
            Score_dict = count_decode_score.Get_the_all_score_from_file(Time, filename)
            for key in Score_dict:
                if key=='Test_Ser_mono':
                    tmp = min(Score_dict[key], key = Score_dict[key].get)
                    Score_list[filename] = Score_dict[key][tmp]
    dataset = {
        'Test_SER_mono' : [],
        'Iteration' : []
    }
    tmp = sorted(Score_list)
    for Itera in tmp:
        dataset['Test_SER_mono'].append(Score_list[Itera])
        dataset['Iteration'].append(Itera)
    data_g = []
    # 构建数据关系，折线图
    Test_SER_mono = go.Scatter(
        x = dataset['Iteration'],
        y = dataset['Test_SER_mono'],
        name = 'Test_SER_mono')
    data_g.append(Test_SER_mono)
  # 设置图表布局
    layout = go.Layout(title="Line iteration test SER mono",
        xaxis={'title':'Iteration'}, yaxis={'title':'Test_SER_mono'})
    fig = go.Figure(data=data_g, layout=layout)
  # 生成离线html
    pltoff.plot(fig, filename=name)

def Iteration_test_score_WER_tri_line(Time):
    name = '../log/'+Time+'/Line_iteration_test_WER_tri.html'
    Score_list = {}
    Itera_file_list = os.listdir('../log/'+Time)
    for filename in Itera_file_list:
        if not filename.endswith('.html'):
            Score_dict = count_decode_score.Get_the_all_score_from_file(Time, filename)
            for key in Score_dict:
                if key=='Test_Wer_tri':
                    tmp = min(Score_dict[key], key = Score_dict[key].get)
                    Score_list[filename] = Score_dict[key][tmp]
    dataset = {
        'Test_WER_tri' : [],
        'Iteration' : []
    }
    tmp = sorted(Score_list)
    for Itera in tmp:
        dataset['Test_WER_tri'].append(Score_list[Itera])
        dataset['Iteration'].append(Itera)
    data_g = []
    # 构建数据关系，折线图
    Test_WER_tri = go.Scatter(
        x = dataset['Iteration'],
        y = dataset['Test_WER_tri'],
        name = 'Test_WER_tri')
    data_g.append(Test_WER_tri)
  # 设置图表布局
    layout = go.Layout(title="Line iteration test WER tri",
        xaxis={'title':'Iteration'}, yaxis={'title':'Test_WER_tri'})
    fig = go.Figure(data=data_g, layout=layout)
  # 生成离线html
    pltoff.plot(fig, filename=name)

def Iteration_test_score_SER_tri_line(Time):
    name = '../log/'+Time+'/Line_iteration_test_SER_tri.html'
    Score_list = {}
    Itera_file_list = os.listdir('../log/'+Time)
    for filename in Itera_file_list:
        if not filename.endswith('.html'):
            Score_dict = count_decode_score.Get_the_all_score_from_file(Time, filename)
            for key in Score_dict:
                if key=='Test_Ser_tri':
                    tmp = min(Score_dict[key], key = Score_dict[key].get)
                    Score_list[filename] = Score_dict[key][tmp]
    dataset = {
        'Test_SER_tri' : [],
        'Iteration' : []
    }
    tmp = sorted(Score_list)
    for Itera in tmp:
        dataset['Test_SER_tri'].append(Score_list[Itera])
        dataset['Iteration'].append(Itera)
    data_g = []
    # 构建数据关系，折线图
    Test_SER_tri = go.Scatter(
        x = dataset['Iteration'],
        y = dataset['Test_SER_tri'],
        name = 'Test_SER_tri')
    data_g.append(Test_SER_tri)
  # 设置图表布局
    layout = go.Layout(title="Line iteration test SER tri",
        xaxis={'title':'Iteration'}, yaxis={'title':'Test_SER_tri'})
    fig = go.Figure(data=data_g, layout=layout)
  # 生成离线html
    pltoff.plot(fig, filename=name)

def Get_the_Itera_chart(Time,Itera):
    Score_dict = count_decode_score.Get_the_all_score_from_file(Time,Itera)
    Train_data_mono_WER_score_line(Time, Itera, Score_dict)
    Train_data_mono_SER_score_line(Time, Itera, Score_dict)
    Train_data_tri_WER_score_line(Time, Itera, Score_dict)
    Train_data_tri_SER_score_line(Time, Itera, Score_dict)
    Test_data_mono_WER_score_line(Time, Itera, Score_dict)
    Test_data_mono_SER_score_line(Time, Itera, Score_dict)
    Test_data_tri_WER_score_line(Time, Itera, Score_dict)
    Test_data_tri_SER_score_line(Time , Itera, Score_dict)
    Train_data_gender_division(Time,Itera)
    Train_data_age_division(Time,Itera)
    Train_data_regional_division(Time,Itera)
    Test_data_gender_division(Time,Itera)
    Test_data_age_division(Time,Itera)
    Test_data_regional_division(Time,Itera)
    time.sleep(3)

def Get_the_Iterations_chart(Time):
    Iteration_train_score_WER_mono_line(Time)
    Iteration_train_score_SER_mono_line(Time)
    Iteration_train_score_WER_tri_line(Time)
    Iteration_train_score_SER_tri_line(Time)
    Iteration_test_score_WER_mono_line(Time)
    Iteration_test_score_SER_mono_line(Time)
    Iteration_test_score_WER_tri_line(Time)
    Iteration_test_score_SER_tri_line(Time)
    time.sleep(3)

def Main_self():
    while 1:
        Choice = int(input("请选择操作(1:单轮训练图表)(2:多轮训练图标)(0:退出):"))
        if Choice == 1:
            Time = input("请输入打分数据所在总文件夹（例：18-10-22_18_25_18）：")
            Itera = input("请输入打分数据所在迭代次数文件夹（例：1）：")
            Get_the_Itera_chart(Time,Itera)
        elif Choice == 2:
            Time = input("请输入打分数据所在总文件夹（例：18-10-22_18_25_18）：")
            Get_the_Iterations_chart(Time)
        elif Choice == 0:
            break
        else:
            print("ERROR: 输入错误，请重新输入！")
            continue

if __name__=='__main__':
    Main_self()
    exit()

