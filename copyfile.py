infile=input("Please enter source file: ");

outfile=input("Please enter destination file: ");

fileObject1 = open("sourceFile.txt","r");

fileObject2 = open("destinationFile.txt","w+")

content = fileObject1.read();

fileObject2.write(content);

fileObject1.close();
fileObject2.close();

