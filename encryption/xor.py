# # def xor_encrypt(message, key):
# #     return ''.join(chr(ord(c) ^ ord(key[i % len(key)])) for i, c in enumerate(message))
# #
# # def xor_encrypt_key(key= None):
# #     keys= [
# #     "interpreter", "indentation", "variable", "loop", "function",
# #     "module", "list", "tuple", "dictionary", "set",
# #     "string", "integer", "float", "boolean", "exception",
# #     "recursion", "decorator", "lambda", "comprehension", "pep8"]
# #     if not key:
# #         pass
# #     else:
# #         key = keys[key]
#
# import random
#
#
# def xor_encrypt(message, key):
#     """ מבצע הצפנת XOR על פי המפתח """
#     return ''.join(chr(ord(c) ^ ord(key[i % len(key)])) for i, c in enumerate(message))
#
#
# def xor_encrypt_key(mode, data):
#     """ בוחר מפתח אקראי ומחזיר את האינדקס שלו """
#     keys = [
#         "interpreter", "indentation", "variable", "loop", "function",
#         "module", "list", "tuple", "dictionary", "set",
#         "string", "integer", "float", "boolean", "exception",
#         "recursion", "decorator", "lambda", "comprehension", "pep8"]
#
#     if mode == "extract":
#         key_index = random.randint(0, len(keys) - 1)
#         key = keys[key_index]
#         return key_index,key,data
#     else:
#         key_index = extract_key_index(data)
#         key = keys[key_index]
#         return
#
#
# def insert_key_index(ciphertext, key_index):
#     """ מכניס את האינדקס של המפתח במקום 8 (או במקום אחר אם הטקסט קצר) """
#     position = min(8, len(ciphertext))  # אם ההודעה קצרה, שלא יחרוג מהאורך
#     return ciphertext[:position] + chr(key_index + 65) + ciphertext[position:]  # ממיר את המספר לאות (A=0, B=1 וכו')
#
#
# def extract_key_index(ciphertext):
#     """ מוציא את האינדקס של המפתח מהמיקום שבו הוספנו אותו """
#     position = min(8, len(ciphertext))
#     key_index_char = ciphertext[position]
#     key_index = ord(key_index_char) - 65  # מחזיר את המספר המקורי
#     ciphertext = ciphertext[:position] + ciphertext[position + 1:]  # מסיר את התו של המפתח
#     return key_index, ciphertext
#
#
# # דוגמא לשימוש
# message = "אני מאוד מצליח"
#
# # בוחרים מפתח ומקבלים את האינדקס שלו
# key_index = xor_encrypt_key()
#
# # משחזרים את המפתח לפי האינדקס
#
# key = keys[key_index]  # משחזרים את המפתח הנכון לפי האינדקס
#
# # הצפנה
# encrypted_message = xor_encrypt(message, key)
#
# # הוספת מספר האינדקס למיקום 8
# final_ciphertext = insert_key_index(encrypted_message, key_index)
#
# # פענוח
# extracted_key_index, extracted_ciphertext = extract_key_index(final_ciphertext)
# recovered_key = keys[extracted_key_index]
# decrypted_message = xor_encrypt(extracted_ciphertext, recovered_key)
#
# print(f"Original Message: {message}")
# print(f"Encrypted: {final_ciphertext}")
# print(f"Decrypted: {decrypted_message}")
# print(f"Inserted key character: {final_ciphertext[8]}")
# print(f"Recovered key index: {ord(final_ciphertext[8]) - 65}")
#
import random

def xor_encrypt(message, key):
    return ''.join(chr(ord(c) ^ ord(key[i % len(key)])) for i, c in enumerate(message))

def xor_encrypt_key(mode, data=None):
    keys = [
        "interpreter", "indentation", "variable", "loop", "function",
        "module", "list", "tuple", "dictionary", "set",
        "string", "integer", "float", "boolean", "exception",
        "recursion", "decorator", "lambda", "comprehension", "pep8"]

    if mode == "encrypt":
        key_index = random.randint(0, len(keys) - 1)
        key = keys[key_index]
        return key_index, key
    elif mode == "decrypt":
        key_index, data = extract_key_index(data)
        key = keys[key_index]
        return key_index, key, data

    else:
        raise ValueError("Invalid mode. Choose 'encrypt' or 'decrypt'.")

def insert_key_index(ciphertext, key_index):
    position = min(8, len(ciphertext))
    return ciphertext[:position] + chr(key_index + 65) + ciphertext[position:]  # ממיר את המספר לאות (A=0, B=1 וכו')

def extract_key_index(ciphertext):
    position = min(8, len(ciphertext))
    key_index_char = ciphertext[position]
    key_index = ord(key_index_char) - 65
    ciphertext = ciphertext[:position] + ciphertext[position + 1:]
    return key_index, ciphertext

# דוגמא לשימוש
message = "ט8ו98ט86א768ט"

# **הצפנה**
def extract(data):
    key_index, key = xor_encrypt_key("encrypt")
    encrypted_message = xor_encrypt(message, key)  # מבצע הצפנה
    final_ciphertext = insert_key_index(encrypted_message, key_index)# מכניס את המפתח למיקום 8
    return final_ciphertext
# **פענוח**

def decrypt(data):
    extracted_key_index, recovered_key, extracted_ciphertext = xor_encrypt_key("decrypt",data)
    decrypted_message = xor_encrypt(extracted_ciphertext, recovered_key)  # מפענח את ההודעה
    return decrypted_message
a = extract(message)
b = decrypt(a)
# **תוצאות**
print(f"Original Message: {message}")
print(f"Encrypted: {a}")
print(f"Decrypted: {b}")


