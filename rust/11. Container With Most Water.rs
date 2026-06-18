use std::cmp;
impl Solution {
    pub fn max_area(height: Vec<i32>) -> i32 {
        let n=height.len();
        let mut l=0usize;
        let mut r=n-1;
        let mut ans=-1;
        while l<r {
           let width=(r-l) as i32;
            let heights=cmp::min(height[l],height[r]);
            let area =width*heights;
            ans=cmp::max(ans,area);
            if height[l]<height[r]{
                l+=1;
            }else{
                r-=1;
            }
            
        }
        return ans;
    }
}