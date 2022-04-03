#!/usr/bin/python

import json
import sqlite3
import os
import re

def gy_paraphrase(t): #12568
    if t['translate_frequency']==1:print('*高义频：* ',end='',file=f)
    if t['translate_frequency']==2:print('*低义频：* ',end='',file=f)
    
    b=t['chinese']
    if b!='':
        while b[0]==' ':
            b=b[1:]
        while b[-1]==' ':
            b=b[:-1]
        print('**' + b + '**  ',file=f)
    
    if t['english']!='':print('英译 '+t['english'],file=f)
    
    if t['antonym']!='':print('反义词 ' + t['antonym']+' ',file=f)
    if t['synonyms']!='':print('近义词 ' + t['synonyms']+'  ',file=f)
    print(file=f)

    if t['gy_example']!=[]:
        for exam in t['gy_example']:
            gy_example(exam)     
    if t['gy_sentential_form']!=[]:
        for exam in t['gy_sentential_form']:
            gy_sentential_form(exam)  
          
    if t['gy_notes']!=[]:
        for exam in t['gy_notes']:
            gy_notes(exam)   
    if t['gy_biscrimination']!=[]:
        for exam in t['gy_biscrimination']:
            gy_biscrimination(exam)  
          
    if t['gy_fixed_collocation']!=[]:
        for exam in t['gy_fixed_collocation']:
            gy_fixed_collocation(exam)             
    
def gy_sentential_form(t): #15924
    print('- '+t['sentential_form'],file=f)
    print(file=f)
    if t['gy_example']!=[]:
        for example in t['gy_example']:
            gy_example(example)
          
    if t['gy_notes']!=[]:
        for exam in t['gy_notes']:
            gy_notes(exam) 
    if t['gy_biscrimination']!=[]:
        for exam in t['gy_biscrimination']:
            gy_biscrimination(exam)              
          
def gy_example(t): #18417
    b=t['highlight']
    english = t["english"]
    if b!='' :
        while b[0]==' ':
            b=b[1:]
        while b[-1]==' ':
            b=b[:-1]
        #print(' > **'+b+'**  ',file=f)     
    if b:
        highlight = b.split(",")
        if highlight:
            #print(english)
            for a in highlight:
                #if a== "abandoned":english = english[:english.find(a)] + "**" + a + "**" + english[len(english[:english.find(a)])+english.find(a)-4:]
                start = english.find(a)
                while start>0 and start+len(a)<len(english) and (((english[start-1]>'a' and english[start-1]<'z') or (english[start-1]>'A' and english[start-1]<'Z')) or ((english[start+len(a)]>'a' and english[start+len(a)]<'z') or (english[start+len(a)]>'A' and english[start+len(a)]<'Z'))):
                    start = english.find(a,start+1)
                english = english[:start] + "**" + a + "**" +english[len(english[:start])+len(a):]
                #print(len(english[:english.find(a)])+len(a)+4)
                #print(english)
                #print("01234567891123456789212345678931234567894123456789512345678961234567897123456789812345678991234567890")
            #exit()
    print(' > '+ english +'  ',file=f)
    if t['source']!='' : print(' > '+t['chinese']+'  （'+t['source']+'）  ',file=f)
    if t['source']=='' : print(' > '+t['chinese']+'  '+t['source']+'  ',file=f)
    if t['sound']!='' : print("<audio src=\"./media/" + t['sound'] + "\" controls=\"controls\"></audio>", file=f)
    print(file=f)
    
def gy_notes(t): #16597
    print('Notes: ' + t['notes']+'  ',file=f)
    if t['gy_example']!=[]:
        for example in t['gy_example']:
            gy_example(example)
    if t['gy_sentential_form']!=[]:
        for form in t['gy_sentential_form']:
            gy_sentential_form(form)
            
def gy_biscrimination(t): #16597
    print('#### 辨析 '+t['words'],file=f)
    print(t['paraphrase']+'  ',file=f)
    if t['gy_example']!=[]:
        for example in t['gy_example']:
            gy_example(example)
    if t["gy_biscrimination_word"]:
        for example in t["gy_biscrimination_word"]:
            print("**"+example["word"]+"**",end=" ",file=f)
            print(example["description"],file=f)
        if example["gy_example"]:
            for i in example["gy_example"]:
                gy_example(i)
    print(file=f)
    
