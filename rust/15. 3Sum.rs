impl Solution {
    pub fn three_sum(mut nums: Vec<i32>) -> Vec<Vec<i32>> {
        let n = nums.len();

        if n < 3 {
            return vec![];
        }

        nums.sort();

        let mut ans = Vec::new();

        for i in 0..n - 2 {
            if i > 0 && nums[i] == nums[i - 1] {
                continue;
            }

            let mut low = i + 1;
            let mut high = n - 1;

            while low < high {
                let tot = nums[i] + nums[low] + nums[high];

                if tot == 0 {
                    ans.push(vec![nums[i], nums[low], nums[high]]);

                    low += 1;
                    high -= 1;

                    while low < high && nums[low] == nums[low - 1] {
                        low += 1;
                    }

                    while low < high && nums[high] == nums[high + 1] {
                        high -= 1;
                    }
                } else if tot < 0 {
                    low += 1;
                } else {
                    high -= 1;
                }
            }
        }

        ans
    }
}