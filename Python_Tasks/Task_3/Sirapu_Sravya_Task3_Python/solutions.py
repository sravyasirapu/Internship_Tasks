# Task 3: Python Coding & Problem-Solving
# Each function returns its result.

# Q1. Find the Frequency of Each Word in a Sentence
def word_frequency(sentence):
    frequency = {}
    for word in sentence.split():
        frequency[word] = frequency.get(word, 0) + 1
    return frequency


# Q2. Find the Frequency of Each Character in a Word
def character_frequency(word):
    frequency = {}
    for char in word:
        frequency[char] = frequency.get(char, 0) + 1
    return frequency


# Q3. Find the First Non-Repeating Character in a Word
def first_non_repeating_character(word):
    frequency = character_frequency(word)
    for char in word:
        if frequency[char] == 1:
            return char
    return None


# Q4. Check Whether Two Strings Are Anagrams
def are_anagrams(s1, s2):
    return character_frequency(s1) == character_frequency(s2)


# Q5. Find the First Repeating Character in a String
def first_repeating_character(text):
    seen = set()
    for char in text:
        if char in seen:
            return char
        seen.add(char)
    return None


# Q6. Move All Zeros to the End of a List
def move_zeros_to_end(nums):
    non_zeros = [num for num in nums if num != 0]
    zeros = [num for num in nums if num == 0]
    return non_zeros + zeros


# Q7. Find the Second Highest Distinct Number in a List
def second_highest_distinct(nums):
    distinct = sorted(set(nums), reverse=True)
    return distinct[1] if len(distinct) >= 2 else None


# Q8. Remove Duplicates Without Changing the Original Order
def remove_duplicates_preserve_order(nums):
    result = []
    seen = set()
    for num in nums:
        if num not in seen:
            result.append(num)
            seen.add(num)
    return result


# Q9. Find the Missing Number from 1 to N
def find_missing_number(nums, n):
    expected_sum = n * (n + 1) // 2
    return expected_sum - sum(nums)


# Q10. Find Two Numbers Whose Sum Equals a Target
def first_pair_with_sum(nums, target):
    for second_index in range(len(nums)):
        for first_index in range(second_index):
            if nums[first_index] + nums[second_index] == target:
                return [nums[first_index], nums[second_index]]
    return []


# Q11. Find the Number Closest to Zero
def closest_to_zero(nums):
    if not nums:
        return None
    return min(nums, key=lambda number: (abs(number), -number))


# Q12. Find Common Elements Between Two Lists
def common_elements(list1, list2):
    values_in_second = set(list2)
    result = []
    seen = set()
    for item in list1:
        if item in values_in_second and item not in seen:
            result.append(item)
            seen.add(item)
    return result


# Q13. Rotate a List to the Right by K Positions
def rotate_right(nums, k):
    if not nums:
        return []
    k = k % len(nums)
    if k == 0:
        return nums.copy()
    return nums[-k:] + nums[:-k]


# Q14. Find the Maximum Sum of Two Consecutive Elements
def maximum_consecutive_pair_sum(nums):
    return max(nums[index] + nums[index + 1] for index in range(len(nums) - 1))


# Q15. Find All Pairs of Numbers Whose Sum Equals a Target
def all_unique_pairs_with_sum(nums, target):
    pairs = set()
    for first_index in range(len(nums)):
        for second_index in range(first_index + 1, len(nums)):
            if nums[first_index] + nums[second_index] == target:
                pairs.add(tuple(sorted((nums[first_index], nums[second_index]))))
    return [list(pair) for pair in sorted(pairs)]
