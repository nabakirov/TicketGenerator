def hashCompare(hash1, hash2):
    if len(hash1) != len(hash2):
        raise ValueError('Hashes seem to be different lengths')
    identical = True
    for index in range(0, len(hash1)):
        if hash1[index] != hash2[index]:
            identical = False
    return identical


def toHash(string):
    import hashlib
    return hashlib.sha256(string.encode()).hexdigest()