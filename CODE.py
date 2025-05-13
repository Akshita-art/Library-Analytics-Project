# -*- coding: utf-8 -*-
"""
Created on Thu Dec  5 05:10:57 2024

@author: amitv
"""

import pandas as pd
import matplotlib.pyplot as plt

# Load CSV files
ankara = pd.read_csv("C:\\Users\\amitv\\OneDrive\\Desktop\\spyder\\ankara.csv")
erciyes = pd.read_csv("C:\\Users\\amitv\\OneDrive\\Desktop\\spyder\\erciyes.csv")
frequency_a = pd.read_csv("C:\\Users\\amitv\\OneDrive\\Desktop\\spyder\\frecuency_a.csv")
frequency_e = pd.read_csv("C:\\Users\\amitv\\OneDrive\\Desktop\\spyder\\frequency_e.csv")

# Save function to overwrite CSV files after modificationm 
def save_data():
    ankara.to_csv("C:\\Users\\amitv\\OneDrive\\Desktop\\spyder\\ankara.csv", index=False)
    erciyes.to_csv("C:\\Users\\amitv\\OneDrive\\Desktop\\spyder\\erciyes.csv", index=False)
    frequency_a.to_csv("C:\\Users\\amitv\\OneDrive\\Desktop\\spyder\\frecuency_a.csv", index=False)
    frequency_e.to_csv("C:\\Users\\amitv\\OneDrive\\Desktop\\spyder\\frequency_e.csv", index=False)


