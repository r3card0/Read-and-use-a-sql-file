class Read:
    def __init__(self,pathfile) -> None:
        self.pathfile = pathfile
        self.sql = []

    
    def readsql(self):
        with open(self.pathfile,'r',encoding='utf-8') as file:
            for line in file:
                self.sql.append(line)

        string = """""".join(self.sql)

        return string

sql_file = Read('/c/Documents/sql/file.sql')
print(sql_file.readsql())