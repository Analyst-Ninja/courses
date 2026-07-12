"""
Frozen Sets: Unordered, immutable collections of unique elements.
They are hashable and can be used as keys in dictionaries or elements of other sets.
"""

# Tracking mutual friendships (order doesn't matter)
friendships = set()
friendships.add(frozenset({"Alice", "Bob"}))
friendships.add(frozenset({"Bob", "Alice"}))  # same pair, ignored

print(friendships)  # {frozenset({'Alice', 'Bob'})}
print(len(friendships))  # 1

# Deduplicating lists of lists using frozensets
raw_groups = [
    ["a", "b", "c"],
    ["c", "b", "a"],  # same as first
    ["a", "b"],
]

unique = {frozenset(g) for g in raw_groups}
print(unique)  # {frozenset({'a', 'b'}), frozenset({'a', 'c', 'b'})}
print(len(unique))  # 2
