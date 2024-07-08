import sys

from crossword import *


class CrosswordCreator():

    def __init__(self, crossword):
        """
        Create new CSP crossword generate.
        """
        self.crossword = crossword
        self.domains = {
            var: self.crossword.words.copy()
            for var in self.crossword.variables
        }

    def letter_grid(self, assignment):
        """
        Return 2D array representing a given assignment.
        """
        letters = [
            [None for _ in range(self.crossword.width)]
            for _ in range(self.crossword.height)
        ]
        for variable, word in assignment.items():
            direction = variable.direction
            for k in range(len(word)):
                i = variable.i + (k if direction == Variable.DOWN else 0)
                j = variable.j + (k if direction == Variable.ACROSS else 0)
                letters[i][j] = word[k]
        return letters

    def print(self, assignment):
        """
        Print crossword assignment to the terminal.
        """
        letters = self.letter_grid(assignment)
        for i in range(self.crossword.height):
            for j in range(self.crossword.width):
                if self.crossword.structure[i][j]:
                    print(letters[i][j] or " ", end="")
                else:
                    print("█", end="")
            print()

    def save(self, assignment, filename):
        """
        Save crossword assignment to an image file.
        """
        from PIL import Image, ImageDraw, ImageFont
        cell_size = 100
        cell_border = 2
        interior_size = cell_size - 2 * cell_border
        letters = self.letter_grid(assignment)

        # Create a blank canvas
        img = Image.new(
            "RGBA",
            (self.crossword.width * cell_size,
             self.crossword.height * cell_size),
            "black"
        )
        font = ImageFont.truetype("assets/fonts/OpenSans-Regular.ttf", 80)
        draw = ImageDraw.Draw(img)

        for i in range(self.crossword.height):
            for j in range(self.crossword.width):

                rect = [
                    (j * cell_size + cell_border,
                     i * cell_size + cell_border),
                    ((j + 1) * cell_size - cell_border,
                     (i + 1) * cell_size - cell_border)
                ]
                if self.crossword.structure[i][j]:
                    draw.rectangle(rect, fill="white")
                    if letters[i][j]:
                        _, _, w, h = draw.textbbox((0, 0), letters[i][j], font=font)
                        draw.text(
                            (rect[0][0] + ((interior_size - w) / 2),
                             rect[0][1] + ((interior_size - h) / 2) - 10),
                            letters[i][j], fill="black", font=font
                        )

        img.save(filename)

    def solve(self):
        """
        Enforce node and arc consistency, and then solve the CSP.
        """
        self.enforce_node_consistency()
        self.ac3()
        return self.backtrack(dict())

    def enforce_node_consistency(self):
        """
        Update `self.domains` such that each variable is node-consistent.
        (Remove any values that are inconsistent with a variable's unary
         constraints; in this case, the length of the word.)
        """
        
        for variable in self.domains:
            for value in list(self.domains[variable]):
                if len(value) != variable.length:
                    self.domains[variable].remove(value)

    def revise(self, x, y):
        """
        Make variable `x` arc consistent with variable `y`.
        To do so, remove values from `self.domains[x]` for which there is no
        possible corresponding value for `y` in `self.domains[y]`.

        Return True if a revision was made to the domain of `x`; return
        False if no revision was made.
        """
        
        overlaps = self.crossword.overlaps

        #Keep track if it has been revised
        revised = False

        #Iterating over the value of x
        for domainX in list(self.domains[x]):
                if overlaps[x, y]:
                    i = overlaps[x, y][0]
                    j = overlaps[x, y][1]
                    remove = []
                    for domainY in list(self.domains[y]):
                        #Condition to check arc consistency / Checking if it satisfies the constraint
                        if domainX[i] != domainY[j]:
                            remove.append(True)
                        else:
                            remove.append(False)
                            # if domainX in self.domains[x]:
                            #     self.domains[x].remove(domainX)
                    if all(remove):
                        self.domains[x].remove(domainX)
                        revised = True 
                    
        return revised

    def ac3(self, arcs=None):
        """
        Update `self.domains` such that each variable is arc consistent.
        If `arcs` is None, begin with initial list of all arcs in the problem.
        Otherwise, use `arcs` as the initial list of arcs to make consistent.

        Return True if arc consistency is enforced and no domains are empty;
        return False if one or more domains end up empty.
        """
        if arcs == None:
            queue = [list(self.crossword.overlaps.keys())[i] for i in range(len(self.crossword.overlaps))]
        else:
            queue = arcs

        while len(queue) != 0:
            x,y = queue.pop()
    
            if self.revise(x,y):
                if len(self.domains[x]) == 0:
                    return False
                for z in self.crossword.neighbors(x) - {y}:
                    queue.append((z,x))
        return True

    def assignment_complete(self, assignment):
        """
        Return True if `assignment` is complete (i.e., assigns a value to each
        crossword variable); return False otherwise.
        """
        return len(assignment) == len(self.crossword.variables)
    
    def consistent(self, assignment):
        """
        Return True if `assignment` is consistent (i.e., words fit in crossword
        puzzle without conflicting characters); return False otherwise.
        """

        no_conflict = []
        for v1 in assignment:
            for v2 in assignment:
                if v1 != v2:
                    overlaps = self.crossword.overlaps[v1, v2]
                    if overlaps:
                        i = overlaps[0]
                        j = overlaps[1]
                        if assignment[v1][i] != assignment[v2][j]:
                            no_conflict.append(False)
                        else:
                            no_conflict.append(True)

        no_conflict = all(no_conflict)

        return all(
            (len(assignment[variable]) == variable.length) and
            (list(assignment.values()).count(assignment[variable]) == 1) and
            no_conflict
            for variable in assignment
        )


    def order_domain_values(self, var, assignment):
        """
        Return a list of values in the domain of `var`, in order by
        the number of values they rule out for neighboring variables.
        The first value in the list, for example, should be the one
        that rules out the fewest values among the neighbors of `var`.
        """
        
        elimination = dict()
        neighbors = self.crossword.neighbors(var)

        for value in list(self.domains[var]):
            
            n = 0
            for neighbor in neighbors:
               if neighbor not in assignment:
                    i = self.crossword.overlaps[var, neighbor][0]
                    j = self.crossword.overlaps[var, neighbor][1]
                    for val in self.domains[neighbor]:
                        if value[i] != val[j]:
                            n += 1
            elimination[value] = n 
        
        return sorted(elimination, key=lambda k: elimination[k])
    

    def select_unassigned_variable(self, assignment):
        """
        Return an unassigned variable not already part of `assignment`.
        Choose the variable with the minimum number of remaining values
        in its domain. If there is a tie, choose the variable with the highest
        degree. If there is a tie, any of the tied variables are acceptable
        return values.
        """
        
        vars = []
        for variable in self.crossword.variables:
            if variable not in assignment:
                vars.append([variable, len(self.domains[variable]), len(self.crossword.neighbors(variable))])

        return sorted(vars, key=lambda x: (x[1], x[2]))[0][0]

        # for v1 in self.crossword.variables:
        #     best_variable = v1
        #     for v2 in self.crossword.variables:
        #         if v1 not in assignment and v2 not in assignment and v1 != v2: 
        #             current_variable = v2
        #             if len(self.domains[best_variable]) < len(self.domains[current_variable]):
        #                 best_variable = best_variable
        #             elif len(self.domains[best_variable]) > len(self.domains[current_variable]):
        #                 best_variable = current_variable
        #             else:
        #                 degree1 = len(self.crossword.neighbors[best_variable])
        #                 degree2 = len(self.crossword.neighbors[current_variable])
        #                 if degree1 < degree2:
        #                     best_variable = current_variable
        #                 else:
        #                     best_variable = best_variable
        #     return best_variable

    def backtrack(self, assignment):
        """
        Using Backtracking Search, take as input a partial assignment for the
        crossword and return a complete assignment if possible to do so.

        `assignment` is a mapping from variables (keys) to words (values).

        If no assignment is possible, return None.
        """
        
        if self.assignment_complete(assignment):      
            return assignment
        
        var = self.select_unassigned_variable(assignment)

        for value in self.order_domain_values(var, assignment):
                new_assignment = assignment.copy()
                new_assignment[var] = value
                if self.consistent(new_assignment):
                    result = self.backtrack(new_assignment)
                    if result is not None:
                        return result
                    del new_assignment[var]
        return None

def main():

    # Check usage
    if len(sys.argv) not in [3, 4]:
        sys.exit("Usage: python generate.py structure words [output]")

    # Parse command-line arguments
    structure = sys.argv[1]
    words = sys.argv[2]
    output = sys.argv[3] if len(sys.argv) == 4 else None

    # Generate crossword
    crossword = Crossword(structure, words)
    creator = CrosswordCreator(crossword)
    assignment = creator.solve()

    # Print result
    if assignment is None:
        print("No solution.")
    else:
        creator.print(assignment)
        if output:
            creator.save(assignment, output)


if __name__ == "__main__":
    main()
