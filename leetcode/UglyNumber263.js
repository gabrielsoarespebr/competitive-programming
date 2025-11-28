// platform: leetcode - https://leetcode.com/problems/ugly-number
// programming language: JavaScript
// status: Time Limit Exceeded (514 / 1013 testcases passed)

// author: Gabriel Soares
// https://www.linkedin.com/in/gabrielsoarespebr/
// https://github.com/gabrielsoarespebr

/*
 * @param {number} n
 * @return {boolean}
 */
var isUgly = function (n) {
  let result = false;

  if (n <= 0) return result;

  for (let i = 7; i <= n; i++) {
    if (isPrimeNumber(i)) {
      if (n % i === 0) return result;
    }
  }

  result = true;
  return result;
};

const isPrimeNumber = (numberToCheck) => {
  const factorList = [];

  for (let numberTemp = 2; numberTemp < numberToCheck; numberTemp++) {
    if (numberToCheck % numberTemp === 0) {
      factorList.push(numberTemp);
    }

    if (factorList.length > 0) return false;
  }

  return true;
};
