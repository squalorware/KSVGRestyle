import sys

from .post_commit import post_commit
from .prepare_commit_msg import prepare_commit_msg


def cz_prepare_msg() -> None:
    with open("/dev/tty") as tty:
        sys.stdin = tty
        exit(prepare_commit_msg(sys.argv[1]))


def cz_post_commit() -> None:
    exit(post_commit())
