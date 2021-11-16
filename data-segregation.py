import csv

data_book = "data.csv"
countries_list = []
categories_list = []

def use_csv_book(file_name_1, countries, file_name_2, categories):
    
    with open(data_book, "r") as file1:
        csv_reader = csv.reader(file1)

        for data in csv_reader:
            country = data[0]
            category = data[3]
            if country not in countries:
                countries.append(country)
            if category not in categories:
                categories.append(category)

    file1.close()

    with open(file_name_1 + '.txt', "w", newline="") as file2:
        for data in countries:
            data = data + "\n"
            file2.writelines(data)

    file2.close()

    with open(file_name_2 + '.txt', "w", newline="") as file3:
        for data in categories:
            data = data + "\n"
            file3.writelines(data)

    file3.close()

use_csv_book('countries', countries_list, 'categories', categories_list)            
