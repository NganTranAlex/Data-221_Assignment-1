# Data-221_Assignment-1
--- QUESTION 1 --- <br>
With the product and the current number both start at 1, the multiplication loop will carry out as: <br>
1 * 1 = 1 <br>
1 * 2 = 2 # The current number will increase by 1 each time after the multiplication is carried out <br>
2 * 3 = 6 <br>
6 * 4 = 24 <br>
24 * 5 = 120 # This is where the loop stops because it exceed the threshold, for which the threshold = 100 <br>
Before printing the final product, since the last multiplication is carried out to get the final product, the current number is currently at 6. <br>
To get the number that causes the product to exceed the threshold, we just simply take the current number minus 1, then print it out along with the final product. <br>
<br>
--- QUESTION 2 --- <br>
According to the question, an empty dictionary is created first within the function for storing the outputs later. <br>
Then it is looped through each string in the provided list using a for loop to make sure no string is excluded, and then calculate the length of each string using the len() function. <br>
After that I checked the parity of the string based on the number of length for each string to determine if it is "even" or "odd". <br>
Finally, I stored the length along with the parity of the strings as a nested dictionary for each string and simply return the dictionary I created at the start. <br>
<br>
--- QUESTION 3 --- <br>
Since the question tells me to store the valid results in a list for the output, I first created an empty list within the function for later use. <br>
It is given a list of pairs of x and y, I just simply loop through every pairs included in the given input with a condition that if y < 0, then that pair is not calculated and skipped through using the 'continue' function. <br>
If a pair satisfies the given condition, then the calculation is carried out by taking the first number in the pair, which is x, to the power of the second number in the pair, which is y (x ** y). <br>
Then the list 'append' function is used to add the pairs that are calculated to the empty list and return the list from the function to print and get the desired output. <br>
<br>
--- QUESTION 4 --- <br>
I started the code with the given starter code in the question to get random numbers for both the "values" list and the variable x. <br>
Following the question, I used the 'sort()' function to sort out the list of random numbers so that the values are organized in an increasing order. <br>
To determine if the first index exists, I just simply started by assuming it does not exist by using the 'None' function. <br>
After that, I looped through the sorted list by their indices to determine which value is greater than or equal to x. <br>
The loop stops if the first index is found (if there is one), and if the first index exists using the 'is not None' function. <br>
Finally, I printed out the sorted list, the value of x and the first matching index if it does exist. <br>
<br>
--- QUESTION 5 --- <br>
Firstly, I used 'import math' to get 'math.pi' for the PI number for more accurate answer instead of using '3.14'. <br>
Then I would use the 'if' condition to check if the radii of both circles satisfy the condition of whether they're positive integers are not. If an invalid input is provided, I would return a short message so that the user knows that their input is wrong and that the calculations are not carried out. <br>
If both radii satisfy the condition, I move on to calculating the area of both circles by using simple calculating functions (radius * radius * PI). <br>
Moving on to comparing whether the area of the first circle (circle 1) is larger than the area of the second circle (circle 2), or vice versa, I used the 'if - else' condition to compare them and clearly distinguish the circles' areas by putting them into new variables such as "smaller_circle" and "larger_circle". <br>
I then returned the percentage of the larger circle's area that can be covered by the smaller circle by using the area of the smaller circle dividing the area of the larger circle, then multiplying that division by 100 to get the desired percentage. <br>
<br>
--- QUESTION 6 --- <br>
An empty dictionary is first created to store the output. <br>
Then I used the 'len()' function to count the total number exist in the list, so that it can be used to calculate the percentage later. <br>
By definition, unique value is a number that is only counted once no matter how many times it repeats. A function that suit this definition the most is the 'set()' function to remove any duplicates and sort them to ensure that the resulting values are sorted by the key before returning. <br>
Continuously, for each unique value (the key), I counted how many numbers in the given original list that is less than or equal to it, and converted into percentage by taking the counted value divided by the total numbers exist in the original list, multiplying it to 100. <br>
Finally, I simply stored the them in the dictionary by the keys and their percentage. <br>
<br>
--- QUESTION 7 --- <br>
I first validated the input by checking if the number of seconds is within a day (24 hours). <br>
Then using simple python calculations I converted the total seconds into hours, minutes, and the remaining seconds. <br>
After that, based on the value of the current hour, I determined whether the time is in AM or PM (based on a 24-hour time). <br>
Since all of the calculations and time period are based on 24-hour time, I had to convert them into 12-hour clock by adjusting the hour for midnight and the time in the afternoon (since the 12-hour clock starts from 1 again after 12PM). Then I simply return the result in the given format. <br>
<br>
--- QUESTION 8 --- <br>
Based on the starter code I used pip install to get the pandas package in python terminal. <br>
I stored the data frame into a variable of the given A, B, and C columns. <br>
Then I created a new column based on the total of values given in the first three columns and print out the final data frame. <br>
