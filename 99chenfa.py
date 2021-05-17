for i in range(1,10):
    for j in range(1,i+1):
        print("{}*{}={:1}".format(j,i,i*j),end='\t')
    print('')