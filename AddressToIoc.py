import sys

"""go to Args source folder"""
"""open comand prompt"""
'''type python 1 2 3'''

if __name__ == "__main__":

    """read the system args"""
    if len(sys.argv) > 0:
        for i in range(len(sys.argv)):
            arg = sys.argv[i]
            if arg == "OPC" or arg =="REST":
                print(F'RUNNING WITH PROFILE: {arg}')


