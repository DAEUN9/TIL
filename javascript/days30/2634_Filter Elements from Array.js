/**
 * @param {number[]} arr
 * @param {Function} fn
 * @return {number[]}
 */
var filter = function(arr, fn) {
  let answer = []
    for (let i=0; i<arr.length; i++) {
      let temp = fn(arr[i], i)
      if (temp) {
        answer.push(arr[i])
      }
      
    }
    return answer
};