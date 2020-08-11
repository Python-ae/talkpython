# see this page!
# -> https://www.geeksforgeeks.org/print-lists-in-python-4-different-ways/


def main():
    
    int_dict ={12: 'one', 11: 'two', 33: 'three'}
    int_dict_keys = list(int_dict.keys())
    int_dict[44] = 'last'
    print(f"int key are: {int_dict_keys}")
    print(' '.join(map(str, int_dict_keys)))  #for integers only - using map
    

    board = {'first': 100, 'second': 3993}
    board['third'] = 333
    listOfDictKeys = list(board.keys())
    
    print(f" string keys are: {listOfDictKeys}")
    print(' '.join(listOfDictKeys))  # for string wihout using map



if __name__ == '__main__':
    main()