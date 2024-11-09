use std::collections::HashMap;

impl Solution {
    pub fn is_anagram(s: String, t: String) -> bool {
        if s.len() != t.len() {
            return false;
        }

        let mut s_count = HashMap::new();
        let mut t_count = HashMap::new();

        for c in s.chars() {
            *s_count.entry(c).or_insert(0) += 1;
        }

        for c in t.chars() {
            *t_count.entry(c).or_insert(0) += 1;
        }

        s_count == t_count
    }
}