#iç içe sözlük kullanımı
# kisiler={
#     0:"mustafa",
#     1:"erkan",
#     2:"osman"
# }
# print(kisiler[0])

# kisiler={
#     "mustafa":{
#         "yas":36,
#         "öğrenim":"lisans"
#     },
#     "erkan":{
#     "yas":40,
#     "öğrenim":"lisans"
#     },
#     "osman":{
#         "yas":30,
#         "öğrenim":"lise",
#         "cocuklar":{
#             0:"ali",
#             1:"ömer"
#         }
#     }
# }
# print("mustafanın bilgileri=", kisiler["mustafa"])
# print("mustafanın bilgileri=", kisiler["mustafa"]["yas"])
# print("mustafanın bilgileri=", kisiler["mustafa"] ["öğrenim"])
# print("osmanın bilgileri=", kisiler["osman"] ["cocuklar"][0])

kisiler={
    1:["mustafa",36, "lisans"],
    2:["erkan",40,"lisans"]
}
print(kisiler[1][0])