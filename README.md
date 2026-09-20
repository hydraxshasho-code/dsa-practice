# DSA Practice 🚀
LeetCode solutions in Python | My DSA journey

## Problems Solved

### 1 Two Sum
**Approach:** HashMap - stored complement in dictionary  
**Time:** O(n) | **Space:** O(n)  
**Learning:** Check if target-num exists in dict before adding current num

## 2 Best time to buy and sell stock II
**Approach:** Greedy Algorithm- add the profit whenever the price increases from previous day without worrying about the future by pairing the first two consecutive pair.
**Time:** O(n) | ** Space:*O(1)
**Learning:**- arnt what actually Greedy algorithm is , multiple transcations are allowed so capture every upward price movement instead of finding single best buy-sell pair.

## 3 Best Time to Buy and Sell Stock I
**Approach:** Track minimum price seen so far, calculate max profit at each step
**Time:** O(n) | **Space:** O(1)
**Learning:** Single transaction allowed — only need to track the best buy point and compare against it, unlike Stock II

## 4 Move Zeroes
**Approach:** Two Pointer — track position for next non-zero element, swap when found
**Time:** O(n) | **Space:** O(1)
**Learning:** Two-pointer isn't greedy — no profit/optimization decision, just position management while traversing.
## 5 Reverse Linked List
**Approach:** Three Pointer — track prev, current, and next node while reversing links iteratively
**Time:** O(n) | **Space:** O(1)
**Learning:** Learned linked list fundamentals (nodes linked via pointers, no direct index access) and the three-pointer technique for reversal
## 6 Longest Substring Without Repeating Characters
**Approach:** Sliding Window — two pointers (left, right) with a set tracking characters in current window; shrink window from left when duplicate found ( learned for the first time)
**Time:**a O(n) | **Space:** O(min(n, 26))
**Learning:** set() alone gives unique characters overall, not the longest continuous substring — needed sliding window to track a continuous, valid stretch