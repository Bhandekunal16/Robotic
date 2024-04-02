from store import Store


def main():
    userInput = input("enter your command :")

    if userInput == 'write':
        print("--------------------------------------------------------------")
        sec = input("enter your input: ")
        print("--------------------------------------------------------------")
        inputString = f"{sec}\n"
        return Store.create(inputString)
    elif userInput == 'read':
        return Store.read()
    elif userInput == 'line' :
        sec = int(input("enter your input: "))
        return Store.read_specific_line(sec)
    elif userInput == 'edit':
        one = int(input("enter line to edit: "))
        sec = input("enter new line: ")
        return Store.edit(one,sec)
    else :
        return print('thank you!')
main()