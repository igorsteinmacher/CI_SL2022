<a href="https://colab.research.google.com/github/igorsteinmacher/CI_SL2022/blob/main/Copy_of_HW4_Solutions.ipynb" target="_parent"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/></a>


```python
# package imports
import csv
import random
import string
```

# Solutions HW4:
Thanks for the initial solutions Bhaskar

## Instructions:

1. Access the menu *File -> Save a copy in Drive* to make a copy of this notebook to your own Google Drive
2. Change the name of the new notebook to be HW4_*StudentName* (where *StudentName* is actually your own name!)
3. Do the activities listed in the notebook and share with the instructor granting Editor rights (use the email is339@nau.edu).
**To turn in the assignment (on BBLearn):**

After sharing the notebook with me (ALL MANDATORY):
1. Add the Notebook URL to the field `Text Submission`
2. Download the file as a .py file from here (*File-->Download-->Download .py*): use the same naming format as the one used in the Notebook.
3. Submit the the py file to the assignment on BBLearn (`Attach File - Browse Local File`)

**Late submissions will not be evaluated -- LATE MEANS WHAT BBLEARN CALLS LATE. I WILL NOT EXCUSE ANY LATE (even if it is 12:00)**


## IMPORTANT
* **Please use exception handling whenever necessary**
* **Host your files wherever you find more interesting** 
* **I will take the whole mark if something is not in accordance**


## Exercise 1
Write a Python function (`copy_file`) that, given two file names (`file_from` and `file_to`), copy the contents of `file_from` (which MUST be a CSV file) to `file_to` (which MUST be a TSV file). The file may have one or multiple lines, and each line may have 1 or multiple values.

* CSV file: Comma-Separated-Values: `value 1, value 2, value 3, ...`
* TSV file: `value 1  value 2  value 3   ...` (the spaces between values are tabs `\t`)


Example:
file1.csv:
```
Line 1, animals, 0
Line 2, veggies, 0, 5
Line 3, animals, 2, 3
Line 4
```

would be converted to:
```
Line 1	animals	0
Line 2	veggies	0	5
Line 3	animals	2	3
Line 4
```


### Rubric (20 marks)

*Correct Inputs (3 marks):*
 - using this function signature: "copy_file(file_from, file_to)" --> They must use these names (1)
 - Correctly opens the file_from (reading) and file_to (writing) files. (2)

*Error Handling (4 marks)*
 - Include error handling for file opening (try-except for the excerpt with each open --> can be a single try-except) (4)

*Processing steps (7 marks):*
 - Read from file file_from (2)
 - Write to file_to (2)
 - file_to needs to be created using tabs ("\t"). If they use csv writer: delimiter ='\t'; if they write line by line, they need to include '\t' on their string (3)

*Output (3 marks):*
 - Notify user that there was an error. (3)

*Style (3 marks)*
 -  PEP (variables and functions all lower case. Meaningful names) (3)



```python
## This is the actual solution
## They may or may not use csv. Both are OK!

def copy_file(file_from, file_to):
  try:
    # opening two files in read and write modes
    # it is OK if they do in 2 steps
    with open(file_from,'r') as source_file_iterator, open(file_to, 'w') as destination_file_iterator:
      
      # instantiating the file reader 
      reader = csv.reader(source_file_iterator)

      # instantiating the file writer with the delimiter '\t'
      writer = csv.writer(destination_file_iterator, delimiter ='\t')

      # writing content to the output file using file writer
      writer.writerows(reader)

      # # iterating over the rows using the file reader
      # for row in reader:
      #   # writing a row to the output file using file writer
      #   writer.writerow(row)

      print("contents copied successfully...")

  # handling the exception
  except Exception as e:
    print("Exception occurred:{}".format(e))

copy_file('file1.csv','output.tsv')
```

    contents copied successfully...



```python
def copy_file(file_from, file_to):
  try:
    with open(file_from,'r') as source_file_iterator:  
      # instantiating the file reader 
      reader = list(csv.reader(source_file_iterator))

    with open(file_to, 'w') as destination_file_iterator:
      # instantiating the file writer with the delimiter '\t'
      writer = csv.writer(destination_file_iterator, delimiter ='\t')
      # writing content to the output file using file writer
      writer.writerows(reader)

      # # iterating over the rows using the file reader
      # for row in reader:
      #   # writing a row to the output file using file writer
      #   writer.writerow(row)

      print("contents copied successfully...")

   # handling the exception
  except Exception as e:
    print("Exception occurred:{}".format(e))
```

