def read_file(file_name):
    """ Reads in a file.

    [IMPLEMENT ME]
        1. Open and read the given file into a variable using the File read()
           function
        2. Print the contents of the file
        3. Return the contents of the file

    Args:
        file_name: the name of the file to be read

    Returns:
        string: contents of the given file.
    """
    ### WRITE SOLUTION HERE

    try:
        with open(file_name) as my_file01:
            f_content = my_file01.read()
        print(f_content)
        return f_content
    except FileNotFoundError as e:
        print("We can not find this file!!!", e)
    except Exception as e:
        print("ERROR!!!", e)  

    #raise NotImplementedError()

def read_file_into_list(file_name):
    """ Reads in a file and stores each line as an element in a list

    [IMPLEMENT ME]
        1. Open the given file
        2. Read the file line by line and append each line to a list
        3. Return the list

    Args:
        file_name: the name of the file to be read

    Returns:
        list: a list where each element is a line in the file.
    """
    ### WRITE SOLUTION HERE
    try:
        with open(file_name) as my_file01:
            f_content_list = my_file01.readlines()
        #print(f_content)
        #return [line.rstrip('\n') for line in f_content_list]
        return f_content_list
    except FileNotFoundError as e:
        print("We can not find this file!!!", e)
    except Exception as e:
        print("ERROR!!!", e) 
    #raise NotImplementedError()

def write_first_line_to_file(file_contents, output_filename):
    """ Writes the first line of a string to a file.

    [IMPLEMENT ME]
        1. Get the first line of file_contents
        2. Use the File write() function to write the first line into a file
           with the name from output_filename

        We determine the first line to be everything in a string before the
        first newline ('\n') character.

    Args:
        file_contents: string to be split and written into output file
        output_filename: the name of the file to be written to
    """
    ### WRITE SOLUTION HERE
    #str.split("\n", 1)
    try:
        with open(output_filename, "w") as my_file02:
            my_file02.write(file_contents.split("\n", 1)[0])

    except FileNotFoundError as e:
        print("We can not find this file!!!", e)
    except Exception as e:
        print("ERROR!!!", e) 

    #raise NotImplementedError()

    
def read_even_numbered_lines(file_name):
    """ Reads in the even numbered lines of a file

    [IMPLEMENT ME]
        1. Open and read the given file into a variable
        2. Read the file line-by-line and add the even-numbered lines to a list
        3. Return the list

    Args:
        file_name: the name of the file to be read

    Returns:
        list: a list of the even-numbered lines of the file
    """
    ### WRITE SOLUTION HERE
    try:
        with open(file_name) as my_file01:
            f_content_list = my_file01.readlines()
        #return [line.rstrip('\n') for line in f_content_list][0::2]
        return f_content_list[1::2]
    except FileNotFoundError as e:
        print("We can not find this file!!!", e)
    except Exception as e:
        print("ERROR!!!", e) 

    #raise NotImplementedError()


def read_file_in_reverse(file_name):
    """ Reads a file and returns a list of the lines in reverse order

    [IMPLEMENT ME]
        1. Open and read the given file into a variable
        2. Read the file line-by-line and store the lines in a list in reverse order
        3. Print the list
        4. Return the list

    Args:
        file_name: the name of the file to be read

    Returns:
        list: list of the lines of the file in reverse order.
    """
    ### WRITE SOLUTION HERE
    try:
        with open(file_name) as my_file01:
            f_content_list = my_file01.readlines()
        #my_list_reverse = [line.rstrip('\n') for line in f_content_list][::-1]
        my_list_reverse = f_content_list[::-1]
        print(my_list_reverse)
        return my_list_reverse
    except FileNotFoundError as e:
        print("We can not find this file!!!", e)
    except Exception as e:
        print("ERROR!!!", e)

    #raise NotImplementedError()


def main():
    file_contents = read_file("sampletext.txt")
    print(read_file_into_list("sampletext.txt"))
    write_first_line_to_file(file_contents, "online.txt")
    print(read_even_numbered_lines("sampletext.txt"))
    print(read_file_in_reverse("sampletext.txt"))

if __name__ == "__main__":
    main()