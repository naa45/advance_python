
def is_even():
    number= int (input("please enter a number : "))
    if number%2 !=0:
        print("true")
    else:
        print("false")
is_even()

'''def is_even1(number):return number%2 ==0
numbers = [1,56,234,87,4,76,24,69,90,135]
print(list(filter(is_even1,numbers)))'''


'''numbers=[1,56,234,87,4,76,24,69,90,135]
filtered_list = list(filter(lambda num:(num%2==0),numbers))
print(filtered_list)'''

'''numbers=[1,56,234,87,4,76,24,69,90,135]
filtered_list = list(filter(lambda num:(num%2==1),numbers))
print(filtered_list)'''



    
