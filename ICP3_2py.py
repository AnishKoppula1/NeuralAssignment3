import numpy as np

starting_range = 1    #variable indicating starting range of vector elements
ending_range = 20     #variable indicating ending range of vector elements
no_of_elements = 20   #variable indicating no of elements the vector should hold

# Creating a random vector of size 20 with floats in the range 1-20
random_vector = np.random.uniform(starting_range, ending_range, no_of_elements)

#printing the random vector
print("random vector : \n" + str(random_vector) + "\n\n")

# Reshape the array to 4 by 5
new_vector = random_vector.reshape(4, 5)

#printing the reshaped vector
print("reshaped vector : \n" + str(new_vector) + "\n\n")

# getting indexes in each row where the element is maximum (axis=1)
max_index = np.argmax(new_vector, axis=1)

#creating new vector with no of rows like [0 1 2 3] so that we can use pairing for replacing elements
rows_vector = np.arange(new_vector.shape[0])

#replacing vector element of each row's maxindex with zero by creating pair of indexes 
new_vector[rows_vector, max_index] = 0

#printing the reshaped vector after replacing max with 0
print("replaced vector : \n" + str(new_vector))