# MAIN MENU
while True:
    print("Main Menu")
    print("1 - Fetch Data")
    print("2 - Data Statistics")
    print("3 - Insert Record")
    print("4 - Update Record")
    print("5 - Delete Record")
    print("6 - Data Visualization")
    print("7 - To Exit")
    
    A = int(input("Enter Your Choice- "))

    # FETCH DATA
    if A == 1:
        while True:
            print("a - To View Genre Students Prefer in Ankara University")
            print("b - To View Genre Students Prefer in Erciyes University") 
            print("c - To View Reading Frequency in Ankara University")
            print("d - To View Reading Frequency in Erciyes University")
            print("e - To Exit")
            N = input("Enter Your Choice- ")
            
            if N == "a":
                print(ankara)
                
            elif N == "b":
                print(erciyes)
                
            elif N == "c":
                print(frequency_a)
                
            elif N == "d":
                print(frequency_e)
                
            elif N == "e":
                break
            
            else:
                print("Invalid choice. Please try again.")
    
    
    #VIEW STATISTICS              
    elif A==2:
        while(True):
            print("a - To view statistics of Genre Students Prefer in Ankara University")
            print("b - To view statistics of Genre Students Prefer in Erciyes University")
            print("c - To view statistics of Reading Frequency in Ankara University")
            print("d - To view statistics of Reading Frequency in Erciyes University")
            print("e - To Exit")
            N = input("Enter Your Choice- ")
            
            if N=="a":
                print("1 - To View Transpose")
                print("2 - Display All Columns Name")
                print("3 - Display Indexes")
                print("4 - Display Shape")
                print("5 - Display Dimensions")
                print("6 - Display Data Type of All Columns")
                print("7 - Display Size")
                print("8 - Display Top 5 Records")
                print("9 - Display Bottom 5 Records")
                print("10 - To View Specific no. of Records From Top")
                print("11 - To View Specific no. of Records From Bottom") 
                print("12 - To View Details of Specific Genre")
                print("0 - To Exit")
                n=int(input("Enter Your Choice- "))
                
                if n==1:
                    print(ankara.T)
                elif n==2:
                    print(ankara.columns) 
                elif n==3:
                    print(ankara.index)
                elif n==4:
                    print(ankara.shape)
                elif n==5:
                    print(ankara.ndim)
                elif n==6:
                    print(ankara.dtypes)
                elif n==7:
                    print(ankara.size)
                elif n==8:
                    print(ankara.head())
                elif n==9:
                    print(ankara.tail())
                elif n==10:
                    p=int(input("Enter how many records you want to display from the top- "))
                    print(ankara.head(p))
                elif n==11:
                    q = int(input("Enter how many records you want to display from the bottom- "))
                    print(ankara.tail(q))
                elif n==12:
                    S = input("Enter the Genre name of which you want to see the details- ")
                    d = ankara.loc[ankara["GENRE"]==S]
                    print(d)
                elif n==0:
                    break
                else:
                    print("Invalid choice. Please try again.")
                    
            elif N=="b":    
                print("1 - To View Transpose")
                print("2 - Display All Columns Name")
                print("3 - Display Indexes")
                print("4 - Display Shape")
                print("5 - Display Dimensions")
                print("6 - Display Data Type of All Columns")
                print("7 - Display Size")
                print("8 - Display Top 5 Records")
                print("9 - Display Bottom 5 Records")
                print("10 - To View Specific no. of Records From Top")
                print("11 - To View Specific no. of Records From Bottom") 
                print("12 - To View Details of Specific genre")
                print("0 - To Exit")
                n=int(input("Enter Your Choice- "))
                
                if n==1:
                    print(erciyes.T)
                elif n==2:
                    print(erciyes.columns) 
                elif n==3:
                    print(erciyes.index)
                elif n==4:
                    print(erciyes.shape)
                elif n==5:
                    print(erciyes.ndim)
                elif n==6:
                    print(erciyes.dtypes)
                elif n==7:
                    print(erciyes.size)
                elif n==8:
                    print(erciyes.head())
                elif n==9:
                    print(erciyes.tail())
                elif n==10:
                    p=int(input("Enter how many records you want to display from the top- "))
                    print(erciyes.head(p))
                elif n==11:
                    q = int(input("Enter how many records you want to display from the bottom- "))
                    print(erciyes.tail(q))
                elif n==12:
                    S = input("Enter The Genre Name of Which You Want to See The Details- ")
                    d = erciyes.loc[erciyes["GENRE"]==S]
                    print(d)
                elif n==0:
                    break
                else:
                    print("Invalid choice. Please try again.")
                   
            elif N=="c":
                print("1 - To View Transpose")
                print("2 - Display All Columns Name")
                print("3 - Display Indexes")
                print("4 - Display Shape")
                print("5 - Display Dimensions")
                print("6 - Display Data Type of All Columns")
                print("7 - Display Size")
                print("8 - Display Top 2 Records")
                print("9 - Display Bottom 2 Records")
                print("10 - To View Specific no. of Records From Top")
                print("11 - To View Specific no. of Records From Bottom") 
                print("12 - To View Details of Specific Reading Habit")
                print("0 -  To Exit")
                n=int(input("Enter Your Choice- "))
                
                if n==1:
                    print(frequency_a.T)
                elif n==2:
                    print(frequency_a.columns) 
                elif n==3:
                    print(frequency_a.index)
                elif n==4:
                    print(frequency_a.shape)
                elif n==5:
                    print(frequency_a.ndim)
                elif n==6:
                  print(frequency_a.dtypes)
                elif n==7:
                  print(frequency_a.size)
                elif n==8:
                    print(frequency_a.head(2))
                elif n==9:
                    print(frequency_a.tail(2))
                elif n==10:
                    p=int(input("Enter how many records you want to display from the top- "))
                    print(frequency_a.head(p))
                elif n==11:
                    q = int(input("Enter how many records you want to display from the bottom- "))
                    print(frequency_a.tail(q))
                elif n==12:
                    S = input("Enter the Reading Frequency of which you want to see the details- ")
                    d = frequency_a.loc[frequency_a["FREQUENCY OF READING"]==S]
                    print(d)
                elif n==0:
                    break
                else:
                    print("Invalid choice. Please try again.")
                   
            elif N=="d":
                print("1 - To View Transpose")
                print("2 - Display All Columns Name")
                print("3 - Display Indexes")
                print("4 - Display Shape")
                print("5 - Display Dimensions")
                print("6 - Display Data Type of All Columns")
                print("7 - Display Size")
                print("8 - Display Top 2 Records")
                print("9 - Display Bottom 2 Records")
                print("10 - To View Specific no. of Records From Top")
                print("11 - To View Specific no. of Records From Bottom") 
                print("12 - To View Details of Specific Reading Habit")
                print("0 - To Exit")
                n=int(input("Enter Your Choice- "))
                
                if n==1:
                    print(frequency_e.T)
                elif n==2:
                    print(frequency_e.columns) 
                elif n==3:
                    print(frequency_e.index)
                elif n==4:
                    print(frequency_e.shape)
                elif n==5:
                    print(frequency_e.ndim)
                elif n==6:
                    print(frequency_e.dtypes)
                elif n==7:
                    print(frequency_e.size)
                elif n==8:
                    print(frequency_e.head(2))
                elif n==9:
                    print(frequency_e.tail(2))
                elif n==10:
                    p=int(input("Enter how many records you want to display from the top- "))
                    print(frequency_e.head(p))
                elif n==11:
                    q = int(input("Enter how many records you want to display from the bottom- "))
                    print(frequency_e.tail(q))
                elif n==12:
                    S = input("Enter the Reading Frequency of which you want to see the details- ")
                    d = frequency_e.loc[frequency_e["FREQUENCY OF READING"]==S]
                    print(d)
                elif n==0:
                    break
                else:
                    print("Invalid choice. Please try again.")
                
            elif N =="e":
                break
    
            else:
                print("Invalid choice. Please try again.")

    # INSERT RECORD
    elif A == 3:
        while True:
            print("a - Insert into Ankara University")
            print("b - Insert into Erciyes University")
            print("c - Insert into Reading Frequency for Ankara")
            print("d - Insert into Reading Frequency for Erciyes")
            print("e - To Exit")
            N = input("Enter Your Choice- ")
            
            if N == "a":
                print(ankara)
                sno = int(input("Enter the s.no. after the existing record- "))
                new_genre = input("Enter new Genre- ")
                new_students = int(input("Enter new Number of Students- "))
                new_percentage = float(input("Enter new Percentage- "))
                ankara.loc[sno]=[new_genre, new_students, new_percentage]
                save_data()
                print(ankara)
                print("Record inserted successfully.")
                
            elif N == "b":
                print(erciyes)
                sno = int(input("Enter the s.no. after the existing record- "))
                new_genre = input("Enter new Genre- ")
                new_students = int(input("Enter new Number of Students- "))
                new_percentage = float(input("Enter new Percentage- "))
                erciyes.loc[sno]=[new_genre, new_students, new_percentage]
                save_data()
                print(erciyes)
                print("Record inserted successfully.")
                
            elif N == "c":
                print(frequency_a)
                sno = int(input("Enter the s.no. after the existing record- "))
                new_freq = input("Enter Frequency of Reading- ")
                new_students = int(input("Enter Number of Students- "))
                new_percentage = float(input("Enter Percentage- "))
                frequency_a.loc[sno]=[new_freq, new_students, new_percentage]
                save_data()
                print(frequency_a)
                print("Record inserted successfully.")
                
            elif N == "d":
                print(frequency_e)
                sno = int(input("Enter the s.no. after the existing record- "))
                new_freq = input("Enter Frequency of Reading- ")
                new_students = int(input("Enter Number of Students- "))
                new_percentage = float(input("Enter Percentage- "))
                frequency_e.loc[sno]=[new_freq, new_students, new_percentage]
                save_data()
                print(frequency_e)
                print("Record inserted successfully.")
                
            elif N == "e":
                break
            
            else:
                print("Invalid choice. Please try again.")
    
    
    # UPDATE RECORD
    elif A == 4:
        while True:
            print("a - Update Ankara University")
            print("b - Update Erciyes University")
            print("c - Update Reading Frequency for Ankara")
            print("d - Update Reading Frequency for Erciyes")
            print("e - To Exit")
            N = input("Enter Your Choice- ")
            
            if N == "a":
                print(ankara)
                sno = int(input("Enter the s.no. of which you want to update record- "))
                if sno in ankara.index:
                    genre = input("Enter new Genre- ")
                    new_students = int(input("Enter new Number of Students- "))
                    new_percentage = float(input("Enter new Percentage- "))
                    ankara.loc[sno]=[genre, new_students, new_percentage]
                    save_data()
                    print(ankara)
                    print("Record updated successfully.")
                else:
                    print("Invalid s.no. Please try again.")
                    
            elif N == "b":
                print(erciyes)
                sno = int(input("Enter the s.no. of which you want to update record- "))
                if sno in erciyes.index:
                    genre = input("Enter new Genre- ")
                    new_students = int(input("Enter new Number of Students- "))
                    new_percentage = float(input("Enter new Percentage- "))
                    erciyes.loc[sno]=[genre, new_students, new_percentage]
                    save_data()
                    print(erciyes)
                    print("Record updated successfully.")
                else:
                    print("Invalid s.no. Please try again.")
                    
            elif N == "c":
                print(frequency_a)
                sno = int(input("Enter the s.no. of which you want to update record- "))
                if sno in frequency_a.index:
                    freq = input("Enter new Frequency- ")
                    new_students = int(input("Enter new Number of Students- "))
                    new_percentage = float(input("Enter new Percentage- "))
                    frequency_a.loc[sno]=[freq, new_students, new_percentage]
                    save_data()
                    print(frequency_a)
                    print("Record updated successfully.")
                else:
                    print("Invalid s.no. Please try again.")
                    
            elif N == "d":
                print(frequency_e)
                sno = int(input("Enter the s.no. of which you want to update record- "))
                if sno in frequency_e.index:
                    freq = input("Enter new Frequency- ")
                    new_students = int(input("Enter new Number of Students- "))
                    new_percentage = float(input("Enter new Percentage- "))
                    frequency_e.loc[sno]=[freq, new_students, new_percentage]
                    save_data()
                    print(frequency_e)
                    print("Record updated successfully.")
                else:
                    print("Invalid s.no. Please try again.")
            elif N == "e":
                break
            
            else:
                print("Invalid choice. Please try again.")
    
    
    # DELETE RECORD
    elif A == 5:
        while True:
            print("a - Delete from Ankara University")
            print("b - Delete from Erciyes University")
            print("c - Delete from Reading Frequency for Ankara")
            print("d - Delete from Reading Frequency for Erciyes")
            print("e - To Exit")
            N = input("Enter Your Choice- ")
            
            if N == "a":
                print(ankara)
                sno = int(input("Enter the s.no. of which you want to delete record- "))
                if sno in ankara.index:
                    ankara = ankara.drop([sno])
                    save_data()
                    print(ankara)
                    print("Record deleted successfully.")
                else:
                    print("Genre not found.")
                    
            elif N == "b":
                print(erciyes)
                sno = int(input("Enter the s.no. of which you want to delete record- "))
                if sno in erciyes.index:
                    erciyes = erciyes.drop([sno])
                    save_data()
                    print(erciyes)
                    print("Record deleted successfully.")
                else:
                    print("Genre not found.")
                
            elif N == "c":
                print(frequency_a)
                sno = int(input("Enter the s.no. of which you want to delete record- "))
                if sno in frequency_a["FREQUENCY OF READING"].index:
                    frequency_a = frequency_a.drop([sno])
                    save_data()
                    print(frequency_a)
                    print("Record deleted successfully.")
                else:
                    print("Frecuency not found.")
                    
            elif N == "d":
                print(frequency_e)
                sno = int(input("Enter the s.no. of which you want to delete record- "))
                if sno in frequency_e["FREQUENCY OF READING"].index:
                    frequency_e = frequency_e.drop([sno])
                    save_data()
                    print(frequency_e)
                    print("Record deleted successfully.")
                else:
                    print("Frecuency not found.")
                    
            elif N == "e":
                break
            
            else:
                print("Invalid choice. Please try again.")
    
   
    # DATA VISUALIZATION
    elif A == 6:
        while True:
            print("DATA VISUALIZATION MENU")
            print("1 - Visualize Genre Preferences in Ankara University")
            print("2 - Visualize Genre Preferences in Erciyes University")
            print("3 - Visualize Reading Frequency in Ankara University")
            print("4 - Visualize Reading Frequency in Erciyes University")
            print("5 - To Exit")
            
            vis_choice = int(input("Enter Your Choice- "))
            
            if vis_choice in [1,2,3,4]:
                print("Select Visualization Type- ")
                print("1 - Bar Chart")
                print("2 - Line Chart")
                print("3 - Pie Chart")
                chart_type = int(input("Enter Your Choice- "))

                if vis_choice == 1:
                    data = ankara
                    title = "Genre Preferences in Ankara University"
                elif vis_choice == 2:
                    data = erciyes
                    title = "Genre Preferences in Erciyes University"
                elif vis_choice == 3:
                    data = frequency_a
                    title = "Reading Frequency in Ankara University"
                elif vis_choice == 4:
                    data = frequency_e
                    title = "Reading Frequency in Erciyes University"
                
                if chart_type == 1:
                    plt.figure(figsize=(10, 6))
                    plt.bar(data["FREQUENCY OF READING"] if vis_choice >= 3 else data["GENRE"], 
                            data["NUMBER OF STUDENTS"], color="blue" if vis_choice < 3 else "purple")
                    plt.title(title)
                    plt.xlabel("Category")
                    plt.ylabel("Number of Students")
                    plt.xticks(rotation=45, ha="right")
                    plt.show()
                    
                elif chart_type == 2:
                    plt.figure(figsize=(10, 6))
                    plt.plot(data["FREQUENCY OF READING"] if vis_choice >= 3 else data["GENRE"], 
                             data["NUMBER OF STUDENTS"], marker="o", color="orange")
                    plt.title(title)
                    plt.xlabel("Category")
                    plt.ylabel("Number of Students")
                    plt.xticks(rotation=45, ha="right")
                    plt.show()
                    
                elif chart_type == 3:
                    plt.figure(figsize=(10, 6))
                    plt.pie(data["NUMBER OF STUDENTS"], labels=data["FREQUENCY OF READING"] if 
                            vis_choice >= 3 else data["GENRE"], autopct="%1.1f%%")
                    plt.title(title)
                    plt.axis("equal")  # Equal aspect ratio ensures that pie is drawn as a circle.
                    plt.show()
                
                else:
                    print("Invalid choice. Please try again.")
                        
            elif vis_choice == 5:
                break
            
            else:
                print("Invalid choice. Please try again.")
   
    
   # EXIT
    elif A == 7:
        print("Thank you for using the program.")
        break

    else:
        print("Invalid choice. Please try again.")