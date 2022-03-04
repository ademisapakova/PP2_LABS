class Rocket:
    def __init__(self, mark, destination, engines):
        # Write your code here
        # Hint: engines is an array of rocket's engines

    def launch(self):
        # Write your code here

    def getAbsolutePower(self):
        # Write your code here

    def addEngine(self, newEngine):
        # Write your code here


class Engine:
    def __init__(self, weight, e_class):
        # Write your code here

    def getPower(self):
    	# Write your code here
        # Power formula: g(9.81) multiplied by engine weight.
        
    
    def getClass(self):
        # Write your code here


def main():
    n = int(input())
    quazar_13 = Engine(12500, 'Quazar')
    R1 = Rocket('Falcon-1', 'Mars', quazar_13)
    for i in range(n):
        command = input()
        if command == 'Launch':
            print(R1.launch())
        elif command == 'getAbsolutePower':
            print(R1.getAbsolutePower())
        elif command == 'addEngine':
            quazar_14 = Engine(25000, 'QuazarL')
            R1.addEngine(quazar_14)
        elif command == 'showEngineClasses':
            print(f'Engines of {R1.mark} are:')
            for i in R1.engines:
                print(i.getClass())

if __name__ == '__main__':
    main()