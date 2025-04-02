import random

class BankAccount:
    def __init__(self, account_holder, password, balance=0):
        self.account_holder = account_holder
        self.password = password
        self.balance = balance
        self.account_number = random.randint(100000, 999999)  # Unik hesab nömrəsi
        print(f"Yeni hesabınız yaradıldı. Hesab nömrəniz: {self.account_number}")

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"{amount} manat hesabınıza əlavə olundu. Cari balans: {self.balance} manat.")
        else:
            print("Yatırılacaq məbləğ müsbət olmalıdır!")

    def withdraw(self, amount):
        if amount > 0:
            if amount <= self.balance:
                self.balance -= amount
                print(f"{amount} manat hesabınızdan çəkildi. Cari balans: {self.balance} manat.")
            else:
                print("Hesabınızda yetərli balans yoxdur!")
        else:
            print("Çıxarılacaq məbləğ müsbət olmalıdır!")

    def check_balance(self):
        print(f"{self.account_holder} üçün cari balans: {self.balance} manat.")

    def update_password(self, old_password, new_password):
        if old_password == self.password:
            self.password = new_password
            print("Şifrə uğurla dəyişdirildi.")
        else:
            print("Yanlış şifrə!")

    def get_account_info(self):
        return f"Ad: {self.account_holder}, Hesab Nömrəsi: {self.account_number}, Balans: {self.balance} manat"

class BankSystem:
    def __init__(self):
        self.accounts = {}

    def create_account(self):
        print("Yeni hesab açmaq üçün məlumatları daxil edin.")
        account_holder = input("Adınızı daxil edin: ")
        password = input("Şifrəni daxil edin: ")
        account = BankAccount(account_holder, password)
        self.accounts[account.account_number] = account
        print(f"{account_holder} adlı istifadəçi üçün yeni hesab yaradıldı.")

    def login(self, account_number, password):
        if account_number in self.accounts:
            account = self.accounts[account_number]
            if account.password == password:
                return account
            else:
                print("Yanlış şifrə!")
        else:
            print("Belə bir hesab mövcud deyil!")
        return None

    def get_account_by_number(self, account_number):
        if account_number in self.accounts:
            return self.accounts[account_number]
        else:
            print("Belə bir hesab mövcud deyil!")
        return None

def main():
    bank = BankSystem()

    while True:
        print("\nƏməliyyatlar:")
        print("1. Yeni hesab aç")
        print("2. Hesaba daxil ol")
        print("3. Çıxış")

        choice = input("Seçiminizi edin (1-3): ")

        if choice == "1":
            bank.create_account()
        elif choice == "2":
            account_number = int(input("Hesab nömrənizi daxil edin: "))
            password = input("Şifrəni daxil edin: ")
            account = bank.login(account_number, password)

            if account:
                while True:
                    print("\nƏməliyyatlar:")
                    print("1. Balansı yoxla")
                    print("2. Pul yatır")
                    print("3. Pul çıxar")
                    print("4. Şifrəni dəyiş")
                    print("5. Hesab məlumatlarını göstər")
                    print("6. Çıxış")

                    action = input("Seçiminizi edin (1-6): ")

                    if action == "1":
                        account.check_balance()
                    elif action == "2":
                        amount = float(input("Yatırılacaq məbləği daxil edin: "))
                        account.deposit(amount)
                    elif action == "3":
                        amount = float(input("Çıxarılacaq məbləği daxil edin: "))
                        account.withdraw(amount)
                    elif action == "4":
                        old_password = input("Mövcud şifrəni daxil edin: ")
                        new_password = input("Yeni şifrəni daxil edin: ")
                        account.update_password(old_password, new_password)
                    elif action == "5":
                        print(account.get_account_info())
                    elif action == "6":
                        print("Sistemdən çıxılır...")
                        break
                    else:
                        print("Yanlış seçim, yenidən cəhd edin.")
        elif choice == "3":
            print("Sistemdən çıxılır...")
            break
        else:
            print("Yanlış seçim, yenidən cəhd edin.")

if __name__ == "__main__":
    main()
