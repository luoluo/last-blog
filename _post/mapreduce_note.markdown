---
layout: post
title: "MapReduce回忆录"
date: 2018-02-14 10:40
comments: true
categories: [BigData, Note]
---

####Apache Hadoop简介

>The Apache Hadoop software library is a framework that allows for the distributed processing of large data sets across clusters of computers using simple programming models. 

Apache Hadoop是一个分布式计算框架，采用极简的表述模型，在由多台计算机组成的机器集群上，分布式处理计算任务。

Apache Hadoop由以下几部分组成：

* Hadoop Common: 通用组件，以此来构建其他基础模块
* Hadoop Distributed File System (HDFS™): 分布式文件系统，提供数据访问高吞吐
* Hadoop YARN: 任务调度&集群资源管理器
* Hadoop MapReduce: 基于yarn实现的大数据并行处理框架

本文讲重点介绍Hadoop MapReduce。


####编程模型

MapReduce提供两种抽象：

	Map：
	（k1, v1）=> list(k2, v2)
	Reduce:
	  (k2, list(v2)) => list(v3)

抽象的好处:程序员只需专注业务，调度、分发、容错均由集群保证，大大降低研发成本及门槛。

屏蔽细节:

+  map输入分partition，reduce输入划分
+  计算资源、存储相关map和reduce的调度
+  Failover
+  数据分发

####举个栗子

最最经典的word-count

	map(String key, String value): // key: document name
	// value: document contents for each word w in value:
	EmitIntermediate(w, "1");

	reduce(String key, Iterator values): // key: a word
	// values: a list of counts
	int result = 0;
	    for each v in values:
	      result += ParseInt(v);
	    Emit(AsString(result));

<div class="image-div"> <img class="content-image" src="/static/img/mapreduce1.png" alt="x" /> </div>

xxxx

<div class="image-div"> <img class="content-image" src="/static/img/mapreduce2.png" alt="x" /> </div>

xxxx

<div class="image-div"> <img class="content-image" src="/static/img/mapreduce3.png" alt="x" /> </div>
