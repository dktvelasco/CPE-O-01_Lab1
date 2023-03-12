# Statisticians would like to have a set of functions to compute the median and mode of a list of numbers.
# The median is the number that would appear at the midpoint of a list if it were sorted.
# The mode is the number that appears most frequently in the list.
# Define these functions in a module named stats.py.
# Also include a function named mean, which computes the average of a set of numbers.
# Each function expects a list of numbers as an argument and returns a single number.

import statistics

while True:
  
  try:
      print("Enter a set of numbers.")
      print("ENTER ONE AT A TIME.")
      print("Press * to finalize.")
      var = True
      num_list = []
      
      while (var == True):
          num = input("Enter number: ")
          if(num =='*'):
            var = False
            break
          else :
              num = int(num)
              num_list.append(num)
      print("Input List: ")
      print(num_list)
      print()
        
      # calculate the median of the given list
      def median(num_list):
          length = len(num_list)
          if(length%2)==0):
              first = num_list[int((length/2))-1]
              second = num_list[int((length/2)]
              i =(first+second)/2
              return i
          else:
              return num_list[length//2]
                                    
      # calculate the mode of the given list
      def mode(num_list):
          return statistics.mode(num_list)
                                    
      # calculate the average of the list
      def mean(number_list):
          return statistics.mean(num_list)
