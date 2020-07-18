#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a)
a = 0
   while (a < n * n * n): # O(n)
     a = a + n * n # O(1)

     Time complexity = O(n) * O(1) = O(n)

b)
sum = 0
   for i in range(n): # O(n)
     j = 1
     while j < n: # O(n-1)
       j *= 2
       sum += 1

       Time complexity: O(n) * O(n-1) = O(n² - n) = O(n^2)


c)
def bunnyEars(bunnies):
      if bunnies == 0:
        return 0

      return 2 + bunnyEars(bunnies-1) # O(1) * O(n!)

Time complexity = O(n!)

## Exercise II





--strategy--
If we throw the eggs form any floor less than 3, that is to say the third floor, the eggs won't break, that is to say broken = 0 and dropped = 10000, therefore: dropped + broken = 10000 + 0 so the strategy would be to throw them from any floor less than the third floor, for example from the first floor, if there is a ground floor, like in the UK, or from the second floor if we are in the USA, where there is no ground floor.

The strategy would be to throw 1 egg from the first floor and see if it breaks,and the same with the second floor, third floor etc until one of them breaks, and once we find out the floor from which the first egg breaks we need to throw them from the immediate inferior floor or less to get the minimum value for dropped + broken

Time complexity will depend on the floor that they will be thrown off of so time complexity = O (n)
