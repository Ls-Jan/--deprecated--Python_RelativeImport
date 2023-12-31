# 此项目已废弃

本项目的内容是幼稚且不靠谱的，为了您的项目安全着想，强烈不建议使用本项目相关内容，理由：
- 本质上使用``sys.path``和``exec``实现相对路径导入
- 由于是使用``exec``这种动态方式进行模块导入，使用pyinstaller将项目打包成exe时并不会将相关模块打包进去，也就是exe文件将完全无法运行(提示模块不存在)


<br>
<br>
<br>


## 安装：
原本是打算发布pypi的，但发现近段时间都没法注册新用户，然后就算了。<br>
1. 下载轮子：[RelativeImport-1.1-py3-none-any.whl](https://github.com/Ls-Jan/Python_RelativeImport/releases/download/v1.1/RelativeImport-1.1-py3-none-any.whl)
2. 安装轮子：``pip install RelativeImport-1.1-py3-none-any.whl``
3. ~成为轮子~

建议还是安装比较好，不然每个子目录都得拖进一个``RelativeImport.py``文件就很蠢，不然就是把``RelativeImport.py``这个文件放到环境路径上(虽然这做法也好不到哪去

## 用法：
```python
from RelativeImport import RImport
RImport('M')#导入模块M。【等同import M】【类似from . import M但规避了“相对导入”问题】
RImport('M','info','func')#导入模块M中的info和func。【等同from M import info,func】【类似from .M import info,func但规避了“相对导入”问题】
RImport('M','*')#导入模块M中所有内容。【等同from M import *】【类似from .M import *但规避了“相对导入”问题】
RImport('../M')#导入上级目录中的模块M。【类似from .. import M但规避了“相对导入”问题】
RImport('A/M','info')#导入A目录下的模块M中名为info的变量。【等同from A.M import info】【类似from .A.M import info但规避了“相对导入”问题】

```
(本来打算函数名``RelativeImport``原封不动的，但发现每次都打那么长的字串就很烦，然后改成``RImport``


## 说明：

#### 主要用于相对路径模块的导入，但实际上也可以正常导入其他模块：
- ``RImport('numpy')``等效于``import numpy``

#### 特别的，支持“重命名”行为：
- ``RImport(('M','mmm'))``：导入模块M并命名为mmm。【等同``import M as mmm``】
- ``RImport(('../M','mmm'))``：导入上级目录中的模块M并命名为mmm。【类似``from .. import M as mmm``但规避了“相对导入”问题】
- ``RImport('M',('info','i'),('func','f'))``：导入模块M中的info和func并分别命名为i和f。【等同``from M import info as i,func as f``】


<br>


## 例子：

附上一份测试样例test，其中两份代码，一个是使用相对导入，另一个是用RImport，两份代码的目录结构都是一样的：
```
+--A.py
|
+--M1
   |
   +--B.py
   |
   +--M2
      |
      +--C.py
```
T1代码：
```python
#A.py
from M1.B import *
a=1
print(f'A:{a,b,c}')


#B.py
from .M2.C import c
b=2
print(f'B:{b,c}')


#C.py
c=3
print(f'C:{c}')
```

T2代码：
```python
#A.py
from RelativeImport import RImport
RImport('M1.B','*')
a=1
print(f'A:{a,b,c}')


#B.py
from RelativeImport import RImport
RImport('M2.C','c')
b=2
print(f'B:{b,c}')


#C.py
c=3
print(f'C:{c}')
```

分别运行每个单独的py文件后，T1中的B.py运行报错，原因是使用了相对导入，但T2用RImport规避了这个问题，满足了B.py单独运行测试的情况。<br>
好像py古老版本(py2.x)原本就支持相对导入的，但不知为啥又撤走了，或许是为了增强“包”的概念？毕竟“相对导入”用于文件关联性强的“包”，<br>
但也多亏这画蛇添足的改动，单文件受阻于“相对导入问题”没法很好的进行测试。(估计规范的包的脚本测试是在顶层目录额外创建测试文件进行的


