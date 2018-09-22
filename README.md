# Hash Table Implementation Lab

+ __Author__: John Broere
+ __Email__: jbroere@siue.edu
+ __Date__: Fall 2018
+ __Company__: Southern Illinois University Edwardsville
+ __Course__: CS534 - Advanced Database Management Systems
+ __Professor__:  Mark McKenney, Ph.D.

***

```
usage: Hasher [-h] [-s n] [-c n] [-r] [-v]

Hash Table Implementation Lab

optional arguments:
  -h, --help        show this help message and exit
  -s n, --size n    size of the hash table [default: 10]
  -c n, --cycles n  number of cycles to run [default: 1]
  -r, --random      use random numbers for insert [default: sequential]
  -v, --verbose     display verbose output
```

***

```
Experiment 1 (sequential numbers):
  arraySize = 10
  cycles = 10

successful    |     average
insertions    |     success
__________    |   ___________
  10/10       |     100.0%
   6/10       |      60.0%
   6/10       |      60.0%
  10/10       |     100.0%
   1/10       |      10.0%
  10/10       |     100.0%
  10/10       |     100.0%
   5/10       |      50.0%
  10/10       |     100.0%
  10/10       |     100.0%
      Overall Results
 78/100       |      78.0%
```
```
 Experiment 1 (random numbers):
   arraySize = 10
   cycles = 10

 successful    |     average
 insertions    |     success
 __________    |   ___________
    6/10       |      60.0%
    5/10       |      50.0%
    2/10       |      20.0%
    8/10       |      80.0%
    5/10       |      50.0%
    7/10       |      70.0%
    4/10       |      40.0%
    9/10       |      90.0%
    5/10       |      50.0%
    3/10       |      30.0%
       Overall Results
  54/100       |      54.0%
```

***

```
Experiment 2 (sequential numbers):
  arraySize = 100
  cycles = 10

successful    |     average
insertions    |     success
__________    |   ___________
  20/100      |      20.0%
  20/100      |      20.0%
 100/100      |     100.0%
  50/100      |      50.0%
 100/100      |     100.0%
  75/100      |      75.0%
  51/100      |      51.0%
  26/100      |      26.0%
 100/100      |     100.0%
  30/100      |      30.0%
      Overall Results
572/1000      |      57.2%
```

```
Experiment 2 (random numbers):
  arraySize = 100
  cycles = 10

successful    |     average
insertions    |     success
__________    |   ___________
  18/100      |      18.0%
  15/100      |      15.0%
  27/100      |      27.0%
  19/100      |      19.0%
  20/100      |      20.0%
  13/100      |      13.0%
  17/100      |      17.0%
  12/100      |      12.0%
   6/100      |       6.0%
  11/100      |      11.0%
      Overall Results
158/1000      |      15.8%
```

***

## Conclusion

For some reason, I saw a lot more collisions when I was attempting to insert
numbers into the hash table instead of sequential numbers. I am not sure if
this was due to the fact that even random numbers have a chance of repeating
while sequential numbers do not. I even tried changing the random range and
continued to see the same results.
