#project3
"""author - Avipreet singh"""
""" last modified - 27/11/2022"""

#Function1

def convert_to_shingles(k, file):
    """This function take two input first the file and other length od shingles from which it creates a list of shingles."""
    shingles_list= []   #list which will contain all shingles.
    all_words = file.readlines()   # It creates the list of all sentences including the \n.
    remove = all_words.remove('\n')# It removes the \n for paragraph from list all_words.
    
    for i in range(len(all_words)):
        a_line = all_words[i]   # This represents first string of the list all_words means the first sentence.
        remove_n = a_line[0:-2]# This represents the first string without the \n in the end.
        
        pos1 = 0   # position one
        pos2 = k   # position two
        
        while pos1 < (len(remove_n) - 2):
            if remove_n[pos1:pos2] not in shingles_list:
                shingles_list.append(remove_n[pos1:pos2])  # appending the each shingle from the sentence remove_n.
            pos1 = pos1 + 1   # addition to the position one
            pos2 = pos2 + 1   # addition to the position two
    return shingles_list   # In the end, return the list of all shingles.

#Function2
def numerator(setA, setB):
    """This function take two lists as input and returns the intersection of these two lists."""
    count = 0
    for a in setA:
        if a in (setA and setB):   # If a is in both setA and SetB then it counts one.
            count = count +1   #count represents the shringes that appear in both the sets.
    return count   # In the end, returns the total.


#Function3
def denominator(setA,setB):
    """This funtion take two lists as input and returns the union of these two lists."""
    sub = 0
    count = len(setA) + len(setB)   # count is equal to the length of the both setA and setB.
    for a in setA:
        if a in (setA and setB):   # If a is in both setA and setB then one is added to the sub.
            sub = sub +1   # sub represents the shringes that appears in both the sets.
    return count - sub   # In the end, shringes that appear in both sets(sub) are removed from the total.


def main():
    """Three inputs are taken from user"""
    file1 = str(input("which is the first file?"))  #asked for the first file name.
    file2 = str(input("which is the second file?")) #asked for the second file name.
    k = int(input("what is the value of the k?"))   #asked for the value of the k.
    
    first_file = open(file1 + ".txt", 'r')   # file1 is opened here for reading.
    second_file = open(file2 + ".txt", 'r')   # file2 is opened here for reading.
    
    """Function1 is called twice with two different files"""
    a_list = convert_to_shingles(k,first_file)   # a_list  is created by the function1 from file1.
    b_list = convert_to_shingles(k,second_file)   # b_list is created by the function1 from file2.
    
    """Function2 and Function3 is called with parameters from function1."""
    upper = numerator(a_list,b_list)   # numerator of the formula is created by the function2.
    lower = denominator(a_list,b_list)   # denominator of the formula is created by the function3.
    
    """In the last, Jacquards similarity is calculated by dividing the result of the Fuction2 and Function3"""
    Jacquards_similarity = round(upper/lower, 2)  # formula is applied here along rounding the value to the two deciaml places.
    print(Jacquards_similarity)
          
if __name__ == "__main__":
    main()