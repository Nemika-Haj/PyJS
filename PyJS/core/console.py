__all__ = (
    "log"
)

def log(*other) -> None:
    print(' '.join([str(i) for i in other]))