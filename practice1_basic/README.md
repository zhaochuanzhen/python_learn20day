# 数据类型和变量
## 字符串
<p>字符串是以单引号<code>'</code>或双引号<code>"</code>括起来的任意文本，比如<code>'abc'</code>，<code>"xyz"</code>等等。请注意，<code>''</code>或<code>""</code>本身只是一种表示方式，不是字符串的一部分，因此，字符串<code>'abc'</code>只有<code>a</code>，<code>b</code>，<code>c</code>这3个字符。如果<code>'</code>本身也是一个字符，那就可以用<code>""</code>括起来，比如<code>"I'm OK"</code>包含的字符是<code>I</code>，<code>'</code>，<code>m</code>，空格，<code>O</code>，<code>K</code>这6个字符。</p>

<p>如果字符串内部既包含<code>'</code>又包含<code>"</code>怎么办？可以用转义字符<code>\</code>来标识，比如：</p>

```angular2
'I\'m \"OK\"!'
```
<p>如果字符串内部既包含<code>'</code>又包含<code>"</code>怎么办？可以用转义字符<code>\</code>来标识，比如：</p>

```angular2
>>> print('I\'m ok.')
I'm ok.
>>> print('I\'m learning\nPython.')
I'm learning
Python.
>>> print('\\\n\\')
\
\
```
<p>如果字符串里面有很多字符都需要转义，就需要加很多<code>\</code>，为了简化，Python还允许用<code>r''</code>表示<code>''</code>内部的字符串默认不转义，可以自己试试：</p>

```javascript
>>> print('\\\t\\')
\       \
>>> print(r'\\\t\\')
\\\t\\
```
<p>如果字符串内部有很多换行，用<code>\n</code>写在一行里不好阅读，为了简化，Python允许用<code>'''xxx'''</code>的格式表示多行内容，可以自己试试：</p>

```javascript
>>> print('''line1
line2
line3''')
line1
line2
line3
```

## 空值
<p>空值是Python里一个特殊的值，用<code>None</code>表示。<code>None</code>不能理解为<code>0</code>，因为<code>0</code>是有意义的，而<code>None</code>是一个特殊的空值。</p>

## 常量

<p>所谓常量就是不能变的变量，比如常用的数学常数π就是一个常量。在Python中，通常用全部大写的变量名表示常量：</p>

```javascript
PI = 3.14159265359
```
<p>但事实上<code>PI</code>仍然是一个变量，Python根本没有任何机制保证<code>PI</code>不会被改变，所以，用全部大写的变量名表示常量只是一个习惯上的用法，如果你一定要改变变量<code>PI</code>的值，也没人能拦住你。</p>
<p>最后解释一下整数的除法为什么也是精确的。在Python中，有两种除法，一种除法是<code>/</code>：</p>

```javascript
>>> 10 / 3
3.3333333333333335
```

<p><code>/</code>除法计算结果是浮点数，即使是两个整数恰好整除，结果也是浮点数：</p>

```javascript
>>> 9 / 3
3.0
```

<p>还有一种除法是<code>//</code>，称为地板除，两个整数的除法仍然是整数：</p>

```javascript
>>> 10 // 3
3
```

<p>你没有看错，整数的地板除<code>//</code>永远是整数，即使除不尽。要做精确的除法，使用<code>/</code>就可以。</p>
<p>因为<code>//</code>除法只取结果的整数部分，所以Python还提供一个余数运算，可以得到两个整数相除的余数：</p>

```javascript
>>> 10 % 3
1
```
<p>无论整数做<code>//</code>除法还是取余数，结果永远是整数，所以，整数运算结果永远是精确的。</p>


