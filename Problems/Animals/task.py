# read animals.txt
# and write animals_new.txt

file_read = open('animals.txt', 'r')
animals = [line.strip('\n') + ' ' for line in file_read]
file_read.close()

file_write = open('animals_new.txt', 'w')
file_write.writelines(animals)
file_write.close()
