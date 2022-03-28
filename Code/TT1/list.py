questions = {
    "What is the most universal command to access root privilages?": ["sudo","test"],
    "Computer?" : ["laptop, but yes","test"],
    "Linux is a(n)..." : ["kernel","test"],
    "Who is RMS?" : ["Someone who belongs in GNU","test"],
    "Which of the following characters can combine several commands?" : ["pipe - |","test2"],
    "Can Linux can run on every computer?" : ["True without exceptions.","test2"],
    "A derivative of Ubuntu made to be more user-friendly is called..." : ["Linux Mint","test2","kernel","test"]
}

for i in questions:
  a = i.key()
  print(a[1]) 

i = 0 

while i < 5:
  print("hello")
  i+=1
