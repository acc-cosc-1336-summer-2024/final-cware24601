#write functions here, don't add input('') statements here!




def get_user_numbers():

    numbers = []
    
    for i in range(5):
        while True:
            try:
                num = float(input(f"Enter Number {i+1}: "))
                numbers.append(num)
                break
            except ValueError:
                print("Invalid input. Enter a valid number.")

    return numbers
            


def main():
    user_numbers = get_user_numbers()
    display_user_numbers(user_numbers)



main()

