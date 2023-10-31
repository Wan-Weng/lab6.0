

def encoder(password):
    user_input = password
    list = ''.join([str(int(char) + 3) for char in user_input])
    return list


def decoder(password):
    decoded_password = ""
    for num in str(password):
        num = int(num) - 3
        decoded_password += num
    return decoded_password


def print_menu():
    print("Menu")
    print("-------------")
    print("1. Encode ")
    print("2. Decode ")
    print("3. Quit ")