## Exercise 2
A csv file "students.csv" has each line presenting the information organized as follows:
* `<ID>, <Student_Name>, <Grade>`.

Write a function `count_above(threshold)` in Python that reads the contents of `students.csv` and displays the details of those students whose grades are above `threshold` and the number of students that are below the threshold. The `threshold` must be a float.

### Rubric (20 marks)

*Correct Inputs (3 marks)*:
 - using this function signature: "count_above(threshold)" --> They must use these names (1)
- Correctly reads the students.csv file -- Open with reading flag (2)

*Error Handling (3 marks):*
 - Include error handling for file opening (try-except) (3)

*Processing steps (6 marks):*
  - Determine the students whose grades are above threshold. (3)
  - Count the number of students that are below the threshold. (3)

*(Output 4 marks):*
  - Outputs the results from the Processing step:
    - (names above threshold) (2)
    - (number of the students below threshold) (2)
    - Nice print to notify user that there was an error. (2)

*Style (2 marks):*
 -  PEP (variables and functions all lower case. Meaningful names) (2)


```python
def count_above(threshold):
  try:
    # initializing the student count threshold to 0
    student_count_below_threshold = 0

    # opening the students.csv in read mode
    with open('students.csv','r') as file_iterator:
      # creating the instance of file reader
      reader = csv.reader(file_iterator)
      
      # iterating through the file rows using file reader
      for row in reader:
        # checking the grade column is greater than threshold
        if float(row[2]) > threshold:
          print(row)
        else:
          # if grade is below threshold incrementing the student count below threshold by 1
          student_count_below_threshold += 1

      print("Number of students that are below the threshold:{}".format(student_count_below_threshold))

  # handling the exception
  except Exception as e:
    print("Exception occurred:{}".format(e))

try:
  # taking the user input
  threshold = float(input("Enter threshold value:"))
  count_above(threshold)

# handling the exception
except Exception as e:
  print("Invalid threshold value")
```

    Enter threshold value:50
    Exception occurred:[Errno 2] No such file or directory: 'students.csv'


## Exercise 3
Write a Python function that prints the last `num_lines` of a files.

The function should be called `file_read_from_tail` that receives two parameters: `fname` (a string with the complete path of the file to be read), and `num_lines` (an integer, representing number of lines to be read).

### Rubric (20 marks)

*Correct Inputs (3 marks):*
 - signature should be "file_read_from_tail(fname, num_lines)" (1)
 - Correctly reads the fname file. (2)

*Error Handling (2 marks):*
 - Include error handling for file opening (try-except) (2)

*Processing steps (4 marks):*
 - Reads and stores the contents of the file up to num_lines. (4)

*Output (4):*
• Outputs the results from the Processing step. (10%)
• Notify user that there was an error. (10%)

*Style (2 marks)*
 -  PEP (variables and functions all lower case. Meaningful names)


```python
# people can be really creative here. They may iterate over the thing, somehow
# to figure out the num_lines latest ones

def file_read_from_tail(fname, num_lines):
  try:
    # opening the file in read mode
    with open(fname,'r') as file_iterator:

      # creating the instance of file reader
      reader = csv.reader(file_iterator)

      # creating the rows list using the file reader
      rows = [row for row in reader]

      # slicing the list to pring last lines
      print(rows[-num_lines:])

      # # reading all lines from the file iterator
      # lines = file_iterator.readlines()

      # # printing the lines using list slicing
      # print(lines[-num_lines:])

      # creating the instance of file reader and making it a list
      #reader = list(csv.reader(file_iterator))

      # slicing the list to pring last lines
      #print(rows[-num_lines:])  

  # handling the exception
  except Exception as e:
    print("Exception occurred:{}".format(e))

file_read_from_tail('students.csv',2)
```

    [['9963', 'aMHBe', '48'], ['5789', 'nzzyF', '86']]


## Exercise 4
*Deja-vu (HW1)*
Please revisit the solution of the following examples from HW1 (Exercise 2, and Exercise 4), and capture and handle all possible exceptions.

**Exercise 2.** Write a Python program that, given two integers input by the user, calculates and displays the addition, subtraction, multiplication and division of these two numbers.


**Exercise 4.** Write a Python program that, given the scores (0-100) of three exams, calculates and displays the student's final grade, considering that the final grade is the average of the three exams. 

