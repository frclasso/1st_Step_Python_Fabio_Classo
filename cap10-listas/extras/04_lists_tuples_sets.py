#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 11 09:12:45 2018

@author: fabio
"""

courses = ['History', 'Math', 'Physics','CompSci' ]

#indexing
#print(courses[0])
#print(courses[1])
#print(courses[2])
#print(courses[3])

# Slincing
#print(courses[0:5])
#print(courses[:5])
#print(courses[2:])

# Add items
#courses.append('Art')
#courses.insert(0, 'Biology')

# Add items from another list
courses_2 = ['Chemistry', 'Art']

#courses.insert(0, courses_2)
#print(courses[0])
courses.extend(courses_2)



# Removing items

# Usisng remove method
#courses.remove('Math')

#Using pop method (last object)
#courses.pop()

# Using del method
#del courses[0] 

# Sorting lists
#courses.sort()
#courses.sort(reverse=True)

nums = [6,1,4,2,5,3,0,9,8,7]
#nums.sort()
#nums.sort(reverse=True) # inverte a ordem
#print(nums)

# Sorting a new list, using sorted method 
new_courses = sorted(courses)
#print(new_courses)


#print(min(nums))
#print(max(nums))
#print(sum(nums))


#print(courses.index('CompSci'))

# Membership operators
#print('Medicine' in courses)
#print('Math' in courses)

#print(courses)

# for loop

#for course in courses:
#    print(course)

#for index, course in enumerate(courses, start=1):
#    print(index, course)

# Join
#courses_str = ', '.join(courses)
#print(courses_str) 

#new_list = courses_str.split(', ')
#print(new_list)

# Mutable list
#list1 = ['History', 'Math', 'Physics', 'CompSci', 'Chemistry', 'Art']
#list2 = list1
#print(list1)
#print(list2)

#list1[0] = 'Bio'  # Altera ambas as listas

#print(list1)
#print(list2)

# Tuples
#tuple_1 = ['History', 'Math', 'Physics', 'CompSci', 'Chemistry', 'Art']
#tuple_2 = tuple_1
#print(tuple_1)
#print(tuple_2)

#tuple_1[0] = 'Bio'  # Altera ambas as listas
#
#print(tuple_1)
#print(tuple_2)

# Sets
#cs_courses = {'History', 'Math', 'Physics', 'CompSci', 'Chemistry', 'Art',
#              'Math'}
#print('Math' in cs_courses)
#print(cs_courses)

cs_courses = {'History', 'Math', 'Physics', 'CompSci', 'Chemistry'}
art_courses = {'History', 'Design', 'Art', 'Math'}
#print(cs_courses.intersection(art_courses))
#print(cs_courses.difference(art_courses))
print(cs_courses.union(art_courses))
