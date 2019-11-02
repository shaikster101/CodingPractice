/*
Given a valid (IPv4) IP address, return a defanged version of that IP address.

A defanged IP address replaces every period "." with "[.]".

*/

#include <string>

class Solution {
public:
    string defangIPaddr(string address) {
     
     size_t len = address.find("."); 
    
     while(len != std::string::npos){
        
         address.replace(len, 1, "[.]");
         
         len = address.find(".", len+3); 
     }
    return address;   
    }
};