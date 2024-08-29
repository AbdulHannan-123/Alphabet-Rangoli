def print_rangoli(size):
    number = (size*2)-1
    number = number+number-1
    
    for i in range(size):
        character = ''
        for k in range(i+1):
            character += chr(size -k + 96)
        for k in reversed(range(i)):
            character += chr(size- k + 96)
    
        character = '-'.join(character)
       
        print((character).center(number, '-'))
    for i in reversed(range(size-1)):
        character = ''
        for k in range(i+1):
            character += chr(size -k + 96)
        for k in reversed(range(i)):
            character += chr(size- k + 96)
        character = '-'.join(character)
        print((character).center(number, '-'))
        
        

if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)
