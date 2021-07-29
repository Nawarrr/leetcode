// Question Link
//https://leetcode.com/problems/valid-parentheses/


/**
 * Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

-Open brackets must be closed by the same type of brackets.
-Open brackets must be closed in the correct order.
 */


/**
 * @param {string} s
 * @return {boolean}
 */
 var isValid = function(s) {
    const openArray = ['(' , '{' , '[' ]
    let checkArray = [];
    for ( i of s ) {
        
        if (openArray.includes(i)) {
            checkArray.push(i)
             
        }else {
            if (i === ')' && checkArray[checkArray.length -1] === '(') {
                checkArray.pop()
            }else if (i === '}' && checkArray[checkArray.length -1] === '{'){
                checkArray.pop()
            }else if (i === ']' && checkArray[checkArray.length -1] === '['){
                checkArray.pop()
            }else{
                return false
            }
        }
    }
    return checkArray.length === 0
};