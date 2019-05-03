sample_output="sample_output.txt"
def pred():
  f=open(sample_output,"r")
  l1=f.readline()
  while(l1):
    l=[]
    l1=l1.rstrip('\n')
    l.extend(l1.split(" "))
    l1=f.readline()
  return l
