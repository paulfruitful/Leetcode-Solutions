
/**
 * @param {number[]} nums
 * @return {void} Do not return anything, modify nums in-place instead.
 */
var moveZeroes = function(nums) {
    let no_zeroes=nums.filter(x=>x!==0)
    let zeroes=Array(nums.length-no_zeroes.length).fill(0)
    nums.splice(0,nums.length,...no_zeroes,...zeroes)

};
