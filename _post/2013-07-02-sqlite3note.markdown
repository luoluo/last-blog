---
layout: post
title: "Sqlite3 usage"
date: 2013-07-02 16:17
comments: true
categories: [Tools, Languages]
---
Recently I wirte a spider to grasp the infomation. And I have to store the data somewhere for reuse. And I chose sqlite. Here are the command used in python.

*import the package*
{% highlight python %}
import sqlite3
{% endhighlight %}
*connect to a db*
{% highlight python %}
con = sqlire3.connect("dbname")
{% endhighlight %}
*get a cursor*
{% highlight python %}
cur = con.cursor()
{% endhighlight %}
*initial db*
{% highlight python %}
cur.execute('''creat table if not exists tablename(id integer, name text, score real)''')
{% endhighlight %}
*insert into db*
{% highlight python %}
val = [12, 'asdf', 12.0]
cur.execute('insert into doc values(?,?,?)', val)
con.commit()
{% endhighlight %}
*select from db*
{% highlight python %}
result = cur.execute('select * from doc')
{% endhighlight %}
*use the selected result*
{% highlight python %}
rows = result.fetchall()
for row in rows:
	print row
	row = result.fetchone()
	print row
{% endhighlight %}
*update db*
{% highlight python %}
cur.execute('update doc det score = ? where id = ?', (score, id))
con.commit()
{% endhighlight %}

*merge two db(same data format)*
{% highlight python %}
#write db2 to db1
import sqlite3
con1 = sqlite3.connect("db1")
con2 = sqlite3.connect("db2")
cur1 = con1.cursor()
cur2 = con2.cursor()
f = cur2.execute("select * from doc")
rows = f.fetchall()
for row in rows:
	cur1.execute("insert into doc values(?, ?,..etc.. ,?)," row)
con1.commit()	
{% endhighlight %}
*get sub-db*
{% highlight python %}
import sqlite3
con1 = sqlite3.connect("db1")
con2 = sqlite3.connect("db2")
cur1 = con1.cursor()
cur2 = con2.cursor()
f = cur2.execute("select * from doc")
rows = f.fetchall()
i = 0
for row in rows:
	if i < 50: #store top 50
		cur1.execute("insert into doc values(?, ?,..etc.. ,?)," row)
	i += 1
con1.commit()
{% endhighlight %}
*view db in shell*
{% highlight sh %}
lo@ubuntu:sqlite3 dbname    
SQLite version 3.7.13 2012-06-11 02:05:22
Enter ".help" for instructions
Enter SQL statements terminated with a ";"
sqlite select * from doc;    
{% endhighlight %}

####tips:
Don't forget to commit().
