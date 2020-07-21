#### Please add your answers to the **_Analysis of Algorithms_** exercises here.

## Exercise I

a)

       a = 0
       while (a < n * n * n):      # times it runs O(n^3)
          a = a + n * n   # one operation is O(1)

           O(1) * O(n^3) = O(n^3)

solution:
runtime = O(n^3)

b)
sum = 0 # O(1)
for i in range(n): # O(n)
j = 1 # O(1)
while j < n: # O(1)
j \*= 2 # O(1)
sum += 1 # O(1)

#########################################################
runtime = O(1) + O(n) _ O(1) _ O(1) _ ( O(1) + O(1) ) =
= O(1) + O(n) _ O(2)=
= O(1) + O(2n) =
we take the biggest term only:
= O(2n)
############################################################

In big-O (worst-case) we eliminate any term whose contribution to the total is insignificant as n becomes large. So:

runtime = O(2n) for small sets of data
worst-case = O(n) for large sets of data

SOLUTION -> runtime complexity = O(n)

c)
def bunnyEars(bunnies):
if bunnies == 0:
return 0

      return 2 + bunnyEars(bunnies-1) # O(2) + O(n!) = O(n!)

      it's standard in Big-O to consider O(k) as O(1) so we would write O(1) instead of O(k) or O(2) or O(3), etc... so:
      runtime = O(1) + O(n!)

      We consider only the biggest term here so:
      runtime = O(n!)

Runtime = O(n!)

## Exercise II

--strategy--
Plan
we start by throwing an egg from the ground floor (in the UK) (or the first floor (in the USA)) and see if it breaks, if it doesn't, we take it to the first floor if they can be reused, or we try with a new one if it can't be reused and try again, if it doesn't break we try yet again a floor higher, and we keep doing this until we find the floor where if thrown it breaks and that floor is f.

So if we are in the USA and the floor at the street level is the first floor:
case a) if eggs can be reused, we will only break one egg once we reach f and therefore:
dropped eggs = 1
broken = 1
solution -> dropped + broken = 1 + 1 = 2

case b) if I have to use a different egg each time because after the first impact it might get a bit damage internally, like a helmet that falls from your hand and impacts the floor becomes more likely to break if you have an accident later on, we'll have to try with a different egg each time and so the minimum number of broken eggs will be n and therefore:

dropped eggs = number of floors we try until first egg breaks = n
broken \_eggs = 1

solution --> dropped + broken = n + 1

floors = [n]
eggs = 10000
f = 0 #floor on which the first egg breaks
broken = 0
current_floor = 0 or None
eggIsBroken = False

function throw_and_egg ():

if egg breaks:
eggs -= 1
broken += 1

        return 1

loop thru list of floors: #O(n)

    #base case
    if eggIsBroken == True:
        return floor at which it broke          # O(1)

    current_floor += 1                          # O(1)

    if throw_and_egg() == 1: #if it breaks      # O(1)
        return current_floor                   # O(1)

---

For If statements we take the slowest sequence of statements, in this case we take O(1)

Here the runtime depends on which floor it breaks on, if it breaks on the first floor would be best-case scenario and that would be O(1), average case would be O(3n), where n is the number of floors the building has, so the worst-case scenario (time complexity) would be O(n).

SOLUTION:
best-case scenario and that would be O(1)
best-case = O(1)
average-case = O(n) \* ( O(1) + O(1) + O(1) ) = O(3n)

"3" becomes insignificant when n is huge, we can eliminate it:

worst-case scenario = runtime complexity O(n)
