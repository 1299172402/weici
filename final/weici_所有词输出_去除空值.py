#!/usr/bin/python

#所有词组输出到文件

import json
import sqlite3
import os

# "gy_biscrimination_word"
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
    if t['english']!='':print(t['english'],file=f)
    if t['antonym']!='':print('反义词 ' + t['antonym']+' ',end='',file=f)
    if t['synonyms']!='':print('近义词 ' + t['synonyms']+'  ',end='',file=f)
    print(file=f)
    print(file=f)
    if t['gy_sentential_form']!=[]:
        #i=1
        for exam in t['gy_sentential_form']:
            #print('==句型'+str(i),file=f)
            gy_sentential_form(exam) 
            #=i+1
    if t['gy_example']!=[]:
        for exam in t['gy_example']:
            gy_example(exam)  
    if t['gy_notes']!=[]:
        for exam in t['gy_notes']:
            gy_notes(exam)   
    if t['gy_biscrimination']!=[]:
        for exam in t['gy_biscrimination']:
            gy_biscrimination(exam)  
    if t['gy_fixed_collocation']!=[]:
        for exam in t['gy_fixed_collocation']:
            gy_fixed_collocation(exam)              
    #print('---------------------',file=f)       
    

def gy_sentential_form(t): #15924
    #print('==')
    print('- #### '+t['sentential_form'],file=f)
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
    if b!='' :
        while b[0]==' ':
            b=b[1:]
        while b[-1]==' ':
            b=b[:-1]
        print('> **'+b+'**  ',file=f)
    print('> '+t['english']+'  ',file=f)
    print('> '+t['chinese'],file=f)
    print(file=f)
    
def gy_notes(t): #16597
    print(t['notes'],file=f)
    if t['gy_example']!=[]:
        for example in t['gy_example']:
            gy_example(example)
    if t['gy_sentential_form']!=[]:
        for form in t['gy_sentential_form']:
            gy_sentential_form(form)
            
def gy_biscrimination(t): #16597
    print('### 辨析 '+t['words'],file=f)
    print(t['paraphrase'],file=f)
    if t['gy_example']!=[]:
        for example in t['gy_example']:
            gy_example(example)
    #print('==',file=f)
    

def gy_fixed_collocation(t): #26462
    print('- #### '+t['fixed_word'],file=f)
    if t['gy_paraphrase']!=[]:
        i=1
        for exam in t['gy_paraphrase']:
            print(str(i) + '. ',end='',file=f)
            #print('--------释义'+str(i),file=f)
            gy_paraphrase(exam) 
            i=i+1
            #print('---------------------')
    
    

def gy_derivative(t): #10112
    print(t['derivative_word']+' '+t['phonogram']+' ' +t['part_of_speech']+' ' +t['use_method'],file=f)
    if t['gy_example']!=[]:
        for example in t['gy_example']:
            gy_example(example)
    if t['gy_paraphrase']!=[]:
        i=1
        for exam in t['gy_paraphrase']:
            print(str(i) + '. ',end='',file=f)
            #print('--------释义'+str(i),file=f)
            gy_paraphrase(exam) 
            i=i+1
            #print('---------------------')
    if t['gy_fixed_collocation']!=[]:
        for exam in t['gy_fixed_collocation']:
            gy_fixed_collocation(exam)  
            

def gy_exam_link(exam): #10112
    print('##### 题目  ',file=f)
    print(exam['subject']+'  ',file=f)
    if exam['answer_a']!='' :print('A.'+exam['answer_a']+'  ',file=f)
    if exam['answer_b']!='' :print('B.'+exam['answer_b']+'  ',file=f)
    if exam['answer_c']!='' :print('C.'+exam['answer_c']+'  ',file=f)
    if exam['answer_d']!='' :print('D.'+exam['answer_d']+'  ',file=f)
    print('##### 答案 '+ exam['answer']+'  ',file=f)
    print('  ',file=f)
#def gy_word_expand
#137136




