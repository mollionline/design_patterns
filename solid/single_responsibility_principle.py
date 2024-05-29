# SRP SOC

# Single Responsibility Principle
# - A class should only have one reason to change
# - Separation of concerns - different classes handling different, independent tasks/problems

class Journal:
    def __init__(self):
        self.entries = []
        self.count = 0

    def add_entry(self, text):
        self.count += 1
        self.entries.append(f'{self.count}: {text}')

    def remove_entry(self, pos):
        del self.entries[pos]

    def __str__(self):
        return '\n'.join(self.entries)

    # def save(self, filename):
    #     file = open(filename, 'w')
    #     file.write(str(self))
    #     file.close()
    #
    # def load(self, filename):
    #     pass
    #
    # def low_from_web(self, uri):
    #     pass


""" YOU shouldn't put too many responsibility to one class """


class PersistenceManager:
    @staticmethod
    def save_to_file(journal, filename):
        file = open(filename, 'w')
        file.write(str(journal))
        file.close()


j = Journal()
j.add_entry('I cried today')
j.add_entry('I ate a bug')

file = './journal.txt'
PersistenceManager.save_to_file(j, file)
print(f'Journal entries : \n{j}')

with open(file) as f:
    print(f.read())
