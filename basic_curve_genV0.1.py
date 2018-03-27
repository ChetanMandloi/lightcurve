from astropy.io import fits
print "\n   Testing weather this interpreter works or not"
hdulist = fits.open('/home/tachyon/Lab/PreCode/datafiles/SPITZER_I2_46466816_0000_0000_2_bcd.fits')
print hdulist.info()
hhandle = hdulist[0].header
#print "\n Header Info: :"
#for i in range(len(hhandle.keys())):
#   print hhandle.keys()[i], ":" , hdulist[0].header[i]
print "\n\n\t\tNOW FOR DATA PARSING !"
dhandle = hdulist[0].data
dimension = dhandle.shape   # [num of frames, X pixels, Y Pixels]
print "Dimensions of data are like :",dimension
bright_pixel_intensity = []
bright_pixel_location = []
for i in range(dimension[0]):
    max = dhandle[i][1][1]
    maxloc = []
    print "\n\n\t\tFRAMECHANGE\n"
    for j in range(dimension[1]):
        for k in range(dimension[2]):
            print dhandle[i][j][k],
            if dhandle[i][j][k] > max:
                max = dhandle[i][j][k]
                maxloc = [j,k]
        print
    bright_pixel_intensity.append(max)
    bright_pixel_location.append(maxloc)

print "\n Number of bright pixels obtained:", len(bright_pixel_intensity), "Intensity:", bright_pixel_intensity
print "Bright Pixel Address:", bright_pixel_location

