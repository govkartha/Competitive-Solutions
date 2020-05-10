function getSecondLargest(nums) {
  // Complete the function
  nums.sort((a, b) => {
    console.log(a - b);
    return a - b;
  });
  return nums[nums.indexOf(nums[nums.length - 1]) - 1];
}
