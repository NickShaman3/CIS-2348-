import csv

class csvReader:
    manufactureIndex = []
    #def __init__(self):
      #self.manufactureIndex = []
    
    #def printIndex(self):
        #return self.manufactureIndex
        
    def manuInput(self, csvFile):
      with open(csvFile, newline='') as csvfile:
          file = csv.reader(csvfile)
          for line in file:
              manuDict = {
                  'ID': line[0], 
                  'ManufacturerName': line[1], 
                  'itemType': line[2], 
                  'damagedInd': line[3]
              }
              self.manufactureIndex.append(manuDict)


    def priceInput(self, csvFile):
      with open(csvFile, newline='') as csvfile:
          file = csv.reader(csvfile)
          for priceInputLine in file:
              for j in self.manufactureIndex:
                  if int(priceInputLine[0]) == int(j['ID']): 
                      j['Price'] = priceInputLine[1] 

    def serviceInput(self, csvFile):
      with open(csvFile, newline='') as csvfile:
          file = csv.reader(csvfile)
          for priceInputLine in file:
              for j in self.manufactureIndex:
                  if int(priceInputLine[0]) == int(j['ID']): 
                      j['Date'] = priceInputLine[1] 

    def inventoryOutput(self, outputFile):
        self.manufactureIndex.sort(key=lambda x: x['ManufacturerName'])
        with open(outputFile, mode='w', newline='') as file:
              writer = csv.writer(file)
              for i in self.manufactureIndex:
                  writer.writerow([
                      i['ID'], 
                      i['ManufacturerName'], 
                      i['itemType'], 
                      i.get('Price', 'N/A'),  
                      i.get('Date', 'N/A'),   
                      i['damagedInd']
                  ])
              
    def inventoryListOutput(self, csvFile1, csvFile2, csvFile3):
        self.manufactureIndex.sort(key=lambda x: x['ID'])
        with open(csvFile1, mode='w', newline='') as file:
              writer = csv.writer(file)
              for i in self.manufactureIndex:
                  if i['itemType'] == 'phone':
                      writer.writerow([
                          i['ID'], 
                          i['ManufacturerName'], 
                          i.get('Price', 'N/A'),  
                          i.get('Date', 'N/A'),   
                          i['damagedInd']
                      ])
        with open(csvFile2, mode='w', newline='') as file: 
              writer = csv.writer(file)
              for i in self.manufactureIndex:
                  if i['itemType'] == 'tower':
                      writer.writerow([
                          i['ID'], 
                          i['ManufacturerName'], 
                          i.get('Price', 'N/A'),  
                          i.get('Date', 'N/A'),   
                          i['damagedInd']
                      ])    
        with open(csvFile3, mode='w', newline='') as file: 
              writer = csv.writer(file)
              for i in self.manufactureIndex:
                  if i['itemType'] == 'laptop':
                      writer.writerow([
                          i['ID'], 
                          i['ManufacturerName'], 
                          i.get('Price', 'N/A'),  
                          i.get('Date', 'N/A'),   
                          i['damagedInd']
                      ])




go = csvReader()
go.manuInput('ManufacturerList.csv')
print(go.manufactureIndex)
"""go.priceInput('PriceList.csv')
  go.serviceInput('ServiceDatesList.csv')

  
  go.inventoryOutput('FullInventory.csv')
 
  go.inventoryListOutput('PhoneInventory.csv', 'TowerInventory.csv', 'LaptopInventory.csv')
  
  #c
  

  #d


if __name__ == "__main__":
  main()

#skeleton"""
