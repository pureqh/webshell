## webshell
v2.0<br>
仅供学习 请勿用作非法用途<br>
更新了部分规则，现在可以绕过包括但不仅限于D盾、webdir+、河马、安全狗等查杀工具<br>
项目适配了asp、aspx、php、jsp语言<br>
此项目内的所有shell均支持蚁剑<br>

## 免杀webshell生成工具

知识点：使用注释分隔eval函数内关键字,使用类和构造函数替代引用函数<br>
blog：https://pureqh.top/?p=4577<br>
command：python php_webshell.py<br>
~~知识点：使用分隔关键字等绕过<br>~~
~~blog：https://pureqh.top/?p=4611<br>~~
知识点：使用自定义加密绕过杀软拼接关键字<br>
blog:https://pureqh.top/?p=4638<br>
知识点：利用函数分隔关键字<br>
https://pureqh.top/?p=4720

## 更新日志 2021/2/12

由于D盾增加规则 将 if(md5($_GET["pass"])=="df24bfd1325f82ba5fd3d3be2450096e") 作为匹配规则 所以更新专用于D盾的webshell生成器<br>
php_D_webshell.py<br>
只用注释依然可以过D盾<br>
其他生成器不受影响

## 更新日志 2021/4/18

由于D盾将aspx生成器的马提取规则，所以更新专用于D盾的webshell生成器<br>
aspx_D_webshell.py<br>
改动很小 正则查杀万岁！

## 更新日志 2021/4/22

万众瞩目的jsp生成器它来了<br>
