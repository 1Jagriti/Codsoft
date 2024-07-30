from tkinter import * 

First_number=Second_number=Operator=None

# Function to handle the button click event
def get_digit(digit):
    current = result_box ['text']
    new =(current) + str(digit)
    result_box.config(text=new)
    
def clear():
    result_box.config(text='')
    First_no_box.config(text='')
    Operator_box.config(text='')
    Second_no_box.config(text='')
    

def get_operator(optr):
    global First_number,Operator
    
    First_number=int(result_box['text'])
    Operator = optr
    First_no_box.config(text=First_number)
    Operator_box.config(text=Operator)
    result_box.config(text='')
    
# Function to print the final result
def get_result():
    global First_number,Second_number,operator
    
    Second_number = int(result_box['text'])
    Second_no_box.config(text = Second_number)
    
    if Operator == '+':
        result_box.config(text = str('=') + ' ' + str(First_number + Second_number))
    elif Operator == '-':
        result_box.config(text = str('=') + ' ' + str(First_number - Second_number)) 
    elif Operator == '*':
        result_box.config(text = str('=') + ' ' +  str(First_number * Second_number))
    else:
        if Second_number == 0:
            result_box.config(text='Error')
        else:
            result_box.config(text = str('=') + ' ' +  str(round(First_number / Second_number,2)))
                       
# Create the main window            
base = Tk()
base.title('Calculator')
base.geometry('378x628')
base.resizable(0,0)
base.configure(background='black')

# Create and place the widgets
First_no_box = Label(base,text='',bg='black',fg='white')
First_no_box.grid(row=0, column=0,columnspan = 1000, pady=(0,25),sticky = 'w')
First_no_box.config(font=('verdana',20,'bold'))

Operator_box = Label(base,text='',bg='black',fg='white')
Operator_box.grid(row=1, column=0,columnspan = 1000, pady=(0,25),sticky = 'w')
Operator_box.config(font=('verdana',20,'bold'))

Second_no_box = Label(base,text='',bg='black',fg='white')
Second_no_box.grid(row=2, column=0,columnspan = 1000, pady=(0,25),sticky = 'w')
Second_no_box.config(font=('verdana',20,'bold'))

result_box = Label(base,text='',bg='black',fg='white')
result_box.grid(row=3, column=0,columnspan = 1000, pady=(0,25),sticky = 'w')
result_box.config(font=('verdana',35,'bold'))

btn7 = Button(base,text = '7',bg='#00a65a',fg='white',width=5,height=2,command=lambda :get_digit(7))
btn7.grid(row=4,column=0)
btn7.config(font=('verdana',20))

btn8 = Button(base,text = '8',bg='#00a65a',fg='white',width=5,height=2,command=lambda :get_digit(8))
btn8.grid(row=4,column=1)
btn8.config(font=('verdana',20))

btn9 = Button(base,text = '9',bg='#00a65a',fg='white',width=5,height=2,command=lambda :get_digit(9))
btn9.grid(row=4,column=2)
btn9.config(font=('verdana',20))

btn_Add = Button(base,text = '+',bg='#00a65a',fg='white',width=5,height=2,command=lambda :get_operator('+'))
btn_Add.grid(row=4,column=3)
btn_Add.config(font=('verdana',20))

btn4 = Button(base,text = '4',bg='#00a65a',fg='white',width=5,height=2,command=lambda :get_digit(4))
btn4.grid(row=5,column=0)
btn4.config(font=('verdana',20))

btn5 = Button(base,text = '5',bg='#00a65a',fg='white',width=5,height=2,command=lambda :get_digit(5))
btn5.grid(row=5,column=1)
btn5.config(font=('verdana',20))

btn6 = Button(base,text = '6',bg='#00a65a',fg='white',width=5,height=2,command=lambda :get_digit(6))
btn6.grid(row=5,column=2)
btn6.config(font=('verdana',20))

btn_Subtract = Button(base,text = '-',bg='#00a65a',fg='white',width=5,height=2,command=lambda :get_operator('-'))
btn_Subtract.grid(row=5,column=3)
btn_Subtract.config(font=('verdana',20))

btn1 = Button(base,text = '1',bg='#00a65a',fg='white',width=5,height=2,command=lambda :get_digit(1))
btn1.grid(row=6,column=0)
btn1.config(font=('verdana',20))

btn2 = Button(base,text = '2',bg='#00a65a',fg='white',width=5,height=2,command=lambda :get_digit(2))
btn2.grid(row=6,column=1)
btn2.config(font=('verdana',20))

btn3 = Button(base,text = '3',bg='#00a65a',fg='white',width=5,height=2,command=lambda :get_digit(3))
btn3.grid(row=6,column=2)
btn3.config(font=('verdana',20))

btn_Multiply = Button(base,text = '*',bg='#00a65a',fg='white',width=5,height=2,command=lambda :get_operator('*'))
btn_Multiply.grid(row=6,column=3)
btn_Multiply.config(font=('verdana',20))

btn_Clear = Button(base,text = 'C',bg='#00a65a',fg='white',width=5,height=2,command=lambda :clear())
btn_Clear.grid(row=7,column=0)
btn_Clear.config(font=('verdana',20))

btn0 = Button(base,text = '0',bg='#00a65a',fg='white',width=5,height=2,command=lambda :get_digit(0))
btn0.grid(row=7,column=1)
btn0.config(font=('verdana',20))

btn_Equals = Button(base,text = '=',bg='#00a65a',fg='white',width=5,height=2,command=get_result)
btn_Equals.grid(row=7,column=2)
btn_Equals.config(font=('verdana',20))

btn_Divide = Button(base,text = '/',bg='#00a65a',fg='white',width=5,height=2,command=lambda :get_operator('/'))
btn_Divide.grid(row=7,column=3)
btn_Divide.config(font=('verdana',20))

# Run the application
base.mainloop()