*TIP: You can consider grades as integer values (`int`) or decimal (`float`), but remember that the average is the result of a division and must therefore be decimal (`float`).*

### Rubric (20 marks)

*Error handling (20 marks)*
All of the student’s code should be surrounded by try/except clauses that handle the appropriate errors.
- conversions to int or float need to be surrounded by try-except  (there will be cases in both exercises...)
- division needs to be surrounded by try-except


```python
# HW_1 Exercise - 2
# Write a Python program that, given two integers input by the user, calculates 
# and displays the addition, subtraction, multiplication and division 
# of these two numbers.

try:
  # type conversion of inputs to float
  # if they do int it is OK as well
  a=float(input("Enter the first number: "))
  b=float(input("Enter the second number: "))


# handling type conversion exceptions
except ValueError:
  print("Invalid inputs")
# I do not expect them to catch the KeyboardInterrupt, but it may appear
except KeyboardInterrupt:
  print("No input! Bye bye!")

else:
  # addition of inputs
  print(f"{a} + {b} = ", a+b)

  # absolute difference of inputs
  print(f"{a} - {b} = ", a-b)

  # multiplication of inputs
  print(f"{a} * {b} = ", a*b)
  try:

    # division of inputs
    print(f"{a} / {b} = ", a/b)

  # handling division by zero exception
  except ZeroDivisionError:
    print("Division by Zero")

  # handling other exception
  except Exception as e:
    print("Exception:{}".format(e))



```

    Enter the first number: 3
    Enter the second number: 3.2
    3.0 + 3.2 =  6.2
    3.0 - 3.2 =  -0.20000000000000018
    3.0 * 3.2 =  9.600000000000001
    3.0 / 3.2 =  0.9375



```python
# Write a Python program that, given the scores (0-100) of three exams, calculates and 
# displays the student's final grade, considering that the final grade is the average of the three exams.

# TIP: You can consider grades as integer values (int) or decimal (float),
#  but remember that the average is the result of a division and must therefore be decimal (float).
try:
  # inputs and conversion: may trigger ValueError
  score1 = float (input("Please enter the score of exam 1 between 0 and 100 : "))
  score2 = float (input("Please enter the score of exam 2 between 0 and 100 : "))
  score3 = float (input("Please enter the score of exam 3 between 0 and 100 : "))
  final_grade=(score1+score2+score3)/3
  #output - final average score
  print("Final grade of three exams is : %.2f" %final_grade)
# handling type conversion exception
except ValueError:
  print("Invalid inputs")

# handling other exceptions
except Exception as e:
  print("Exception:{}".format(e))

2
```

    Please enter the score of exam 1 between 0 and 100 : 21
    Please enter the score of exam 2 between 0 and 100 : 3
    Please enter the score of exam 3 between 0 and 100 : 34
    Final grade of three exams is : 19.33


## Exercise 5
*Deja-vu (HW3)*

Let's revisit Exercise 5 from HW3, making sure we capture potential exceptions. This would include potential errors during the input raising a new `IndexError` when n is greater than the length of the list. (Feel free to bring any function you need)

**Problem5**

Write a program that returns the nth smallest and the nth largest numbers in a list. Both the list numbers and the `n` need to be input by the user. The list must be composed ONLY by integers .

You must implement 3 functions here: 
* `inputs_for_list()` which will return a list (with numbers input by the user)
* `nth_smallest_value(lst, n)` which will return one item of the list
* `nth_largest_value(lst, n)` which will return one item of the list

Some constraints:
1. The function `inputs_for_list` is one case in which `input` is used in a function.
2. The user must be requested to input numbers to the list until he types "exit" (in this case the function must return the list)
3. The list MUST have only  or ints (use the function created on Problem 3 to check each input)    
  * Be careful, you must check if the user wants to exit before checking
  * In case the user types anything that is not a number, you must not consider the number and request a new input.

4. `n` can be requested as part of the main body of your program


Important: in case of repeated numbers, you count them as just ONCE. For example, in the list `[1,2,2,2,3,3,4]` the 3rd smallest number is `3` while the 3rd greatest is `2`

### Problem 5:
*Error handling (20 marks)*

All of the student’s code should be surrounded by try/except clauses that handle the appropriate errors.
- conversions to int or float need to be surrounded by try-except  
- accessing the index of a list/set on nth_smallest_value anmd nth_largest_value --> THEY MAY or MAYNOT need.



