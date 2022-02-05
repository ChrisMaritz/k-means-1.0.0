
#K-Means clustering implementation

'''
First thing I did which was needed was to create the function to define the function for the distance
of each point, I simply took the formula given and just applied returning the distance.

The next step I took was to define the function to open the csv file which is pretty straight forward
similar to opening a text file

The next step I took was to assign each country to which centroid it was closest to. The first thing I did was loop through 
the array of all the countries and assign each x and y value to and x and y value variable and then the next thing to loop 
through within this loop was the centroids, applying each x and y value of the centroid to seperate varables and then measuring 
the distance between the point from the array and then the centroid and appending the return distance to an array thus having all 
the distance for each centroid in an array, the exiting that loop still in the first loop it loops through the centroids again checking
wether the index of the smallest point with the centroids matches the centroid being looped through and if it matches it will add the 
chosen array item to a dictionary where it is applied to the centroid (being the key of the dictionary) it is closest to. the dictionary 
then returned

The next step I took was to define the new centroids which were the means of the centroids. a Parameter of this function is the return of
the function which returns the assigned points to the centroids. The first step to find the mean was to loop through the through the dictionary
then splitting the dictionary item being iteritated in an array and then looping through that array. Each item being looped in this 
array is an country with its x and y values so how it would go is that it would apply the x value to a variable and then dd the y value to 
a variable as well as having a counter for this loop, the x or y value keeps adding each x and y value in each item upon one another so you end
up with the sum of x and y values and amount of values and  then the mean for x and y value is calculated and appended to an array and then 
eventually all the new centroids are calculated.

The last remaining function being the plot function is there to serve the purpose of plotting all the information on a plot, it will go through the data 
created by the findCentroid function seperating each centroids data and then seperating the x and y axis in seperate variables, then it is plotted on a 
scatter plot with a colour map to ensure it can be seen where the points are seperated. The plot is given the appropiate title and displayed

so in short with each of these function the centroids are chosen at random and then each item is assigned to each centroids and then each new centroids is 
calculated and it is repeated however many times stated. And this happens with each data set from the csv files of 1953, 2008 and both
'''

#Some hints on how to start, as well as guidance on things which may trip you up, have been added to this file.
#You will have to add more code that just the hints provided here for the full implementation.
#You will also have to import relevant libraries for graph plotting and maths functions.

# ====
# Define a function that computes the distance between two data points



from cmath import sqrt
import csv as csv
import matplotlib.pyplot as plt
import random as rdm

import numpy 


'''Each new distance is calcualted '''

def distance(x1, y1, x2, y2):
    distance = sqrt((float(x2) - float(x1))**2 + (float(y2) - float(y1))**2)
    return distance


# ====
# Define a function that reads data in from the csv files  
# HINT: http://docs.python.org/2/library/csv.html. 
# HINT2: Remember that CSV files are comma separated, so you should use a "," as a delimiter. 
# HINT3: Ensure you are reading the csv file in the correct mode.


'''A function that serves to open a csv file and then applying it to a array '''
#To learn how to read a csv file I used this link https://www.analyticsvidhya.com/blog/2021/08/python-tutorial-working-with-csv-file-for-data-science/ I read their explanation of all the info
#and then coded what was  explained on what is consisted in a csv reader. I found this site more simple as the one provided

def open_csv(csv1):
    output = []
    with open(csv1, 'rt') as read_this:
        write = csv.reader(read_this, delimiter = ",")
        for row in write:
            output.append(row)
    output.remove(output[0])
    return output


# ====
# Define a function that finds the closest centroid to each point out of all the centroids
# HINT: This function should call the function you implemented that computes the distance between two data points.
# HINT: Numpy has a useful method that allows you to find the index of the smallest value in an array. 


''' This function serves as purpose to find all the closest points to each centroids'''

def find_centroid(centroids, array):
    number = 0
    assigned = {}


    #Each item in the array which contains all the countries is iterated through

    for f in array:


        #the x and y value is applied to variables

        x_var = float(array[number][1])
        y_var = float(array[number][2])
        number_2 = 0
        smallest = []


        #All the centroids are then looped through

        for y in centroids:


            #The x and y values are the applied to varaibles

            try:
                x_cent = float(centroids[number_2][1])
                y_cent = float(centroids[number_2][2])
            except:
                x_cent = float(centroids[number_2][0])
                y_cent = float(centroids[number_2][1])

            
            #The distance from the centroid to the array item is appended to an array

            smallest.append(distance(x_var, y_var, x_cent, y_cent))
            number_2 += 1


        #The index of the smallest value is applied to a variable
        #With argimin method this clue was given in the compulsary and this was the function I found when I googled for a method that returns
        #the index of the smallest value, I found it here https://numpy.org/doc/stable/reference/generated/numpy.argmin.html

        tiniest = numpy.argmin(smallest)


        #The centroids are looped through again

        for t in centroids:


            #If the centroid index of the smallest value of the distance of all the three centroids equal to t the following will happen
            #f being the array item is then added to which value is the centroid its closest to being the key of the dictionary

            if centroids[tiniest] == t:
                try:
                    assigned[str(t)] += str(f)
                except:
                    assigned[str(t)] = str(f)
       
        number += 1
    
    
    #The dictionary is then returned

    return assigned


#====
#Write a function to visualise the clusters. (optional, but useful to see the changes and if your algorithm is working)

'''This function serves as a purpose of displaying all the data with their final centroids data each in a different colour'''

