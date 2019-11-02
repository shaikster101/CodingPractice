/*
From: Leetcode
Difficulty: Easy
Description: Balanced strings are those who have equal quantity of 'L' and 'R' characters.

Given a balanced string s split it in the maximum amount of balanced strings.

Return the maximum amount of splitted balanced strings.

*/

class Solution {
public:
    int balancedStringSplit(string s) {
   
        
    char letters[s.size() + 1]; 
    strcpy(letters, s.c_str()); 
        
    int counter = 0; 
        
    int pairs = 0; 
    for(char c : letters){
        if(c == 'R'){
            counter = counter + 1; 
        }else{
            counter = counter - 1; 
        }
        
        if(counter == 0){
            pairs = pairs + 1; 
        }
    }
        
        
    return pairs; 
        
    }
};