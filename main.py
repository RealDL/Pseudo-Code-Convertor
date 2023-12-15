# RealDL pseudocode convertor. Your welcome.
print("RealDL: Python to Pseudocode Convertor.")

class PythonToPseudocode:
    def __init__(self):
        self.python_processing = self.get_file()
        self.by_hand = []
        self.variables = {}
        self.remove_spaces()
        self.comments()
        self.iteration()
        self.selection()
        self.files()
        self.self_variables()
        self.functions_and_procedures()
        self.classes()
        self.try_except()
        self.imports()
        self.create_txt_file('pseudocode.txt')
        self.print_pseudocode()
    
    def print_pseudocode(self):
        for line in self.python_processing:
            print(line)

    def create_txt_file(self, filename):
        with open(filename, 'w') as file:
            for line in self.python_processing:
                file.write(line + '\n')

    def imports(self):
        last_import_index = None
        line_number = 0
        for index, line in enumerate(self.python_processing):
            if "import" in line:
                last_import_index = True
                line_number = index
        if last_import_index != None:
            self.python_processing[line_number] = f"{self.python_processing[line_number]}\n"

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
   
    def remove_spaces(self):
        spaces = True
        while spaces:
            for index, line in enumerate(self.python_processing):
                to_delete = False
                if line == '':
                    to_delete = True
                    
                if line.isspace():
                    to_delete = True

                if to_delete == True:
                    del self.python_processing[index]    
            if to_delete == False:
                spaces = False

    def comments(self):
        self.python_processing.insert(0,"# Created by RealDL - @realdl on discord.\n")
        self.python_processing.insert(len(self.python_processing),"# Created by RealDL - @realdl on discord.\n")
        for index, line in enumerate(self.python_processing):
            if "#" in line:
                self.python_processing[index] = line.replace("#","//")
            if '"""' in line:
                self.python_processing[index] = line.replace('"""','//')
    
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
   
    def self_variables(self):
        for index, line in enumerate(self.python_processing):
            create_class = True
            if "class" in line:
                if "//" in line:
                    if line.find("//") < line.find("class"):
                        create_class = False
                if create_class == True:
                    class_name = self.get_class_name(index)
                    self.variables[class_name] = []
                    lines = 1
                    found = False
                    while not found:
                        try:
                            new_line = self.python_processing[index+lines]
                            if "self." in new_line and "=" in new_line:
                                if new_line.find("=") > new_line.find("self."):
                                    words = new_line.split()  # Split the line into words
                                    words = words[0]
                                    if not "[" in words and not "]" in words and not "if" in words and not "elseif" in words and not "else" in words:
                                        words = words.replace("self.","")
                                        if words not in self.variables[class_name]:
                                            self.variables[class_name].append(words)
                            elif "class" in new_line:
                                if "//" in new_line:
                                    if new_line.find("//") > new_line.find("class"):
                                        found = True
                                else:
                                    found = True
                        except:
                            # List out of range
                            found = True
                        lines+= 1

    def get_class_name(self, index):
        line = self.python_processing[index]
        if not "(" in line and not ")" in line:
            line = line.replace(":","")
            line = f"{line}():"

        class_details = line.split('(')
        if len(class_details) >= 2:
            class_name = class_details[0].split(' ')[1]
            return class_name

    def classes(self):
        for index, line in enumerate(self.python_processing):
            if "class" in line:
                create_class = True
                if "//" in line:
                    if line.find("//") < line.find("class"):
                        create_class = False
                if create_class == True:
                    if "(" in line and ")" in line:
                        class_details = line.split('(')
                        if len(class_details) >= 2:
                            class_name = class_details[0].split(' ')[1]
                            base_class = class_details[1].split(')')[0]
                            if base_class == '':
                                line = f"\nclass {class_name}"
                            else:
                                line = f"\nclass {class_name} inherits {base_class}"
                    else:
                        if "()" in line:
                            line = line.replace("()","")
                        line = line.replace(":","")
                if create_class == True:
                    class_name = self.get_class_name(index)
                    variable_list = self.variables[class_name]
                    for index_range, variable in enumerate(variable_list):
                        number_of_spaces = self.code_indent(index+1)
                        spaces = " "*number_of_spaces
                        space = ""
                        if index_range == 0:
                            space = "\n"
                        self.python_processing.insert(index+1, f"{spaces}private {variable}{space}")
                    self.variables[class_name] = []

            if "=" in line and "(" in line and ")" in line:
                if "= " in line:
                    line = line.replace("=","= new")
                else:
                    line = line.replace("=","= new ")
           
            if "def __init__(" in line:
                if "self" in line:
                    if "self, " in line:
                        line = line.replace("self, ","")
                    else:
                        line = line.replace("self,","")
                if ":" in line:
                    line = line.replace(":","")
                line = line.replace("def __init__(","public procedure new(")
                self.ending_insert(index,"endprocedure\n")

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
            type_of_procedure = ""
            if "def" in line:
                if "self" in line:
                    type_of_procedure = "class"
                else:
                    type_of_procedure = "normal"
                if "def __init__(" not in line:
                    lines = 1
                    type_of_def = ""
                    found = False
                    while found != True:
                        try:
                            if "def" in self.python_processing[index+lines]: 
                                if "//" in line:
                                    if line.find("//") > line.find("def"):
                                        found = True
                                        type_of_def = "procedure"

                                else:
                                    found = True
                                    type_of_def = "procedure"
                            elif "return" in self.python_processing[index+lines]:
                                if "//" in line:
                                    if line.find("//") > line.find("return"):
                                        found = True
                                        type_of_def = "function"

                                else:
                                    found = True
                                    type_of_def = "function"
                        except:
                            # List out of range
                            found = True
                            type_of_def = "procedure"
                        lines += 1

                    if type_of_def == "procedure":
                        if type_of_procedure == "class":
                            line = line.replace("def","public procedure")
                        elif type_of_procedure == "normal":
                            line = line.replace("def","procedure")
                        self.ending_insert(index,"endprocedure\n")
                    elif type_of_def == "function":
                        line = line.replace("def","function")
                        self.ending_insert(index,"endfunction\n")
                    if ":" in line:
                        line = line.replace(":","")
                    self.python_processing[index] = line

converter = PythonToPseudocode()
