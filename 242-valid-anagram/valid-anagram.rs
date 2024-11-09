use std::collections::HashMap;

impl Solution {
    pub fn is_anagram(s: String, t: String) -> bool {
        if s.len() != t.len() {
            return false;
        }

        let mut count = [0; 26];

        for (sc, tc) in s.chars().zip(t.chars()) {
            count[(sc as usize) - ('a' as usize)] += 1;
            count[(tc as usize) - ('a' as usize)] -= 1;
        }

        count.iter().all(|&x| x == 0)
    }
}