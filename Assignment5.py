class number:
  def pow(self,x,n):
    return x**n
x=int(input("Enter the number: "))
n=int(input("Enter the power value: "))
obj=number()
data=obj.pow(x,n)
print(data)