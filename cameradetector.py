# By Matthew Jake Corpus Alix, ID 287 661 72.
# Last modified 20.05.18

from fixed_min_heap import FixedMinHeap

def _read_graph(camera_file, road_file):
    with open(camera_file) as f:
        for camera in f:



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
    _ROAD_FILE = "edges.txt"
    _CAMERA_FILE = "vertices.txt"
    _XSECTION_COUNT = 6105

    def _user_input():
        VERTEX_PROMPT = "Enter your location: "
        K_PROMPT = "Enter k: "  # i.e. to get the k closest vertices with cameras.

        def __take_location():
            try:
                location = input(VERTEX_PROMPT)
                if (isinstance(location, int)
                    ) and (location in range(_XSECTION_COUNT)):
                    return location
                else:
                    raise IOError
            except IOError:
                __take_location()

        def __take_k():
            try:
                k = input(K_PROMPT)
                if (isinstance(k, int)) and (k > 0):
                    return k
                else:
                    raise IOError
            except IOError:
                __take_k()

        return __take_location(), __take_k()

    intersections = [-2] * _XSECTION_COUNT  # '-2' = 'undiscovered'
    loc, k = _user_input()

    _read_graph(_CAMERA_FILE, _ROAD_FILE)



    loc
    k



if __name__=='__main__':
    main()

