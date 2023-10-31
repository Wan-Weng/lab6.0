

def encoder(password):
    user_input = password
    list = ''.join([str(int(char) + 3) for char in user_input])
    return list






def print_menu():
    print("Menu")
    print("-------------")
    print("1. Encode ")
    print("2. Decode ")
    print("3. Quit ")




