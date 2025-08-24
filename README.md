# Greatest Common Divisor of Strings
LeetCode

# Question:

For two strings s and t, we say "t divides s" if and only if s = t + t + t + ... + t + t (i.e., t is concatenated with itself one or more times).

Given two strings str1 and str2, return the largest string x such that x divides both str1 and str2.

Example 1:

Input: str1 = "ABCABC", str2 = "ABC"
Output: "ABC"
Example 2:

Input: str1 = "ABABAB", str2 = "ABAB"
Output: "AB"
Example 3:

Input: str1 = "LEET", str2 = "CODE"
Output: ""

# Ans + Dry Run:


Python
str1 = "ABABAB"
str2 = "AB"
```

---

# 📌 Code Recap

```python
class Solutions(object):
    def gcdOfStrings(self, str1, str2):
        if str1 + str2 != str2 + str1:
            return ""   # not compatible, no gcd string

        if len(str1) == len(str2):
            return str1  # equal length, must be answer

        if len(str1) > len(str2):
            return self.gcdOfStrings(str1[len(str2):], str2)

        return self.gcdOfStrings(str1, str2[len(str1):])
```

---

# 📌 Step-by-step Execution

### Initial call:

```python
gcdOfStrings("ABABAB", "AB")
```

1. **Check concatenation**
   `"ABABAB" + "AB" = "ABABABAB"`
   `"AB" + "ABABAB" = "ABABABAB"`
   ✅ Equal → valid, continue.

2. **Check lengths**
   len("ABABAB") = 6, len("AB") = 2 → not equal.

3. **Check greater length**
   `len("ABABAB") > len("AB")` → True
   So recurse:

   ```python
   gcdOfStrings("ABABAB"[2:], "AB")
   gcdOfStrings("ABAB", "AB")
   ```

---

### Second call:

```python
gcdOfStrings("ABAB", "AB")
```

1. **Check concatenation**
   `"ABAB" + "AB" = "ABABAB"`
   `"AB" + "ABAB" = "ABABAB"`
   ✅ Equal.

2. **Check lengths**
   len("ABAB") = 4, len("AB") = 2 → not equal.

3. **Greater length?**
   Yes, `len("ABAB") > len("AB")`.
   So recurse:

   ```python
   gcdOfStrings("ABAB"[2:], "AB")
   gcdOfStrings("AB", "AB")
   ```

---

### Third call:

```python
gcdOfStrings("AB", "AB")
```

1. **Check concatenation**
   `"AB" + "AB" = "ABAB"`
   `"AB" + "AB" = "ABAB"`
   ✅ Equal.

2. **Check lengths**
   len("AB") = 2, len("AB") = 2 → Equal
   So return `"AB"`.

---

# 📌 Backtracking results

* Third call returned `"AB"`
* Second call returns `"AB"`
* First call returns `"AB"`

✅ Final Output:

```
AB
```

---

# 📌 How this recursion works

This solution is mimicking the **Euclidean Algorithm for GCD of numbers**:

* If `str1` is longer, cut off the prefix of length `len(str2)` (since we know they match due to the concatenation check).
* Keep recursing until lengths match.
* The final result is the **string GCD**.
