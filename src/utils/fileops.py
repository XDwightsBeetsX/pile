


class FileHandler(object):
    def __init__(self, dir):
        self.Dir = dir

    def rename_subfolders(self, old_id_bracket, new_id_bracket):
        """
        Renames files in self.Dir  
        Does NOT walk subfolders  
        use new_id_bracket to change filename
        """
        import os
        
        p = self.Dir
        fs = get_files(p)
        print(f"Scanning: {len(fs)} files in {p}")
        for f in fs:
            try:
                old_file = p + '\\' + f
                f_type = os.path.splitext(f)[1]
                
                try:
                    f_id = old_id_bracket.getId(f)
                except:
                    print(f"Could not find file id: '{f}'")
                
                new_title = f"{new_id_bracket.Id_Start}{f_id}{new_id_bracket.Id_End}{f_type}"
                new_file = p + '\\' + new_title
                os.rename(old_file, new_file)
                print(f"renamed file {f} -> {new_title}")
                
            except:
                print(f"Unable to rename file: '{f}'")
        
    def replace_char_in_filename(self, char_to_replace, new_char, replace_limit=0):
        """
        Does NOT walk subfolders  
        Inspects only file names, not extensions  
        will replace all occurences of char_to_replace unless specified
        """
        import os

        p = self.Dir
        fs = get_files(p)
        print(fs)
        print(f"Scanning: {len(fs)} files in {p}")
        for f in fs:
            try:
                old_file = p + '\\' + f
                f_type = os.path.splitext(f)[1]
                f_name = f.split(f_type)[0]

                if replace_limit == 0:
                    replace_limit = len(f_name)

                if char_to_replace in f_name:
                    new_f_name = f_name.replace(char_to_replace, new_char)
                    new_file = p + '\\' + new_f_name + f_type
                    os.rename(old_file, new_file)
                    print(f"renamed file '{f_name + f_type}' -> '{new_f_name + f_type}'")
                else:
                    print(f"Could not find '{char_to_replace}' in '{f_name}'")
            except:
                print(f"Unable to rename file: '{f}'")


class IdBracket(object):
    """
    Used to rename files or find ids within filenames.  
    Can manipulate id_start, id_end to edit filenames with FileHandler.rename_subfolders
    """
    def __init__(self, id_start, id_end):
        self.Id_Start = id_start
        self.Id_End = id_end
    
    def getId(self, s):
        """
        Finds the Id based on start/end chars in a string s
            returns '' if not found
        use '' to denote the beginning of the string
        """
        
        # find returns -1 if not found
        si = s.find(self.Id_Start)
        ei = s.find(self.Id_End)
        
        # check vals
        if si < ei:
            if si != -1 and ei != -1:
                # valid
                sl = len(self.Id_Start)
                if self.Id_Start != "":
                    i = si + sl
                else:
                    i = sl
                j = ei
                return s[i:j]
        else:
            raise Exception(f"Could not find id in {s}")


def get_files(path):
    import os
    files = []
    for file in os.listdir(path):
        if os.path.isfile(os.path.join(path, file)):
            files.append(file)
    
    return files


if __name__ == "__main__":
    filepath = r""
    FH = FileHandler(filepath)
    
    B_old = IdBracket("", "-")
    B_new = IdBracket("L", " material")

    # FH.rename_subfolders(B_old, B_new)
    # FH.replace_char_in_filename("p", "")
