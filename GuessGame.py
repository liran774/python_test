def guess():
        import random
        secret_num=random.randint(0,9)
        print("enter your guess")
        get_num=input()
        if secret_num==get_num:
            print("true")
        else:
            print("fulse")


