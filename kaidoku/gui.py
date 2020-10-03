import tkinter
import copy

class GUIBord(tkinter.Tk):
    def __init__(self):
        super().__init__()

    def display(self,s,move):
        self.title("KAIDOKU")
        self.geometry("270x300")
        self.resizable(0,0)
        self.move = copy.deepcopy(move)

        frame1 = tkinter.Frame(self)
        frame1.grid()

        bordFrame = tkinter.Frame(frame1)
        bordFrame.grid(row=0, column=0)

        # make 3 * 3 blocks
        blockList = [[None]*3 for i in range(3)]
        for i in range(3):
            for j in range(3):
                block = tkinter.Frame(
                    bordFrame,
                    width = 90,
                    height = 90,
                    borderwidth = 1,
                    relief="solid",
                )
                block.grid(row=i, column=j)
                block.grid_propagate(0)
                blockList[i][j] = block
        self.inputList = [[None]*9 for i in range(9)]
        for i in range(9):
            for j in range(9):
                square = tkinter.Frame(
                    blockList[i//3][j//3],
                    width = 30,
                    height = 30,
                    borderwidth = 0,
                    background="white smoke",
                    relief="solid",
                )
                square.propagate(0)
                square.grid(row=i%3, column=j%3)
                # If the value is 0 , create a text box
                if s[i * 9 + j] != 0:
                    label = tkinter.Label(
                        square,
                        text = s[i * 9 + j],
                    )
                    label.pack()
                    self.inputList[i][j] = s[i * 9 + j]
                else:
                    textBox = tkinter.Entry(
                        square,
                        background = "white smoke",
                        justify = "center",
                        validate = 'key',
                        vcmd = (self.register(self.validation),'%P',i,j)
                    )
                    textBox.pack()
                    self.inputList[i][j] = textBox
        for v in move:
            idx = int(v[0]) - 1;jdx = int(v[1]) - 1
            nval = v[2]
            self.inputList[idx][jdx].insert(0,nval)
        # set button
        buttonFrame = tkinter.Frame(frame1)
        buttonFrame.grid(row=1, column=0)
        submitButton = tkinter.Button(
            buttonFrame,
            text="save",
            command=self.saveClick,
        )
        submitButton.pack()
        self.mainloop()

    """When user click save-button"""
    def saveClick(self):
        numList = [[None]*9 for i in range(9)]
        self.move = []
        for i in range(9):
            for j in range(9):
                if type(self.inputList[i][j]) != int:
                    if self.inputList[i][j].get() == '':continue
                    self.move.append(str(i + 1) + str(j + 1) + self.inputList[i][j].get())

    def validation(self,P,idx,jdx):
        idx = int(idx);jdx = int(jdx)
        if len(P) == 0:return True
        if len(P) > 1:return False
        if not (ord('1') <= ord(P) <= ord('9')):return False
        # If input value get stuck in a constraint , return False
        for i in range(9):
            if self.objToStr(self.inputList[idx][i]) == P:return False
            if self.objToStr(self.inputList[i][jdx]) == P:return False
            if self.objToStr(self.inputList[(idx//3)*3+i//3][(jdx//3)*3+i%3]) == P:return False
        return True

    def objToStr(self,obj):
        if type(obj) == int:return str(obj)
        if type(obj) == str:return obj 
        return obj.get()
