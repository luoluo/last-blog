---
layout: post
title: shell related wiki
date: 2014-12-11 22:49
comments: true
categories: HeadStream
---

    常用命令：

    文本处理：
    cat
    less
    head/tail
    sort
    vim
    wc
    grep
    cp/mv/rm
    awk
    sed
    diff
    echo
    printf

    任务管理：
    ctrl + z/c/r/b/f
    jobs/fg/bg
    source
    date
    xargs

    文件处理：
    ls
    ln
    tree
    tar
    du
    find
    file
    ldd
    iconv

    系统处理：
    sudo
    chmod
    passwd
    bashrc/bash_profile
    export
    netstat

    文件传输：
    scp
    wget
    lftp

文本处理相关：

    vim

        vim regex 匹配使用group: `s/\(xx\)ad\(xx\)/xx\1\2/g`
        vim 显示隐藏字符：`set list`
        vim 扩大文件之间的copy行数到100 `:set viminfo='100,<100,s10,h`
        vim case casting:
            vim to UPPER CASE gU
            vim to downcase  gu
            vim to opposite case g~
        vim 换行 %s/html:/&\r/g
        vim buffer:
        set noexpa
        shift+3  高亮当前代码
        :g/^$/d   去除空行
        %s/xx/&\r/g 换行

    sed 
        sed 's/[\t]//g' test.txt > out.txt
        sed 's/[\x09]//g' test.txt > out.txt
        sed -e 's/^A/xxx/g' file > newFile

    示例单个文件转换
        iconv -f encoding -t encoding inputfile
        iconv -f GBK -t UTF-8 file1 -o file2

    6. 2>&1 将标准错误输出 输出到标准输出http://www.cnblogs.com/caolisong/archive/2007/04/25/726896.html

任务管理：

    进程前后台操作相关Ctrl+C 退出前台命令执行，回到shell
    Ctrl+Z 暂停前台命令执行，回到shell
    jobs 查看当前在后台执行命令，可查看进程号码
    &运行命令时，在末尾添加&,使得命令在后台执行
    fg N 将命令进程号码为N的进程，放到前台执行
    bg N将命令进程号码为N的进程，放到后台执行
    7.source 的作用http://www.ansen.org/2012/04/point-in-the-shell-command-and-the-difference-of-the-source-command.html
    5. date date
        date -d
        date -d "1 day ago" 
        date -d "1 day ago" +%Y%m%d
        date +%Y%m%d
        date --date='20140902 2 day' +%Y%m%d
        date --date='20140902 2 days ago' +%Y-%m-%d
    34. source 和 .  

文件处理：

    1.文件压缩解压 tar -zcvf 
    2.链接文件
        ln -s path/to/file linkName
        unlink linkName
        rm linkName
        ln -rf linkName
        Not!!! ln -fr linkName/

    3.查找制定文件
        find start_path -name file_to_find
        find /home/work -name my.sh
        find . -name "*py" | xargs cat | wc -l
        find . -type d -name ".svn" | xargs rm -fr 
        find . -type f -exec rm -v {} \;
        find . -type f -print -delete
        find . -name "*.md5" -exec md5sum -c {} \;
        find . -name "*.md5" | xargs -i md5sum -c {}


文件传输：

    46.下载、查看带user/pwd的内容
        lftp -u user,pwd host:/path/to/file
        wget --ftp-user=xxx --ftp-password=xxx ftp://host:/path/to/file
        wget --no-check-certificate xxx


系统处理：

    show machine hardware info
        lscpu
        cat /proc/meminfo

    mysql dump
        mysqldump -u root -ppassword tablename --no-data > tablename.sql
        mysql -u root -ppassword tablename < tablename.sql
        mysql set name gbk

    mysql alter table
        alter table aka_audit_output_hour change   ideaid ideaid bigint;
        alter table aka_audit_output_hour change   audit_pipe audit_type string

    mysql function
        select count(distinct idvisit) as counted,
            FROM_UNIXTIME(TRUNCATE(UNIX_TIMESTAMP(server_time)/900.0,0)*900) as server_time_ed
            FROM visits group by server_time_ed
        select lpad(id, 4, '0000') from t1;
        select substring_index("/test/examplepath/use/rlo/g.txtasdf", '/', 3);

shell语言：

    27.目录是否存在
    if [ -d "$DIRECTORY" ]; then
      # Control will enter here if $DIRECTORY exists.
    fi

    28.shell 获取命令的输出值
    count=$(ls |　wc -l)

    30. shell 的参数 $# 参数个数  $1 $2 .. $n 第一、第二、第n个参数

    31. '' 与 "" 的区别 

    32. 数组 shell里变量的类型不是特别明确，字符串和变量可以混用，关键是看参与什么运算；
    so 数组可以用字符串来表示  days="1 2 3 4 5"
    for day in days;do
         echo $day;
    done

    33. write to 和 write append  <==>    > 和 >>
 
    35. sleep
         sleep <nubmer>s/m/h/d   #sleep number秒/分钟/小时/天 
    
    40.执行一条字符串
    cmd="date +Y%m%d"
    eval $cmd
    val=$(eval $cmd)

    63. shell array
    ## declare an array variable
    declare -a arr=("element1" "element2" "element3")

    ## now loop through the above array
    for i in "${arr[@]}"do
        echo "$i"
    # or do whatever with individual element of the arraydone

    64 printf 会对\n做转义的echo
    echo -e "Hello\nworld"
    echo -e 'Hello\nworld'
    echo Hello$'\n'world
    echo $'hello\nworld'
    printf "hello\nworld\n"

    65.base64 in terminal
    openssl enc -base64 <<< fengkong-hadoop #hadoop的密码居然不能有等号
    openssl enc -base64 <<< fengkonghadoop
    echo `echo xxxx | base64 --decode`

