class nel:
    def __init__(self):
        self.len=5
    def __len__(self):
        return self.len
    def __mix(self):
        self.len=self.len*2
    def pup(self):
        self.__mix()
        return print(self.len)
    
        
