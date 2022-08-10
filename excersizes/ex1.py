class Indenter:
    def __init__(self) -> None:
        self.indented = -1

    def __enter__(self) -> "Indenter":
        self.indented += 1
        return self

    def __exit__(self, exc_type, exc_value, exc_tb) -> None:
        self.indented -= 1

    def print(self, text: str) -> None:
        print("    " * self.indented + text)


with Indenter() as indent:
    indent.print("Hi")
    with indent:
        indent.print("Talk is Cheap!")
        with indent:
            indent.print("Show me the Code...")
    indent.print("Torvalds")
