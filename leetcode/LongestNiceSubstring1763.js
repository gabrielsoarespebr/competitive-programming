// platform: leetcode - https://leetcode.com/problems/longest-nice-substring
// programming language: JavaScript
// status: Accepted

// author: Gabriel Soares
// https://www.linkedin.com/in/gabrielsoarespebr/
// https://github.com/gabrielsoarespebr

/*
 * @param {string} s
 * @return {string}
 */
var longestNiceSubstring = function (s) {
  let result = "";

  if (s.length === 1) return result;

  if (s.length === 2) {
    let isFirstCaractereLowerCase = true;
    let isSecondCaractereLowerCase = true;
    let sameLetter = true;

    const firstCaractere = s[0];
    const secondCaractere = s[1];

    if (firstCaractere !== firstCaractere.toLowerCase()) {
      isFirstCaractereLowerCase = false;
    }

    if (secondCaractere !== secondCaractere.toLowerCase()) {
      isSecondCaractereLowerCase = false;
    }

    if (firstCaractere.toLowerCase() !== secondCaractere.toLowerCase()) {
      sameLetter = false;
    }

    if (
      isFirstCaractereLowerCase !== isSecondCaractereLowerCase &&
      sameLetter
    ) {
      result = s;
    }

    return result;
  }

  const size = s.length;
  let substringSize = size;

  let substringTemp = "";

  while (result === "" && substringSize > 1) {
    for (let i = substringSize; i <= size; i++) {
      substringTemp = s.slice(i - substringSize, i);

      if (isNiceSubstring(substringTemp)) {
        result = substringTemp;
        break;
      }
    }

    substringSize--;
  }

  return result;
};

const isNiceSubstring = (substring) => {
  let stopLoop = false;

  for (let caractere of substring) {
    const revertedCaractere = revertCase(caractere);

    stopLoop = substring.includes(revertedCaractere) ? false : true;

    if (stopLoop) break;
  }

  return !stopLoop;
};

const revertCase = (caractere) => {
  let revertedCaractere = caractere.toLowerCase();

  if (caractere === caractere.toLowerCase()) {
    revertedCaractere = caractere.toUpperCase();
  }

  return revertedCaractere;
};
