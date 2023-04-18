function twoSum(nums: number[], target: number): number[] {
    let diff={}
    let res=[]
    let i=0
    while (i<nums.length){
      if(diff.hasOwnProperty(target-nums[i]) ){
        res.push(diff[target-nums[i]])
        res.push(i)
        break
      }
     
      diff[nums[i]]=i;
       i++
      }

      return res

