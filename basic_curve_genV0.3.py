from astropy.io import fits
from os import listdir
from os.path import isfile, join


def print_data(data):        # Have to add frame select ability later. Will need to see how to give default parameters
    """
    Prints the whole data in all/selected frame(s) in the console
    :param data: The data cube in question
    :return: NULL doesn't return anything, just prints in console
    """
    for i in range(data.shape[0]):
        print "\n\t\tNext Frame Begins"
        for j in range(data.shape[1]):
            for k in range(data.shape[2]):
                print data[i][j][k],
            print


def get_bright_pixel_intensity(data):
    """
    :param data: The data cube to be processed
    :return: An array of ints holding value of max intensity
    """
    bright_pixel_intensity = []
    for i in range(data.shape[0]):
        maximum = data[i][1][1]
        for j in range(data.shape[1]):
            for k in range(data.shape[2]):
                if data[i][j][k] > maximum:
                    maximum = data[i][j][k]
        bright_pixel_intensity.append(maximum)
    return bright_pixel_intensity


def get_bright_pixel_location(data):
    """
    :param data: The data cube to be processed
    :return: An Array of Arrays
    """
    bright_pixel_location = []
    for i in range(data.shape[0]):
        maximum = data[i][1][1]
        maximum_location = []
        for j in range(data.shape[1]):
            for k in range(data.shape[2]):
                if data[i][j][k] > maximum:
                    maximum = data[i][j][k]
                    maximum_location = [j, k]
        bright_pixel_location.append(maximum_location)
    return bright_pixel_location


def get_bright_pixel_time(head):
    """
    Gives time of observation for each frame
    :param head: Heaader part of data cube to be processed
    :return: An array holding UTCS Observation times of each frame
    """
    time_obs = []
    for i in range(head['NAXIS3']):
        time_obs.append(head['UTCS_OBS'] + i * head['FRAMTIME'])  # Assuming Delay between frames is totally dependent on FRAMTIME. Will need to check with mentor
    return time_obs

path = "/home/tachyon/Lab/PreCode/datafiles/"                    # Will get all the files within the given directory
only_files = [f for f in listdir(path) if isfile(join(path, f))]

fin = []
for i in range(len(only_files)):
    fin.append(fits.open(path+only_files[i]))

data_handler = []
for i in range(len(only_files)):
    #data_handler.append(fin[i][0].data)
    print "Cube Name:", only_files[i], "Cube No.: ", i
    print "Peak intensities: ", get_bright_pixel_intensity(fin[i][0].data)
    print "Peak locations: ", get_bright_pixel_location(fin[i][0].data)
    print "Peak time:", get_bright_pixel_time(fin[i][0].header)
    print "\n\n"

