import itertools
main_list =list()
S_max = 0

if __name__ == '__main__':
    list_len, mod = map(int,input().split())
    for i in range(list_len):
         input_data = input()
         numbers = list(map(int, input_data.split()))
         n = numbers[0]
         result_list = numbers[1:n+1]
         
         main_list.append(result_list)
    
   
    for l in itertools.product(*main_list):
        s = sum([x**2 for x in l]) % mod

        if s > S_max:
            S_max = s
            
    print(S_max)
        
        
        
        