def plot(array, data):


    #Variables

    colour_number = 0
    number_name = 0


    #A for loop is created which goes through the dictionary returned by find_centroid()

    for x in array:


        #Colour number is plused by 1

        colour_number += 1


        #The arrays are initialized which are meant to seperate the x and y axis from array

        x_values = []
        y_values = []


        #array2 is equal to each item of the item in array being iterated

        array2 = str(array[x]).split("[")


        #A for loop is created which goes through array2

        for y in array2:


            #The necessary steps are taken to create an array item to be used of y 

            single = y.replace("]", "")
            single = single.replace("'", "")
            array_single = single.split(",")


            #the x and y values are added to x_values and y_values

            if(len(array_single) != 1):
                x_values.append(float(array_single[1]))
                y_values.append(float(array_single[2]))
        

        #The scatter plot is created with a colourmap of tab20
        #I got information I needed to use colour maps from this video https://www.youtube.com/watch?v=VolIkTkYqMw
        #I watched the video to understand more about colouring in matplot, and then just with the explanations on hand put in a colourmap I liked the most.

        plt.scatter(x_values, y_values, cmap = "tab20")


        #number_name is plused by 1

        number_name += 1


    #A title is given to the plot and it is displayed
    
    plt.title(data)
    plt.show()


#====
# Write the initialisation procedure 

number_cluster = int(input("How many clusters would you like?"))
iterations = int(input("How many iterations must there be?"))
data_array = ["dataBoth.csv", "data2008.csv", "data1953.csv"]


         
#====
# Implement the k-means algorithm, using appropriate looping for the number of iterations
# --- find the closest centroid to each point and assign the point to that centroid's cluster
# --- calculate the new mean of all points in that cluster
# --- visualise (optional, but useful to see the changes)
#---- repeat


''' A function is defined here where new centroids is found which is the mean of all the points of each centroid'''

def mean(centroids_assign_1):
    new_centroids = []


    #The dictionary is looped through which is the dictionary returned from the find_centroid function 

    for x in centroids_assign_1:


        #attributes

        sum_x = 0
        sum_y = 0
        amount = 0
        array = []
        array_add = []


        #The item from centroids_assign_1 which is being iterated is then split it into an array which is is a centroids with all its points

        array = str(centroids_assign_1[x]).split("[")


        #Each item in array is then iterated through

        for y in array:
            array_add = str(y).split(",")
            if(len(array_add) != 1):


                #Each x and y value is then add to variables 

                x_add = array_add[1]
                x_add = x_add.replace("'", "")
                y_add = array_add[2]
                y_add = y_add.replace("'", "")
                y_add = y_add.replace("]", "")


                #The sum of all the x values and y values is calculated by adding them upon each other by each iteration
                #the amount is also calculated by just +1 each iteration, all these are set to 0 each time the first loop runs again.

                sum_x += float(x_add)
                sum_y += float(y_add)
                amount += 1

        
        #The new centroids are then calculated by getting the mean for the x and y value and then it is appended to an array, it is then returned

        new_centroids.append([sum_x / amount, sum_y / amount])

    return new_centroids


#A while loop is created which runs for the length of data_array being all the csv files

counter = 0
while counter < len(data_array):

    #The needed csv file is opened, noticed how the name is in data_array allowed the loop to go through each csv file

    array = open_csv(data_array[counter])


    #A random sample is taken from the data

    centers = rdm.sample(array, number_cluster)


    #The needeed function are called to implement the k-means algorthm then repeated for the needed iteration - 1


    centroids_assign_1 = find_centroid(centers, array)
    centers_3 =  mean(centroids_assign_1)

    number = 0
    while number <= iterations - 1:
        centroids_assign_1 = find_centroid(centers_3, array)
        centers_3 =  mean(centroids_assign_1)
        number += 1

        

# ====
# Print out the results for questions
#1.) The number of countries belonging to each cluster
#2.) The list of countries belonging to each cluster
#3.) The mean Life Expectancy and Birth Rate for each cluster

    #A title is given to each data set being displayed

    print("\n---------",data_array[counter],"---------\n")


#The number of countries in each cluster is calculated

    for x in centroids_assign_1:
        amount = 0
        array_5 = []
        array_add = []
        array_5 = str(centroids_assign_1[x]).split("[")
        for y in array_5:
            array_add = str(y).split(",")
            if(len(array_add) != 1):
                amount += 1

        print("number of countries in cluster", x, " - ", amount)


#The countries in each cluster is calculated

    for x in centroids_assign_1:
        amount = 0
        array_5 = []
        array_add = []
        array_5 = str(centroids_assign_1[x]).replace("]", "").split("[")
        print("\ncountires in cluster", x, "\n")
        for y in array_5:
            array_add = str(y).split(",")
            if(len(array_add) != 1):
                print(y)


#The mean life expentancy and birth rate is calculated and displayed

    newCentroids = []
    for x in centroids_assign_1:
        split_1 = str(x).split(",")
        sum_x = 0
        sum_y = 0
        amount = 0
        y_number = ""
        x_number = ""
        array = []
        array_add = []
        array = str(centroids_assign_1[x]).split("[")
        for y in array:
            array_add = str(y).split(",")
            if(len(array_add) != 1):
                x_add = array_add[1]
                x_add = x_add.replace("'", "")
                y_add = array_add[2]
                y_add = y_add.replace("'", "")
                y_add = y_add.replace("]", "")
                sum_x += float(x_add)
                sum_y += float(y_add)
                amount += 1

        print("\nmean birth rate for cluster ", x, " - ", sum_x/amount)
        print("mean life expentancy for cluster ", x, " - ", sum_y/amount)
    

    #The dataset name being iterated is set in data_name

    data_name = data_array[counter]


    #The function plot is called with paramaters centroid_assign_1 and data_name

    plot(centroids_assign_1, data_name)

    
    #Counter is plused 1

    counter += 1