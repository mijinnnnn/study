
import sys
read = sys.stdin.readline
sys.setrecursionlimit(10**6)

def main():
    my_dict = {'a': 123123, 'b': "blog", 'c': 3333}

    my_dict['d'] = 2023
    print(my_dict)

    print('a' in my_dict)


    print(my_dict.keys())
    print(my_dict.values())
    print(my_dict.items())
    print(my_dict['a'])
    del my_dict['a']

    print(my_dict)

    my_dict.clear()
    print(my_dict)



if __name__ == '__main__':
    main()


