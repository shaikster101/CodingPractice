/*
From: Leetcode
Difficulty: Easy
Description: You're given strings J representing the types of stones that are jewels, and S representing the stones you have.
             Each character in S is a type of stone you have.  You want to know how many of the stones you have are also jewels.
*/


class Solution {
public:
    int numJewelsInStones(string J, string S) {
        
        int answer = 0; 
        
        unordered_set<char> jewels{J.begin(), J.end()}; 
    
        for(int i = 0; i < S.size(); i++){
            if(jewels.count(S[i])){
                answer = answer + 1; 
            }
        }
        
        return answer; 
        
    }
};