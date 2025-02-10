# -*- coding: utf-8 -*-
"""
@date: 10-02-2025
@author: sap218
"""

import pandas as pd

df = pd.read_excel("input.xlsx")

# perhaps PK / FK datatypes are NULL?
df["DATATYPE"] = df.apply(lambda row: "Int" if pd.isna(row["DATATYPE"]) and pd.notna(row["KEY"]) else row["DATATYPE"], axis=1)


tables = {}

for index,row in df.iterrows():
    
    table = row["TABLE"]
    field = row["FIELD"]
    key = row["KEY"]
    datatype = row["DATATYPE"]
    
    if table not in tables:
        tables[table] = []
    
    
    if "FK" in str(key): pass
    else:
        define = "%s %s" % (field,datatype)
    
    
    if "PK" in str(key):
        define += " PRIMARY KEY"
    
    elif "FK" in str(key):
        fktable, fkfield = field.split(".")
        
        define = "CONSTRAINT fk_%s" % fkfield.lower()
        
        define += " FOREIGN KEY (%s) REFERENCES %s(%s)" % (fkfield,fktable,fkfield)
        
    tables[table].append(define)

del index,row,table,field,key,datatype,define,fktable,fkfield



sql_statements = []

for table,fields in tables.items():
    statement = "CREATE TABLE %s (\n" % table
    statement += ",\n".join(fields)
    statement += "\n);"
    sql_statements.append(statement)
del table,fields,statement
    

sql_script = "\n\n".join(sql_statements)


with open("output.sql", "w") as f:
    f.write(sql_script)
del f

# end
