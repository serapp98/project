Python 3.9.5 (tags/v3.9.5:0a7dcbd, May  3 2021, 17:27:52) [MSC v.1928 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> list1=[9,11,17,23,39,41,47,51,55,89,93,125]
>>> list2=[8,12,18,26,34,42,50,58,64,72,88,100]
>>> list1.extend(list2)
>>> print(list1)
[9, 11, 17, 23, 39, 41, 47, 51, 55, 89, 93, 125, 8, 12, 18, 26, 34, 42, 50, 58, 64, 72, 88, 100]
>>> newlist=[9, 11, 17, 23, 39, 41, 47, 51, 55, 89, 93, 125, 8, 12, 18, 26, 34, 42, 50, 58, 64, 72, 88, 100]
>>> for sayi in newlist:
	print(sayi*2)
	print(type(newlist))

	
18
<class 'list'>
22
<class 'list'>
34
<class 'list'>
46
<class 'list'>
78
<class 'list'>
82
<class 'list'>
94
<class 'list'>
102
<class 'list'>
110
<class 'list'>
178
<class 'list'>
186
<class 'list'>
250
<class 'list'>
16
<class 'list'>
24
<class 'list'>
36
<class 'list'>
52
<class 'list'>
68
<class 'list'>
84
<class 'list'>
100
<class 'list'>
116
<class 'list'>
128
<class 'list'>
144
<class 'list'>
176
<class 'list'>
200
<class 'list'>
>>> 