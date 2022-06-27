# ugly-numbers
This is a solution to the google ugly numbers problem:</br>
I came across this in a coding interview:</br>

The question:</br>
Ugly Numbers</br>
Programming challenge description:</br>
Credits: This challenge has appeared in a google competition.</br>

Once upon a time in a strange situation, people called a number ugly if it was divisible by any of the one-digit primes (2, 3, 5 or 7). Thus, 14 is ugly, but 13 is fine. 39 is ugly, but 121 is not. Note that 0 is ugly. Also note that negative numbers can also be ugly; -14 and -39 are examples of such numbers.</br>

One day on your free time, you are gazing at a string of digits, something like:</br>
123456</br>
You are amused by how many possibilities there are if you are allowed to insert plus or minus signs between the digits. For example you can make:</br>

1 + 234 - 5 + 6 = 236</br>
which is ugly. Or</br>
123 + 4 - 56 = 71</br>
which is not ugly.</br>

It is easy to count the number of different ways you can play with the digits: Between each two adjacent digits you may choose put a plus sign, a minus sign, or nothing. Therefore, if you start with D digits there are 3^(D-1) expressions you can make. Note that it is fine to have leading zeros for a number. If the string is '01023', then '01023', '0+1-02+3' and '01-023' are legal expressions.</br>

Your task is simple: Among the 3^(D-1) expressions, count how many of them evaluate to an ugly number.</br>
Input:</br>
Your program should read lines of text from standard input. Each line will consist of a non-empty string containing only the characters '0' through '9'. Each string is no more than 13 characters long.</br>
Output:</br>
For each input string, print to standard output the number of expressions that evaluate to an ugly number, one number per line.</br>
Test 1</br>
Test Input</br>
Download Test 1 Input</br>
1</br>
Expected Output</br>
Download Test 1 Input</br>
0</br>
Test 2</br>
Test Input</br>
Download Test 2 Input</br>
9</br>
Expected Output</br>
Download Test 2 Input</br>
1</br>
Test 3</br>
Test Input</br>
Download Test 3 Input</br>
011</br>
Expected Output</br>
Download Test 3 Input</br>
6</br>
Test 4</br>
Test Input</br>
Download Test 4 Input</br>
12345</br>
Expected Output</br>
Download Test 4 Input</br>
64</br>
