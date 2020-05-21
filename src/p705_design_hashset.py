class MyHashSet:
    def __init__(self):
        self.m = {}

    def add(self, key: int) -> None:
        self.m[key] = True

    def remove(self, key: int) -> None:
        if key in self.m:
            del self.m[key]

    def contains(self, key: int) -> bool:
        return key in self.m
