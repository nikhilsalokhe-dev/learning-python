from typing import List, Tuple, Dict, Union

numbers: List[int] = [1, 2, 3, 4, 5.6, 7, 8, 9]  # List of integers

person: Tuple[str, int] = ("Name", 20)  # Tuple of string and integer

scores: Dict[str, int] = {
    "Student1": 95,
    "Student2": 72,
}  # Dictionary of string and integer

identifier: Union[int, str] = "ID123"  # Union type
identifier = 98765  # Still valid because 'int' is part of the Union!
