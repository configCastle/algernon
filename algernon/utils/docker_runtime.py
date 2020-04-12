"""Functional for docker-runtime utils."""


def in_docker():
    """
    Check docker or native application running.

    Returns:
        True if application in running in Docker, False if not.
    """
    with open('/proc/1/cgroup') as cgroup:
        for line in cgroup:
            if 'docker' in line:
                return True
        return False
