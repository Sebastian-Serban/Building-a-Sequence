# Building-a-Sequence

<p>You will receive an uncertain amount of integers in a certain order <code>k1, k2, ..., kn</code>.</p>

<p>You form a new number of n digits in the following way:
you take one of the possible digits of the first given number, <code>k1</code>, then the same with the given number <code>k2</code>, repeating the same process up to <code>kn</code> and you concatenate these obtained digits(in the order that were taken) obtaining the new number. As you can see, we have many possibilities.</p>
<p>Let's see the process above explained with three given numbers:</p>

<pre><code>k1 = 23, k2 = 17, k3 = 89
Digits Combinations   Obtained Number
  ('2', '1', '8')           218    &lt;---- Minimum
  ('2', '1', '9')           219
  ('2', '7', '8')           278
  ('2', '7', '9')           279
  ('3', '1', '8')           318
  ('3', '1', '9')           319
  ('3', '7', '8')           378
  ('3', '7', '9')           379    &lt;---- Maximum
             Total Sum =   2388   (8 different values)
</code></pre>

<p>We need the function that may work in this way:</p>
<pre><code class="language-python"><span class="cm-variable">proc_seq</span>(<span class="cm-number">23</span>, <span class="cm-number">17</span>, <span class="cm-number">89</span>) <span class="cm-operator">==</span> [<span class="cm-number">8</span>, <span class="cm-number">218</span>, <span class="cm-number">379</span>, <span class="cm-number">2388</span>]
</code></pre>

<pre style="display: none;"><code class="language-javascript"><span class="cm-variable">procSeq</span>(<span class="cm-number">23</span>, <span class="cm-number">17</span>, <span class="cm-number">89</span>) <span class="cm-operator">--</span><span class="cm-operator">-</span><span class="cm-operator">&gt;</span> [<span class="cm-number">8</span>, <span class="cm-number">218</span>, <span class="cm-number">379</span>, <span class="cm-number">2388</span>]
</code></pre>
<p>See this special case and deduce how the function should handle the cases which have many repetitions.</p>
<pre><code class="language-python"><span class="cm-variable">proc_seq</span>(<span class="cm-number">22</span>, <span class="cm-number">22</span>, <span class="cm-number">22</span>, <span class="cm-number">22</span>) <span class="cm-operator">==</span> [<span class="cm-number">1</span>, <span class="cm-number">2222</span>] <span class="cm-comment"># we have only one obtained number, the minimum, maximum and total sum coincide</span>
</code></pre>
<pre style="display: none;"><code class="language-javascript"><span class="cm-variable">procSeq</span>(<span class="cm-number">22</span>, <span class="cm-number">22</span>, <span class="cm-number">22</span>, <span class="cm-number">22</span>) <span class="cm-operator">--</span><span class="cm-operator">-</span><span class="cm-operator">&gt;</span> [<span class="cm-number">1</span>, <span class="cm-number">2222</span>] <span class="cm-comment">/* we have only one obtained number, the minimum, maximum and total sum coincide*/</span>
</code></pre>
<p>The sequence of numbers will have numbers of n digits only. Numbers formed by leading zeroes will be discarded.</p>
<pre><code class="language-python"><span class="cm-variable">proc_seq</span>(<span class="cm-number">230</span>, <span class="cm-number">15</span>, <span class="cm-number">8</span>) <span class="cm-operator">==</span> [<span class="cm-number">4</span>, <span class="cm-number">218</span>, <span class="cm-number">358</span>, <span class="cm-number">1152</span>]
</code></pre>
<pre style="display: none;"><code class="language-javascript"><span class="cm-variable">procSeq</span>(<span class="cm-number">230</span>, <span class="cm-number">15</span>, <span class="cm-number">8</span>) <span class="cm-operator">--</span><span class="cm-operator">-</span><span class="cm-operator">&gt;</span> [<span class="cm-number">4</span>, <span class="cm-number">218</span>, <span class="cm-number">358</span>, <span class="cm-number">1152</span>]
</code></pre>

