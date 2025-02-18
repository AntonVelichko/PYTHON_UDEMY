

https://www.youtube.com/watch?v=em-QrwbVxig
https://www.youtube.com/watch?v=fX64q6sYom0
https://www.youtube.com/watch?v=iOxF5cDVIZo
https://www.youtube.com/watch?v=uJA-GVWNjcc
https://www.youtube.com/watch?v=npopDLgUXzU




n = 5
for i in range(n):
  for j in range(n):
    print('*', end = ' ')
  print()

* * * * * 
* * * * * 
* * * * * 
* * * * * 
* * * * * 


-------------------------------------------------------------


n = 5
for i in range(n):
  for j in range(i+1):
    print('*', end = ' ')
  print()

* 
* * 
* * * 
* * * * 
* * * * * 


-------------------------------------------------------------


n = 5
for i in range(n):
  for j in range(i,n):        # or range(n-i)
    print('*', end = ' ')
  print()

* * * * * 
* * * * 
* * * 
* * 
* 
  

-------------------------------------------------------------


n = 5
for i in range(n):
  for j in range(n): 
    if j == n - 1 - i:
      print('*', end = ' ')
    else:
      print(' ', end = ' ')
  print()

        * 
      *   
    *     
  *       
* 


-------------------------------------------------------------


n = 5
for i in range(n):
  for j in range(n): 
    if j >= n - 1 - i:
      print('*', end = ' ')
    else:
      print(' ', end = ' ')
  print()


        * 
      * * 
    * * * 
  * * * * 
* * * * * 


n = 5
for i in range(n):
  for j in range(i,n-1): 
    print(' ', end = ' ')
  for j in range(i + 1):
    print('*', end = ' ')
  print()

        * 
      * * 
    * * * 
  * * * * 
* * * * * 


-------------------------------------------------------------


n = 5
for i in range(n):
  for j in range(i): 
    print(' ', end = ' ')
  for j in range(i, n):
    print('*', end = ' ')
  print()

* * * * * 
  * * * * 
    * * * 
      * * 
        *


-------------------------------------------------------------


n = 5
for i in range(n):
  for j in range(i,n-1): 
    print(' ', end = ' ')
  for j in range(i + 1):
    print('*', end = ' ')
  for j in range(i):
    print('*', end = ' ')
  print()

        * 
      * * * 
    * * * * * 
  * * * * * * * 
* * * * * * * * * 


-------------------------------------------------------------

  
n = 5
for i in range(n):
  for j in range(i):
    print(' ', end = ' ')
  for j in range(i,n): 
    print('*', end = ' ')
  for j in range(i,n-1):
    print('*', end = ' ')
  print()

* * * * * * * * * 
  * * * * * * * 
   * * * * * 
      * * * 
        * 

-------------------------------------------------------------

        
n = 5
for i in range(n-1):
  for j in range(i,n-1): 
    print(' ', end = ' ')
  for j in range(i + 1):
    print('*', end = ' ')
  for j in range(i):
    print('*', end = ' ')
  print()
for i in range(n):
  for j in range(i):
    print(' ', end = ' ')
  for j in range(i,n): 
    print('*', end = ' ')
  for j in range(i,n-1):
    print('*', end = ' ')
  print()

        * 
      * * * 
    * * * * * 
  * * * * * * * 
* * * * * * * * * 
  * * * * * * * 
    * * * * * 
      * * * 
        * 


-------------------------------------------------------------


for i in range(5):
  print(i, '* - ', end = '')
  for j in range(i):
    print(j, end = ' ')
  print()
  
0 * - 
1 * - 0 
2 * - 0 1 
3 * - 0 1 2 
4 * - 0 1 2 3 


-------------------------------------------------------------


for i in range(5):
  print(i, "*")
  for j in range(5):
    print(j, end = ' ')
  print()

0 *
0 1 2 3 4 
1 *
0 1 2 3 4 
2 *
0 1 2 3 4 
3 *
0 1 2 3 4 
4 *
0 1 2 3 4 


-------------------------------------------------------------


for i in range(5):
  print(i, "*")
  for j in range(5):
    print(j, end = ' ')
  print('\n')

0 *
0 1 2 3 4 

1 *
0 1 2 3 4 

2 *
0 1 2 3 4 

3 *
0 1 2 3 4 

4 *
0 1 2 3 4 


