# Child multiple parents

class Camera:
    def __init__(self, camera_resolution):
        self.camera_resolution = camera_resolution

    def record_video(self):
        print(f"Recording video in {self.camera_resolution} resolution")

    def test(self):
        print("Testing camera functionality")

class Telephone:
    def __init__(self, telephone_number):
        self.telephone_number = telephone_number

    def make_call(self):
        print(f"Making a call to {self.telephone_number}")

    def test(self):
        print("Testing telephone functionality")

class SmartPhone(Telephone, Camera):
    def __init__(self, camera_resolution, telephone_number, brand):
        Camera.__init__(self, camera_resolution)
        Telephone.__init__(self, telephone_number)
        self.brand = brand


s1 = SmartPhone("1080p", "123-456-7890", "BrandX")
s1.test()