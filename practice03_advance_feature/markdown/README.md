# 高级特性
<div id="x-content">
<h4>迭代器</h4>
<div class="x-wiki-content x-main-content"><p>我们已经知道，可以直接作用于<code>for</code>循环的数据类型有以下几种：</p>
<p>一类是集合数据类型，如<code>list</code>、<code>tuple</code>、<code>dict</code>、<code>set</code>、<code>str</code>等；</p>
<p>一类是<code>generator</code>，包括生成器和带<code>yield</code>的generator function。</p>
<p>这些可以直接作用于<code>for</code>循环的对象统称为可迭代对象：<code>Iterable</code>。</p>
<p>可以使用<code>isinstance()</code>判断一个对象是否是<code>Iterable</code>对象：</p>
<pre><code class="python"><span class="prompt">&gt;&gt;&gt; </span><span class="keyword">from</span> collections <span class="keyword">import</span> Iterable
<span class="prompt">&gt;&gt;&gt; </span>isinstance([], Iterable)
<span class="built_in">True</span>
<span class="prompt">&gt;&gt;&gt; </span>isinstance({}, Iterable)
<span class="built_in">True</span>
<span class="prompt">&gt;&gt;&gt; </span>isinstance(<span class="string">'abc'</span>, Iterable)
<span class="built_in">True</span>
<span class="prompt">&gt;&gt;&gt; </span>isinstance((x <span class="keyword">for</span> x <span class="keyword">in</span> range(<span class="number">10</span>)), Iterable)
<span class="built_in">True</span>
<span class="prompt">&gt;&gt;&gt; </span>isinstance(<span class="number">100</span>, Iterable)
<span class="built_in">False</span>
</code></pre>
<p>而生成器不但可以作用于<code>for</code>循环，还可以被<code>next()</code>函数不断调用并返回下一个值，直到最后抛出<code>StopIteration</code>错误表示无法继续返回下一个值了。</p>
<p>可以被<code>next()</code>函数调用并不断返回下一个值的对象称为迭代器：<code>Iterator</code>。</p>
<p>可以使用<code>isinstance()</code>判断一个对象是否是<code>Iterator</code>对象：</p>
<pre><code class="python"><span class="prompt">&gt;&gt;&gt; </span><span class="keyword">from</span> collections <span class="keyword">import</span> Iterator
<span class="prompt">&gt;&gt;&gt; </span>isinstance((x <span class="keyword">for</span> x <span class="keyword">in</span> range(<span class="number">10</span>)), Iterator)
<span class="built_in">True</span>
<span class="prompt">&gt;&gt;&gt; </span>isinstance([], Iterator)
<span class="built_in">False</span>
<span class="prompt">&gt;&gt;&gt; </span>isinstance({}, Iterator)
<span class="built_in">False</span>
<span class="prompt">&gt;&gt;&gt; </span>isinstance(<span class="string">'abc'</span>, Iterator)
<span class="built_in">False</span>
</code></pre>
<p>生成器都是<code>Iterator</code>对象，但<code>list</code>、<code>dict</code>、<code>str</code>虽然是<code>Iterable</code>，却不是<code>Iterator</code>。</p>
<p>把<code>list</code>、<code>dict</code>、<code>str</code>等<code>Iterable</code>变成<code>Iterator</code>可以使用<code>iter()</code>函数：</p>
<pre><code class="python"><span class="prompt">&gt;&gt;&gt; </span>isinstance(iter([]), Iterator)
<span class="built_in">True</span>
<span class="prompt">&gt;&gt;&gt; </span>isinstance(iter(<span class="string">'abc'</span>), Iterator)
<span class="built_in">True</span>
</code></pre>
<p>你可能会问，为什么<code>list</code>、<code>dict</code>、<code>str</code>等数据类型不是<code>Iterator</code>？</p>
<p>这是因为Python的<code>Iterator</code>对象表示的是一个数据流，Iterator对象可以被<code>next()</code>函数调用并不断返回下一个数据，直到没有数据时抛出<code>StopIteration</code>错误。可以把这个数据流看做是一个有序序列，但我们却不能提前知道序列的长度，只能不断通过<code>next()</code>函数实现按需计算下一个数据，所以<code>Iterator</code>的计算是惰性的，只有在需要返回下一个数据时它才会计算。</p>
<p><code>Iterator</code>甚至可以表示一个无限大的数据流，例如全体自然数。而使用list是永远不可能存储全体自然数的。</p>
<h3>小结</h3>
<p>凡是可作用于<code>for</code>循环的对象都是<code>Iterable</code>类型；</p>
<p>凡是可作用于<code>next()</code>函数的对象都是<code>Iterator</code>类型，它们表示一个惰性计算的序列；</p>
<p>集合数据类型如<code>list</code>、<code>dict</code>、<code>str</code>等是<code>Iterable</code>但不是<code>Iterator</code>，不过可以通过<code>iter()</code>函数获得一个<code>Iterator</code>对象。</p>
<p>Python的<code>for</code>循环本质上就是通过不断调用<code>next()</code>函数实现的，例如：</p>
<pre><code class="python"><span class="keyword">for</span> x <span class="keyword">in</span> [<span class="number">1</span>, <span class="number">2</span>, <span class="number">3</span>, <span class="number">4</span>, <span class="number">5</span>]:
    <span class="keyword">pass</span>
</code></pre>
<p>实际上完全等价于：</p>
<pre><code class="python"><span class="comment"># 首先获得Iterator对象:</span>
it = iter([<span class="number">1</span>, <span class="number">2</span>, <span class="number">3</span>, <span class="number">4</span>, <span class="number">5</span>])
<span class="comment"># 循环:</span>
<span class="keyword">while</span> <span class="built_in">True</span>:
    <span class="keyword">try</span>:
        <span class="comment"># 获得下一个值:</span>
        x = next(it)
    <span class="keyword">except</span> StopIteration:
        <span class="comment"># 遇到StopIteration就退出循环</span>
        <span class="keyword">break</span>
</code></pre>

[返回主页](../../README.md)