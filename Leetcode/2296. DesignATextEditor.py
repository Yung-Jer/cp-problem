class TextEditor:

    def __init__(self):
        self.txt = ""
        self.cursor = 0

    def addText(self, text: str) -> None:
        strA = self.txt[:self.cursor]
        strB = self.txt[self.cursor:]
        self.txt = strA + text + strB
        self.cursor += len(text)

    def deleteText(self, k: int) -> int:
        if self.cursor <= k:
            self.txt = self.txt[self.cursor:]
            original_cursor = self.cursor
            self.cursor = 0
            return original_cursor
        else:
            strA = self.txt[:self.cursor-k]
            strB = self.txt[self.cursor:]
            self.txt = strA + strB
            self.cursor -= k
            return k
            
    def cursorLeft(self, k: int) -> str:
        self.cursor -= min(self.cursor, k)
        txt = self.txt[:self.cursor]
        return txt[-10:]

    def cursorRight(self, k: int) -> str:
        self.cursor += min(len(self.txt)-self.cursor, k)
        txt = self.txt[:self.cursor]
        return txt[-10:]
        


# Your TextEditor object will be instantiated and called as such:
# obj = TextEditor()
# obj.addText(text)
# param_2 = obj.deleteText(k)
# param_3 = obj.cursorLeft(k)
# param_4 = obj.cursorRight(k)