


def _take_input():
    VERTEX_PROMPT = "Enter your location: "
    K_PROMPT = "Enter k: " # i.e. to get the k closest vertices with cameras.
    VERTEX_RANGE = 6104 # PRECOND: must be an int > 0, representing # of vertices.
    def __take_location():
        try:
            location = input(VERTEX_PROMPT)
            if (isinstance(location,int)
                ) and (location in range(VERTEX_RANGE+1)):
                return location
            else:
                raise IOError
        except IOError:
            __take_location()
    def __take_k():
        try:
            k = input(K_PROMPT)
            if (isinstance(k,int)) and (k>0):
                return k
            else:
                raise IOError
        except IOError:
            __take_k()

    return __take_location(),__take_k()

def _output_paths():
    NO_PATHS_MSG = "Oops! Cannot help, Alice!!! Smile for the camera!"
    STUCK_HERE_MSG = "Oops! You're stuck here Alice!"


    # output for a given path
    print("Camera %: % Distance from your location: % \nShortest path:",end='')

    print("initial v")
    print(" --> %")


    print(NO_PATHS_MSG)
    print(STUCK_HERE_MSG)
    pass

def main():
    _EDGE_FILE = "edges.txt"
    _VERTEX_FILE = "vertices.txt"

    loc, k = _take_input()
    loc
    k


    with open(_VERTEX_FILE) as vf:
        pass

    with open(_EDGE_FILE) as ef:
        pass


if __name__=='__main__':
    main()
