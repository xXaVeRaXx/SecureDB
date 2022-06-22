import os.path
import os

dictionary = ""

print ("Select one dictionary (write corresponding number):")
print ("1. English")
print ("2. Spanish")
option_dic = input()

if option_dic == "1":
    dictionary = 'diccionarios/dic_EN.txt'
elif option_dic == "2":
    dictionary = 'diccionarios/dic_SP.txt'
else:
    print ("This option doesn't exist. Run the script another time selecting an existing dictionary option.")
    exit(0)

print()

print ("Select a complexity for the hash cracking (write corresponding number):")
print ("1. Low")
print ("2. Medium")
print ("3. High")
option_com = input()



if option_com == "1" or option_com == "2" or option_com == "3":
    print()
    print("***************************")
    print("*Starting to crack hashes:*")
    print("***************************")
    print()
    os.system('hashcat -a 0 -m 100 hash.txt ' + dictionary + ' -r rules/rule_replace1 -r rules/rule_replace2 -r rules/rule_replace3 -r rules/rule_replace4 -o cracked_replace -w 3 -O')
    if option_com == "2" or option_com == "3":
        print()
        os.system('hashcat -a 0 -m 100 hash.txt ' + dictionary + ' -r rules/rule_appendChar -o cracked_append -w 3 -O')
        print()
        os.system('hashcat -a 0 -m 100 hash.txt ' + dictionary + ' -r rules/rule_capitalize -o cracked_capitalize -w 3 -O')
        if option_com == "3":
            print()
            os.system('hashcat -a 0 -m 100 hash.txt ' + dictionary + ' -r rules/rule_reverse -o cracked_reverse -w 3 -O')
            print()
            os.system('hashcat -a 0 -m 100 hash.txt ' + dictionary + ' -r rules/rule_duplicate -o cracked_duplicate -w 3 -O')   
else:
    print ("This option doesn't exist. Run the script another time selecting an existing complexity option.")
    exit(0)

if os.path.isfile('cracked_replace') or os.path.isfile('cracked_append') or os.path.isfile('cracked_capitalize') or os.path.isfile('cracked_reverse') or os.path.isfile('cracked_duplicate'):
    os.system('cat cracked_* > results')
    os.system('rm cracked_*')
    print()
    os.system('ls')
    print()
    print ("You can find the cracked hashes in the 'results' file.")
else:
    print()
    print ("The tool can't decrypt any hash.")
