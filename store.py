class Store :
    
    def create(data):
        binary_data = bin(int.from_bytes(data.encode(), 'big'))
        with open('index.bin', "ab") as file:
            file.write(binary_data.encode())

    def read():
        with open('index.bin', "rb") as file:
            read_data = file.read()
            binary_strings = read_data.split(b'0b')[1:]  
            decoded_data = ''
            for binary_str in binary_strings:
                binary_data_int = int(binary_str, 2)
                binary_data_bytes = binary_data_int.to_bytes((binary_data_int.bit_length() + 7) // 8, 'big')
                decoded_data += binary_data_bytes.decode()
            print("--------------------------------------------------------------\n")
            print(decoded_data)
            print("--------------------------------------------------------------\n")


    def read_specific_line(line_number):
        with open('index.bin', "rb") as file:
            read_data = file.read()
            binary_strings = read_data.split(b'0b')[1:]  
            decoded_data = ''
            for binary_str in binary_strings:
                binary_data_int = int(binary_str, 2)
                binary_data_bytes = binary_data_int.to_bytes((binary_data_int.bit_length() + 7) // 8, 'big')
                decoded_data += binary_data_bytes.decode()
                lines = decoded_data.split('\n')
                if 0 < line_number <= len(lines):
                    print("--------------------------------------------------------------\n")
                    return print(lines[line_number - 1])
                else:
                    return "Line number out of range"
                
    def edit(line_number, new_line):
        with open('index.bin', "r") as file:
            read_data = file.read()
            word = bin(int.from_bytes(new_line.encode(), 'big'))
            binary_strings = read_data.split('0b')[1:]  
            decoded_data = ''
            for binary_str in binary_strings:
                binary_data_int = int(binary_str, 2)
                binary_data_bytes = binary_data_int.to_bytes((binary_data_int.bit_length() + 7) // 8, 'big')
                decoded_data += binary_data_bytes.decode()
            lines = decoded_data.split('\n')
            if 0 < line_number <= len(lines):
                lines[line_number - 1] = word
                with open('index.bin', "w") as file:
                    file.write('\n'.join(lines))
                    print('-----------------your line is edited---------------------')
                return '\n'.join(lines)
            else:
                return "Line number out of range"


            


