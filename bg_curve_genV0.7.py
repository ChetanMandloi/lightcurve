"""
 * Basic Light Curve generator V0.7
 * - Chetan Mandloi
 *
 * Takes spitzer fits files and generates a raw light curve for the given data frames
 * Accounts for the background flux
 *
 * TODO:
 *  -Verify the correctness of get_flux function
 *  -Make a class to handle values, at this preliminary stage, this seemed unnecessary. This can be easily done quickly
 *    later if required
 *
"""

import matplotlib.pyplot as plt         # For plots
from astropy.io import fits             # To handle FITS files
from os import listdir                  # To detect files in a directory
from os.path import isfile, join
import frame_functions as frm           # Has all the processing functions
from matplotlib.backends.backend_pdf import PdfPages # From exporting plots to pdf

path = raw_input(
    'Enter the directory required to be processed. ensure \'/\' at end. Will detect only .fits files\n -->')
# Will get all the files of given extension within the given directory
choice = 1
while True:
    only_files = [f for f in listdir(path) if isfile(join(path, f)) if ".fits" in f] # Will get all the files of given extension within the given directory
    print "\n\nDirectory selected is: ", path
    print "What would you like to do?\n"
    print "\tChange Directory (1)"
    print "\tProcess all the files in present directory (2)"
    print "\tList all the FITS file in present directory (3)"
    print "\tPrint info of a selected FITS file(4)"
    print "\tExit (5)"
    choice = int(raw_input('\nEnter choice:'))
    if choice == 1:
        path = raw_input(
            'Enter the directory needed to be processed. Ensure \'/\' at end. Will detect only .fits files\n -->')
    elif choice == 2:
        data_handler = []
        for i in range(len(only_files)):
            fin = fits.open(path + only_files[i])
            print "Cube Name:", only_files[i], "Cube No.: ", i+1, "/", len(only_files)+1, " - ", (float((i+1))/float(len(only_files)))*100, "%"
            plt.plot(frm.get_bright_pixel_time(fin[0].header),
                     frm.get_flux(fin[0].header, fin[0].data, 1), 'ro')
            fin.close()
        plt.ylabel('FLUX (photons/sec/pixel)')
        plt.xlabel('UTCS_OBS Time (s)')
        plt.title('Plot of Flux Vs Time')
        printer = PdfPages(path+'graph.pdf')
        plt.show()
        printer.close()
    elif choice == 3:
        for i in range(len(only_files)):
            print "File", i, ": ", only_files[i]
    elif choice == 4:
        for i in range(len(only_files)):
            print "File", i, ": ", only_files[i]
        file_num = int(raw_input("Enter file no. as shown above"))
        fin = fits.open(path + only_files[file_num])
        while True:
            print "What do you want to see?"
            print "General info of FITS file(1)"
            print "Header of FITS file(2)"
            print "All the frame-wise Raw Data(3)"
            print "Exit(4)"
            sele = int(raw_input('\nEnter your choice:'))
            if sele == 1:
                print fin.info()
            elif sele == 2:
                for i in range(len(fin[0].header.keys())):
                    print fin[0].header.keys()[i], ":", fin[0].header[i]
            elif sele == 3:
                data_handler = fin[0].data
                frm.print_data(data_handler)
            elif sele == 4:
                print "Exiting..."
                break
            else:
                "Invalid Input. Try again."
    elif choice == 5:
        print "Exiting..."
        break
    else:
        print "Invalid Input. Try again"

