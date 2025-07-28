# 🟢 Palindrome Number

**Problem link:** [Palindrome Number](https://leetcode.com/problems/palindrome-number/)  
**Difficulty:** Easy  
**Runtime:** 34 ms  
**Memory Usage:** 12.3 MB  

### 🧠 Approach
- First, check if the number is non-negative (since negative numbers can't be palindromes).
- Extract each digit using modulo and integer division, store them in a list.
- Reverse the list and compare it with the original.
- If they match, the number is a palindrome.
