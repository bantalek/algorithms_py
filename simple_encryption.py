# For building the encrypted string:
# If the input-string is null or empty or n is <= 0 then return the input text.

def encrypt(encrypted_text, n):
    if (encrypted_text == None or
        len(encrypted_text) <= 0 or 
        n <= 0):
        return encrypted_text
    else:
        counter = 0
        length = len(encrypted_text)
        text = encrypted_text
        result = ''

        while (counter < n):
            for i in range(length):
                if (i % 2 == 0 or i == 0):
                    result += text[i]

            for i in range(length - 1, 0, -1):
                if (i % 2 != 0 and i != 0):
                    result = text[i] + result

            counter += 1
            text = result
            result = ''

    return text

def decrypt(encrypted_text, n):
    if (encrypted_text == None or
        len(encrypted_text) <= 0 or 
        n <= 0):
        return encrypted_text
    else:        
        length = len(encrypted_text)
        first_part, second_part = encrypted_text[:length//2], encrypted_text[length//2:]
        text = ''
        repititions, counter, first_index, second_index = 0, 0, 0, 0

        while repititions < n:
            text, counter, first_index, second_index = '', 0, 0, 0
            while counter < length:
                if counter % 2 == 0 or counter == 0:
                    text += second_part[first_index]
                    first_index += 1

                if (counter % 2 != 0 and counter != 0):
                    text += first_part[second_index]
                    second_index += 1

                counter += 1

            first_part, second_part = text[:length//2], text[length//2:]
            repititions += 1

    return text
                

print(encrypt("This is a test!", 1))
# si  etTi sats!
print(encrypt("This is a test!", 2)) #
# s eT ashi tist!
print(decrypt(encrypt("This is a test!", 1), 1)) #
# This is a test!
print(decrypt(encrypt("This is a test!", 2), 2)) #
# This is a test!
print(decrypt("hsi  etTi sats!", 1)) #
# This is a test!
print(decrypt("s eT ashi tist!", 2)) #
# This is a test!

