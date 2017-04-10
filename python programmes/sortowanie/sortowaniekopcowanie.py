tab=[4,5,6,3,5,8,9,4]
start=len(tab)//2-1
print(tab)
def heapsort( aList ):
# convert aList to heap
    length = len( aList ) - 1    #dlugosc listy
    leastParent = length // 2       #ostatni rodzic
    for i in range ( leastParent, -1, -1 ):     #petla od ostatniego rodzica do pierwszego rodzica
        moveDown( aList, i, length )        #przekazujemy liste numer iteracji i dlugosc

        # flatten heap into sorted array
    for i in range ( length, 0, -1 ):
        if aList[0] > aList[i]:
            swap( aList, 0, i )
            moveDown( aList, 0, i - 1 )

def moveDown( aList, first, last ):
    largest = 2 * first + 1         #najwieksszy to  => lewe dziecko forst to nuemr aktualnego rodzica
    while largest <= last:          #dopoki wieksze dziecko jest mnijesze lub rowne dlugosci listy
# right child exists and is larger than left child
        if ( largest < last ) and ( aList[largest] < aList[largest + 1] ): #jesli ostatni jest prawym dxzeckiem i jest wikeszy od lewego
            largest += 1        #najwiekszy jest prawym dizeckiem

# right child is larger than parent
        if aList[largest] > aList[first]:
            swap( aList, largest, first )
# move down to largest child
            first = largest;
            largest = 2 * first + 1
        else:
            return # force exit 

def swap( A, x, y ):
    tmp = A[x]
    A[x] = A[y]
    A[y] = tmp
heapsort(tab)
print(tab)