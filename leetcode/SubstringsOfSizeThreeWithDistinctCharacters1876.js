// platform: leetcode - https://leetcode.com/problems/substrings-of-size-three-with-distinct-characters
// programming language: JavaScript
// status: Accepted
// Note: Using substring() instead of slice() would be a more elegant way to handle strings in JavaScript. I only realized that after submitting the question.

// author: Gabriel Soares
// https://www.linkedin.com/in/gabrielsoarespebr/
// https://github.com/gabrielsoarespebr

/*
 * @param {string} s
 * @return {number}
 */
var countGoodSubstrings = function (s) {
  let result = 0;

  if (s.length < 3) return result;

  const n = s.length;
  const substringSize = 3;
  let substringTemp = "";

  for (let i = 0; i <= n - substringSize; i++) {
    substringTemp = s.slice(i, i + substringSize);
    const tempSet = new Set(substringTemp.split(""));
    if (tempSet.size === substringSize) {
      result += 1;
    }
  }

  return result;
};
