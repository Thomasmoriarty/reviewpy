# collection of data, data structure 

# list = [] ordered, changeable. duplicates ok
# sets = {} unordered, unchangeable, duplicates no, add/remove ok
# tuples = () ordered, unchangeable. duplicates ok. Faster than list

nums= [1,3,3,4,45,6,5,75,65,4,34,3,34,43,5]
sentence=["hello", "how", "you", "going", "m8"]

# print(dir(nums))
# print(help(nums))
nums.append(100) # 100 added to end
print(nums)

print("-----------------------")
count1=nums.count(3) #records amount of x present in list
print(count1)

print("-----------------------")

nums.extend(sentence)
print(nums)
print(sentence)

print("-----------------------")
print(nums.index(3)) #records first index incidence of value
print(nums.index("you"))
print(nums[18])

print("-----------------------")
print(nums.index("hello"))
nums.insert(16, "strings begin")
print(nums)

print("-----------------------")
nums.pop() # will remove last value == "m8"
nums.pop(0) # will pop at that index 
print("should not have 1 as first element and m8 should be gone", nums)

print("-----------------------")
nums.remove(3) #doesnt remove all just the first instance like index
nums.remove("you")
print(nums) 

print("-----------------------")
#print(dir(nums))
nums.reverse()
L1=[1,2,3,4]
L1.reverse()
print(nums)
print(L1)
print("-----------------------")
L5=[1,2,3,4]
L5.sort()
print(L5)
print("^sorted ascending")
L5.sort(reverse=True)
print(L5)
print("sorted reversed ^^")

