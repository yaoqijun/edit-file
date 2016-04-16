# edit-file
###simple edit file content when develop.

```
1.	Developer 对文本的重复处理过程

2.	不同的数据源数据的读取

3.	固定话文本的处理方式

4.	定制话文本信息的处理结果

5.	开发过程中不必要重复的结果信息的处理	
```

模拟数据 Collection 过滤操作， Spark！！

### 项目结构的设计
+ input 定制化信息的输入(不同的数据源数据方式)
	+ 信息录入的格式
		- Excel
		- TEXT 文本信息格式
		- Json Object
		- date source 
		- etc
	+ 插件方式， 用户自定义格式的输入

+ produce 文本信息的处理方式
	+ 对应的数据集合 dict 数据形式
	+ Collections 基本的操作方式， map, flapMap Filter, reduce convert ... etc
	+ Action ， key reduce , etc ..... 
	+ 转换后的结果信息的输出

+ Output 定制化信息内容的输出
	+	文本， Excel 信息的导出
	+	Datasource 信息内容的导出
	+	用户定制化文本操作方式
	
### 实现
+ total
	- input -> reduce -> output 通过data 数据格式传递
	- data dict {input_info:[对应的数据内容], context:{total, type hasData 对应的上下文环境}}

+	input
	- data_source interface 数据信息
		+ context 数据源信息
		+ source_data 数据信息获取 (用户配置数据源)
	- data_source_txt 文本信息
		+ path 文本文件路径输入
	- data_source_xls Excel 问蹦信息
	    + context:  对应Excel File文件路径, 
	        - sheetIndex : 对应sheet index
	        - startRows endRows, 读入数据行列 default （1, max rows）
	        - startCols endCols， 对应的开始结束列 default (1, max clos)
	        - OVER
	- mysql connection 
	    + context
	        - config 对应的mysql 配置信息
	        - params 'sql' 获取数据 对应的操作语句
	
+	output
	- 当前简单的文本文件信息输出
	- TODO 不同 EXCEL , DataSource, etc 文本信息的输出 
	
+	reduce
    -   handle 过滤处理信息结果
    -   定义default handler 信息内容
    - 	each line handler 对其中的每行Data 信息的处理方式。
    	-	user definition each line reduce method
    	- 	add annotation context
    	
+ reduce factory 构建对应的Factory 信息内容
	-	构建对应Source, Produce, Output 数据信息内容
	
	
### 输入
1.  默认Txt 文件配置方式 Path 文件位置

2.  context Handler 名称, 构建对应的List名称

3.  output 指定对应的输出文件， 默认TXT文件
