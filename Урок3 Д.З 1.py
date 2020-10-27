class Airline:
    __N_rei=""
    __T_air=""
    __p_naz=""
    __t =""
    __day=""


    def __init__(self,N_rei,T_air,p_naz,t,day):
        self.__N_rei=N_rei
        self.__T_rei=T_air
        self.__p_naz=p_naz
        self.__t=t
        self.__day=day

    def get_N_rei(self):
        return self.__N_rei

    def get_T_rei(self):
        return self.__T_rei

    def get_p_naz(self):
        return self.__p_naz

    def get_time(self):
        return self.__t

    def get_day(self):
        return self.__day

    def __str__(self):
        return "Номер рейса: " + str(self.__N_rei) + " Тип самолета: " + str(self.__T_rei) + " Пункт назначения: "+str(self.__p_naz) + " Время вылета: " + str(self.__t) + " Дни недели: " + str(self.__day)


minsk=[
    Airline("B2-4315","Embraer E-195","Berlin","16:25)","Sunday"),
    Airline("M1-1610","Boeing 737-800","Milan","10:20)","Sunday"),
    Airline("M1-1110","Boeing 737-800","Porto","6:25)","Tuesday"),
    Airline("O1-0001","Boeing 737-800","London","15:15)","Wednesday"),
    Airline("D4-7801","Boeing 737-500","London","10:15)","Friday"),
    Airline("J0-1331","Boeing 737-500","Lille","13:45)","Friday"),
    Airline("T2-4381","Boeing 737-800","Trondheim","9:25)","Saturday")]


def punkt(p_naz):
     for i in minsk:
        if i.get_p_naz() == p_naz:
            print(i.__str__())


def sorday(day):
    for i in minsk:
        if i.get_day() == day:
            print(i.__str__())

print("Ввдите пункт назначения(по анг.): ")
punkt(input())
print("Ввдите день недели(по анг.): ")
sorday(input())