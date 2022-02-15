###Q. 1

chars = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
shifted_chars=["11","12","13","21","22","23","31","32","33","41","42","43","51","52","53","61","62","63","71","72","73","81","82","83","91","92","93"]
def find_in_list(query, mainlist):
    i=0
    while i<len(mainlist):
        if query==mainlist[i]:
            return i
        i+=1

def encrypt_message(plain_msg):
    encrypted_msg = ""
    for character in plain_msg:
        if character in chars:
            char_index = find_in_list(character, chars)
            new_char = shifted_chars[char_index]
            encrypted_msg = encrypted_msg + new_char
        else:
            encrypted_msg = encrypted_msg + character
    return encrypted_msg

def decrypt_message_multi(message):
    decrypted_msg = ""
    n = 2
    for x in range(len(message)):
        for character in message:
            split_strings = [character[index : index + n] for index in range(0, len(character), n)]
            for character in split_strings:
                if character in shifted_chars:
                    char_index = find_in_list(character, shifted_chars)
                    new_char = chars[char_index]
                    decrypted_msg = decrypted_msg + new_char
                else:
                    decrypted_msg = decrypted_msg + character
            decrypted_msg = decrypted_msg + " "
        return decrypted_msg	
	
flag = True
while flag==True:
    choice = input("What do you want to do? 1. Encrypt a message 2. Decrypt a message \nEnter= ")
    if choice =='e':
        plain_message = input("Enter message to encrypt??")
        print(encrypt_message(plain_message.lower()))
    elif choice =='d':
        encrypted_msg = input("Enter message to decrypt?").split(' ')
        print(decrypt_message_multi(encrypted_msg))
    else:
        play_again = input("Do you want to try agian or Do you want to exit? (Y/N)")
        if play_again == 'Y':
            continue
        elif play_again == 'N':
            break


##Q.2

def encrypt():
  message = input("Enter the message you want to encrypt")
  ascii_message = [ord(char)+3 for char in message]
  encrypt_message = [ chr(char) for char in ascii_message]  
  print (''.join(encrypt_message))


def decrypt():
  message = input("Enter the message you want to decrypt")
  print(ascii_message = [ord(char)+3 for char in message])
  print(decrypt_message = [ chr(char) for char in ascii_message])
  print (''.join(decrypt_message))

flag = True
while flag ==True:
    choice = input("What do you want to do? \n1. Encrypt a message 2. Decrypt a message \nEnter E or D respectively!")
    if choice == 'e':
        encrypt()
    elif choice == 'd':
        decrypt()    
    else:
        play_again = input("Do you want to try agian or Do you want to exit? (Y/N)")
        if play_again == 'Y':
            continue
        elif play_again == 'N':
            break



##Q.3
chars= ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
value= ["29","28","27","26","25","24","23","22","21","20","19","18","17","16","15","14","13","12","11","10","9","8","7","6","5","4","3","2","1"]
           
def find_in_list(query, mainlist):
    i=0
    while i<len(mainlist):
        if query==mainlist[i]:
            return i
        i+=1


def encrypt_message(plain_msg):
    encrypted_msg = ""
    for character in plain_msg:
        if character in chars:
            char_index = find_in_list(character, chars)
            new_char = value[char_index]
            encrypted_msg = encrypted_msg + new_char
        else:
            encrypted_msg = encrypted_msg + character
    return encrypted_msg



def decrypt_message(encrypted_msg):
    decrypted_msg = ""
    for character in encrypted_msg:
        if character in value:
            char_index = find_in_list(character, value)
            new_char = chars[char_index]
            decrypted_msg = decrypted_msg + new_char
        else:
            decrypted_msg = decrypted_msg + character
    return decrypted_msg



flag = True
while flag == True:
    choice = input("What do you want to do? 1. Encrypt a message 2. Decrypt a message  Enter e or d respectively!")
    if choice == 'e':
        plain_message = input("Enter message to encrypt??")
        print(encrypt_message(plain_message))
    elif choice == 'd':
        encrypted_msg = input("Enter message to decrypt?")
        print(decrypt_message(encrypted_msg))
    play_again = input("Do you want to try agian or Do you want to exit? (Y/N)")
    if play_again == 'Y':
        continue
    elif play_again == 'N':
        break
    else:
        play_again = input("Do you want to try agian or Do you want to exit? (Y/N)")
        if play_again == 'Y':
            continue
        elif play_again == 'N':
            break





