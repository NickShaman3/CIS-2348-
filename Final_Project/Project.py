import csv
from datetime import datetime


class csvReader:
    manufactureIndex = []

    #def __init__(self):
    #self.manufactureIndex = []

    #def printIndex(self):
    #return self.manufactureIndex

    def manuInput(self, csvFile):  #recievs input
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

    def priceInput(self, csvFile):  #recieves input
        with open(csvFile, newline='') as csvfile:
            file = csv.reader(csvfile)
            for input in file:
                for j in self.manufactureIndex:
                    if int(input[0]) == int(j['ID']):
                        j['Price'] = input[1]

    def serviceInput(self, csvFile):  #recieves input
        with open(csvFile, newline='') as csvfile:
            file = csv.reader(csvfile)
            for priceInputLine in file:
                for j in self.manufactureIndex:
                    if int(priceInputLine[0]) == int(j['ID']):
                        j['Date'] = priceInputLine[1]

    def inventoryOutput(self, outputFile):  #this is for a
        self.manufactureIndex.sort(key=lambda x: x['ManufacturerName'])
        with open(outputFile, mode='w', newline='') as file:
            writer = csv.writer(file)
            for input in self.manufactureIndex:
                writer.writerow([
                    input['ID'], input['ManufacturerName'], input['itemType'],
                    input.get('Price', 'N/A'),
                    input.get('Date', 'N/A'), input['damagedInd']
                ])

    def inventoryListOutput(self, csvFile1, csvFile2,
                            csvFile3):  #this is for b
        self.manufactureIndex.sort(key=lambda x: x['ID'])
        with open(csvFile1, mode='w', newline='') as file:
            writer = csv.writer(file)
            for input in self.manufactureIndex:
                if input['itemType'] == 'phone':
                    writer.writerow([
                        input['ID'], input['ManufacturerName'],
                        input.get('Price', 'N/A'),
                        input.get('Date', 'N/A'), input['damagedInd']
                    ])
        with open(csvFile2, mode='w', newline='') as file:
            writer = csv.writer(file)
            for input in self.manufactureIndex:
                if input['itemType'] == 'tower':
                    writer.writerow([
                        input['ID'], input['ManufacturerName'],
                        input.get('Price', 'N/A'),
                        input.get('Date', 'N/A'), input['damagedInd']
                    ])
        with open(csvFile3, mode='w', newline='') as file:
            writer = csv.writer(file)
            for i in self.manufactureIndex:
                if i['itemType'] == 'laptop':
                    writer.writerow([
                        i['ID'], i['ManufacturerName'],
                        i.get('Price', 'N/A'),
                        i.get('Date', 'N/A'), i['damagedInd']
                    ])

    def serviceDateOutput(self, outputFile):
        self.manufactureIndex.sort(
            key=lambda x: datetime.strptime(x['Date'], '%m/%d/%Y'))
        with open(outputFile, mode='w', newline='') as file:
            writer = csv.writer(file)
            for input in self.manufactureIndex:
                if input['Date'] != 'N/A':
                    theDate = datetime.strptime(input['Date'],
                                                '%m/%d/%Y').date()
                    if theDate < datetime.today().date():  #compares the dates
                        writer.writerow([
                            input['ID'], input['ManufacturerName'],
                            input['itemType'],
                            input.get('Price', 'N/A'),
                            input.get('Date', 'N/A'), input['damagedInd']
                        ])

    def damagedListOutput(self, csvFile):  #this is for d
        self.manufactureIndex.sort(reverse=True, key=lambda x: x['Price'])
        with open(csvFile, mode='w', newline='') as file:
            writer = csv.writer(file)
            for input in self.manufactureIndex:
                if input['damagedInd'] != '':
                    writer.writerow([
                        input['ID'], input['ManufacturerName'],
                        input['itemType'],
                        input.get('Price', 'N/A'),
                        input.get('Date', 'N/A'), input['damagedInd']
                    ])


def main():
    go = csvReader()
    go.manuInput('ManufacturerList.csv')
    go.priceInput('PriceList.csv')
    go.serviceInput('ServiceDatesList.csv')

    go.inventoryOutput('FullInventory.csv')
    go.inventoryListOutput('PhoneInventory.csv', 'TowerInventory.csv',
                           'LaptopInventory.csv')
    go.serviceDateOutput('PastServiceDateInventory.csv')
    go.damagedListOutput('DamagedInventory.csv')


if __name__ == "__main__":
    main()


