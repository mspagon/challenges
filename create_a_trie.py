from typing import Optional


class Node:
    def __init__(self, letter=Optional[str]):
        self.letter = letter
        self.children = {}  # type: dict[str, 'Node']
        self.valid_word = False

    def add_child(self, node: 'Node'):
        self.children[node.letter] = node

    def has_child(self, letter: str):
        return True if letter in self.children else False

    def get_child(self, letter: str):
        return self.children[letter] if letter in self.children else None


class Trie:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = Node()
        self.length = 0

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        current_node = self.root
        for char in word:
            child_node = current_node.get_child(char)
            if child_node is not None:
                current_node = child_node
            else:
                new_node = Node(char)
                current_node.add_child(new_node)
                current_node = new_node
        current_node.valid_word = True

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        current_node = self.root
        for char in word:
            child_node = current_node.get_child(char)
            if child_node is None:
                return False
            else:
                current_node = child_node

        if current_node.valid_word:
            return True
        else:
            return False

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        current_node = self.root
        for char in prefix:
            child_node = current_node.get_child(char)
            if child_node is None:
                return False
            else:
                current_node = child_node
        return True


def pretty(some_node, indent=0):
    seperator = ['└──'] if indent > 0 else ['']
    for _ in range(indent - 1):
        seperator.insert(0, '    ')
    seperator = ''.join(seperator)

    for letter, node in some_node.children.items():
        valid_indicator = '*' if node.valid_word else ''
        print(seperator + str(letter.upper()) + valid_indicator)
        if isinstance(node, Node):
            pretty(node, indent+1)


if __name__ == '__main__':
    t = Trie()
    t.insert('hello')
    t.insert('hell')
    t.insert('help')
    t.insert('ace')
    t.insert('held')
    t.insert('hold')
    pretty(t.root)
