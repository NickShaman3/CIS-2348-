import csv
from datetime import datetime

class csvReader:
    manufactureIndex = []
    #def __init__(self):
      #self.manufactureIndex = []
    
    #def printIndex(self):
        #return self.manufactureIndex
        
    def manuInput(self, csvFile):
      with open(csvFile) as csvfile:
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
          for input in file:
              for j in self.manufactureIndex:
                  if int(input[0]) == int(j['ID']): 
                      j['Price'] = input[1] 

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
              for input in self.manufactureIndex:
                  writer.writerow([
                      input['ID'], 
                      input['ManufacturerName'], 
                      input['itemType'], 
                      input.get('Price', 'N/A'),  
                      input.get('Date', 'N/A'),   
                      input['damagedInd']
                  ])
              
    def inventoryListOutput(self, csvFile1, csvFile2, csvFile3):
        self.manufactureIndex.sort(key=lambda x: x['ID'])
        with open(csvFile1, mode='w', newline='') as file:
              writer = csv.writer(file)
              for input in self.manufactureIndex:
                  if input['itemType'] == 'phone':
                      writer.writerow([
                          input['ID'], 
                          input['ManufacturerName'], 
                          input.get('Price', 'N/A'),  
                          input.get('Date', 'N/A'),   
                          input['damagedInd']
                      ])
        with open(csvFile2, mode='w', newline='') as file: 
              writer = csv.writer(file)
              for input in self.manufactureIndex:
                  if input['itemType'] == 'tower':
                      writer.writerow([
                          input['ID'], 
                          input['ManufacturerName'], 
                          input.get('Price', 'N/A'),  
                          input.get('Date', 'N/A'),   
                          input['damagedInd']
                      ])    
        with open(csvFile3, mode='w', newline='') as file: 
              writer = csv.writer(file)
              for input in self.manufactureIndex:
                  if input['itemType'] == 'laptop':
                      writer.writerow([
                          input['ID'], 
                          input['ManufacturerName'], 
                          input.get('Price', 'N/A'),  
                          input.get('Date', 'N/A'),   
                          input['damagedInd']
                      ])


    def getpastServicedateinventory(self, outputFile):
        pastServicedateinventory = sorted([item for item in self.manufactureIndex if datetime.strp(item['ServiceDate'], '%Y-%m-%D') < datetime.today()], key= lambda x: datetime.strptime(x['ServiceDate'], '%Y-%m-%D'))
        with open(outputFile, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([
                input["ID"],
                input["ManufacturerName"],
                input["itemType"],
                input["Price", 'N/A'],
                input["Date", "N/A"],
                input["damagedInd"]
                ]
                )
            for input in pastServicedateinventory:
                writer.writerow([
                    input["ID"],
                    input["ManufacturerName"],
                    input["itemType"],
                    input["Price"],
                    input["Date"],
                    input["damagedInd"]
                    ]
                    )
                
                
        def damagedInventoryOutput(self, outputFile):
            damagedInventory = sorted([input for input in self.manufactureIndex if input["damagedInd"] == "damaged"], key = lambda x: float(x["Price"]), reverse = True)
            with open(outputFile, "w", newline='') as file:
                writer = csv.writer(file)
                writer.writerow([
                    input["ID"],
                    input["ManufacturerName"],
                    input["itemType"],
                    input["Price"],
                    input["Date"],
                    input["damagedInd"]
                    ]
                    )
                for input in damagedInventory:
                    writer.writerow([
                        input["ID"],
                        input["ManufacturerName"],
                        input["itemType"],
                        input["Price"],
                        input["Date"]
                        ]
                        )




go = csvReader()
go.manuInput("CIS-2348-/Final_Project/ManufacturerList.csv")
print(go.manufactureIndex)
go.priceInput("CIS-2348-/Final_Project/PriceList.csv")
go.serviceInput("CIS-2348-/Final_Project/ServiceDatesList.csv")

  
go.inventoryOutput('FullInventory.csv')
 
go.inventoryListOutput('PhoneInventory.csv', 'TowerInventory.csv', 'LaptopInventory.csv')
  
  
go.getpastServicedateinventory('PastServiceDateInventory.csv')

  
go.damagedInventoryOutput('DamagedInvetory.csv')

if __name__ == "__main__":
  main()