```python
# The goal here is FOCUS ON EXCEPTIONS

# function to scan inputs from the user
def inputs_for_list():
  # initializing the input elements list
  list_elements = [] 
  
  #students may be creative here... using flags or the while condition
  while True:
    try:
      # taking the user input
      value = input("Enter list element or enter exit to stop input scan:")

      # check the value and stop the input scan if it is 'exit'
      if (value.lower()=='exit'):
        break
      
      # adding the integer input to the input elements list
      list_elements.append(int(value))

    # handling the type conversion exceptions
    # Students may only print the exception
    except ValueError:
      print("Enter valid input")
    
    # handling other exceptions
    except Exception as e:
      print("Exception:{}".format(e))
      break
  
  # returning the inputs elements list
  return list_elements
```


```python
# function to find nth smallest value
def nth_smallest_value(lst, n):
  try:
    # taking the unique elements in the given list
    unique_sorted_elements = list(set(lst))

    # check whether nth smallest can be calculated or not
    if len(unique_sorted_elements) < n:
      print("nth_smallest_value cannot be calculated")
      return -1

    # returning the nth smallest value
    return unique_sorted_elements[n-1]
  
  # handling indexing related exceptions
  except IndexError:
    print("Index Error")
  
  # handling other exceptions
  except Exception as e:
    print("Exception:{}".format(e))
```


```python
# function to find nth largest value
def nth_largest_value(lst, n):
  try:
    # taking the unique elements in the given list
    unique_sorted_elements = list(set(lst))

    # check whether nth largest can be calculated or not
    if len(unique_sorted_elements) < n:
      print("nth_largest_value cannot be calculated")
      return -1

    # returning the nth largest value
    return unique_sorted_elements[len(unique_sorted_elements)-n]
  
  # handling indexing related exceptions
  except IndexError:
    print("Index Error")
  
  # handling other exceptions
  except Exception as e:
    print("Exception:{}".format(e))
```


```python
# it is not mandatory to have this, OK?

def execute_function():
  try:
    # function call to scan the integer inputs
    input_list = inputs_for_list()

    # sorting the integer inputs
    input_list.sort()

    # printing the input integer elements in sorted order
    print("Elements:{}".format(input_list))

    # taking the user input for n value
    n = int(input("Enter value of n:"))

    # checking whether n is valid or not i.e. greater than zero
    if(n>0):
      # call for the nth smallest number
      smallest_value = nth_smallest_value(input_list, n)

      # checking whether nth smallest is calculated or not
      if smallest_value !=-1:
        print("{} smallest value:{}".format(n, smallest_value))

      # call for the nth largest number
      largest_value = nth_largest_value(input_list, n)

      # checking whether nth largest is calculated or not
      if largest_value !=-1:
        print("{} largest value:{}".format(n, largest_value))
    else:
      print("Invalid input")

  # handling type conversion exceptions
  except ValueError:
    print("Invalid input")

  # handling other exceptions
  except Exception as e:
    print("Exception:{}".format(e))

execute_function()
execute_function()
```

    Enter list element or enter exit to stop input scan:edsg
    Enter valid input
    Enter list element or enter exit to stop input scan:12
    Enter list element or enter exit to stop input scan:51
    Enter list element or enter exit to stop input scan:12
    Enter list element or enter exit to stop input scan:12
    Enter list element or enter exit to stop input scan:436
    Enter list element or enter exit to stop input scan:34
    Enter list element or enter exit to stop input scan:1235
    Enter list element or enter exit to stop input scan:123
    Enter list element or enter exit to stop input scan:ex
    Enter valid input
    Enter list element or enter exit to stop input scan:exit
    Elements:[12, 12, 12, 34, 51, 123, 436, 1235]
    Enter value of n:4
    4 smallest value:436
    4 largest value:51
    Enter list element or enter exit to stop input scan:dgrgw
    Enter valid input
    Enter list element or enter exit to stop input scan:12
    Enter list element or enter exit to stop input scan:123
    Enter list element or enter exit to stop input scan:1234
    Enter list element or enter exit to stop input scan:12
    Enter list element or enter exit to stop input scan:123
    Enter list element or enter exit to stop input scan:1234
    Enter list element or enter exit to stop input scan:exit
    Elements:[12, 12, 123, 123, 1234, 1234]
    Enter value of n:10
    nth_smallest_value cannot be calculated
    nth_largest_value cannot be calculated



```python
e
```
