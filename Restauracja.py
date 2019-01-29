import pymysql

class Connect:

    def __init__(self):
        try:
            self.conn = pymysql.connect(host = "localhost", user="root", password="zaq12wsx", db="Restauracja", port=3307,
                                        charset='utf8')
            print("polaczenie ustanowione")
            self.wybor()
        except:
            print("bledne dane")

    def wybor(self):
        dec = input("1.Gość 2.Logowanie")
        if dec =="1":
            self.menu()
        elif dec=="2":
            self.logowanie()
        else:
            print("Błędna wartość")
            self.wybor()

    def logowanie(self):
        login = input("podaj login")
        passw = input("podaj haslo")

        self.cursor = self.conn.cursor()
        self.cursor.execute("Select * from logowanie WHERE login=%s and passwd=%s", (login,passw))
        resultsLogs = self.cursor.fetchall()

        if(len(resultsLogs) == 1):
            print("zalogowano w systemie")
            self.admenu()
        else:
            print("niepoprawny login lub haslo")
            self.logowanie()

    def menu(self):
        while(True):
            dec = input("P-Pizza, D-Dania, K-Kontakt, Q-Wyjdź").upper()

            if(dec=="P"):
                self.Pizza()
            elif(dec=="D"):
                self.Dania()
            elif(dec=="K"):
                self.Kontakt()
            elif(dec=="Q"):
                print("Koniec")
                break

    def Pizza(self):
        self.cursor = self.conn.cursor()
        self.cursor.execute("select * from pizza")
        pizza = self.cursor.fetchall()
        for row in pizza:
            nazwa          = 1
            skladniki      = 2
            Cena           = 3
            print(row[nazwa], row[skladniki], row[Cena])

    def Dania(self):
        self.cursor = self.conn.cursor()
        self.cursor.execute("select * from Dania")
        dania = self.cursor.fetchall()

        for row in dania:
            nazwa          = 1
            skladniki      = 2
            Cena           = 3
            print(row[nazwa], row[skladniki], row[Cena])

    def Kontakt(self):
        self.cursor = self.conn.cursor()
        self.cursor.execute("select * from Kontakt")
        kontakt = self.cursor.fetchall()

        for row in kontakt:
            cel = 0
            numer = 1
            print(row[cel], row[numer])

    def admenu(self):
        while(True):
            dec = input("A-Aktulizacja, U-Usuwanie, D-Dodawanie, Q-Wyjdź").upper()

            if(dec=="A"):
                self.AktualizujMenu()
            elif (dec=="U" ):
                self.UsunMenu()
            elif(dec=="D"):
                self.DodajMenu()
            elif(dec=="Q"):
                print("Koniec")
                break
    def APizza(self):
        self.cursor = self.conn.cursor()
        self.cursor.execute("select * from pizza")
        pizza = self.cursor.fetchall()
        for row in pizza:
            id             = 0
            nazwa          = 1
            skladniki      = 2
            Cena           = 3
            print(row[id] ,row[nazwa], row[skladniki], row[Cena])

    def AktualizujMenu(self):
        while(True):
            dec = input("P-Pizza, D-Dania, K-Kontakt W-Wróć").upper()

            if(dec=="P"):
                self.AktualizujPizza()
            elif(dec=="D"):
                self.AktualizujDania()
            elif(dec)=="K":
                self.AktualizujKontakt()
            elif(dec=="W"):
                self.admenu()

    def UsunMenu(self):
        while(True):
            dec = input("P-Pizza, D-Dania, K-Kontakt W-Wróć").upper()

            if(dec=="P"):
                self.UsunPizza()
            elif(dec=="D"):
                self.UsunDania()
            elif (dec == "K"):
                self.UsunKontakt()
            elif(dec=="W"):
                self.admenu()

    def DodajMenu(self)        :
        while(True):
            dec = input("P-Pizza, D-Dania, K-Kontakt W-Wróć").upper()

            if(dec=="P"):
                self.DodaPizza()
            elif(dec=="D"):
                self.DodajDania()
            elif(dec=="K"):
                self.DodajKontakt()
            elif(dec=="W"):
                self.admenu()

    def AktualizujPizza(self):
        self.APizza()
        decp = input("Co chcesz uaktulnić N - Nazwe, S-Składniki, C-Cene").upper()
        if(decp=="N"):
            DP = input("podaj id")
            NW = input("podaj nową nazwe")
            self.cursor.execute("UPDATE pizza SET nazwa = %s WHERE id = %s", (NW,DP))
            dec = input("Czy zatwierdzasz zmiany T/N").upper()
            if(dec=="T"):
                self.conn.commit()

                print("wartość zaktualizowano")
            else:
                self.conn.rollback()
                print("Come to menu")
        elif (decp == "S"):
            DP = input("podaj id")
            NW = input("podaj nowe składniki")
            self.cursor.execute("UPDATE pizza SET skladniki = %s WHERE id = %s", (NW, DP))
            dec = input("Czy zatwierdzasz zmiany T/N").upper()
            if (dec == "T"):
                self.conn.commit()
                print("wartość zaktualizowano")
            else:
                self.conn.rollback()
                print("Come to menu")
        elif (decp == "C"):
            DP = input("podaj id")
            NW = input("podaj nową cene")
            self.cursor.execute("UPDATE pizza SET Cena = %s WHERE id = %s", (NW, DP))
            dec = input("Czy zatwierdzasz zmiany T/N").upper()
            if (dec == "T"):
                self.conn.commit()
                print("wartość zaktualizowano")
            else:
                self.conn.rollback()
                print("Come to menu")

    def UsunPizza(self):
        self.APizza()
        ID = input("Podaj ID")
        self.cursor.execute("DELETE FROM pizza WHERE id = %s", ID)
        dec = input("Czy na pewno chcesz usunąc rekord T/N").upper()
        if(dec=="T"):
            self.conn.commit()
            print("usunięto rekord")
        else:
            self.conn.rollback()
            print("Come to MENU")

    def DodaPizza(self):
        nazwa     = input("Nazwa")
        skladniki = input("Składniki")
        cena      = input("Cena")

        self.cursor.execute("INSERT INTO pizza(nazwa,skladniki,Cena) values (%s,%s,%s)", (nazwa,skladniki,cena))
        self.conn.commit()

    def ADania(self):
        self.cursor = self.conn.cursor()
        self.cursor.execute("select * from Dania")
        pizza = self.cursor.fetchall()
        for row in pizza:
            id             = 0
            nazwa          = 1
            skladniki      = 2
            Cena           = 3
            print(row[id] ,row[nazwa], row[skladniki], row[Cena])

    def AktualizujDania(self):
        self.ADania()
        decp = input("Co chcesz uaktulnić N - Nazwe, S-Składniki, C-Cene").upper()
        if(decp=="N"):
            DP = input("podaj id")
            NW = input("podaj nową nazwe")
            self.cursor.execute("UPDATE Dania SET nazwa = %s WHERE id = %s", (NW,DP))
            dec = input("Czy zatwierdzasz zmiany T/N").upper()
            if(dec=="T"):
                self.conn.commit()

                print("wartość zaktualizowano")
            else:
                self.conn.rollback()
                print("Come to menu")
        elif (decp == "S"):
            DP = input("podaj id")
            NW = input("podaj nowe składniki")
            self.cursor.execute("UPDATE Dania SET skladniki = %s WHERE id = %s", (NW, DP))
            dec = input("Czy zatwierdzasz zmiany T/N").upper()
            if (dec == "T"):
                self.conn.commit()
                print("wartość zaktualizowano")
            else:
                self.conn.rollback()
                print("Come to menu")
        elif (decp == "C"):
            DP = input("podaj id")
            NW = input("podaj nową cene")
            self.cursor.execute("UPDATE Dania SET Cena = %s WHERE id = %s", (NW, DP))
            dec = input("Czy zatwierdzasz zmiany T/N").upper()
            if (dec == "T"):
                self.conn.commit()
                print("wartość zaktualizowano")
            else:
                self.conn.rollback()
                print("Come to menu")

    def UsunDania(self):
        self.ADania()
        self.cursor = self.conn.cursor()
        ID = input("Podaj ID")
        self.cursor.execute("DELETE FROM Dania WHERE id = %s", ID)
        dec = input("Czy na pewno chcesz usunąc rekord T/N").upper()
        if(dec=="T"):
            self.conn.commit()
            print("usunięto rekord")
        else:
            self.conn.rollback()
            print("Come to MENU")

    def DodajDania(self):
        self.cursor = self.conn.cursor()
        nazwa     = input("Nazwa")
        skladniki = input("Składniki")
        cena      = input("Cena")

        self.cursor.execute("INSERT INTO Dania(nazwa,skladniki,Cena) values (%s,%s,%s)", (nazwa,skladniki,cena))
        self.conn.commit()

    def AktualizujKontakt(self):
        self.Kontakt()
        decp = input("Co chcesz uaktulnić C - Cel, N-Numer").upper()
        if(decp=="C"):
            NK = input("podaj numer")
            CK = input("podaj nowy cel")
            self.cursor.execute("UPDATE kontakt SET cel = %s WHERE numer = %s", (CK,NK))
            dec = input("Czy zatwierdzasz zmiany T/N").upper()
            if(dec=="T"):
                self.conn.commit()

                print("wartość zaktualizowano")
            else:
                self.conn.rollback()
                print("Come to menu")
        elif (decp == "S"):
            CK = input("podaj Cel")
            NK = input("podaj nowy numer")
            self.cursor.execute("UPDATE kontakt SET numer = %s WHERE cel = %s", (NK, CK))
            dec = input("Czy zatwierdzasz zmiany T/N").upper()
            if (dec == "T"):
                self.conn.commit()
                print("wartość zaktualizowano")
            else:
                self.conn.rollback()
                print("Come to menu")

    def UsunKontakt(self):
        self.Kontakt()
        self.cursor = self.conn.cursor()
        CK = input("Podaj cel")
        self.cursor.execute("DELETE FROM kontakt WHERE cel = %s", CK)
        dec = input("Czy na pewno chcesz usunąc rekord T/N").upper()
        if(dec=="T"):
            self.conn.commit()
            print("usunięto rekord")
        else:
            self.conn.rollback()
            print("Come to MENU")

    def DodajKontakt(self):
        self.Kontakt = self.conn.cursor()
        cel     = input("Cel")
        numer = input("Numer")

        self.cursor.execute("INSERT INTO kontakt(cel,numer) values (%s,%s)", (cel,numer))
        self.conn.commit()


Connect = Connect()