def gy_fixed_collocation(t): #26462
    print('## \#'+t['fixed_word'],file=f)
    if len(t['gy_paraphrase']) >= 1:
        i=1
        for exam in t['gy_paraphrase']:
            print(str(i) + '.',end='',file=f)
            gy_paraphrase(exam) 
            i=i+1
    
def gy_derivative(t): #10112
    print(t['derivative_word']+' '+t['phonogram']+' ' +t['part_of_speech']+' ' +t['use_method']+'  ',file=f)
    #print(file=f) #debug
    if t['gy_example']!=[]:
        for example in t['gy_example']:
            gy_example(example)
    if t['gy_paraphrase']!=[]:
        i=0
        for exam in t['gy_paraphrase']:
            i=i+1
            print( str(i) + '. ',end='',file=f)
            gy_paraphrase(exam) 
    if t['gy_fixed_collocation']!=[]:
        for exam in t['gy_fixed_collocation']:
            gy_fixed_collocation(exam)  
           
def gy_exam_link(exam,case): #10112
    if case=='q':
        if exam['source']!='' : print(exam['subject']+'  （'+exam['source']+'）  ',file=f)
        if exam['source']=='' : print(exam['subject']+'  ',file=f)
        if exam['answer_a']!='' :print('A.'+exam['answer_a']+'  ',file=f)
        if exam['answer_b']!='' :print('B.'+exam['answer_b']+'  ',file=f)
        if exam['answer_c']!='' :print('C.'+exam['answer_c']+'  ',file=f)
        if exam['answer_d']!='' :print('D.'+exam['answer_d']+'  ',file=f)
    if case=='a':
        print(exam['answer'],end='  ',file=f)
    
def chuli(t):
    a=json.loads(t)
    
    #word_info
    b=a['word']
    while b[0]==' ':
        b=b[1:]
    while b[-1]==' ':
        b=b[:-1]
    print('# ***\#' + b + '*** ' + a['part_of_speech'],end='', file = f)
    if a['point']==1 :print('  重难点词汇',end='',file=f)
    print(file=f)
    
    #word_phonetic
    if a['en_phonetic_symbols']!='':print('英音 ' + a['en_phonetic_symbols']+'  ', file=f)
    if a['en_file']!='': print("英音\n<audio src=\"./media/" + a['en_file'] + "\" controls=\"controls\"></audio>\n", file=f)
    if a['usa_phonetic_symbols']!='':print('美音 ' + a['usa_phonetic_symbols']+'  ', file=f)
    if a['usa_file']!='': print("美音\n<audio src=\"./media/" + a['usa_file'] + "\" controls=\"controls\"></audio>\n", file=f)
    print(file=f)
    
    #word_level
    print(file=f)
    if a['lv_frequency']!=0 or a['lv_speak']!=0 or a['lv_write']!=0 or a['lv_read']!=0 : print('|',end='',file=f)
    if a['lv_frequency']!=0 : print(' 词频 ' + str(a['lv_frequency']),end=' |',file=f)
    if a['lv_speak']!=0 : print(' 口语 ' + str(a['lv_speak']),end=' |',file=f)
    if a['lv_write']!=0 : print(' 书面 ' + str(a['lv_write']),end=' |',file=f)
    if a['lv_read']!=0 : print(' 阅读 ' + str(a['lv_read']),end=' |',file=f)
    print('  ',file=f)
    print(file=f)
    
    #word_use_method
    if a['use_method']!='' : 
        print('用法点拨  '+ a['use_method'],file=f)
        print(file=f)
    
    #paraphrase
    if a['gy_paraphrase']!=[]:
        print('英文释义',file=f)
        print('---',file=f)
        i=1
        for exam in a['gy_paraphrase']:
            print('### '+str(i) + '.',end='',file=f)
            gy_paraphrase(exam)    
            i=i+1
        print(file=f)
    
    #fixed_word固定搭配
    if a['gy_fixed_collocation']!=[]:
        print('固定搭配',file=f)
        print('---',file=f) 
        for exam in a['gy_fixed_collocation']:
            gy_fixed_collocation(exam)    
        print(file=f)
       
    #derivative派生词
    if a['gy_derivative']!=[]:
        print('派生词汇',file=f)
        print('---',file=f)
        for exam in a['gy_derivative']:
            gy_derivative(exam)   
        print(file=f)
        
    #exam真题解析
    if a['gy_exam_link']!=[]:
        print('真题解析',file=f)
        print('---',file=f)  
        i=1
        for exam in a['gy_exam_link']:
            print(str(i)+'. ',end='',file=f)
            gy_exam_link(exam,'q')
            i=i+1
        print(file=f)
        i=1
        print('答案：',file=f)
        for exam in a['gy_exam_link']:
            print(str(i)+'. ',end='',file=f)
            gy_exam_link(exam,'a')
            i=i+1            
        print(file=f) 
        print(file=f)
         
