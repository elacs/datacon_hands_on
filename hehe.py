def fix_salesdate (salesdate):
    lis = salesdate.split('/')
    d = lis[0]
    m = lis[1]
    y = lis[2]
    while len(d) < 2:
        d = '0' + d
    while len(m) < 2:
        m = '0' + m
    return y + '-' + m + '-' + d


fp = open('sales.csv','r')
fc = fp.read()
rows = fc.split('\n')
#print(len(rows))
#print(rows[-2])
l = len(rows)
#print (rows[0])
newtext = rows[0] + '\n'
print(newtext)
for i in range(1,l-1):
    row_contents = rows[i].split(',')
    salesdate = row_contents[1]
    new_salesdate = fix_salesdate(salesdate)
#    print(rows[i])
    new_row = row_contents[0] + ',' + new_salesdate + ',' + row_contents[2] + ',' + row_contents[3] + ',' + row_contents[4] + ',' + row_contents[5] + ',' + row_contents[6] + ',' + row_contents[7] + ',' + row_contents[8] + ',' + row_contents[9]
    newtext += new_row + '\n'
#    print(row_contents)
 #   print(new_salesdate)
    #print(new_row)
#for row in fc.split('\n'):
 #   print(row)
#print(fc)
newfp = open('newsales.csv', 'w')
newfp.write(newtext)
newfp.close()
fp.close()
