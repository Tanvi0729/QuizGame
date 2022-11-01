import csv
from datetime import date



print("Wellcome to quiz game !!")
print('NOTE: if your spelling is incorrect then it is considered as wrong answer')
r = int (input("Enter the roll number: "))
print ("Roll Number is: ", r)
score = 0
question_no = 0
playing = input('Do you want to play ? ').lower()
if playing == 'yes':
    question_no += 1
    ques = input(f'\n{question_no}. what does CPU stand for? 1. central processing unit 2. COntrol Processing unit 3. Command Press unit 4. Common Print unit ').lower()
    
    if ques == 'central processing unit':
        score +=1
        print('correct! you got 1 point')
        
    else:
        print('Incorrect!')
        print(f'current answer is --> central processing unit')

# ------1
    question_no += 1
    ques = input(f'\n{question_no}. what does GPU stand for?   1. graphics processing unit 2. Group Processing unit 3. Graphic Print unit 4. Graph Print unit ').lower()
    
    
    if ques == 'graphics processing unit':
        score +=1
        print('correct! you got 1 point')
        
    else:
        print('Incorrect!')
        print(f'current answer is --> graphics processing unit')

# -----2
    question_no += 1
    ques = input(f'\n{question_no}. what does RAM stand for?  1. random access memory 2. read acces memory 3. roman access memory 4. rich access memory ').lower()
    
    if ques == 'random access memory':
        score +=1
        print('correct! you got 1 point')
        
    else:
        print('Incorrect!')
        print(f'current answer is --> random access memory')

# -----3
    question_no += 1
    ques = input(f'\n{question_no}. what does PSU stand for? 1. power supply unit 2. power strain unit 3. present select unit 4. power store unit').lower()
  
    if ques == 'power supply unit':
        score +=1
        print('correct! you got 1 point')
        
    else:
        print('Incorrect!')
        print(f'current answer is --> power supply unit')

else:
    print('thankyou you are out of a game.')
    quit()

print(f'\nnumber of question is {question_no}')
print(f'your score is {score}')
print(score)
try:
    percentage = (score *100)/question_no
except ZeroDivisionError:
    print('0% quetions are correct')

print(f'{percentage}% questions are correct.')




with open("results.csv", "a") as f:
    f.write('Date,roll no Question,Score\n {}, {},{},{}'.format(date, r,question_no,score))
