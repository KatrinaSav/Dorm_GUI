import pickle

from model.Room import Room
from model.Student import Student

class Dorm:
    __month: int
    __student_list: list[Student] = []
    __room_list: list[Room] = []
    __index_of_duty: int
    __is_kitchen_okey: bool
    __level_of_happiness: int
    __mode: bool

    def print_field(self):
        print("#########################################\n"
              "#   1   #   2   #   3   #   4   #   5   # room\n"
              "#   %d   #   %d   #   %d   #   %d   #   %d   # students\n"
              "#   %d   #   %d   #   %d   #   %d   #   %d   # roaches\n"
              "#########################################\n"
              "#   6   #   7   #   8   #   9   #   10  # room\n"
              "#   %d   #   %d   #   %d   #   %d   #   %d   # students\n"
              "#   %d   #   %d   #   %d   #   %d   #   %d   # roaches\n"
              "#########################################\n"
              "#   11  #   12  #   13  #   14  #   15  # room\n"
              "#   %d   #   %d   #   %d   #   %d   #   %d   # students\n"
              "#   %d   #   %d   #   %d   #   %d   #   %d   # roaches\n"
              "#########################################\n"
              % (self.__room_list[0].get_number_of_students(), self.__room_list[1].get_number_of_students(),
                 self.__room_list[2].get_number_of_students(), self.__room_list[3].get_number_of_students(),
                 self.__room_list[4].get_number_of_students(),
                 self.__room_list[0].get_is_roach_in_room(), self.__room_list[1].get_is_roach_in_room(),
                 self.__room_list[2].get_is_roach_in_room(), self.__room_list[3].get_is_roach_in_room(),
                 self.__room_list[4].get_is_roach_in_room(),
                 self.__room_list[5].get_number_of_students(), self.__room_list[6].get_number_of_students(),
                 self.__room_list[7].get_number_of_students(), self.__room_list[8].get_number_of_students(),
                 self.__room_list[9].get_number_of_students(),
                 self.__room_list[5].get_is_roach_in_room(), self.__room_list[6].get_is_roach_in_room(),
                 self.__room_list[7].get_is_roach_in_room(), self.__room_list[8].get_is_roach_in_room(),
                 self.__room_list[9].get_is_roach_in_room(),
                 self.__room_list[10].get_number_of_students(), self.__room_list[11].get_number_of_students(),
                 self.__room_list[12].get_number_of_students(), self.__room_list[13].get_number_of_students(),
                 self.__room_list[14].get_number_of_students(),
                 self.__room_list[10].get_is_roach_in_room(), self.__room_list[11].get_is_roach_in_room(),
                 self.__room_list[12].get_is_roach_in_room(), self.__room_list[13].get_is_roach_in_room(),
                 self.__room_list[14].get_is_roach_in_room()))

    def __init__(self):
        self.__month = 0
        self.__index_of_duty = 0
        self.__is_kitchen_okey = True
        for i in range(15):
            self.__room_list.append(Room(i+1))
        for i in range(15):
            if i == 0:
                self.__room_list[0].add_neighbour_room(self.__room_list[1])
                self.__room_list[0].add_neighbour_room(self.__room_list[5])
            if i == 1:
                self.__room_list[1].add_neighbour_room(self.__room_list[0])
                self.__room_list[1].add_neighbour_room(self.__room_list[2])
                self.__room_list[1].add_neighbour_room(self.__room_list[6])
            if i == 2:
                self.__room_list[2].add_neighbour_room(self.__room_list[1])
                self.__room_list[2].add_neighbour_room(self.__room_list[3])
                self.__room_list[2].add_neighbour_room(self.__room_list[7])
            if i == 3:
                self.__room_list[3].add_neighbour_room(self.__room_list[2])
                self.__room_list[3].add_neighbour_room(self.__room_list[4])
                self.__room_list[3].add_neighbour_room(self.__room_list[8])
            if i == 4:
                self.__room_list[4].add_neighbour_room(self.__room_list[3])
                self.__room_list[4].add_neighbour_room(self.__room_list[9])
            if i == 5:
                self.__room_list[5].add_neighbour_room(self.__room_list[0])
                self.__room_list[5].add_neighbour_room(self.__room_list[6])
                self.__room_list[5].add_neighbour_room(self.__room_list[10])
            if i == 6:
                self.__room_list[6].add_neighbour_room(self.__room_list[1])
                self.__room_list[6].add_neighbour_room(self.__room_list[5])
                self.__room_list[6].add_neighbour_room(self.__room_list[7])
                self.__room_list[6].add_neighbour_room(self.__room_list[11])
            if i == 7:
                self.__room_list[7].add_neighbour_room(self.__room_list[2])
                self.__room_list[7].add_neighbour_room(self.__room_list[6])
                self.__room_list[7].add_neighbour_room(self.__room_list[8])
                self.__room_list[7].add_neighbour_room(self.__room_list[12])
            if i == 8:
                self.__room_list[8].add_neighbour_room(self.__room_list[3])
                self.__room_list[8].add_neighbour_room(self.__room_list[7])
                self.__room_list[8].add_neighbour_room(self.__room_list[9])
                self.__room_list[8].add_neighbour_room(self.__room_list[13])
            if i == 9:
                self.__room_list[9].add_neighbour_room(self.__room_list[4])
                self.__room_list[9].add_neighbour_room(self.__room_list[8])
                self.__room_list[9].add_neighbour_room(self.__room_list[14])
            if i == 10:
                self.__room_list[10].add_neighbour_room(self.__room_list[5])
                self.__room_list[10].add_neighbour_room(self.__room_list[11])
            if i == 11:
                self.__room_list[11].add_neighbour_room(self.__room_list[6])
                self.__room_list[11].add_neighbour_room(self.__room_list[10])
                self.__room_list[11].add_neighbour_room(self.__room_list[12])
            if i == 12:
                self.__room_list[12].add_neighbour_room(self.__room_list[7])
                self.__room_list[12].add_neighbour_room(self.__room_list[11])
                self.__room_list[12].add_neighbour_room(self.__room_list[13])
            if i == 13:
                self.__room_list[13].add_neighbour_room(self.__room_list[8])
                self.__room_list[13].add_neighbour_room(self.__room_list[12])
                self.__room_list[13].add_neighbour_room(self.__room_list[14])
            if i == 14:
                self.__room_list[14].add_neighbour_room(self.__room_list[13])
                self.__room_list[14].add_neighbour_room(self.__room_list[9])
        self.__room_list[0].set_duty(True)

    def save_to_file(self):
        with open("saved_step.pickle", "wb") as write_file:
            pickle.dump(self, write_file)
        write_file.close()
        with open("saved_step_2.pickle", "wb") as write_file:
            pickle.dump(self.__room_list, write_file)
        write_file.close()

    def find_all_students(self):
        for each_room in self.__room_list:
            self.__student_list.extend(each_room.get_students())

    def get_room_list(self):
        return self.__room_list

    def set_room_list(self, list_room: list):
        self.__room_list = list_room

    def next_month(self):
        if self.__month == 4:
            self.__month = 1
        else:
            self.__month += 1

    def get_month(self):
        return self.__month

    def define_is_kitchen_okey(self):
        lvl_of_response: int = 0
        for each_student in self.__room_list[self.__index_of_duty].get_students():
            lvl_of_response += each_student.get_responsability()
        if lvl_of_response < 5:
            self.__is_kitchen_okey = False
            # ?????????????? ?????? ????????????
            return False
        else:
            self.__is_kitchen_okey = True
            return True

    def change_duty(self):
        self.__room_list[self.__index_of_duty].set_duty(False)
        if self.__index_of_duty == len(self.__room_list) - 1:
            self.__index_of_duty = 0
        else:
            self.__index_of_duty += 1
        self.__room_list[self.__index_of_duty].set_duty(True)

    def kick_student(self, student: Student, roomy: Room):
        self.__student_list.remove(student)
        roomy.move_out(student)
        return "?????????????? " + student.get_name()+" ?????? ?????????????? ???? ??????????????????\n"

    def check_in(self, roomy: Room):
        student = Student()
        if roomy.get_number_of_students() >= 2:
            return '???????????????????????? ???????????????????? ?????????????????? ?? ?????????????? 2'
        else:
            roomy.add_student(student)
            self.__student_list.append(student)
            return "__???????????????????? ??????????????__\n" + student.info() + "\n______________________"

    def get_room_by_number(self, number: int) -> Room:
        return self.__room_list[number - 1]

    def check_in_all(self):
        for each_room in self.__room_list:
            for i in range(2):
                self.check_in(each_room)

    def roach(self):
        rooms_with_roaches: list[Room] = []
        for each_room in self.__room_list:
            if each_room.movement_of_roach() == 0:
                continue
            else:
                rooms_with_roaches.append(each_room.movement_of_roach())
        for each_room in rooms_with_roaches:
            each_room.set_roach(True)
            return '?? ?????????????? ???'+ str(each_room.get_number_of_room()) + '???????????????? ????????????????'

    def noise_in_dorm(self):
        for each_room in self.__room_list:
            each_room.noise_in_room()
        for each_room in self.__room_list:
            if each_room.get_is_source_of_noise():
                for room in each_room.get_room_neighbours():
                    if not room.get_is_source_of_noise():
                        room.set_is_noisy(True)

    def visit_every_room(self):
        message = ''
        for each_room in self.__room_list:
            each_room.dirty_up()
            for each_student in each_room.get_students():
                if self.__month == 1:
                    if not each_student.exams():
                        message = message + "?????????????? " + each_student.get_name() + " ?????????????? ???????????? ?? ?????? ????????????????\n"
                        message = message + self.kick_student(each_student, each_room)
            if each_room.get_is_source_of_noise():
                noisiest_stud = each_room.get_students()[0]
                for each_student in each_room.get_students():
                    if each_student.get_noise_level() > noisiest_stud.get_noise_level():
                        noisiest_stud = each_student
                noisiest_stud.give_ban()
                if noisiest_stud.check_kick():
                    message = message + self.kick_student(noisiest_stud, each_room)
            if each_room.get_is_duty():
                if not self.__is_kitchen_okey:
                    for each_student in each_room.get_students():
                        message = message + each_student.give_ban()
                        if each_student.check_kick():
                            message = message + self.kick_student(each_student, each_room)
        return message

    def calculate_level_of_happiness(self):
        roach_rooms: int = 0
        sad_students: int = 0
        bad_kitchen: int = 0
        if not self.__is_kitchen_okey:
            bad_kitchen = 100
        for each_room in self.__room_list:
            if each_room.get_is_roach_in_room():
                roach_rooms += 1
            if each_room.get_is_source_of_noise():
                sad_students += len(each_room.get_students()) - 1
            if each_room.get_is_noisy():
                sad_students += len(each_room.get_students())
        level_of_happiness = 300 - roach_rooms/len(self.__room_list)*100 - sad_students/len(self.__student_list) *\
            100 - bad_kitchen
        return level_of_happiness

    def info(self):
        info = '???????????????????? ?? ?????????????????? ??????????????????\n' + '???????????????? ??????????????: ' + str(self.__index_of_duty) + \
               '\n?????????????? ??????????: ' + str(self.__month) + '\n?????????????? ??????????????: ' + \
               "{:4.2f}".format(self.calculate_level_of_happiness()) + ' ???? 300\n' + '???????????????????? ??????????????????: ' + \
               str(len(self.__student_list))
        if self.__is_kitchen_okey:
            info = info + '\n?????????? ?? ???????????????????? ??????????????????'
        else:
            info = info + '\n?????????? ?? ?????????????????? ??????????????????'
        return info
