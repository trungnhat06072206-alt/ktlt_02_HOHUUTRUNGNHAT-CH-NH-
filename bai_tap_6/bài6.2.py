print("ho huu trung nhat")
print("mssv 245752021610023")

class Hinhchunhat(object):
    def __init__(self, dai, rong):
        self.dai = dai
        self.rong = rong

    def dientich(self):
        return self.dai * self.rong

# Test
hcn = Hinhchunhat(5, 3)
print("Diện tích hình chữ nhật:", hcn.dientich())
