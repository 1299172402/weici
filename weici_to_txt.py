#!/usr/bin/python

import json
import sqlite3
import os

def gy_paraphrase(t): #12568
    if t['translate_frequency']==1:print('高义频：',end='',file=f)
    if t['translate_frequency']==2:print('低义频：',end='',file=f)
    
    if t['chinese']!='':print(t['chinese'],file=f)

    print(file=f)
    
    if t['gy_sentential_form']!=[]:
        for exam in t['gy_sentential_form']:
            gy_sentential_form(exam) 
    if t['gy_example']!=[]:
        for exam in t['gy_example']:
            gy_example(exam)  
       
    if t['gy_fixed_collocation']!=[]:
        for exam in t['gy_fixed_collocation']:
            gy_fixed_collocation(exam)             
    
def gy_sentential_form(t): #15924
    print('- '+t['sentential_form'],file=f)
    print(file=f)
    if t['gy_example']!=[]:
        for example in t['gy_example']:
            gy_example(example)
     
def gy_example(t): #18417
    b=t['highlight']
    if b!='' :
        while b[0]==' ':
            b=b[1:]
        while b[-1]==' ':
            b=b[:-1]
    if b!='' : 
        print('> '+b,file=f)
        print('> '+t['english'],file=f)
        print('> '+t['chinese'],file=f)
        print(file=f)

def gy_fixed_collocation(t): #26462
    if t['fixed_word']!='' :print('- '+t['fixed_word'],file=f)
    if t['gy_paraphrase']!=[]:
        i=1
        for exam in t['gy_paraphrase']:
            print(str(i) + '. ',end='',file=f)
            gy_paraphrase(exam) 
            i=i+1

def chuli(t):
    a=json.loads(t)
    
    #word_info
    print('*' + a['word'] +' '+ a['part_of_speech'],end='', file = f)
    if a['point']==1 :print('  重难点词汇',end='',file=f)
    print(file=f)

    #paraphrase
    if a['gy_paraphrase']!=[]:
        print(file=f)
        i=1
        for exam in a['gy_paraphrase']:
            print(str(i) + '. ',end='',file=f)
            gy_paraphrase(exam)    
            i=i+1
        print(file=f)
    
    #fixed_word固定搭配
    if a['gy_fixed_collocation']!=[]:
        print(file=f)
        #i=1
        for exam in a['gy_fixed_collocation']:
            #print('【搭配'+str(i) + '】',end='',file=f)
            gy_fixed_collocation(exam)    
            #i=i+1
        print(file=f)
   
# 欢迎文字
print('\n\n')
print('####### 维克多英语词汇导出程序 #######\n')
print('Jellow 看见我请一定一定叫我学习')
print('Creative By ZhiyuShang With Love\n')
print('')

#文件位置
path = input('请输入weici_ext.db文件位置：\n')
if path=='' : path=r'C:\Users\Administrator\Desktop\weici_ext.db'
conn = sqlite3.connect(path)
c = conn.cursor()

#保存位置
path_save = input('请输入保存位置：\n')
if path_save=='':path_save = r'C:\Users\Administrator\Desktop\victory'
print('注意：文件将存到%s' % path_save)
if not os.path.exists(path_save):
    os.makedirs(path_save)
    
print()
print('输出类型：')
print('1.所有单词按小写字母输出到文件')
print('2.所有单词输出')
print('3.所有词组输出')
print('4.所有词输出')
print('5.所有单词')
print()
ch = input('请输入数字：')
if ch=='':ch='12345'

#Processing
print()
print('请稍后Processing。。。')

#Save
if ch.find('1')!=-1: #按小写字母输出到文件
    i=1
    while i<=26:  
        f = open('%s' % path_save+'\weici_'+chr(ord('A')+i-1)+'.txt','w',encoding='utf-8')
        cursor = c.execute("select * from fb_word_detail order by word asc")
        print('%s' % path_save+'\weici_'+chr(ord('A')+i-1)+'.txt')
        print('# '+chr(ord('A')+i-1)+chr(ord('a')+i-1),file=f)
        print(file=f)
        for row in cursor:
            if row[6]==0 and row[1][0]==chr(ord('a')+i-1) and row[1].find(' ')==-1:chuli(row[3])
        i=i+1      
        
if ch.find('2')!=-1: #所有单词输出
    f = open('%s' % path_save + '\weici_word_7570.txt','w',encoding='utf-8')
    cursor = c.execute("select * from fb_word_detail order by word asc")
    for row in cursor:
        if row[6]==0 and row[1].find(' ')==-1:chuli(row[3])
    print('%s' % path_save + '\weici_word_7570.txt')
        
if ch.find('3')!=-1: #所有词组输出
    f = open('%s' % path_save + '\weici_phrase_2542.txt','w',encoding='utf-8')
    cursor = c.execute("select * from fb_word_detail order by word asc")
    for row in cursor:
        if row[6]==0 and row[1].find(' ')!=-1:chuli(row[3])
    print('%s' % path_save + '\weici_phrase_2542.txt')
        
if ch.find('4')!=-1: #所有词输出
    f = open('%s' % path_save + '\weici_all_10112.txt','w',encoding='utf-8')
    cursor = c.execute("select * from fb_word_detail order by word asc")
    for row in cursor:
        if row[6]==0 : chuli(row[3])
    print('%s' % path_save + '\weici_all_10112.txt')
    
if ch.find('5')!=-1: #所有词简化输出（仅小写字母开头，不包含空格）
    f = open('%s' % path_save + '\weici_all_lite.txt','w',encoding='utf-8')
    cursor = c.execute("select * from fb_word_detail order by word asc")
    i='A'
    j='a'
    print('#'+i+j,file=f)
    print(file=f)
    for row in cursor:
        if row[6]==0 and row[1][0]>='a' and row[1][0]<='z' and row[1].find(' ')==-1 : 
            if row[1][0]!=j : 
                i=chr(ord(i)+1)
                j=chr(ord(j)+1)
                print('#'+i+j,file=f)
                print(file=f)
            chuli(row[3])
    print('%s' % path_save + '\weici_all_lite.txt')
        
#Finish
print()
input('按Enter以退出')