// Question Link
// https://leetcode.com/problems/fizz-buzz/


/** 
 * Given an integer n, return a string array answer (1-indexed) where:

answer[i] == "FizzBuzz" if i is divisible by 3 and 5.
answer[i] == "Fizz" if i is divisible by 3.
answer[i] == "Buzz" if i is divisible by 5.
answer[i] == i if non of the above conditions are true.*/

/**
 * @param {number} n
 * @return {string[]}
 */
 var fizzBuzz = function(n) {
    let arra = []; 
    for (i = 1 ; i <= n ; i++ ){
        let strin = "" ;

        if (i % 3 == 0) { 
            strin +='Fizz'
            
        }
        if (i % 5 == 0) {
            strin+='Buzz'
        }
        if (strin === ""){
            strin = String(i)

        }
        arra.push(strin)

    }
    return arra
};