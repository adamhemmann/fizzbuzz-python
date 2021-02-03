print('Welcome to FizzBuzz!')
print('--------------------')

def fizz_buzz(r_lower, r_upper):
    print('\nRunning FizzBuzz on the range of numbers between ' +
          str(r_lower) + ' and ' + str(r_upper) + '...\n')
    for n in range(r_lower, r_upper + 1):
        if n % 15 == 0:
            print('FizzBuzz')
        elif n % 5 == 0:
            print('Buzz')
        elif n % 3 == 0:
            print('Fizz')
        else:
            print(str(n))
            

def valid_input(prompt):
    while True:
        try:
            value = int(input(prompt))
        except ValueError:
            print('Only integers are allowed. Please try again.')
            continue
        else:
            return value
        

def do_again():
    again = input('\nWould you like to run FizzBuzz on another range of numbers?'
                  '\nEnter Y for yes, N to exit the program: ')
    # Loop to only accept specific inputs from the user
    # Either yes or no
    while again not in('Y', 'y', 'N', 'n'):
        again = input('Enter Y for yes, N to exit the program: ')
        continue
    if again in ('Y', 'y'):
        return True
    elif again in ('N', 'n'):
        print('\nThank you for using this program. Goodbye.')
        return False
    

def main():  
    again = True    
    while again:
        #empty list to store range of values
        fb_range = []
        #ask user to use default range or custom range
        decide = input('\nEnter 1 to use the default range (1-100).\n'
                       'Enter 2 to input a custom range.\n')
        
        if decide == '1':
            fb_range = [1, 100]
            fizz_buzz(fb_range[0], fb_range[1])
                        
        elif decide == '2':
            #ensure custom range is valid (only integers)
            fb_range.append(valid_input('\nPlease enter a lower range: '))
            fb_range.append(valid_input('Please enter an upper range: '))

            #ensure lower range < upper range, else get new range
            if fb_range[0] > fb_range[1]:
                print('\nLower range must be less than upper range.\n')
                continue
            #run fizzbuzz on given range
            fizz_buzz(fb_range[0], fb_range[1])
        #ask user if they would like to run again
        again = do_again()
        

if __name__ == '__main__':
    main()
