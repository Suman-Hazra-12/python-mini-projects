class Solution:                       
    def romanToInt(self, s):          
        values = {                    
            'I': 1,                  
            'V': 5,                  
            'X': 10,                  
            'L': 50,                  
            'C': 100,                 
            'D': 500,                 
            'M': 1000                 
        }
        
        total = 0                     
        i = 0                        
        
        while i < len(s):            
            
            if i + 1 < len(s) and values[s[i]] < values[s[i + 1]]:  
                total += values[s[i + 1]] - values[s[i]]            
                i += 2                                              
                print(total)                                        
                print(i)                                           
            else:                                                  
                total += values[s[i]]                              
                i += 1                                              
                print(total)                                       
                print(i)                                           
        return total                                                

p1 = Solution()                                                    
result = p1.romanToInt("XIV")  # Example input                 