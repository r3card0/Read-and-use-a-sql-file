# Read a sql file
Once a sql script is saved on a file (file.slq), this Python script takes that one to be used to execute on a relational database.

On the method constuctor there are defined two attributes: the pathfile (self.pathfile) and an empty list (self.sql)

The pathfile it the complete path of the sql file. e.g: ```c/Documents/sql/file.sql```

The instance method takes the pathfile and open it with the line : ```with open(self.pathfile,'r',encoding='utf-8') as file:```

Then, a for loop is executed to append every line on the empty list : 
```
for line in file:
    self.sql.append(line)
``` 

Finally, a string method is implemented to convert the list to a string: ``` string = """""".join(self.sql)```

It can be run by assigned the whole path to a variable
```
path_variable = 'c/Documents/sql/file.sql'
sql_file = Read(path_variable)
print(sql_file.readsql())
```
or set the pathfile directly into the instance
```
sql_file = Read('c/Documents/sql/file.sql')
print(sql_file.readsql())
```
