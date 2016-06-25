# lychrel_count = 0
# For possible_lychrel in ( 0 to 9999 )
#   count = 0
#   sum = possible_lychrel + reverse(possible_lychrel)
#   if is_palindrome(sum) 
#     if count < 50
#       pass
#     else 
#       lychrel_count++
#   elif count > 50
#     lychrel_count++
#     continue
#   else
#     count++

def is_palindrome(num):
    str_num = ''
    if type(num) == int or type(num) == long:
        str_num = str(num)
    else:
        str_num = num
    
    if str_num == "":
        return True
    if len(str_num) == 1:
        return True
    else:
        if str_num[0] != str_num[-1]:
            return False
        else:
            return is_palindrome(str_num[1:-1])

def reverse(num):
   string = str(num)
   result = ""
   while string != "":
       result += string[-1]
       string = string[:-1]
   return int(result)

def is_lychrel(num):
    iterations = 0
    temp = num
    while True:
        if iterations > 50:
            return False 
        sum = temp + reverse(temp)
        # print str(temp) + " + " + str(reverse(temp)) + " = " + str(sum)
        if is_palindrome(sum):
            return True
        temp = sum
        iterations += 1

count = 0
for num in range(0, 10000):
    print num
    if is_lychrel(num):
        print "count: " + str(count)
        count += 1
print "answer: " + str(10000-count)
    
   
    



            
    

