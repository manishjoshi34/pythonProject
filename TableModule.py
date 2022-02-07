import pandas as pd
from datetime import date

class Test:
    def __init__(self, number):
        self._number = number
    def __str__(self):
        return str(self._number)
    def getNumber(self):
        return self._number
    def setNumber(self, number):
        self._number = number

class Table:
    def __init__(self, listOfColmns = []):
        self.dataframe = pd.DataFrame(columns = listOfColmns)

    def __str__(self):
        return str(self.dataframe)

    def addColumns(self,name):
        for col in name:
            self.dataframe[col] = pd.Series(index= self.dataframe.index)
    def addRow(self, index, rowValue):
        self.dataframe.loc[index] = rowValue
    def removeColumn(self,name):
        self.dataframe.drop(name,axis = 1, inplace = True)
    def getRow(self, index):
        return self.dataframe.loc[index]
    def updateValue(self, row, col,value):
        self.dataframe[col][row] = value
        


def testTable():
    print("Test table")
    table = Table()
    print(table)
    table.addColumns(["Date","Amount","Credit"])
    print(table)
    row_val = {}
    row_val["Date"] = date.today()
    row_val["Amount"] = 250
    row_val["Credit"] = True
    index = 0
    table.addRow(index,row_val)
    index +=1
    table.addRow(index,row_val)
    table.addColumns(["Note"])
    print(table)
    table.removeColumn("Note")
    print(table)
    row = table.getRow(0)
    table.updateValue(0,"Amount",300)
    print(table)

if __name__=='__main__':
    testTable()

