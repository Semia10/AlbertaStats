import csv

# with open('albertaCensusData.csv', encoding = "utf-8") as csv_file:
#     csv_reader = csv.reader(csv_file, delimiter=',')
    
#     ridings = {}


#     for row in csv_reader:
#         if (row[1] != ridings):
#             ridings[row[1]] = []

#     csv_reader.seek(0)

#     for row in csv_reader:
#         print(row)

ridings = {}


def main():
    csv_file = open('albertaCensusData.csv')
    csv_reader = csv.reader(csv_file)

    for row in csv_reader:
        if (row[1] != ridings):
            ridings[row[1]] = []
    
    csv_file.seek(0)

    # parse through looking for age groups

    for row in csv_reader:
        if (row[2] == "Total - Age groups"):
            ridings[row[1]].append(("ID", int(row[0])))
            ridings[row[1]].append(("Population", int(float( row[5].replace(',', '')) )))
            ridings[row[1]].append(("Name", row[1]))


            for i in range (0, 6):
                next(csv_reader)
            
            ageCounter = 0
            for i in range(0, 3):
                temp = next(csv_reader)
                ageCounter += int(float(temp[5].replace(',', '')))
            ridings[row[1]].append(("Age20_34", ageCounter/ridings[row[1]][1][1]))
            
            ageCounter = 0
            for i in range(0, 3):
                temp = next(csv_reader)
                ageCounter += int(float(temp[5].replace(',', '')))
            ridings[row[1]].append(("Age35_49", ageCounter/ridings[row[1]][1][1]))

            ageCounter = 0
            for i in range(0, 3):
                temp = next(csv_reader)
                ageCounter += int(float(temp[5].replace(',', '')))
            ridings[row[1]].append(("Age50_64", ageCounter/ridings[row[1]][1][1]))

            temp = next(csv_reader)
            ridings[row[1]].append(("Age64Over", (int(float(temp[5].replace(',', ''))) / ridings[row[1]][1][1])))

    # parse through looking for household income
    csv_file.seek(0)

    for row in csv_reader:
        if (row[2] == "Average total income of households in 2015 ($)"):
            ridings[row[1]].append(("AvgHouseholdIncome", float(row[5].replace(',', ''))))
        
        if (row[2] == "Unemployment rate" and ridings[row[1]][len(ridings[row[1]])-1][0] != "UnemploymentRate"):
            ridings[row[1]].append(("UnemploymentRate", float(row[5].replace(',', ''))))

        if (row[2] == "Total - Immigrant status and period of immigration for the population in private households - 25% sample data"):
            totalPeople = float(row[5].replace(',', ''))
            nonImmigrants = float(next(csv_reader)[5].replace(',', ''))
            immigrants = float(next(csv_reader)[5].replace(',', ''))
            
            ridings[row[1]].append(("Immigration", immigrants / totalPeople))

        if (row[2] == "Total - Visible minority for the population in private households - 25% sample data"):
            totalPeople = float(row[5].replace(',', ''))

            next(csv_file)

            asian = int(float(next(csv_reader)[5].replace(',', '')))
            asian += int(float(next(csv_reader)[5].replace(',', '')))
            african = int(float(next(csv_reader)[5].replace(',', '')))
            asian += int(float(next(csv_reader)[5].replace(',', '')))
            hispanic = int(float(next(csv_reader)[5].replace(',', '')))
            middleEastern = int(float(next(csv_reader)[5].replace(',', '')))
            asian += int(float(next(csv_reader)[5].replace(',', '')))
            middleEastern += int(float(next(csv_reader)[5].replace(',', '')))
            asian += int(float(next(csv_reader)[5].replace(',', '')))
            asian += int(float(next(csv_reader)[5].replace(',', '')))
            next(csv_file)
            next(csv_file)
            white = int(float(next(csv_reader)[5].replace(',', '')))

            ridings[row[1]].append(("Asian", asian/totalPeople))
            ridings[row[1]].append(("African", african/totalPeople))
            ridings[row[1]].append(("Hispanic", hispanic/totalPeople))
            ridings[row[1]].append(("MiddleEastern", middleEastern/totalPeople))
            ridings[row[1]].append(("white", white/totalPeople))

        if (row[2] == "Total - Highest certificate, diploma or degree for the population aged 15 years and over in private households - 25% sample data"):
            totalPeople = float(row[5].replace(',', ''))

            noCertificate = int(float(next(csv_reader)[5].replace(',', '')))
            secondaryDiploma = int(float(next(csv_reader)[5].replace(',', '')))
            postSecondaryDiploma = int(float(next(csv_reader)[5].replace(',', '')))
            
            ridings[row[1]].append(("NoCertificate", noCertificate/totalPeople))
            ridings[row[1]].append(("secondaryDiploma", secondaryDiploma/totalPeople))
            ridings[row[1]].append(("postSecondaryDiploma", postSecondaryDiploma/totalPeople))

    


main()   

with open('data.csv', mode='w') as data:
    employee_writer = csv.writer(data, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

    for row in ridings:
        employee_writer.writerow(ridings[row])
