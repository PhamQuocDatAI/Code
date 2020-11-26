list2 =[({'name': 'Peter', 'age':2}, {'name': 'John', 'age':21}),
        ({'name': 'Mary', 'age':2}, {'name': 'Trandanpro', 'age':21}), 
        ({'name': 'Nam', 'age':2}, {'name': 'Hung', 'age':21}), 
        ({'name': 'Mai', 'age':2}, {'name': 'Loan', 'age':21})]
for index, x in enumerate(list2):
    print(index, '=>',x)
    for index, y in enumerate(x):
        print('  ',index,' ->',y )
        print('     name:',index, y['name'])
        print('     age:',index, y['age'])
        
        

    

        
