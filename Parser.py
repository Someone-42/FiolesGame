import Vials

class Parser:
    def __init__(self, file_path):
        self.file_path = file_path

    def save_level(self, vials: list) -> int:
        """ Saves a level, returns its save index """
        pass

    def load_level(self, index: int) -> list:
        """ Loads the level according to the index (list of vials)"""
        file = open(self.file_path, "r")
        lines = file.readlines()
        file.close()
        if index >= len(lines):            
            raise IndexError("Out of range exception - level doesn't exist UwU")
        else:
            level = self._read_to_list(lines[index])
            level_vials = []
            for colors in level:
                vial = Vials.Vial(len(colors))
                vial.push_content(colors)
                level_vials.append(vial)
            return level_vials

    def _read_to_list(self, level_string: str):
        """ Reads a level in memory and returns it as lists """
        vial_strings = level_string.split("|")
        vials = [[int(color) for color in vial.split(" ")] for vial in vial_strings]
        return vials

if __name__ == "__main__":
    test = Parser("Content/Levels1.txt")
    print(test.load_level(0) )
