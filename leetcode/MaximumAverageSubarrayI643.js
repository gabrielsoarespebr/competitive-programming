// platform: leetcode - https://leetcode.com/problems/maximum-average-subarray-i
// programming language: JavaScript
// status: Accepted

// author: Gabriel Soares
// https://www.linkedin.com/in/gabrielsoarespebr/
// https://github.com/gabrielsoarespebr

/*
 * @param {number[]} nums
 * @param {number} k
 * @return {number}
 */
var findMaxAverage = function (nums, k) {
  const n = nums.length;

  if (n === 1) return nums[0];

  let sumTemp = 0;

  for (let i = 0; i < k; i++) {
    sumTemp += nums[i];
  }

  let maxAverage = sumTemp / k;

  let indexToRemove = null;
  let indexToAdd = null;

  for (let i = 1; i < n; i++) {
    indexToRemove = i - 1;
    indexToAdd = i + k - 1;

    sumTemp -= nums[indexToRemove];
    sumTemp += nums[indexToAdd];

    if (sumTemp / k > maxAverage) {
      maxAverage = sumTemp / k;
    }
  }

  return maxAverage;
};
