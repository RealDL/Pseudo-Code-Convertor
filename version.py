import re

class PythonToPseudocode:
    def __init__(self):
        self.python_processing = self.get_file()
        self.by_hand = []
        self.comments()
        self.iteration()
        self.selection()
        self.files()
        self.classes()
        self.try_except()
        for line in self.python_processing:
            print(line)

    def get_file(self):
        
        with open("MyPythonFile.txt","r") as my_file:
            processing = [line.strip('\n') for line in my_file]
        return processing
    
    def code_indent(self,linestart):
        spaces = 0
        linecheck = self.python_processing[linestart]
        for i in linecheck:
            if i == " ":
                spaces += 1
            else:
                break
        return(spaces)

    def ending_insert(self,linestart,endstatement):
        current_line = linestart+1
        spaces = self.code_indent(linestart)
        start_spaces = spaces
        try:
            while self.code_indent(current_line) > spaces or "else" in self.python_processing[current_line]:
                current_line+=1
                if len(self.python_processing) == current_line: #Handles situations where the indent runs to end of file
                    break
        except:
            byhandadd="line "+str(current_line)+" Hit an error. Please check"
            self.by_hand.append(byhandadd)
        z=(" "*start_spaces)+endstatement
        self.python_processing.insert(current_line,z)
    
    def comments(self):
        for index, line in enumerate(self.python_processing):
            if "#" in line:
                self.python_processing[index] = line.replace("#","//")
    
    def iteration(self):
        for index, line in enumerate(self.python_processing):
            if "else:" in line:
                line = line.replace("else:"," else")
            if "elif" in line and "endif" not in line:
                line = line.replace("elif","elseif")
                line = line.replace(":"," then")
            if "if" in line and "endif" not in line:
                if "//" in line:
                    if line.find("//") > line.find("if"):
                        line = line.replace(":"," then")
                        self.ending_insert(index,"endif")
                else:
                    line = line.replace(":"," then")
                    self.ending_insert(index,"endif")
            if "while" in line and ":" in line and "endwhile" not in line:
                if "//" in line:
                    if line.find("//") > line.find("while"):
                        line = line.replace(":","")
                        self.ending_insert(index,"endwhile")
                else:
                    line = line.replace(":","")
                    self.ending_insert(index,"endwhile")
            self.python_processing[index] = line
    
    def selection(self):
        for index, line in enumerate(self.python_processing):
            if " and " in line:
                if "//" in line:
                    if line.find("//") > line.find("and"):
                        line = line.replace("and", "AND")
                else:
                    line = line.replace("and", "AND")
            if " or " in line:
                if "//" in line:
                    if line.find("//") > line.find("or"):
                        line = line.replace("or", "OR")
                else:
                    line = line.replace("or", "OR")
            if " not " in line:
                if "//" in line:
                    if line.find("//") > line.find("not"):
                        line = line.replace("not", "NOT")
                else:
                    line = line.replace("not", "NOT")
            self.python_processing[index] = line

    def files(self):
        for index, line in enumerate(self.python_processing):
            if "open" in line:
                if "r" in line:
                    line = line.replace("open","openRead")
                    line = line.replace(',"r"','')
                if "w" in line:
                    line = line.replace("open","openWrite")
                    line = line.replace(',"w"','')
            if "write" in line:
                line = line.replace("write","writeLine")
            self.python_processing[index] = line
    
    def classes(self):
        for index, line in enumerate(self.python_processing):
            if "class" in line:
                if "(" in line and ")" in line:
                    class_details = line.split('(')
                    if len(class_details) >= 2:
                        class_name = class_details[0].split(' ')[1]
                        base_class = class_details[1].split(')')[0]
                        line = f"class {class_name} inherits {base_class}"
                else:
                    if "()" in line:
                        line = line.replace("()","")
                    line = line.replace(":","")
            if "=" in line and "(" in line and ")" in line:
                if "= " in line:
                    line = line.replace("=","= new")
                else:
                    line = line.replace("=","= new ")
            
            if "def __init__(" in line:
                if "self" in line:
                    line = line.replace("self","")
                if ":" in line:
                    line = line.replace(":","")
                line = line.replace("def __init__(","public procedure new(")

            if "self" in line:
                if "self," in line:
                    if "self, " in line:
                        line = line.replace("self, ","")
                    else:
                        line = line.replace("self,","")
                if "self." in line:
                    line = line.replace("self.","")
                if "self" in line:
                    line = line.replace("self","")
                
            self.python_processing[index] = line

    def try_except(self):
        for index, line in enumerate(self.python_processing):
            if "try" in line or "except" in line:
                if ":" in line:
                    line = line.replace(":","")
                if "except" in line:
                    self.ending_insert(index,"endtry")
            self.python_processing[index] = line
                
    
    def functions_and_procedures(self):
        for index, line in enumerate(self.python_processing):
            if "def" in line:
                pass

            # found out whether function or procedure.
            # if found return, then its a function, if found
            # no return its a procedure.

            

converter = PythonToPseudocode()
