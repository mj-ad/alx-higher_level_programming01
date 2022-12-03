#!/usr/bin/python3
def remove_char_at(str, n):
   i = 0
   c = ''
   d = ''
   for char in str:
      if i == n:
         c = ''
      if i != n:
         c = char
      i = i + 1
      print(c, end='')
   return d
   print()
