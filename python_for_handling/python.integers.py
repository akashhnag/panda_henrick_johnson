#assignment
whole_num=5
print('whole_num',whole_num)

#addition
num_two=3
num_three= num_two+ whole_num
print('num_three',num_three)

#subtration
num_four=whole_num-num_two
print('num_four',num_four)

#multiplication
num_five=num_four*num_three
print('num_five',num_five)

#division
num_six=num_five/whole_num
print('num_six',num_six)

#type_checking
print(type(num_five))
print(type(num_six))

#floor division
num_seven=num_five//whole_num
print('num_seven',num_seven)

#keep track of python loop
for x in range(1,5):
    print(x)

#Other data types can be coverted or cast as Integers if data types are suitable.
num_eight=int(5.5)
num_nine=int('3')
print('num_eigth',num_eight)
print(type(num_eight))
print('num_nine',num_nine)
print(type(num_nine))