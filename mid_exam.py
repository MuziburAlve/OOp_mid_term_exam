class Star_Cinema:
    __hall_list=[]

    @classmethod
    def entry_hall(self,hall):
        Star_Cinema.__hall_list.append(hall)
    
    @classmethod
    def get_hall_list(self):
        return self.__hall_list

class Hall(Star_Cinema):
    def __init__(self,row,col,hall_no,hall_name) -> None:
        self.__seats={}
        self.__show_list=[]
        self.__rows =row
        self.__cols =col
        self.hall_no=hall_no
        self.hall_name=hall_name
        self.entry_hall(self)

    def entry_show(self,id,movie_name,time):
        tup=(id,movie_name,time)
        self.__show_list.append(tup)
        seatt=[]
        for _ in range(self.rows):
            r=[]
            for _ in range(self.cols):
                r.append("free")
            seatt.append(r)
        self.__seats[id]=seatt
        

    def book_seat(self,id,list):
        if id not in [show[0] for show in self.__show_list]:
            raise ValueError("Wrong ID!")
        for r,c in list:
            if r<0 or r>=self.__rows or c<0 or c>=self.__cols:
                raise ValueError(f"Seat {r}{c} is invalid...!")
            if self.__seats[id][r][c]!="free":
                raise ValueError(f"Seat {r}{c} is booked")
            self.__seats[id][r][c]="booked"
            
        
    def view_show_list(self):
        return self.__show_list
    
    def view_available_seats(self,id):
        if id not in self.__seats:
            raise ValueError("Wrong ID!")
        
        print(f"Available seat for show {id}")
        for i in range(self.__rows):
            for j in range(self.__cols):
                if self.seats[id][i][j]=="free":
                    print(f"seat---> ({i},{j})")
        print("\n")
        for j in self.__seats[id]:
            print(j)
    
def play():
 while True:
    print("###___Welcome to Star Cinema__###")
    print("1. VIEW ALL SHOW TODAY")
    print("2.VIEW ALL AVAILABLE SEAT")
    print("3.BOOK TICKET")
    print("4.EXIT")

    select=int(input("Enter Option: "))
    if select==1:
        halls=Star_Cinema.get_hall_list()
        for hal in halls:
            print("##################")
            print(f"the hall name {hal.hall_name} and hall id is {hal.hall_no}")
            print("##################")
            shs=hal.view_show_list()
            for show in shs:
                print(f"MOVIE NAME :{show[1]} , MOVIE ID : {show[0]} , TIME : {show[2]}")
    elif select == 2:
        t=int(input("Enter Show Id : "))
        halls=Star_Cinema.get_hall_list()
        f=False
        for hal in halls:
            if t not in [show[0] for show in hal.view_show_list()]:
                continue
            elif t in [show[0] for show in hal.view_show_list()]:
                hal.view_available_seats(t)
                f=True
                break
            if f is False:
                raise ValueError("Invalid Show id!")
    elif select == 3:
        show_id=input("Enter show id :")
        show_id=int(show_id)
        seat_to_book=input(" enter row and column : row,column  ")
        seat_to_book=[tuple(map(int, seat.split(','))) for seat in seat_to_book.split()]
        halls=Star_Cinema.get_hall_list()
        f=False
        for hal in halls:
            if show_id not in [show[0] for show in hal.view_show_list()]:
                continue
            else:
                hal.book_seat(show_id,seat_to_book)
                print("successfully booked!")
                hal.view_available_seats(show_id)
                f=True
                break
        if f==False:
            print("invalid show id!")

    elif select == 4:
        break
    else:
        print("Invalid option!")

Cinema=Star_Cinema()
ABC_Hall=Hall(3,4,"10201","ABC")
ABC_Hall.entry_show(101,"Tadak","25/10/23 11:00pm")
ABC_Hall.entry_show(102,"installer","25/10/23 11:00pm")
ABC_Hall.entry_show(103,"Iron man8","25/10/23 1:00pm")
ABC_Hall.entry_show(104,"ghost rider","25/10/23 8:00pm")
ABC_Hall.entry_show(105,"THor the end","25/10/23 7:00pm")

star_Hall=Hall(5,5,"10001","star_Hall")
star_Hall.entry_show(201,"king kong","26/10/23 10:00pm")
star_Hall.entry_show(202,"Batman","26/10/23 12:00pm")
star_Hall.entry_show(203,"king kubra return","26/10/23 1:00am")


play()


            









                











