def findMajority(list, n): 
  
    maxCount = 0; 
    index = -1  
    for x in range(n): 
      
        count = 0
        for y in range(n): 
          
            if(list[x] == list[y]): 
                count += 1
          
        if(count > maxCount): 
          
            maxCount = count 
            index = x
      
    if (maxCount > n//2): 
        print(list[index]) 
      
    else: 
        print("No Majority Element") 
  
if __name__ == "__main__": 
    list = [1, 2, 3, 4, 5, 5, 5, 5, 5, 5, 6] 
    n = len(list) 
    findMajority(list, n) 