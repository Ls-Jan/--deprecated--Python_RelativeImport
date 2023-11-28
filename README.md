

# RelativeImport

#### 主要用于相对路径模块的导入
- ``RelativeImport('M')``：导入模块M。【等同``import M``】
- ``RelativeImport('M','info','func')``：导入模块M中的info和func。【等同于``from M import info,func``】
- ``RelativeImport('M','*')``：导入模块M中所有内容。【等同于``from M import *``】
- ``RelativeImport('../M')``：导入上级目录中的模块M。
- ``RelativeImport('A/M','info')``：导入A目录下的模块M中名为info的变量。

#### 特别的，支持“重命名”行为：
- ``RelativeImport(('M','mmm'))``：导入模块M并命名为mmm。【等同``import M as mmm``】
- ``RelativeImport('M',('info','i'),('func','f'))``：导入模块M中的info和func并分别命名为i和f。【等同``from M import info as i,func as f``】

#### 补充：
- 虽然名字是RelativeImport(相对导入)，但实际上它也能正常导入其他模块，例如``RelativeImport(('numpy','np'))``等效于``import numpy as np``


