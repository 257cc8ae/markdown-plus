class Parser():
    res:list = []

    def convertToObject(self,body):
        self.parse(body)
        return self.res
    
    def isHeadingObject(self,line):
        res:dict = {"isHeading": False,"type":"","context":""}
        for size in range(1,7):
            if line[0:size + 1] == "#" * size + " ":
                res["isHeading"] = True
                res["type"] = "h" + str(size)
                res["context"] = line[size + 1:]
                break
        return res

    def parse(self,body):
        lines:list = body.split("\n")
        for line in lines:
            element:dict = {"type":"","content": ""}
            isHeading:dict = self.isHeadingObject(line)
            if isHeading["isHeading"]:
                element["type"] = isHeading["type"]
                element["content"] = isHeading["context"]
            else:
                element["type"] = "text"
                element["content"] = line
            self.res.append(element)


parser  = Parser()

with open("docs.md") as f:
    s = f.read()
    print(parser.convertToObject(s))