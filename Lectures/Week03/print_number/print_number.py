def numbers():
    while True:
        num = int(input('Please input a number (input 6 to stop the program): '))
        if num != 6:
            print(num)
        else:
            break
        
# if __name__ == "__main__":
#     numbers()