#break döngünün sonuna gelmeden istediğimiz şart geldiğinde döndüyü durdurmak için kullanılır.

# i=1
# while i<6:
#     print(i)
#     if i==3:
#         break
#     i+=1
#
#continue

# i=0
# while i<4:
#     i+=1
#     if i==3:
#         continue # if şartı sağlanırsa continue dan döngü başa sarar ve alttaki printe gelmez.
#         #o yüzden çıktı vermeden döngü başa alınmış olur.
#     print(i)


liste=["salata", "çorba", "sütlaç", "pilav", "kabak", "pırasa"]
i=0
while i<len(liste):
    print(liste[i])
    if liste[i]=="sütlaç":
        break
    i+=1

    
