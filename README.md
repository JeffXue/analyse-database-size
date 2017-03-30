# Example

![样例图片](https://raw.githubusercontent.com/JeffXue/analyse-database-size/master/example.png)

# Config
file: `config.ini`

config the mysql connection information,only support mysql
```config.ini
[db]
ip=192.168.1.200
port=3306
user=root
password=123456
database=test
```

set you target table and sql
you can change the user_id to adapter you key and add some where condition into the sql, but you should only get the count num in first column
```config.ini
[tables]
tables=yourtablename,secondtable # splide with ","
sql=SELECT COUNT(user_id) FROM %s.%s GROUP BY user_id
```

# Run
```
python start.py 
```
check the result dir
