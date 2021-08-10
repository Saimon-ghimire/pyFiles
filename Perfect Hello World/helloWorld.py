from random import randrange 
import time
def hello_world(m_string,expected_character):
    while True:
        char_num=randrange(0,127)
        time.sleep(0.01)
        print_char=('\r'+m_string+chr(char_num))
        print(print_char,end='')
        if chr(char_num) == expected_character:
            return chr(char_num)
        else:continue


        
my_string='hello world'
m_string=''
for letter in my_string:    
    m_string += hello_world(m_string, letter)