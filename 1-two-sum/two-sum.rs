use std::collections::HashMap;

impl Solution {
    pub fn two_sum(nums: Vec<i32>, target: i32) -> Vec<i32> {
        let mut map = HashMap::new();

        for (n, &num) in nums.iter().enumerate() {
            let num = nums[n];
            let complement = target - num;
            if let Some(&index) = map.get(&complement) {
                return vec![index as i32, n as i32];
            }

            map.insert(num, n);
        }

        return vec![];
    }
}