"""Examples of inmports. """


from lessons import helpers

from lessons import helpers as hp 

from lessons.helpers import powerful, THE_ANSWER

def main() -> None: 
    print(helpers.powerful(2, 4))

    print(helpers.THE_ANSWER) 

    print(powerful(2,10))

    print(THE_ANSWER) 

    print(f"imports.py: {__name__}") 

if _name__ == "__main__"
main()