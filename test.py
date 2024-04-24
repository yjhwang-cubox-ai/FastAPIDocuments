from typing import Annotated


name = Annotated[str, "first letter is capital"]

print(name[0])