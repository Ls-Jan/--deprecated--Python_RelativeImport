

# RelativeImport

``from RelativeImport import RImport``
<br>(本来打算函数名``RelativeImport``原封不动，但发现每次都打那么长的字串就很烦，然后改成``RImport``了


#### 主要用于相对路径模块的导入
- ``RImport('M')``：导入模块M。【等同``import M``】
- ``RImport('M','info','func')``：导入模块M中的info和func。【等同于``from M import info,func``】
- ``RImport('M','*')``：导入模块M中所有内容。【等同于``from M import *``】
- ``RImport('../M')``：导入上级目录中的模块M。
- ``RImport('A/M','info')``：导入A目录下的模块M中名为info的变量。


#### 特别的，支持“重命名”行为：
- ``RImport(('M','mmm'))``：导入模块M并命名为mmm。【等同``import M as mmm``】
- ``RImport('M',('info','i'),('func','f'))``：导入模块M中的info和func并分别命名为i和f。【等同``from M import info as i,func as f``】


#### 补充：
- 虽然名字是RelativeImport(相对导入)，但实际上它也能正常导入其他模块，例如``RImport(('numpy','np'))``等效于``import numpy as np``


