def shift_right(bit_list):
    bit_list.append(0)
    return (bit_list.pop(0))

def xor(binary_one,binary_two):
    result = []
    for i in range(0,len(binary_two)):
        result.append(binary_one[i] ^ binary_two[i])
    return result 

def multiple_xor(binaries_lists):
    result = binaries_lists[0]
    for i in range(1, len(binaries_lists)):
        result = xor(result,binaries_lists[i])
    return result

def ordinal_string_to_binary_list(ordinal_string):
    binary_list = []
    binary_string = format(int(ordinal_string),'b')
    for i in binary_string:
        binary_list.append(ord(i)- 48 )
    while len(binary_list) < 8:
        binary_list.insert(0,0)
    return(binary_list)

def multiply(first_byte_list, second_byte_list, cipher_byte):
    multiplier_ones_positions = []
    bytes_for_xor = []  
    for i in range(0, len(second_byte_list)):
        if second_byte_list[i] == 1:
            multiplier_ones_positions.append(abs(i-7))
    for i in range(0, len(second_byte_list)):
        if i in multiplier_ones_positions:
            bytes_for_xor.append(first_byte_list.copy())

        if (shift_right(first_byte_list) == 1):
            first_byte_list = xor(first_byte_list,cipher_byte)
    return multiple_xor(bytes_for_xor)



first_number = input("first byte ?")
second_number = input("second byte ?")
cypher_option = input("aes or snow ?")
first_byte_list = ordinal_string_to_binary_list(first_number)
second_byte_list = ordinal_string_to_binary_list(second_number)
if cypher_option == "aes":
    cipher_byte = [0,0,0,1,1,0,1,1]
elif cypher_option == "snow":
    cipher_byte = [1,0,1,0,1,0,0,1]
print("Primer Bit: " + str(first_byte_list))
print("Segundo Bit: " + str(second_byte_list))
print("Byte algoritmo: " + str(cipher_byte))
print("Multiplicación: " + str(multiply(first_byte_list,second_byte_list,cipher_byte)))




