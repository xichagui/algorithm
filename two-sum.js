//var arr = [-1,-3,-3,-4,-6];

// var twoSum = function(nums, target) {
//     var sortNums = nums.concat([]);
//     sortNums.sort(function(a, b) {
//       return a - b;
//     });
  
//     var i = 0,
//         j = sortNums.length - 1,
//         sum;
  
//     while(i !== j) {
//       sum = sortNums[i] + sortNums[j]
//       if (sum < target) {
//         i++;
//       } else if (sum > target) {
//         j--;
//       } else {
//         break;
//       }
//     }
  
//     var resultArr = [];
//     for (var k = 0; k <= nums.length - 1; k++) {
//       if (nums[k] === sortNums[i]) {
//         resultArr.push(k);
//       } else if (nums[k] === sortNums[j]) {
//         resultArr.push(k);
//       }
//     }
//     return resultArr;
// };

var arr = [-1,-3,-3,-4,-6];

var twoSum = function(nums, target) {
  var numsObjecet = {};
  for (var i = 0; i < arr.length; i++) {
    console.info(i);
    var key = target - nums[i];
    if (numsObjecet.hasOwnProperty(key)) {
      return [numsObjecet[key], i];
    } else {
      numsObjecet[nums[i]] = i;
    }
  }
};
console.info(twoSum(arr, -6));

