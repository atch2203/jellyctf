lookup = "AWawJELYHOSIUMjelyhosiumPCNTpcntBDFGRbdfgr0123456789 .,!'()~_/;\n"
out = " awa awa awa awawawawa awa awa awa awa awawawawawa awa awa awawa awa awa awa awa awa awa awawa awa awa awa awa awa awa awawa awa awa awawa awa awa awawawa awa awawa awa awa awawawa awawawa awa awawa awa awa awawa awa awa awawawawa awa awawa awa awa awawawa awa awawa awa awawa awawa awawa awa awa awa awawawawa awa awa awa awawa awawa awawawa awa awawa awawawa awawa awa awawa awa awa awa awawa awa awawawawawa awa awa awa awa awawawawawawa awa awa awa awa awa awawawa awa awawa awawa awawa awa awa awawawawawa awa awa awa awawa awa awawa awawa awa awawa awawa awawawa awa awa awawawa awawawa awa awawawawawa awa awa awa awa awawawawawawa awa awawa awawa awawa awa awa awawa awawa awawa awa awa awawawawawa awa awa awa awa awa awawawa awawa awa awa awawa awawawa awa awa awa awawawa awa awawa awa awa awawa awa awawa awa awa awawawawa awawa awa"
binary_awascii = out.replace(" awa", "0").replace("wa", "1")
length = int(len(binary_awascii)/8);
print(length)
flag = ""
for i in range(length):
    c = binary_awascii[8*i:8*i+8]
    ind = int(c, 2)
    flag += lookup[ind]
print(flag)
