# # print("hiiii")
# # print("I'm ankit")
# # print("line A\n  line B")
# # print("line B")
# # print("name\t    Ankit")
# # print("this is  backslash\\\\")
# # print("hel\blll lo")
# '''print("Line A \\n Line B")
# print("Line A \\\\\\\\t Line B")
# print(" \\\" \\\' ")'''
# '''print("hell\bo goiu\\")
# print("line A \\n  line B")
# print("\\\" \\\'")'''
# '''print("this is \\\\ double backslsh")
# print("this is /\\/\\/\\/\\/\\  mountain")
# print("he is \tawesome")
# print("\\\" \\n \\t \\'")
# print(r"line a \n line b")
# print(r"This is a /\/\/\/\/\/\/\/\/\/\/\ mountain")
# print("\U0001F602")
# print("\U0001F602")
# print("\U0001F602")
# print("\U0001F602")
# print("\U0001F602")
# print("\U0001F602")
# print("\U0001F602")
# print("\U0001F602")
# print("\U0001F602")
# print("\U0001F602")
# print("\U0001F602")
# print("\U0001F602")
# print("\U0001F602")
# print("\U0001F602")
# print("\U0001F602")
# print(2**0.5)
# print(round(2**0.5,4))
# number =14
# print(number)'''
# # first_name = "Ankit"
# # Last_name = "kumar"
# # print(first_name + ("        "),str(3))
# # number_1 = eval(input("Enter the first number"))
# # number_2 = eval(input("Enter the second number"))
# # total = (number_1 + number_2)
# # print("total number is",(total))
# # name , age = "Ankit" , "24"
# # print("hello " + name + " my age is " + age)
# # x=y=z=1
# # print(x+y+z)
# # name, age = input("enter your name and age ").split(",")
# # print(name)
# # print(age)
# # name = "Ankit"
# # age = 22
# # print("hello {} your age is {}".format(name, age+ 2)) # python 3
# # print(f"hello {name} your age is {age}") #python 3.6 clean syntax
# # print(f"hello {name} your age is {age + 2}") #python 3.6 clean syntax

# # A = int(input("Enter the firts number"))
# # B = int(input("Enter the second number"))
# # C = int(input("Enter the second number"))
# # D = (A+B+C)/3
# # print("The average is",D)

# # User_name = (input("Enter the user name : "))
# # print("Reverse of your name is : ",User_name[-1::-1])

# name = "Amkit kumar"
# print(len(name))

# name = "AnKIt kUMar"
# print(name.lower())

# name = "AnKIt kUMar"
# print(name.upper())
# name = "AnKIt kUMar"
# print(name.title())
# name = "GOOd MORninG"
# print(name.count("G"))

'''name, char = input("enter comma seperated name and character : ").split(",")
print(f"length of your name is : {len(name)}")
print(f"character count : {name.lower().count(char.lower())}")'''

'''def reverse_list(l):
    l.reverse()
    return l
       #or
def reverse_list(l) :
    return l[::-1]      
number = [1,2,3,4]
print(reverse_list(number))

        #or
def reverse_list(l):
    r_list = []
    for i in range(len(l)):
        popped_item = l.pop()
        r_list.append(popped_item)
    return r_list
number = [1,2,3,4]
print(reverse_list(number))'''

'''def reverse_elements(l):
    elements = []
    for i in l:
        elements.append(i[::-1])
    return elements
word = ['abc','tuv','xyz']
print(reverse_elements(word))  '''

'''def filter_odd_even(l):
    odd_nums = []
    even_nums = []
    for i in l:
        if i % 2 ==0:
            even_nums.append(i)
        else:
            odd_nums.append(i)
    output = [odd_nums, even_nums]
    return output
nums = [1,2,3,4,5,6,7]
print(filter_odd_even(nums))'''

'''def common_finder(l1, l2):
    output = []
    for i in l1:
        if i in l2:
            output.append(i)
    return output
print(common_finder([1,2,5,8], [1,2,7,6]))'''

'''number = [6,60,2]
print(min(number))
print(max(number))

def greatest_diff(l):
    return max(l) - min(l)
print(greatest_diff(number))'''

'''def sublist_counter(l):
    count = 0
    for i in l:
        if type(i) == list:
            count+=1
    return count
mixed = [1,2,3, [1,2]]
print(sublist_counter(mixed))'''

'''def infixToPostfix(expression): 

    stack = [] # initialization of empty stack

    output = '' 

    

    for character in expression:

        if character not in expression:  # if an operand append in postfix expression

            output+= character

        elif character=='(':  # else Operators push onto stack

            stack.append('(')

        elif character==')':

            while stack and stack[-1]!= '(':

                output+=stack.pop()

            stack.pop()

        else: 

            while stack and stack[-1]!='(' and Priority[character]<=Priority[stack[-1]]:

                output+=stack.pop()

            stack.append(character)

    while stack:

        output+=stack.pop()

    return output


expression = input('Enter infix expression ')

print('infix notation: ',expression)

print('postfix notation: ',infixToPostfix(expression))'''

#Sure, I can help you send emails using Python. You'll need to use the smtplib library for sending emails. Here's a basic example of how to send an email with sender and receiver email addresses and a text message as input:

#python
'''import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Input variables
sender_email = input("Enter your email address: ")
receiver_email = input("Enter the recipient's email address: ")
message_text = input("Enter the email text: ")

# Your email login credentials (Make sure to allow "Less secure apps" in your email settings)
smtp_server = "smtp.your-email-provider.com"
smtp_port = 587
smtp_username = "your-username"
smtp_password = "your-password"

# Create the email message
msg = MIMEMultipart()
msg['From'] = sender_email
msg['To'] = receiver_email
msg['Subject'] = "Your Subject Here"

msg.attach(MIMEText(message_text, 'plain'))

# Connect to the SMTP server
server = smtplib.SMTP(smtp_server, smtp_port)
server.starttls()
server.login(smtp_username, smtp_password)

# Send the email
server.sendmail(sender_email, receiver_email, msg.as_string())

# Close the SMTP server
server.quit()

print("Email sent successfully!")'''

import smtplib, ssl

smtp_server = "smtp.gmail.com"
port = 587  # For starttls
sender_email = "my@gmail.com"
password = input("Type your password and press enter: ")

# Create a secure SSL context
context = ssl.create_default_context()

# Try to log in to server and send email
try:
    server = smtplib.SMTP(smtp_server,port)
    server.ehlo() # Can be omitted
    server.starttls(context=context) # Secure the connection
    server.ehlo() # Can be omitted
    server.login(sender_email, password)
    # TODO: Send email here
except Exception as e:
    # Print any error messages to stdout
    print(e)
finally:
    server.quit() 


 




