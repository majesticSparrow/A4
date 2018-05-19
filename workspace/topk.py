# By Matthew Jake Corpus Alix, ID 287 661 72, for FIT2004.
# Last modified 18.03.18

TIME_FILE = 'timeSpent.txt'
MAX_USER_DIGITS = 5               # only used to format output
DEBUGGING = False

def DEBUG_print(x):
    if DEBUGGING:
        print(x)


class UserEntry:
    def __init__(self, user, value):
        self.user = user
        self.value = value

    def __gt__(self, other):
        return self.value > other.value

    def __lt__(self, other):
        return self.value < other.value

    def __eq__(self, other):
        return self.value == other.value

    def __le__(self, other):
        return self.value <= other.value



class TopKMinHeap:
    def __init__(self, k):
        self.count = 0
        self.max_size = k
        self.array = [0]*(self.max_size+1) # One more than max_size due to
                                            # 1-based indexing.
        self.root = 1

    def add_element(self, key, item):
        entry = UserEntry(key, item)
        heap_member = True
        if self.count == self.max_size: # Heap is full

            cond_1 = (self.array[self.root] < entry)
            cond_2 = (self.array[self.root] == entry) and \
                        (self.array[self.root].user > entry.user)

            if cond_1 or cond_2:        # Conditions of heap membership

                self._swap(self.root, self.count)
                self.count -= 1
                self._sink(self.root)
            else:
                heap_member = False

        if heap_member:
            self.array[self.count+1] = entry
            self.count += 1

            self._rise(self.count)      # Move new member to correct position.

    def heapsort(self):
        return_array = [0]*self.count   # Must be size of current heap.

        i = 0
        while self.count > 0:           # For the whole heap:
            # 1. 'Pop' off the minimum into return_array, by swapping with last
            #       element and then decrementing the count.
            self._swap(self.root, self.count)
            return_array[i] = [self.array[self.count].value,
                                 self.array[self.count].user]
            self.count -= 1
            # 2. Re-establish the heap.
            self._sink(self.root)
            i += 1

        self.array = return_array.reverse()

        DEBUG_print("Return array END: " + str(return_array) + '\n' + 100 * '#')

        # 3. Return return_array in the required order.
        return return_array

    def _rise(self, k): # O(log k) time; element will rise for at most
                        # the height of the tree.

        DEBUG_print("confirm above is " + str(k) + '\n')

        while k > self.root and self.array[k] < self.array[k//2]:

            self._swap(k, k // 2)

            k //= 2

        while k > self.root and self.array[k] == self.array[k//2]:

            # Ensure parent with equal value has the larger ID.
            if self.array[k].user > self.array[k//2].user: #DO TESTTO

                DEBUG_print('CONFIRMED child is not root AND parent has equal' +
                              ' value to child, but parent has a lower userID.' +
                              '\nSWAPPING...\n')

                self._swap(k, k // 2)

                k //= 2
            else:
                DEBUG_print('CONFIRMED child is not root AND parent has equal' +
                      ' value to child, but parent still has the larger userID.' +
                      '\nNOT SWAPPING...\n')
                break

    def _swap(self, first, second):
        self.array[first], self.array[second] = \
            self.array[second], self.array[first]

    def _sink(self, k): # O(log k) time, for the same reason as _rise().
        while 2*k <= self.count: # Check that there are children

            child = self._smallest_child(k) # only smallest child is considered.
            cond_1 = self.array[k] > self.array[child]
            cond_2 = (self.array[k] == self.array[child]) and\
                             (self.array[k].user < self.array[child].user)

            if cond_1 or cond_2:
                self._swap(k, child)
                k = child

            elif self.array[k] < self.array[child]:
                break
            else:
                break

    def _smallest_child(self, k):
        # left child should be compared to parent
        if (2*k == self.count) or (self.array[2*k] < self.array[2*k+1]):
            return 2*k

        # right child should be compared to parent
        elif self.array[2*k] > self.array[2*k+1]:
            return 2*k + 1

        else: # they are equal

            # left has smaller userID and should be compared to parent
            if self.array[2*k].user < self.array[2*k+1].user:
                return 2*k+1

            else: # right must have smaller userID.
                return 2*k




def main():
    heap_size = int(input("\nEnter the value of k \n>>>"))
    heap = TopKMinHeap(heap_size)
    users = []
    with open(TIME_FILE) as f:
        for line in f:
            entry = line.split(':')
            if '\n' in entry[1]:
                entry[1] = entry[1][:-1]
            # print(entry)
            heap.add_element(int(entry[0]),int(entry[1]))
            users.append(entry)
        heap = heap.heapsort()

    print("These are the top " + str(heap_size) + " users: ")
    counter = 1
    for user in heap:
        print('#',str(counter),(len(str(heap_size))-len(str(counter)))*' ',
                ': User ID: ',user[1],(MAX_USER_DIGITS-len(str(user[1])))*' ',
                'Time spent: ',user[0])
        counter += 1

if __name__ == '__main__':
    main()



