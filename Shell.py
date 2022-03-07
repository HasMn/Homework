import sys
identifiers={}
functions={}
data_types=["int","float","str","bool"]
Bin_ops=["+","-","/","//","%","*","**","="]
Comp_ops=["eq","noteq","<",">"]
key_words=["loop","while","if","or","fin","input","output","give","deFunc"]
seperators=[")","(","]","[","}","{","="]
literals=["true","false"]
key_num=data_types+Comp_ops+key_words+literals

def Variables(str):
    if str in identifiers or (str.isidentifier() and str not in key_num):
        return True
    else:
        return False

def DataTypes(str):
    if str.isnumeric() and str[0]!=0:
        return "int"
    elif str.startswith("-") and str[1]!=0 and str.replace("-","1",1).isnumeric():
        return "int"
    elif str.count(".")==1 and str.replace(".","1").isnumeric():
        return "float"
    elif str.startswith("'") and str.endswith("'"):
        return "str"
    elif str=="true" or str=="false":
        return "bool"
    else:
        return False

def NumData(str):
    if DataTypes(str)=="int" or DataTypes(str)=="float":
        return True
    else:
        return False

def VariableMaker(lst):
        var=lst.pop(0)
        lst.pop(0)
        if IsArithm(lst[0]):
            identifiers.update({var: IsArithm(lst[0])})
        elif lst[0] in identifiers and len(lst)==1:
            identifiers.update({var: identifiers[lst[0]]})
        elif DataTypes(lst[0]) in data_types and len(lst)==1:
            identifiers.update({var: lst[0]})
        elif lst[0] in functions:
            if functions[lst[0]]!="None":
                identifiers.update({var: functions[lst[0]]})
        elif lst[0]=="input" and len(lst)==1:
            identifiers.update({var: input()})
        else:
            return "It's an invalid syntax for defining variables"
def Comp(str):
    count=0
    op=0
    for i in str:
        if i in Comp_ops:
            op=i
            count+=1
    if count == 0:
        if str== "true":
            return True
        elif str== "false":
            return False
        else:
            print("Syntax error")
            return False
    elif count == 1:
        new_lst = str.split(op)
        if NumData(new_lst[0]) and NumData(new_lst[1]):
            new_lst[0]=int(new_lst[0])
            new_lst[1]=int(new_lst[1])
            if op=="<" and new_lst[0]<new_lst[1]:
                return True
            elif op=="<" and new_lst[0]>=new_lst[1]:
                return False
            elif op==">" and new_lst[0]>new_lst[1]:
                return True
            elif op==">" and new_lst[0]<=new_lst[1]:
                return False
            elif op=="eq" and new_lst[0]==new_lst[1]:
                return True
            elif op=="eq" and new_lst[0]!=new_lst[1]:
                return False
            elif op=="noteq" and new_lst[0]!=new_lst[1]:
                return True
            elif op=="noteq" and new_lst[0]==new_lst[1]:
                return False
            else:
                return "Syntax error"
        elif NumData(new_lst[0]) and new_lst[1] in identifiers:
            str=str.replace(new_lst[1], identifiers[new_lst[1]], 1)
            return Comp(str)
        elif NumData(new_lst[1]) and new_lst[0] in identifiers:
            str=str.replace(new_lst[0], identifiers[new_lst[0]], 1)
            return Comp(str)
        elif new_lst[0] in identifiers and new_lst[1] in identifiers:
            str=str.replace(new_lst[0], identifiers[new_lst[0]], 1)
            str=str.replace(new_lst[1], identifiers[new_lst[1]], 1)
        elif NumData(new_lst[0]) and IsArithm(new_lst[1]):
            str=str.replace(new_lst[1], IsArithm(new_lst[1]), 1)
            return Comp(str)
        elif NumData(new_lst[1]) and IsArithm(new_lst[0]):
            str=str.replace(new_lst[0], IsArithm(new_lst[0]), 1)
            return Comp(str)
        elif new_lst[0] in identifiers and IsArithm(new_lst[0]):
            str=str.replace(identifiers[new_lst[0]], IsArithm(new_lst[0]), 1)
            return Comp(str)
        elif new_lst[1] in identifiers and IsArithm(new_lst[0]):
            str=str.replace(identifiers[new_lst[1]], IsArithm(new_lst[0]), 1)
            return Comp(str)
        else:
            print("Syntax error")
            return False
    else:
        print("Syntax error")
        return False

# def Functions(lst_member):
# def WhileLoop():
# def ForLoop():

def IsArithm(lst):
    for i in lst:
        if i in identifiers:
            x=str(identifiers[i])
            lst=lst.replace(i,x)
    if NumData(str(eval(lst))):
        return str(eval(lst))
    else:
        return False

def Give(line):
    if len(line) == 2 and line[0] == "give" and line[1] in identifiers:
        return identifiers[line[1]]
    elif len(line) == 2 and line[0] == "give" and DataTypes(line[1]):
        return line[1]

def Output(line):
    if line[1] in identifiers:
        print(identifiers[line[1]])
    elif line[1] in functions and functions[lst[1]] != "None":
        print(functions[line[1]])
    elif DataTypes(line[1]):
        print(line[1])
    elif IsArithm(line[1]):
        print(int(IsArithm(line[1])))
    else:
        print("Syntax error")
        return False

def Lexer(line):
    for i in line:
        if i in seperators:
            line = line.replace(i," "+i+" ")
    return line.split()

file_name=input()
sys.argv.append(file_name)
prog=open(sys.argv[1])
cpyes=0
cpno=0
for line in prog:
    lst=Lexer(line)
    length=len(lst)
    if cpyes==1 and lst[length-1]=="}":
        cpyes=0
    if cpno==1:
        if lst[length-1]=="}":
            cpno=0
        else:
            continue
    elif length<2:
        print("The length is less than 2")
    elif length>1:
        if lst[0]=="output":
            Output(lst)
        if Variables(lst[0]) and lst[1]=="=":
            VariableMaker(lst)
        elif lst[0]=="give":
            Give(lst)
        elif lst[0]=="if" and lst[length-1]=="{" and length>2:
            if Comp(lst[1]):
                cpyes+=1
                continue
            else:
                cpno+=1

