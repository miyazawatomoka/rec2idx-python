# rec2idx-python

For MXnet, 
If only have rec file, but not have idx file,
like [this](https://mxnet.incubator.apache.org/api/python/io/io.html?highlight=mxrecordio#mxnet.recordio.MXIndexedRecordIO) , 
you can use this tool to generate idx file.
 
 ```
python main.py
```
The default input stream support file.  
Also, you can write your input stream class by 
implements the InputStream to support your input stream. 


