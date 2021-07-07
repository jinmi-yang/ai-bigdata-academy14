#!/usr/bin/env python
# coding: utf-8

# In[205]:




f = open('students.txt', 'r')
some_list = list()
d=dict()
lines=f.readlines() 
for i in lines :
    some_list+=i.split('\t')
    k=1
    while k < len(some_list) :
        name=(some_list[k])
        mid=int(some_list[k+1])
        fin=int(some_list[k+2][:len(some_list[k+2])-1:])
        avg=(mid+fin)/2
        if avg >= 90:
            grade='A'
        elif avg >= 80 and avg <90:
            grade='B'
        elif avg >= 70 and avg <80:
            grade='C'
        elif avg >= 60 and avg <70:
            grade='D'
        else :
            grade='F'
        d[int(some_list[k-1])] = [name,mid,fin,round(avg,1),grade]
        k+=4

f.close()

    
def show():
    sorted_sl = sorted(d.items(), key = lambda a: a[1][3], reverse=True)
    print('Student','\t','%9s'%'name','%11s'%'Midterm','%6s'%'Final','%9s'%'Average','%9s'%'Grade')
    print('-'*65)
    i=0
    while i < len(d):
        print(sorted_sl[i][0],'\t',sorted_sl[i][1][0],'\t',sorted_sl[i][1][1],'\t',sorted_sl[i][1][2],'\t',sorted_sl[i][1][3],'%9s'%sorted_sl[i][1][4])
        i+=1
    
    
    
def search():
    student_num=int(input('Student ID: '))
    if student_num in d:
            print('Student','\t','%9s'%'name','%11s'%'Midterm','%6s'%'Final','%9s'%'Average','%9s'%'Grade')
            print('-'*65)
            print(student_num,'\t',d[student_num][0],'\t',d[student_num][1],'\t',d[student_num][2],'\t',d[student_num][3],'\t','%6s'%d[student_num][4])

    else :
        print( 'NO SUCH PERSON.')

def changescore():
    student_num=int(input('Student ID: '))
    if student_num in d:
        whichone =input('mid/final? ')
        if whichone == 'mid' :
            new_score=int(input('Input new score: '))
            if new_score <= 100 :
                print('Student','\t','%9s'%'name','%11s'%'Midterm','%6s'%'Final','%9s'%'Average','%9s'%'Grade')
                print('-'*65)
                print(student_num,'\t',d[student_num][0],'\t',d[student_num][1],'\t',d[student_num][2],'\t',d[student_num][3],'\t','%6s'%d[student_num][4])
                d[student_num][1]=new_score
                d[student_num][3]=(new_score+d[student_num][2])/2
                avg=d[student_num][3]
                if avg >= 90:
                    grade='A'
                elif avg >= 80 and avg <90:
                    grade='B'
                elif avg >= 70 and avg <80:
                    grade='C'
                elif avg >= 60 and avg <70:
                    grade='D'
                else :
                    grade='F'
                d[student_num][4] = grade

                print('Score changed.')
                print(student_num,'\t',d[student_num][0],'\t',d[student_num][1],'\t',d[student_num][2],'\t',d[student_num][3],'\t','%6s'%d[student_num][4])
            else : 
                print('Please enter a score below 100.')
                
        elif whichone == 'final' :
            new_score=int(input('Input new score: '))
            if new_score <= 100 :
                print('Student','\t','%9s'%'name','%11s'%'Midterm','%6s'%'Final','%9s'%'Average','%9s'%'Grade')
                print('-'*65)
                print(student_num,'\t',d[student_num][0],'\t',d[student_num][1],'\t',d[student_num][2],'\t',d[student_num][3],'\t','%6s'%d[student_num][4])
                d[student_num][2]=new_score
                d[student_num][3]=(new_score+d[student_num][1])/2
                avg=d[student_num][3]
                if avg >= 90:
                    grade='A'
                elif avg >= 80 and avg <90:
                    grade='B'
                elif avg >= 70 and avg <80:
                    grade='C'
                elif avg >= 60 and avg <70:
                    grade='D'
                else :
                    grade='F'
                d[student_num][4] = grade

                print('Score changed.')
                print(student_num,'\t',d[student_num][0],'\t',d[student_num][1],'\t',d[student_num][2],'\t',d[student_num][3],'\t','%6s'%d[student_num][4])
            else : 
                print('Please enter a score below 100.')
        else :
            print("Please enter 'mid' or 'final'")
    else :
        print( 'NO SUCH PERSON.')

