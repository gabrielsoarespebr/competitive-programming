// platform: leetcode - https://leetcode.com/problems/alternating-groups-i
// programming language: JavaScript
// status: Accepted

// author: Gabriel Soares
// https://www.linkedin.com/in/gabrielsoarespebr/
// https://github.com/gabrielsoarespebr

/*
 * @param {number[]} colors
 * @return {number}
 */
var numberOfAlternatingGroups = function (colors) {
  const groupSize = 3;
  const circularArray = [...colors];

  for (let i = 0; i < groupSize - 1; i++) {
    circularArray.push(colors[i]);
  }

  let result = 0;

  for (let i = groupSize - 1; i < circularArray.length; i++) {
    if (
      circularArray[i - 1] !== circularArray[i] &&
      circularArray[i - 1] !== circularArray[i - 2]
    ) {
      result += 1;
    }
  }

  return result;
};
