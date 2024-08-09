import csv
manufactureIndex = []

#input
with open('ManufacturerList.csv', newline='') as csvfile:
  file = csv.reader(csvfile)
  for line in file:
    manuDict = {
      'ID':  line[0],
      'ManufactererName':line[1],
      'itemType': line[2],
      'damagedInd':line[3]
    }
    manufactureIndex.append(manuDict)

print(manufactureIndex)

"""with open('PriceList.csv', newline='') as csvfile:
  file = csv.reader(csvfile)
  for i in file:
      for j in manufactureIndex:
          if int(i[0]) == int(j['ID']):
              j['Price'] = i[1]

i = j = 0
with open('ServiceDatesList.csv', newline='') as csvfile:
  file = csv.reader(csvfile)
  for i in file:
      for j in manufactureIndex:
          if int(i[0]) == int(j['ID']):
              j['Date'] = i[1]



#output
with open('FullInventory.csv', mode='w', newline='') as file:
  writer = csv.writer(file)
  for i in manufactureIndex:
    writer.writerow([i['ID'], i['ManufactererName'], i['itemType'], i['Price'], i['Date'], i['damagedInd']])
"""

class inventoryManager():
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
    inventoryManager.damagedinventory()
