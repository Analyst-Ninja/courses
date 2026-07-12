class Journal:
    def __init__(self):
        self.entries = []
        self.count = 0

    def add_entry(self, text: str):
        self.count += 1
        self.entries.append(f"{self.count} : {text}")

    def remove_entry(self, pos):
        del self.entries[pos]

    def __str__(self):
        return "\n".join(self.entries)

    # below are separate responsibilities
    # def save(self, filename: str):
    #     with open(file=filename, mode="w") as file:
    #         file.write(str(self))

    # def load(self):
    #     pass

    # def low_from_web(self, uri: str):
    #     pass


class PersistentManager:
    @staticmethod
    def save_to_file(journal: Journal, filename: str):
        with open(file=filename, mode="w") as file:
            file.write(str(journal))


j1 = Journal()
j1.add_entry("Today, I have started learning design patterns")
j1.add_entry("Currently, I am learning SOLID principles")
print(f"Journal Entries\n{j1}")
# j1.save("Journal.txt")

file = "Journal.txt"

# Saving the journals with the method from separately -> ensuring the SRP
PersistentManager.save_to_file(journal=j1, filename=file)

with open(file=file, mode="r") as fh:
    print(fh.read())


# Anti-pattern - One of the anti-patterns is God Object -> means all the functionalities in a single object -> not recommended
