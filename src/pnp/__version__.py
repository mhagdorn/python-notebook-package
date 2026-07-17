__all__ = ["__version_tuple__",
           "__version__"]


_major = 1
_minor = 0
_patch = 2

try:
    from ._version import __version__ as _v
    from ._version import __version_tuple__ as _vt
    have_version = True
except ModuleNotFoundError:
    have_version = False

if have_version:
    __version__ = _v
    __version_tuple__ = _vt
    if (__version_tuple__[0] != _major
        or __version_tuple__[1] != _minor
        or __version_tuple__[2] != _patch):  # noqa
        raise ValueError("version does notch match")
else:
    __version_tuple__ = (_major, _minor, _patch)
    __version__ = f"{_major}.{_minor}.{_patch}"
