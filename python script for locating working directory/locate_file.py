def locate_file() :
    working_directory = __file__.split('/')[:-1]
    return_string = ''
    for string in working_directory :
        return_string += string
        return_string += '/'

    return return_string

locate_file()
