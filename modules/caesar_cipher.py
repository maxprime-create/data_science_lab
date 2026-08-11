"""Simple Caesar cipher utilities

Provides encrypt and decrypt helpers for uppercase A-Z and lowercase a-z. Leaves other chars unchanged.
"""

def _shift_char(c: str, shift: int) -> str:
    if 'a' <= c <= 'z':
        return chr((ord(c) - ord('a') + shift) % 26 + ord('a'))
    if 'A' <= c <= 'Z':
        return chr((ord(c) - ord('A') + shift) % 26 + ord('A'))
    return c


def encrypt(text: str, shift: int) -> str:
    return ''.join(_shift_char(c, shift) for c in text)


def decrypt(text: str, shift: int) -> str:
    return encrypt(text, -shift)


if __name__ == "__main__":
    t = "HELLO"
    s = 3
    print("Ciphertext:", encrypt(t, s))
