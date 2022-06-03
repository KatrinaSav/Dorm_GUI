class Controller:
    def __init__(self, model, view):
        self.model = model
        self.view = view

    def show_dorm(self):
        self.model.update()
        if self.model.our_dorm.get_month() == 4:
            self.view.show_popup("Осторожно! В следующем месяце сессия")
        self.view.show_dorm()

    def save(self):
        self.model.save_to_file()

    def kill_roach(self, number):
        self.model.kill_roach(number)
        self.view.show_dorm()

    def add_student(self, number):
        if self.model.add_student(number) == -1:
            self.view.show_popup('В комнате нет места')
        else:
            self.view.show_dorm()
