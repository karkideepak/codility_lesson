
Key idea:
Convert N to binary.

Walk through the bits.
Start counting zeros after the first 1.
Every time you hit another 1, close the gap and update the maximum.
Trailing zeros don’t count unless they’re followed by a 1.

Here’s an efficient Python solution (O(number of bits), constant extra space):
How it works with examples

9 (1001) → gap of 2 → returns 2
529 (1000010001) → gaps of 4 and 3 → returns 4
20 (10100) → gap of 1 → returns 1
15 (1111) → no gaps → returns 0
32 (100000) → trailing zeros only → returns 0
1041 (10000010001) → longest gap is 5

This handles the full range [1..2,147,483,647] efficiently and doesn’t even need to build a binary string.
