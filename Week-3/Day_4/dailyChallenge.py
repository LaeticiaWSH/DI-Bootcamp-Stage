# Part I
class Text():
    def __init__(self,text):
        # self.text = "A good book would sometimes cost as much as a good house."
        self.text = text
        self.list = []
        
        
    def freq(self):
        mystring = self.text.lower()
        string = mystring.split()
        for i in string:
            x = string.count(i)
            w =f"The frequency of {i} : {x}"       
            self.list.append(w) 
        return list(dict.fromkeys(self.list))
        
    def mostcommon(self): 
        max = 0
        mystring = self.text.lower()
        string = mystring.split()
        for i in string:
            x = string.count(i)
            if x > max :
                max = x 
                word = f"The most common are : {i} "
            else:
               if x == max:
                    word += f" {i} "
        text = word.split()
        t =list(dict.fromkeys(text))
        w = ' '.join(t)
        return w

    def unique(self):
        word = " The most unique are "
        min = 1
        mystring = self.text.lower()
        string = mystring.split()
        for i in string:
            x = string.count(i)
            if x == min :
                min = x 
                word += i + ", "
        text = word.split()
        t =list(dict.fromkeys(text))
        w = ' '.join(t)
        return w


txt =Text("A good book would sometimes cost as much as a good house.")
print(txt.freq())
print(txt.mostcommon())
print(txt.unique())