# DataIO
DataIO是一个变量控制器，目前主要用于编辑JSON文件。

构造也很简单，使用Python编写，有多种控制方式。
## 操作方式
### 来自Indev1
- `set <var> <value>`：添加变量并初始化或设置变量的值
- `read <var>`：获取变量的值
- `del <var>`：删除变量
### 来自Indev2
- `set <var> <value> [type=str]`：以Python中定义的数据类型存储变量（默认为字符串），**`type`设置为`auto`会自动识别数据类型并转换**
- `json`：以JSON格式输出所有变量
### 来自Indev3
- `save <filePath>`：将JSON存储到指定的文件
- `open <filePath>`：将指定文件的JSON存储到DataIO，但**会删除原有的所有变量**
- `append <filePath>`：将指定文件JSON的所有变量添加到DataIO
- `append-to <filePath>`：将DataIO中的所有变量添加到指定文件
### 未来推出（暂不可用）
- `hash <var> <hash>`：对变量进行哈希加密，并存储16进制值
- `compare <var1> <var2>`：对两个变量进行比对
- `insert <json>`：输入JSON并将其设置为DataIO
- `insert-append <json>`：输入JSON并将其所有变量添加到DataIO
## 其他说明
1. 本程序代码皆经测试无bug，请放心使用。
2. 本程序经测试确保不会对电脑造成影响（编辑文件时除外）。
## 未来规划
- 预计到1.1版：推出hash和compare
- 预计到1.3版：实现目前未来推出的所有功能
- 预计到1.5版：推出基于easygui的UI Edition
- 预计到2.0版：支持多个DataIO
- ……

希望发布后有好的反馈！
