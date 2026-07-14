"""
Week 1 Homework: Pure Python
=============================

Rules:
- Only built-in Python (lists, dicts, loops, functions)
- Fill all TODOs

Data shape (this is the contract every function below must work with
not just the sample data at the bottom of this file):

    student = {"name": "Sara", "scores": [82, 91, 76]}
    students = [student, ...]

Write every function so it works for ANY list of students in this shape,
not just the `students` list defined in main(). That's why the sample
data lives in main() instead of at the top of the file, the functions
above it should never need to look at it.
"""


def average(scores: list[float]) -> float:
    """Return the average of a list of numbers.

    Args:
        scores: e.g. [82, 91, 76]

    Returns:
        The mean of scores, e.g. 83.0

    WORKED EXAMPLE: this one is done for you. Use it as the pattern
    (signature, docstring, TODO -> real code) for every function below.
    """
    return sum(scores) / len(scores)


def add_average_to_students(students: list[dict]) -> None:
    """Add key 'average' to each student dict, in place.

    Args:
        students: e.g. [{"name": "Sara", "scores": [82, 91, 76]}, ...]
                  Use the `average` function above, don't recompute
                  the mean by hand here.

    Returns:
        None. Modifies each dict in `students` by adding an "average" key,
        e.g. {"name": "Sara", "scores": [82, 91, 76], "average": 83.0}
    """
    # TODO
    pass


def top_student(students: list[dict]) -> str:
    """Return the name of the student with the highest average.

    Args:
        students: list of student dicts that already have an "average" key
                  (call add_average_to_students first).

    Returns:
        The student's name, e.g. "Niloofar"
    """
    # TODO
    pass


def passing_students(students: list[dict], threshold: float = 60) -> list[str]:
    """Return the names of students whose average is >= threshold.

    Args:
        students: list of student dicts that already have an "average" key.
        threshold: minimum passing average (default 60).

    Returns:
        List of names, in the same order as `students`,
        e.g. ["Sara", "Ali", "Niloofar"]
    """
    # TODO
    pass


def class_average(students: list[dict]) -> float:
    """Return the average of all students' averages.

    Args:
        students: list of student dicts that already have an "average" key.

    Returns:
        A single float, e.g. 75.4
    """
    # TODO
    pass


def print_report(students: list[dict]) -> None:
    """Print each student's name, average, and Pass/Fail status.

    Args:
        students: list of student dicts that already have an "average" key.
                  A student passes if average >= 60 (reuse passing_students
                  or the same threshold logic).

    Returns:
        None. Just prints one line per student, e.g.:
        Sara: 83.0 (Pass)
    """
    # TODO
    pass


def most_consistent_student(students: list[dict]) -> str:
    """Return the name of the student with the smallest score range (max - min).

    Args:
        students: e.g. [{"name": "Sara", "scores": [82, 91, 76]}, ...]

    Returns:
        The student's name, e.g. "Niloofar"
    """
    # TODO (optional)
    pass


def main() -> None:
    # Sample data used to try out and test the functions above.
    # Your functions must work for this list AND any other list of
    # students in the same shape, don't hardcode names or values.
    students = [
        {"name": "Sara", "scores": [82, 91, 76]},
        {"name": "Ali", "scores": [65, 70, 72]},
        {"name": "Niloofar", "scores": [95, 89, 92]},
        {"name": "Reza", "scores": [40, 45, 50]},
        {"name": "Maryam", "scores": [50, 55, 57]},
    ]

    add_average_to_students(students)

    print_report(students)

    print()
    print("Class average:", round(class_average(students), 1))
    print("Top student:", top_student(students))
    print("Passing students:", passing_students(students))

    assert round(average([10, 20, 30]), 1) == 20.0
    assert all("average" in s for s in students)
    assert top_student(students) == "Niloofar"
    assert passing_students(students) == ["Sara", "Ali", "Niloofar"]

    # A second, differently-shaped class (different size, names, score
    # counts). If your functions above only work for `students`, they'll
    # break here, that's the point of this check.
    other_class = [
        {"name": "Amir", "scores": [30, 20]},
        {"name": "Hana", "scores": [100, 98, 97, 95]},
        {"name": "Kian", "scores": [61]},
        {"name": "Leila", "scores": [45, 50]},
    ]

    add_average_to_students(other_class)

    print()
    print_report(other_class)
    print("Class average:", round(class_average(other_class), 1))
    print("Top student:", top_student(other_class))
    print("Passing students:", passing_students(other_class))

    assert top_student(other_class) == "Hana"
    assert passing_students(other_class) == ["Hana", "Kian"]

    print("\nAll good!")


if __name__ == "__main__":
    main()
