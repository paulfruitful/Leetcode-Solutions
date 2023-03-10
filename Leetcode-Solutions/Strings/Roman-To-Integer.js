/**
 * @param {number} num
 * @return {string}
 */
var intToRoman = function(num) {
//Make an Array for each of the integers in power of ten
   const ones=["", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"]
   const tens=["","X","XX","XXX","XL","L","LX","LXX","LXXX","XC"]
   const hundreds=["","C","CC","CCC","CD","D","DC","DCC","DCCC","CM"]
   const thousands=["","M","MM","MMM"]
//Use the Math.floor to round up the division of the integer and their remainder in order to get their Index in the arrays above 
   return `${thousands[Math.floor(num/1000)]}${hundreds[Math.floor((num%1000)/100)]}${tens[Math.floor((num%100)/10)]}${ones[Math.floor((num%10))] }`

};
