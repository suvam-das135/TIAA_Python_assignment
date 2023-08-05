class StringProcessor:
    def __init__(self):
        self.input_string = ""

    def getString(self):
        self.input_string = input("Enter a string: ")

    def printString(self):
        print(self.input_string.upper())

def testStringProcessor():
    # Create an instance of the StringProcessor class
    processor = StringProcessor()

    # Get a string from the console
    processor.getString()

    # Print the string in upper case
    processor.printString()

if __name__ == "__main__":
    testStringProcessor()
