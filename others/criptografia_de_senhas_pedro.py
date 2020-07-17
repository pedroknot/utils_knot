from hashlib import md5, sha256
from sys import argv


def hash_md5(pwd):
    return md5(pwd.encode('utf-8')).hexdigest()


def hash_sha256(pwd):
    return sha256(pwd.encode('utf-8')).hexdigest()


if __name__ == '__main__':
    pwd = str(argv[1:])
    print(f'md5: {hash_md5(pwd)}')
    print(f'sha256: {hash_sha256(pwd)}')

