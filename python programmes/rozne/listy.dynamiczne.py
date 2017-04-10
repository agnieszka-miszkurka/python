

class Node:
    def __init__(self, name, score):
        self.name = name
        self.score = score
        self.next = None
        self.prev = None

    def __str__(self):
        return str(self.name)

    def __int__(self):
        return int(self.score)

class DoublyLinkedList:

    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def addAtTheBegginig(self, name, score):
        n = Node(name, score)
        n.prev = None
        n.next = self.head
        self.head = n
        self.size += 1
        if not self.tail:
            self.tail = n
        else:
            n.next.prev = n

    def addAtTheEnd(self, name, score):
        n = Node(name, score)
        n.next = None
        n.prev = self.tail
        self.tail = n
        self.size += 1
        if not self.head:
            self.head = n
        else:
            n.prev.next = n

    def addAtTheGivenPosition(self):
        print("Please specify a position of a new node, choose from 1 to", self.size +1, ": ")
        position = int(input())
        if position > (self.size + 1) or position < 1:
            print("There is no such position!")
        else:
            name = input("Please specify a last name of a student: ")
            score = int(input("Please specify student's score: "))
            if position == 1:
                ll.addAtTheBegginig(name, score)
            elif position == self.size + 1:
                ll.addAtTheEnd(name, score)
            else:
                iterator = self.head
                for i in range(position-1):
                    iterator = iterator.next
                n = Node(name, score)
                n.prev = iterator.prev
                n.next = iterator
                self.size += 1
                iterator.prev.next = n
                iterator.prev = n

    def removeFromTheBeggining(self):
        n = self.head
        n.next.prev = None
        self.head = n.next
        self.size -= 1

    def removeFromTheEnd(self):
        n = self.tail
        n.prev.next = None
        self.tail = n.prev
        self.size -= 1


    def printFromTheBeggining(self):
        n = self.head
        while n:
            print (n.name, n.score)
            n = n.next

    def printFromTheEnd(self):
        n = self.tail
        while n:
            print (n.name, n.score)
            n = n.prev

    def findTheHighestScore(self):
        n = self.head
        highest_score = n.score
        name_of_best_student = n.name
        while n:
            if n.score > highest_score:
                highest_score = n.score
                name_of_best_student = n.name
            n = n.next
        print("\nThe highest score belongs to", name_of_best_student)

#tworzymy liste
ll = DoublyLinkedList()
#dodajemy 2 elementy na poczatku
ll.addAtTheBegginig("Kowalski",14)
ll.addAtTheBegginig("Nowak",12)
#dodajemy 3 elementy na koncu
ll.addAtTheEnd("Stoch",2)
ll.addAtTheEnd("Drabina",9)
ll.addAtTheEnd("Mruga",11)
#dodajemy dowolny element na dowolnej pozycji
ll.addAtTheGivenPosition()
#usuwamy z poczatku
ll.removeFromTheBeggining()
#usuwamy z konca
ll.removeFromTheEnd()
print("\nLista od poczatku do konca: ")
#drukujemy od poczatku listy
ll.printFromTheBeggining()
print("\nLista od konca:")
ll.printFromTheEnd()
#szukamy najwyzszego wyniku
ll.findTheHighestScore()
