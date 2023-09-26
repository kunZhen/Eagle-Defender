from Users.User import *

if __name__ == '__main__':
    print("Test USER.PY")

    testUser = User("Loriel", "Manuel Loria", "T.test01", 56, "jmlc.loria@gmail.com",
                    ["Felipe", "Isaac", "Football", "Hand", "Cellphone"])

    testUser.getUser()

    testUser2 = User.loadJson("Pacman")
