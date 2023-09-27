from User import *

if __name__ == '__main__':
    print("Test USER.PY")

    test = User.LoadJson("Loriel")
    test.GetUser()
    # test.GetUser()
    test2 = User.LoadJson("Riku")