# Doğru istifadəçi adı və şifrə
correct_username= "admin"
correct_password= "12345"

# İstifadəçidən məlumatlaı daxil etməsini istəyirik
username=input("İstifadəçi adınızı daxil edin: ")
password=input("Şifrənizi daxil edin: ")

# Məlumatları yoxlayırıq
if username==correct_username and password==correct_password:
    print("İstifadəçi adı və şifrə doğrudur. Xoş gəlmisiz!")
else:
    print("Şifrə yanlışdır. Yenidən cəhd edin.")
