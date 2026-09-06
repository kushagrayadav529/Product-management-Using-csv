import csv
import os
from datetime import datetime

class ProductCSV:
    def __init__(self, colname, filename="product.csv"):
        self.filename = filename
        with open(self.filename, "w", newline='') as fspcsv:
                csvwrite = csv.writer(fspcsv)
                csvwrite.writerow(colname)

    def add_items(self, data):
        # from object the data is updated in the csv file
        with open(self.filename, "a", newline='') as fspcsv:
            csvwrite = csv.writer(fspcsv)
            csvwrite.writerow(data)

    def display(self):
        # To display the or print the details from the csv
        with open("product.csv","r",newline='') as fspcsv:
            csvreader=csv.reader(fspcsv)
            colname=next(csvreader)
            print(colname)
            for csvrow in csvreader:
                print(csvrow)

    def update(self):
        # To modify the details from prextining data
        product_id=input("Enter product id u want to update:")
        ndata=[]
        
        with open("product.csv","r",newline='') as fspcsv:
            csvreader=csv.reader(fspcsv)
            colname=next(csvreader)
            ndata.append(colname)
            
            for csvrow in csvreader:
                if csvrow[0]==product_id:
                    
                    updatedlist=[]
                    
                    updatedlist.append(product_id)
                    
                    product_name = input("Enter Product Name: ")
                    cost_price = input("Enter Cost Price: ")
                    sell_price = input("Enter Sell Price: ")
                    discount = input("Enter Discount: ")
                    dom = input("Enter Date of Manufacture (DOM): ")
                    doe = input("Enter Date of Expiry (DOE): ")
                    category_name = input("Enter Category Name: ")

                    updatedlist.append(product_name)
                    updatedlist.append(cost_price)
                    updatedlist.append(sell_price)
                    updatedlist.append(discount)
                    updatedlist.append(dom)
                    updatedlist.append(doe)
                    updatedlist.append(category_name)
                    
                    ndata.append(updatedlist)
                    
                else:
                    ndata.append(csvrow)
                    
        with open("product.csv","w",newline='') as fspcsv:
            csvwriter=csv.writer(fspcsv)
            csvwriter.writerows(ndata)
            
        print(" Data is updated ")

    def delete(self):
        
        productid = input("enter product id  you want to delete : ")
        new_product_list = []
        # Read all existing products before removing the selected product
        with open('Product.csv', 'r', newline='') as fspcsv:
            csvread_obj = csv.reader(fspcsv)
            colnames = next(csvread_obj)
            new_product_list.append(colnames)
            print(colnames)
            for csvrow in csvread_obj:
                 # Add every product except the one the user wants to delete
                  if csvrow[0]  !=  productid:
                     new_product_list.append(csvrow)
        with open('Product.csv','w',newline = '') as fspcsv:
            csvwriter  = csv.writer(fspcsv)
            csvwriter.writerows(new_product_list)
            
                
    def search(self):     
            # Ask the user which product field they want to search
        ch = input("1 product name \n"
        "2 cost price\n"
        "3 sell price\n"
        "4 discount\n"
        "5 category name \n"
        "by which you want to search product , enter  :")
        # Store the CSV column number according to the user's choice
        column = 1
        if ch == "1":
           column = 1
        elif ch == "2":
           column = 2
        elif ch == "3":
           column = 3
        elif ch == "4":
           column = 4
        elif ch == "5":
           column = 7
        else:
           print("Invalid choice")
           return


        # Take the value that we want to find in the selected column
        search_value = input("Enter product details you want to search :")
        with open('Product.csv','r',newline = '') as fspcsv:
                csvread_obj = csv.reader(fspcsv)  
                colnames = next(csvread_obj)
                found = False
                for csvrow in csvread_obj:
                    if csvrow[column]  == search_value:
                       print(csvrow) 
                       found = True

                if not found:
                    print("NOT found")

# Initialize object with column headers
info = ['product_id', 'product_name', 'cost_price', 'sell_price', 'discount', 'dom', 'doe', 'category_name']
obj = ProductCSV(info)

while True:

    print("\n======================================")
    print("       PRODUCT MANAGEMENT SYSTEM")
    print("======================================")

    print("1. Add Product")
    print("2. Update Product")
    print("3. Delete Product")
    print("4. Display All Products")
    print("5. Search Product")
    print("6. Exit")

    a = input("\nEnter your choice: ")

    if a == "1":
        choice = 'y'
        while choice.lower() == 'y':
            data = []

            product_id = input("Enter Product ID: ")
            product_name = input("Enter Product Name: ")
            cost_price = input("Enter Cost Price: ")
            sell_price = input("Enter Sell Price: ")
            discount = input("Enter Discount: ")
            dom = input("Enter Date of Manufacture (DOM): ")
            doe = input("Enter Date of Expiry (DOE): ")
            category_name = input("Enter Category Name: ")

            data.extend([product_id, product_name, cost_price, sell_price, discount, dom, doe, category_name])
    
            # Save the row to CSV
            obj.add_items(data)

            choice = input("Want to add more? (y/n): ")

    elif a == "2":
        obj.update()

    elif a == "3":
        obj.delete()

    elif a == "4":
        obj.display()

    elif a == "5":
       obj.search()

    elif a == "6":
        print("\nThank you for using Product Management System!")
        break

    else:
        print("\nInvalid choice! Please try again.")








