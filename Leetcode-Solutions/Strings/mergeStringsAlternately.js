/**
 * @param {string} word1
 * @param {string} word2
 * @return {string}
 */
var mergeAlternately = function(word1, word2) {
    const first=word1.length
    const sec=word2.length
    let merged=''
    let maxLen=Math.max(first,sec)
    for(let i=0; i<maxLen; i++){
       if(i<first){
        merged+=word1[i]
       } 
         if(i<sec){
        merged+=word2[i]
       } 
    }
    return merged
};
