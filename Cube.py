colors = {"R":"🟥", "O":"🟧", "G":"🟩", "B":"🟦", "W":"⬜", "Y":"🟨"}
regularity = 3

class Side:
    def __init__(self, arrangement="default", color="W"):
            self.arrangement = [[colors[color]]*3]*3 if type(arrangement) == str else arrangement

    def rotate(self, next_side, prev_side):
        pass

class Rubiks_cube:
    def __init__(self):
        self.sides = []
        for i in colors.keys():
            self.sides.append(Side(color=i))

    def print_cube(self):
        for i in self.sides:
            for j in i.arrangement:
                print(" ".join(j))
            print("\n")

def main():
    Test_RB = Rubiks_cube()
    Test_RB.print_cube()

if __name__ == "__main__":
    main()