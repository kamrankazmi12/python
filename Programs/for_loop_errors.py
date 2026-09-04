##corrected program with errors

##for i in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10) here the wrong brackets have been used it should be [] these at start and end 
#and range function can be used for printing one to 10
#wrong variable is used as well as in loop it is 'i' not x
#sum = Sum + x  python is case senstive so it  has be sum on both places #sum needs to be initialized as well
#print 'sum: ', sum #here the syntax is incorrect

#corrected program

sum = 0

for i in range(1, 11):
    sum = sum + i

print("sum:", sum)
