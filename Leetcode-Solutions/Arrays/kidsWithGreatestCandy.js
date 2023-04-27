/**
 * @param {number[]} candies
 * @param {number} extraCandies
 * @return {boolean[]}
 */
var kidsWithCandies = function(candies, extraCandies) {
    const maxCandies=Math.max(...candies)
    let result=candies.map(a=>(a+extraCandies)>=maxCandies)
    return result
};
