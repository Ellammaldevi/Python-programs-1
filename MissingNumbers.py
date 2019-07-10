def missing_numbers(num_list):
    
      original_list = [x for x in range(num_list[0], num_list[-1] + 1)]
      num_list = set(num_list)
      
      return (list(num_list ^ set(original_list)))

num_list = [1,2,3,4,6,7,10]

print (missing_numbers(num_list))