from astropy.io import fits


def print_data(data):        # Have to add frame select ability later. Will need to see how to give default parameters
    """
    Prints the whole data in all/selected frame in the console
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
                    maximum_location = [j, k]
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
    :param data: The data cube to be processed
    :return: An array holding UTCS Observation times of each frame
    """
    time_obs = []
    for i in range(head['NAXIS3']):
        time_obs.append(head['UTCS_OBS'] + i * head['FRAMTIME'])
    return time_obs

fin = fits.open('/home/tachyon/Lab/PreCode/datafiles/SPITZER_I2_46466816_0000_0000_2_bcd.fits')
data_handler = fin[0].data
print_data(data_handler)
print "\n\n"
print "Bright Pixel Address:", get_bright_pixel_location(data_handler)
print "Bright Pixel Intensities:", get_bright_pixel_intensity(data_handler)
print "Bright Pixel Times:", get_bright_pixel_time(fin[0].header)

