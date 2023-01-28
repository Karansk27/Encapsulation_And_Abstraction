#Property
class Student():
    def __init__(self, Total):
        self._Total = Total
    @property
    def Average(self):
     return self._Total / 5.0
    @Average.setter
    def Average(self, n):
        if n > 0:
            print("Invaild ")
        else:
            self._Total = n


User = Student(int(input("Enter THe Mark : ")))
print("Average : ", User.Average)
User=Student(200)
print("Average : ",User.Average)

# Other ways
class Student():
    def __init__(self, Total):
        self._Total = Total

    def getter(self):
     return self._Total / 5.0

    def setter(self, n):
        if n > 0:
            print("Invaild ")
        else:
            self._Total = n

    Total=property(getter,setter)

User = Student(int(input("Enter THe Mark : ")))
print("Average : ", User.Average)
User=Student(200)
print("Average : ",User.Average)

#Class Methoad
class Admission():
  count=0
  def __init__(self,Moblie,price):
    self.Moblie=Moblie
    self.price=price
    Admission.count+=1
  def Display(self):
    print("Moblie Name : ",self.Moblie,"Price Amount : ",self.price)
  @classmethod
  def Total(cls):
    return cls.count
A=Admission("Poco X3","Rs : 17,000")
A.Display()
B=Admission("Redmi Note 7 Pro ","15,000")
B.Display()
C=Admission("Redmi Note 10 S","14500")
C.Display()
D=Admission("iPhone 13 Pro Max ","80000")
D.Display()
print("Total Number of Moblie Buying : ",A.Total)


#Property Decorator
class User():
    def __init__(self,User_Name,Age):
        self.User_Name=User_Name
        self.Age=Age
    @property
    def Msg(self):
        return self.User_Name+ "is "+self.Age
U=User("Karan_Sk27","19 Years Old ")
print(U.User_Name)
print(U.Age)
U.User_Name="Karan_Sk@2003"
print(U.Msg)


#instance
class User:
    def __init__(self,User_Name,Password,login):
        self.User_Name=User_Name
        self.Password=Password
        self.login=login

    def Regiester(self):
        print("Regiestering..."+self.User_Name)
    def Login(self):
        print("Login..from"+self.User_Name)
try:
    user_1=User("Kavirajan","Karan_Sk","yes")
    user_1.Regiester()
    user_1.Login()
    Us=User("Thambi","Ram","None")
except Exception as A:
    print("Some Type Error ")
else:
    Us.Regiester()
    Us.Login()
print(user_1.User_Name)
print(user_1.Password)

#Pratice Program_1
#abstration And Encapsulation
class Library():
  def __init__(self,books):
    self.books=books
  def list_Books(self):
    for books in self.books:
      print(books)
  def barrow_books(self,barrow_books):
    if barrow_books in self.books:
      print("Get The Book and Submit the Library Card")
      self.books.remove(barrow_books)
    else:
      print(barrow_books," is Not Avaliable...")
  def Return_book(self,Return_books):
    self.books.append(Return_books)
books=["Python","Core Java","C++","PHP"]
A=Library(books)
Msg="""
      1.Show The Book
      2.Barrow the Book
      3.Return the Book
      """
print(Msg)
while True:
  ch=int(input("Enter Your Choice : "))
  if 1 == ch:
    A.list_Books()
  elif ch==2:
            books=input("Enter The Barrow book : ")
            A.barrow_books(books)
  elif ch==3:
           books=input("Enter The receive Book : ")
           A.Return_book(books)
  else:
    print("ThankYou Welcome")
    quit()
