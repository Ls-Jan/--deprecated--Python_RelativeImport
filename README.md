

# RelativeImport

## 安装：
原本是打算发布pypi的，但发现近段时间都没法注册新用户，然后就算了。<br>
1. 下载轮子：[RelativeImport-1.1-py3-none-any.whl](https://github.com/Ls-Jan/Python_RelativeImport/releases/download/v1.1/RelativeImport-1.1-py3-none-any.whl)
2. 安装轮子：``pip install RelativeImport-1.1-py3-none-any.whl``
3. ~成为轮子~

建议还是安装比较好，不然每个子目录都得拖进一个``RelativeImport.py``文件就很蠢，不然就是把``RelativeImport.py``这个文件放到环境路径上(虽然这做法也好不到哪去

## 用法：
```python
from RelativeImport import RImport
RImport('M')#导入模块M。【等同import M】
RImport('M','info','func')#导入模块M中的info和func。【等同from M import info,func】
RImport('M','*')#导入模块M中所有内容。【等同from M import *】
RImport('../M')#导入上级目录中的模块M。【类似from .. import M但规避了“相对导入”问题】
RImport('A/M','info')#导入A目录下的模块M中名为info的变量。【类似from A.M import info但规避了“相对导入”问题】

```
(本来打算函数名``RelativeImport``原封不动的，但发现每次都打那么长的字串就很烦，然后改成``RImport``


## 说明：

#### 主要用于相对路径模块的导入，但实际上也可以正常导入其他模块：
- ``RImport('numpy')``等效于``import numpy``

#### 特别的，支持“重命名”行为：
- ``RImport(('M','mmm'))``：导入模块M并命名为mmm。【等同``import M as mmm``】
- ``RImport(('../M','mmm'))``：导入上级目录中的模块M并命名为mmm。【类似``from .. import M as mmm``但规避了“相对导入”问题】
- ``RImport('M',('info','i'),('func','f'))``：导入模块M中的info和func并分别命名为i和f。【等同``from M import info as i,func as f``】




