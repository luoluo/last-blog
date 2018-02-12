---
layout: post
title: "Rails 飞起来"
date: 2013-04-11 19:17
comments: true
categories: [Tech, Languages]
---
####一如Rails深似海，从此MVC不离手 

**Rails是什么**
一个符合实际需要而且高效的Web框架.  

**Rails提供了什么**
快速建立Web应用 

---
{% highlight sh %}
rails new tickets  便建立了tickets应用
{% endhighlight %}

---

**支架**
快速完成 CRUD操作(创建(C)\读取(R)\更新(U)\删除(D) 均以数据库为中心)

---
{% highlight sh %}
rails generate scaffold ticket name:string address:string price:decimal
{% endhighlight %}
---
**数据库管理**

---
{% highlight sh %}
rake migrate #数据的迁移
{% endhighlight %}
{% highlight sh %}
rails generate AddPhoneToTickets phone:string  #增加新的数据项
rake db:migrate #数据的迁移
{% endhighlight %}
---
**View浏览器支持预览**

---
{% highlight sh %}
rails server #访问http://localhost:3000/tickets
{% endhighlight %}
---
**Rails应用 = 模型(model) + 视图(view) + 控制器(controller)**
*Model*
模型代码管理如何从数据库中读写数据.

---
{% highlight rb %}
class Ticket < ActiveRecord::Base 
	attr_accessible :address, :name, :price, :phone #model.rb 增加新的数据项记得修改
end
{% endhighlight %}
---

*View*
视图是展现给用户看的部分，即浏览器中所见。 
增加新的数据项记得修改 *views/tickets/*目录下的html文件

*Controller*
决定*模型*和*视图*的交互。决定了那些数据需要从模型中获取；以及视图中的那一部分将显示这些数据。

