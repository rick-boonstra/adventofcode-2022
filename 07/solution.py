import time

FILE_NAME = '07/input.txt'

class Node():
    def __init__(self, type, name, size, parent):
        self.type = type
        self.name = name
        self.size = size
        self.parent = parent
        if parent is None:
            self.depth = 0
        else:
            self.depth = parent.depth + 1
        self.children = {}

    def add_child(self, type, name, size):
        self.children[name] = Node(type, name, size, self)

    def navigate_up(self):
        return self.parent

    def navigate_down(self, target_node):
        return self.children[target_node]
    
    def return_size(self):
        total_size = 0
        total_size += self.size
        for child in self.children:
            total_size += self.children[child].return_size()
        return total_size

    def print_tree(self):
        spacing_string = self.depth * '\t'
        print(f'{spacing_string}{self.name} ({self.type}, {self.return_size():,})')
        for child in self.children:
            self.children[child].print_tree()

    def part_one_answer(self, answer):
        dir_size = self.size
        
        for child in self.children:
            dir_size += self.children[child].return_size()
            answer = self.children[child].part_one_answer(answer)
        
        if self.type == 'dir' and int(dir_size) <= 100000:
            answer += dir_size

        return answer

    def part_two_answer(self, space_needed, answer):
        dir_size = self.return_size()
        
        if self.type == 'dir' and (answer == 0 or dir_size < answer) and dir_size >= space_needed:
            answer = dir_size

        for child in self.children:
            answer = self.children[child].part_two_answer(space_needed, answer)

        return answer

def process_input():
    # Process the input file
    with open(FILE_NAME, 'r') as inputfile:
        input_lines = inputfile.read().splitlines()    
    
    root_node = None
    current_node = None

    for line in input_lines:
        line_parts = line.split(' ')
        if line_parts[0] == '$':
            if line_parts[1] == 'cd':
                if line_parts[2] == '..':
                    current_node = current_node.navigate_up()
                else:
                    node_name = line_parts[2]
                    if root_node is None:
                        root_node = Node('dir', node_name, 0, None)
                        current_node = root_node
                    else:
                        current_node = current_node.navigate_down(node_name)
            if line_parts[1] == 'ls':
                pass
        elif line_parts[0] == 'dir':
            node_name = line_parts[1] 
            current_node.add_child('dir',node_name, 0)
        else:
            node_size = int(line_parts[0])
            node_name = line_parts[1]
            current_node.add_child('file',node_name, node_size)

    return root_node
    

def main():
    root_node = process_input()
    
    print(f'Part one answer: {root_node.part_one_answer(0)}')

    space_needed = root_node.return_size() - 40000000
    print(f'Part two answer: {root_node.part_two_answer(space_needed, 0)}')

if __name__ == "__main__":
    start_time = time.time()
    main()
    end_time = time.time()
    print(f'All done! Total time was {(end_time - start_time):.3f} seconds.')