def chuli(t):
    print(file=f)  
    a=json.loads(t)
    #info
    b=a['word']
    
    #print(b)
    while b[0]==' ':
        b=b[1:]
    while b[-1]==' ':
        b=b[:-1]
    
    print('# ***' + b + '*** ' + a['part_of_speech'],end='', file = f)
    if a['point']==1 :print('  重难点词汇',end='',file=f)
    print(file=f)
    print('---',file=f)
    if a['en_phonetic_symbols']!='':print('英音 ' + a['en_phonetic_symbols'],end='     ',file=f)
    if a['usa_phonetic_symbols']!='':print('美音 ' + a['usa_phonetic_symbols'],end='',file=f)
    print(file=f)
    print(file=f)
    #print('英音 ' + a['en_phonetic_symbols'] + '       美音 ' + a['usa_phonetic_symbols'], file = f )
    print('词频 ' + str(a['lv_frequency'])+' | 口语 ' + str(a['lv_speak']) + ' | 书面 ' + str(a['lv_write']) + ' | 阅读 ' + str(a['lv_read'])  , file = f)
    print(file=f)
    #note
    #if a['point']==1 :print('重难点词汇',file=f)
    #if a['not_use']==0 : print('高考从未出现',file=f)
    #if a['outpoint']==1 : print('课标外词汇',file=f)
    #if a['outpoint']==2 : print('课标派生/合成词',file=f) 
    if a['use_method']!='' : print('用法点拨  '+ a['use_method'],file=f)
    print(file=f)
    #if a['area']!='':print('地方性考试说明词汇  '+a['area'],file=f)
    
    #paraphrase
    #print('===========英文释义===========',file=f)
    if a['gy_paraphrase']!=[]:
        print('英文释义',file=f)
        print('---',file=f)
        i=1
        for exam in a['gy_paraphrase']:
            print(str(i) + '. ',end='',file=f)
            #print('--------释义'+str(i),file=f)
            gy_paraphrase(exam)    
            i=i+1
    print(file=f)
    
    
    #fixed_word固定搭配
    #print('===========固定搭配===========',file=f)  
    if a['gy_fixed_collocation']!=[]:
        print('固定搭配',file=f)
        print('---',file=f)  
        for exam in a['gy_fixed_collocation']:
            gy_fixed_collocation(exam)    
    print(file=f)
        
    #derivative派生词
    #print('===========派生词汇===========',file=f)
    if a['gy_derivative']!=[]:
        print('派生词汇',file=f)
        print('---',file=f)    
        for exam in a['gy_derivative']:
            gy_derivative(exam)   
    print(file=f)
        
    #exam
    #print('===========真题解析===========',file=f)
    if a['gy_exam_link']!=[]:
        print('真题解析',file=f)
        print('---',file=f)  
        for exam in a['gy_exam_link']:
            gy_exam_link(exam)        
    print(file=f)            

            
# 欢迎文字
print('\n\n')
print('####### 维克多英语词汇导出程序 #######\n')
# print('Author~~')
print('Jellow 看见我请一定一定叫我学习')
print('Creative By ZhiyuShang With Love\n')
# print('Thanks for being addicted')
print('')

path = input('请输入weici_ext.db文件位置：\n')
if path=='' : path=r'C:\Users\Administrator\Desktop\weici_ext.db'

conn = sqlite3.connect(path)
c = conn.cursor()

path_save = input('请输入保存位置：\n')
if path_save=='':path_save = r'C:\Users\Administrator\Desktop\victory'
print('注意：文件将存到%s' % path_save + '\weici_所有词_去空值.md')
if not os.path.exists(path_save):
    os.makedirs(path_save)
  
  
print('请稍后Processing。。。')


f = open('%s' % path_save + '\weici_所有词_去空值.md','w',encoding='utf-8')


cursor = c.execute("select * from fb_word_detail order by word asc")
for row in cursor:
    #if row[6]==0 and row[1].find(' ')!=-1:chuli(row[3]) #仅输出词组
    if row[6]==0 : chuli(row[3]) #仅输出单词

input('工作已完成！按Enter退出')