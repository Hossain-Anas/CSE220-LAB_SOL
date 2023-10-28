class Patient:
    def __init__(self, idd=-1, name=-1, age=-1, bg=-1):
        self.id = int(idd)
        self.name = name
        self.age = int(age)
        self.bloodgroup = bg
        self.next = None
        self.prev = None
    


class WRM:
    size = 0
    dummy_head = Patient()
    tail = dummy_head
    dummy_head.prev = tail
    tail.next = dummy_head

    def RegisterPatient(self,idd,name,age,bg):
        new_patient = Patient(idd,name,age,bg)
        WRM.size += 1

        print("Successfully Registered Patient")

        new_Node = new_patient
        WRM.tail.next = new_Node
        new_Node.prev = WRM.tail
        WRM.tail = new_Node
        WRM.tail.next = WRM.dummy_head

    def ServePatient(self):
        if WRM.size == 0:
            print("No Patient to be Served")
            return
        
        if WRM.size == 1:
            name = WRM.dummy_head.next.name
            print(f"{name} is being served")
            WRM.tail = WRM.dummy_head
            WRM.dummy_head = WRM.tail
            WRM.tail.next = WRM.dummy_head
            WRM.size -= 1
            return
        
        
        name = WRM.dummy_head.next.name
        print(f"{name} is being served")

        WRM.dummy_head.next = WRM.dummy_head.next.next
        WRM.dummy_head.next.prev = WRM.dummy_head
        WRM.size -= 1
    
    def CancelAll(self):

        WRM.dummy_head = Patient()
        WRM.tail = WRM.dummy_head
        WRM.dummy_head.prev = WRM.tail
        WRM.tail.next = WRM.dummy_head
        WRM.size = 0

        print("All apointments are cancelled")
    
    def CanDoctorGoHome(self):
        if WRM.size == 0 :
            print("YES")
            return
        
        print("NO")
    
    def ShowAllPatient(self):
        if WRM.size == 0 :
            print("No Patient in the WRM")
            return
        
        temp = WRM.dummy_head.next

        while temp != WRM.dummy_head :
            print(temp.name, end = " ")
            temp = temp.next
        
        print()

    def ReverseTheLine(self):
        if WRM.size == 0 :
            print("No Patient in Line")
            return
        
        first = WRM.dummy_head.next
        mid = None
        last = None

        while first != WRM.dummy_head :
            last = mid
            mid = first
            first = first.next
            mid.next = last
            mid.prev = first
        
        WRM.tail = WRM.dummy_head.next
        WRM.dummy_head.next = mid
        WRM.tail.next = WRM.dummy_head
        WRM.dummy_head.prev = WRM.tail

        print("Reversed the Line")

class Tester:
    wrm = WRM()

    while True:
        print()
        print("==Choose an Option==")
        print("""1. RegisterPatient()
2. ServePatient()
3. CancelAll()
4. CanDoctorGoHome()
5. ShowAllPatient()
6. ReverseTheLine()
7. exit""")
        print("==============================")

        print("Enter Your Choice : ", end="")
        val = int(input())
        print()

        if val == 7 :
            print("Exiting...")
            break
        
        elif val == 1 :
            print("Executing RegisterPatient()...")
            print()

            print("Enter ID : ", end="")
            idd = input()

            print("Enter Name : ", end = "")
            name = input()

            print("Enter Age : ", end = "")
            age = input()

            print("Enter Blood Group : ", end = "")
            bg = input()
            print()

            wrm.RegisterPatient(idd, name, age, bg)

        elif val == 2 :
            wrm.ServePatient()
        
        elif val == 3:
            wrm.CancelAll()

        elif val == 4:
            wrm.CanDoctorGoHome()
        
        elif val == 5 :
            wrm.ShowAllPatient()
        elif val == 6 :
            wrm.ReverseTheLine()

test = Tester()