print("ho huu trung nhat")
print("mssv 245752021610023")

class Nguoi(object):
    def getGender(self):
        return "Unknown"

class Nam(Nguoi):
    def getGender(self):
        return "Nam"

class Nu(Nguoi):
    def getGender(self):
        return "Nữ"

# Test
aNam = Nam()
aNu = Nu()

print(aNam.getGender())
print(aNu.getGender())
