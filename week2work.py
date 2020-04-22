# xyz_there

def xyz_there(str):
  for i in range(len(str)):
    if str[i] != '.' and str[i+1:i+4] == 'xyz':
      return True
  if str[0:3] == 'xyz':
    return True
  return False
  
# end_other

def end_other(a, b):
    a = a.lower()
    b = b.lower()
        
    return a.endswith(b) or b.endswith(a)
    
# count_code

def count_code(str):
  times = 0
  for i in range(0,len(str)):
    if str[i:i + 2] == 'co':
      if str[i + 3: i + 4] == 'e':
        times = times + 1
  return times
  
# has 22

def has22(nums):
  for i in range(0, len(nums) - 1):
    if nums[i] == 2 and nums[i + 1] == 2:
      return True
  return False

# sum67

def sum67(nums):
    total = 0
    found6 = False
      
    for i in range(len(nums)):
        if nums[i] == 6:
            found6 = True
        if not found6:
            total += nums[i]
        if nums[i] == 7 and found6:
            found6 = False
            
    return total

# centered_average

def centered_average(nums):
  items = len(nums)
  total = 0
  high = max(nums)
  low = min(nums)
  for num in nums:
    total += num
  aveg = (total -high-low) / (items-2)
  return aveg

# round_sum

def round10(num):
  if num % 10 >= 5:
    return num + (10 - num % 10)
  if num % 10 < 5:
    return num - (num % 10)
def round_sum(a, b, c):
  return round10(a) + round10(b) + round10(c)

# no_teen_sum

def no_teen_sum(a, b, c):
  myList1 = [13,14]
  myList2 = [17,18,19]
  if a not in myList1 and a not in myList2:
    a = a
  else:
    a = 0
  if b not in myList1 and b not in myList2:
    b = b
  else:
    b = 0
  if c not in myList1 and c not in myList2:
    c = c
  else:
    c = 0
  return a + b + c

# lucky_sum

def lucky_sum(a, b, c):
  if a != 13:
    if b != 13:
      if c != 13:
        return a + b + c
      else:
        return a + b
    else:
      return a
  else:
    return 0

# string_match

def string_match(a, b):
    amount = 0
    for i in range(len(a)):
        if (len(a[i:i+2]) == 2) and a[i:i+2]  == b[i:i+2]:
            amount += 1
    return amount

# array123

def array123(nums):
  for i in range(0,len(nums) - 2):
    if nums[i] == 1:
      if nums[i + 1] == 2:
        if nums[i + 2] == 3:
          return True
  else:
    return False

# array_front9

def array_front9(nums):
    for i in xrange(4):
        if i < len(nums) and nums[i] == 9:
            return True
                  
    return False
    

