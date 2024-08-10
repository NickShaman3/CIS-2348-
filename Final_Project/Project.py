import csv

class csvReader:
    def __init__(self):
      self.manufactureIndex = []
    
    def printIndex(self):
        return self.manufactureIndex
        
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



def main():
  go = csvReader()
  go.manuInput('ManufacturerList.csv')
  go.priceInput('PriceList.csv')
  go.serviceInput('ServiceDatesList.csv')

  
  go.inventoryOutput('FullInventory.csv')
 
  go.inventoryListOutput('PhoneInventory.csv', 'TowerInventory.csv', 'LaptopInventory.csv')
  
  #c
  

  #d


if __name__ == "__main__":
  main()

#skeleton
"""class inventoryManager():
    inventorydata = {}
    def read_files(file1 = "Name of first file", file2 = "Name of second file", file3 = "Name of third file"):
        print(file1)#write a wit block that reads from the file and puts data into the inventory data that I have defined making the customer ID the key.
        print(file2)
        print(file3) 
        
    #four methods after the file method that will read for the documents

    def fullinventory():
        return inventoryManager.inventorydata
    
    def inventorylist():
        return inventoryManager.inventorydata
    
    def pastservicedata():
        return inventoryManager.inventorydata
    
    def damagedinventory():
        return inventoryManager.inventorydata

if __name__ == "__main__":
    file1 = "manufacturerlist.csv"
    file2 = "pricelist.csv"
    file3 = "servicedatelist.csv"
    inventoryManager = inventoryManager()
    inventoryManager.read_files(file1, file2, file3)
    inventoryManager.fullinventory()
    inventoryManager.inventorylist()
    inventoryManager.pastservicedata()
    inventoryManager.damagedinventory()"""
