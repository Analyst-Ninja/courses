# Sets:
# 1. Unordered
# 2. Mutable
# 3. No Duplicates

mySet = {1, 2, 3, 4, 5, 5}
mySet = set([1, 2, 3, 4, 5, 5])
mySet = set(
    "Hello"
)  # O/P --> {'H', 'e', 'o', 'l'} --> Unordered --> Order Not Maintained

print(mySet)

# mySet2 = {} # Will Create a Empty Dict
mySet2 = set()  # Will Create a Empty Set

mySet2.add(1)
mySet2.add(1)
mySet2.add(2)
mySet2.add(4)

mySet2.remove(4)

# mySet2.remove(5) # Raise Key Error if element is not there

mySet2.discard(5)  # Remove Element but Doesn't Raise Error if element is not there

mySet2.clear()  # Clear the Set

mySet.pop()  # Remove Arbitary Element

print(mySet)

for i in mySet2:
    print(i)

odds = {1, 3, 5, 7, 9}
evens = {2, 4, 6, 8, 10}
primes = {2, 3, 5, 7, 11}

print(odds.union(evens))  # A union B
print(odds.intersection(evens))  # A intersection B --> Returns a Empty set
print(odds.intersection(primes))
print(odds.difference(primes))  # A - B
print(odds.symmetric_difference(primes))  # Remove the number which are in both the sets

# odds.update(evens) # Update the set

# odds.intersection_update(primes) # Keeping the element present in both the sets
# odds.difference_update(primes) # Keeping the element present in both the sets

print(odds)

setA = {1, 2}
setB = {1, 2, 3}
setC = {4, 5}

print(setA.issubset(setB))
print(setA.issuperset(setB))

print(setA.isdisjoint(setB))  # Return True if No Element is Common
print(setA.isdisjoint(setC))  # Return True if No Element is Common

# Frozen Set --> Set that is Immuatble

fSet = frozenset([1, 2, 3, 4, 5])

# fSet.add(10) # Will give a attribute error --> Once the Frozen Set is created it can't be changed
# fSet.remove(10) # Will give a attribute error --> Once the Frozen Set is created it can't be changed

print(fSet)
