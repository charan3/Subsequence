import random
import string

def generate_random_letters_file(filename, size: float) -> None:
    chars = ''.join(random.choice(string.ascii_lowercase) for _ in range(size))
    with open(filename, 'w') as f:
        f.write(chars)
    pass


generate_random_letters_file("random_letters_file.txt", 1024*1024*1024*3)  # 3GB = 1024*1024*1024*3
