sample_output="sample_output.txt"
def pred():
  f=open(sample_output,"r")
  l1=f.readline()
  l=[]
  while(l1):
    l1=l1.rstrip('\n')
    l.extend(l1.split(" "))
    l1=f.readline()
  return l
