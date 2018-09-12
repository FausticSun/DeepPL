def read_pdb(filename):
    
    with open(filename, 'r') as file:
        strline_L = file.readlines()
        # print(strline_L)
    strline_L=[strline.strip() for strline in strline_L]

    X_list=[float(strline.split()[-6]) for strline in strline_L]
    Y_list=[float(strline.split()[-5]) for strline in strline_L]
    Z_list=[float(strline.split()[-4]) for strline in strline_L]
    atomtype_list=[strline.split()[-1] for strline in strline_L]
    

    return X_list, Y_list, Z_list, atomtype_list


X_list, Y_list, Z_list, atomtype_list=read_pdb("training_first_100_samples/0001_pro_cg.pdb")
# X_list, Y_list, Z_list, atomtype_list=read_pdb("training_first_100_samples/0001_lig_cg.pdb")
print(X_list)
print(Y_list)
print(Z_list)
print(atomtype_list)
