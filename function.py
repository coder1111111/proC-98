def swapFileData():
   filename =  input("name of the important file:")
   file = open(filename, 'r')
   data_a = file.read()
   swappedfilename = input("name of the file you want to replace it with:")
   file2 = open(swappedfilename, 'r')
   data_b = file2.read()
   file = open(filename, 'w')
   file.write(data_b)
   file2 = open(swappedfilename, 'w')
   file2.write(data_a)

swapFileData()