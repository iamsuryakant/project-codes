import cv2
import numpy as np

import restore as res
import tester as tes

print("\nTest Secret Sharing (k out of n) on an Image\n")

# prompt user for input to test functionality, loop until a valid id
id = input("\n\npress 1 for continue or press q to quit:")
while id != '1' and id != 'q':
    id = input("\n\nPlease press 1 for continue or press q to quit:")

# quit and close the application
if (id == 'q'):
    print("Thank you.")



# if 1 is selected
else:
    id = int(id)
    print("\n\nYou have selected %d" % id)

    # image test functionality
    if id == 1:
        print("\nRunning Secret Sharing on Image Tests")
        # begin image tests
        # get a valid filename
        filename = input("Please enter a filename: ")
        filename = "../DATA/pictures/" + filename
        print(filename)
        img = cv2.imread(filename)

        while isinstance(img, np.ndarray) == False:
            print("Error.  Not a valid filename.")
            filename = input("Please enter a valid filename: ")
            filename = "../DATA/pictures/" + filename
            img = cv2.imread(filename)

        # get value for k
        k = input("Please enter an int value for parameter k: ")
        while isinstance(k, int) == False:
            try:
                k = int(k)

            except ValueError:
                k = input("Please enter a valid value for parameter k: ")
                continue
            if k < 1:
                k = input("Please enter a value greater than or equal to 1: ")

        # get value for n
        n = input("Please enter an int value for parameter n: ")
        while isinstance(n, int) == False:
            try:
                n = int(n)
            except ValueError:
                n = input("Please enter a valid value for parameter n: ")
                continue
            if k > n:
                n = input("Please enter a value greater than or equal to t: ")

        # run secret sharing on image
        tes.image_test(filename, k, n)

        # begin image restoration
        print("Restoring an image.")
        pictures = []
        key = []
        id = input("Enter the filename of a share, 'r' to restore or 'q' to quit:")

        # enter the names of the files you wish to use to restore
        # press r when you have a valid number of images to restore
        # press q if you want to quit
        # loop until r is pressed
        while id != 'r':
            # quit if user inputs q
            if id == 'q':
                break
            else:
                # enter the name of the file and the corresponding key value
                print(id)
                id = "..\DATA\pictures\\" + id
                image = cv2.imread(id)
                if isinstance(image, np.ndarray):
                    pictures.append(id)
                    keyvalue = input("Enter key value of image: ")
                    try:
                        keyvalue = int(keyvalue)
                    except ValueError:
                        continue
                    while isinstance(keyvalue, int) == False:
                        keyvalue = input("Please enter a correct value:")
                        try:
                            keyvalue = int(keyvalue)
                        except ValueError:
                            continue
                    key.append(keyvalue)
                    id = input("Enter a filename, 'r' to restore or 'q' to quit: ")
                # if file is not an image instance, inform the user
                else:

                    while isinstance(image, np.ndarray) == False:
                        id = input("Please enter a correct filename or 'q' to quit: ")
                        if id == 'q':
                            break
                        image = cv2.imread(id)
        # begin restoration, throw exception if image can't be restored
        try:
            restore = res.restoreImg(pictures, key)
            restore = np.asarray(restore)
            cv2.imshow("restored", restore)
            cv2.waitKey(0)
            cv2.destroyAllWindows()
        except:
            print("Restoring failed")
