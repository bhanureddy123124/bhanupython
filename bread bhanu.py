a=int(input("enter the n.of loves purchased"));
b=int(input("enter the day old loves purhased"));
if(a<0):
    print("enter a postove integter grater then 0");
else:
    f=a*185
    o=(b*185)*60/100
print("regular price,185.00");
print("amount of new loves",float(f));
print("amoun of day old loves",float(o));
print("Total Amount to be paid",f+o);
