<h2><a href="https://leetcode.com/problems/cyclically-shift-rows-and-columns">4416. Cyclically Shift Rows and Columns</a></h2><h3>Easy</h3><hr><p>You are given an integer <code>n</code>, a 2D integer array <code>grid</code> of size <code>n x n</code>, and two integer arrays <code>rowShift</code> and <code>colShift</code>, each of length <code>n</code> where:</p>

<ul>
	<li><code>rowShift[i]</code> represents the number of positions to <strong>cyclically left shift</strong> the <code>i<sup>th</sup></code> row of <code>grid</code>.</li>
	<li><code>colShift[j]</code> represents the number of positions to <strong>cyclically upward shift</strong> the <code>j<sup>th</sup></code> column of <code>grid</code>.</li>
</ul>

<p>First, cyclically shift each row according to <code>rowShift</code>, then cyclically shift each column according to <code>colShift</code>.</p>

<p>Return the resulting grid after performing all the shifts.</p>

<p>A <strong>cyclic left shift</strong> of the <code>i<sup>th</sup></code> row by <code>k</code> positions shifts only that row. The element at column <code>j</code> moves to column <code>(j - k + n) % n</code>, while all other rows remain unchanged.</p>

<p>A <strong>cyclic upward shift</strong> of the <code>j<sup>th</sup></code> column by <code>k</code> positions shifts only that column. The element at row <code>i</code> moves to row <code>(i - k + n) % n</code>, while all other columns remain unchanged.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">n = 2, <code>grid</code> = [[1,2],[3,4]], rowShift = [1,0], colShift = [0,1]</span></p>

<p><strong>Output:</strong> <span class="example-io">[[2,4],[3,1]]</span></p>

<p><strong>Explanation:</strong></p>

<p>The <code>grid</code> changes as follows:</p>

<p><img alt="" src="https://assets.leetcode.com/uploads/2026/08/18/4743-1.png" style="width: 760px; height: 92px;" /></p>
</div>

<p><strong class="example">Example 2:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">n = 3, <code>grid</code> = [[1,2,3],[4,5,6],[7,8,9]], rowShift = [1,2,0], colShift = [2,2,1]</span></p>

<p><strong>Output:</strong> <span class="example-io">[[7,8,5],[2,3,9],[6,4,1]]</span></p>

<p><strong>Explanation:</strong></p>

<p>The <code>grid</code> changes as follows:</p>

<p><img alt="" src="https://assets.leetcode.com/uploads/2026/08/18/4743-2.png" style="width: 750px; height: 349px;" /></p>
</div>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= n == grid.length == grid[i].length &lt;= 10</code></li>
	<li><code>1 &lt;= grid[i][j] &lt;= 100</code></li>
	<li><code>rowShift.length == colShift.length == n</code></li>
	<li><code>0 &lt;= rowShift[i], colShift[i] &lt; n</code></li>
</ul>