# 欢迎文字
print('\n\n')
print('####### 维克多英语词汇导出程序 #######\n')
print('Jellow 看见我请一定一定叫我学习')
print('Creative By ZhiyuShang With Love\n')
print('')

#文件位置
path = input('请输入weici_ext.db文件位置：\n')
if path=='' : path=r'D:\weici_ext.db'
conn = sqlite3.connect(path)
c = conn.cursor()

#保存位置
path_save = input('请输入保存位置：\n')
if path_save=='':path_save = r'D:\weici'
print('注意：文件将存到%s' % path_save)
if not os.path.exists(path_save):
    os.makedirs(path_save)
    
print()
print('输出类型：')
print('1.所有单词按小写字母输出到文件')
print('2.所有单词输出')
print('3.所有词组输出')
print('4.所有词输出')
print('5.所有词独立输出')
print()
ch = input('请输入数字：')
if ch=='':ch='1234'

#Processing
print()
print('请稍后Processing。。。')

#Save
if ch.find('1')!=-1: #按小写字母输出到文件
    i=1
    while i<=26:  
        f = open('%s' % path_save+'\weici_'+chr(ord('A')+i-1)+'.md','w',encoding='utf-8')
        cursor = c.execute("select * from fb_word_detail order by word asc")
        print('%s' % path_save+'\weici_'+chr(ord('A')+i-1)+'.md')
        print('# '+chr(ord('A')+i-1)+chr(ord('a')+i-1),file=f)
        print(file=f)
        for row in cursor:
            if row[6]==0 and row[1][0]==chr(ord('a')+i-1) and row[1].find(' ')==-1:chuli(row[3])
        i=i+1      
        
if ch.find('2')!=-1: #所有单词输出
    f = open('%s' % path_save + '\weici_word_7570.md','w',encoding='utf-8')
    cursor = c.execute("select * from fb_word_detail order by word asc")
    for row in cursor:
        if row[6]==0 and row[1].find(' ')==-1:chuli(row[3])
    print('%s' % path_save + '\weici_word_7570.md')
        
if ch.find('3')!=-1: #所有词组输出
    f = open('%s' % path_save + '\weici_phrase.md','w',encoding='utf-8')
    cursor = c.execute("select * from fb_word_detail order by word asc")
    for row in cursor:
        if row[6]==0 and row[1].find(' ')!=-1:chuli(row[3])
    print('%s' % path_save + '\weici_phrase.md')
        
if ch.find('4')!=-1: #所有词输出
    f = open('%s' % path_save + '\weici_all_10112.md','w',encoding='utf-8')
    cursor = c.execute("select * from fb_word_detail order by word asc")
    for row in cursor:
        if row[6]==0 : chuli(row[3])
    print('%s' % path_save + '\weici_all_10112.md')

if ch.find('5')!=-1: #所有词独立输出
    f_sidebar = open('%s' % path_save + '\\'+'_sidebar.md','w',encoding='utf-8')
    cursor = c.execute("select * from fb_word_detail order by word asc")
    for row in cursor:
        if row[6]==0 : 
            a=json.loads(row[3])
            b=a['word']
            while b[0]==' ':
                b=b[1:]
            while b[-1]==' ':
                b=b[:-1]
            f_sidebar.write(f"[{b}]")
            b=b.replace("/", "")
            b=b.replace("?", "")
            b=b.replace(" ", "_")
            b=b.replace("(", "")
            b=b.replace(")", "")
            f_sidebar.write(f"({b})\n\n")
            f = open('%s' % path_save + '\\'+b+'.md','a',encoding='utf-8')
            chuli(row[3])
            f.close()
        
if ch.find('1')==-1 and ch.find('2')==-1 and ch.find('3')==-1 and ch.find('4')==-1 and ch.find('5')==-1:
    print('输入错误，请重试')

#Finish
print()
#input('按Enter以退出')