def add():
    new_student_num=int(input('Student ID: '))
    if new_student_num in d:
        print('ALREADY EXISTS.')
    else :
        new_name=input('Name: ')
        new_mid=int(input('Midterm Score: '))
        if new_mid > 100 :
            print('Please enter a score below 100.')
        new_fin=int(input('Final Score: '))
        if new_fin > 100 :
            print('Please enter a score below 100.')
        new_avg=(new_mid+new_fin)/2
        if new_avg >= 90:
            new_grade='A'
        elif new_avg >= 80 and new_avg <90:
            new_grade='B'
        elif new_avg >= 70 and new_avg <80:
            new_grade='C'
        elif new_avg >= 60 and new_avg <70:
            new_grade='D'
        else :
            new_grade='F'
        d[new_student_num]=[new_name,new_mid,new_fin,round(new_avg,1),new_grade]
        print('Student added.')

def searchgrade ():
    search=input('Grade to search: ')
    if search == 'A':
        some=0
        for i in d :
            if d[i][4] =='A':
                some+=1
                if some == 0 :
                    print ('NO RESULTS.')
                else :
                    print('Student','\t','%9s'%'name','%11s'%'Midterm','%6s'%'Final','%9s'%'Average','%9s'%'Grade')
                    print('-'*65)
                    for i in d :
                        if d[i][4] =='A':
                            print(i,'\t',d[i][0],'\t',d[i][1],'\t',d[i][2],'\t',d[i][3],'\t','%6s'%d[i][4])
                            
    elif search == 'B':
        some=0
        for i in d :
            if d[i][4] =='B':
                some+=1
                if some == 0 :
                    print ('NO RESULTS.')
                else :
                    print('Student','\t','%9s'%'name','%11s'%'Midterm','%6s'%'Final','%9s'%'Average','%9s'%'Grade')
                    print('-'*65)
                    for i in d :
                        if d[i][4] =='B':
                            print(i,'\t',d[i][0],'\t',d[i][1],'\t',d[i][2],'\t',d[i][3],'\t','%6s'%d[i][4])
                            
    elif search == 'C':
        some=0
        for i in d :
            if d[i][4] =='C':
                some+=1
                if some == 0 :
                    print ('NO RESULTS.')
                else :
                    print('Student','\t','%9s'%'name','%11s'%'Midterm','%6s'%'Final','%9s'%'Average','%9s'%'Grade')
                    print('-'*65)
                    for i in d :
                        if d[i][4] =='C':
                            print(i,'\t',d[i][0],'\t',d[i][1],'\t',d[i][2],'\t',d[i][3],'\t','%6s'%d[i][4])
    elif search == 'D':
        some=0
        for i in d :
            if d[i][4] =='D':
                some+=1
                if some == 0 :
                    print ('NO RESULTS.')
                else :
                    print('Student','\t','%9s'%'name','%11s'%'Midterm','%6s'%'Final','%9s'%'Average','%9s'%'Grade')
                    print('-'*65)
                    for i in d :
                        if d[i][4] =='D':
                            print(i,'\t',d[i][0],'\t',d[i][1],'\t',d[i][2],'\t',d[i][3],'\t','%6s'%d[i][4])
    elif search == 'F':
        some=0
        for i in d :
            if d[i][4] =='F':
                some+=1
                if some == 0 :
                    print ('NO RESULTS.')
                else :
                    print('Student','\t','%9s'%'name','%11s'%'Midterm','%6s'%'Final','%9s'%'Average','%9s'%'Grade')
                    print('-'*65)
                    for i in d :
                        if d[i][4] =='F':
                            print(i,'\t',d[i][0],'\t',d[i][1],'\t',d[i][2],'\t',d[i][3],'\t','%6s'%d[i][4])
                            
    else:
        print('NO RESULTS.')

def remove():
    want_student_num=int(input('Student ID: '))
    if not d :
        print ('List is empty.')
    else:
        if want_student_num in d:
            del d[want_student_num]
            print('Student removed.')
        else :
            print('NO SUCH PERSON.')
            
while True:
    word=input('#')
    if word.upper() == 'SHOW':
        show()
    elif word.upper() == 'SEARCH':
        search()
    elif word.upper() == 'CHANGESCORE':
        changescore()
    elif word.upper() == 'SEARCHGRADE':
        searchgrade()
    elif word.upper() == 'ADD':
        add()
    elif word.upper() == 'REMOVE':
        remove()
    elif word.upper() == 'QUIT':
        say=input('Save data?[yes/no]')
        if say.upper() == 'YES':
            file_name=input('File name: ')
            txt=file_name + '.txt'
            new_f=open(txt,'a')
            sorted_sl = sorted(d.items(), key = lambda a: a[1][3], reverse=True)
            for i in d:
                data = "%s\t%s\t%s\t%s\t"%(i, d[1][0], d[1][1], d[1][2])
                new_f.write(data)
                
            new_f.close()
        elif say.upper() == 'NO':
            break
        else:
            print("Please enter 'yes'or'no'")
        
    else :
        continue
        

