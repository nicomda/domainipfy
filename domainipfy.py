#!/bin/python
import dns
import dns.resolver
import sys
import getopt
import os

isVerbose=getMX=getCNAME=getALL=False
file_path=output_file='';
domain_list=list()
ip_list=list()

def printHelp():
    print('Available options:')
    print('-v           Will print all output')
    print('-i           <input_file>')
    print('-o           <output_file>')
    print('--cname      Test cname registers')
    print('--mx         Test mx registers')
    print('--all        Test all register types')

try:
    opts,args = getopt.getopt(sys.argv[1:], 'i:o:vh', ["cname","mx","all","help"])
except getopt.GetoptError:
    print('Arguments error, just use as below or -h,--help for more options.')
    print('Quick usage: ./domainipfy.py -i <input_file>')
    sys.exit()
for opt, arg in opts:
    if opt in ('-h',"--help"):
        printHelp()
    elif opt == '-i':
        file_path=str(arg)
    elif opt == '-o':
        output_file= str(arg)
    elif opt == '-v':
        isVerbose=True
    elif opt == '--cname':
        getCNAME=True
    elif opt == '--mx':
        getMX=True
    elif opt == '--all':
        getALL=True

with open(file_path, 'r') as file:
    for line in file:
#        if isVerbose:
#            print(line, end='')
        domain_list.append(str(line))
print(f'{len(domain_list)} domains will be processed.')
if output_file == '':
    output_file= f'{os.path.splitext(file_path)[0]}_output.txt'
with open(output_file, 'a') as out_file:
    for domain in domain_list:
        if isVerbose:
            print(f'Processing domain: {domain[:-1]}')
        print(f'[{domain[:-1]}]',file=out)
        print(domain[:-1])
        result = dns.resolver.resolve(domain[:-1], 'A') #BYTHEFACE \n at the end of the string
        for ip in result:
            print(ip.to_text())
            print(ip.to_text(),file=out)
        print()


        
        




    
