from io import StringIO, BytesIO

f = StringIO()
f.write("你好，世界")
print(f.getvalue())

b = BytesIO()
b.write("你好，世界。我是字节流".encode('utf-8'))
print(b.getvalue())
