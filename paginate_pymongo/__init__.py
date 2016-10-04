"""Enhances the paginate.Page class to work with pymongo cursors"""

import paginate


class PyMongoWrapper(object):
    """Wrapper class to access elements of the pymongo Cursor object"""
    def __init__(self, obj):
        self.obj = obj

    def __getitem__(self, range):
        if not isinstance(range, slice):
            raise Exception('__getitem__ without slicing not supported')
        offset_v = range.start
        limit = range.stop - range.start
        result = self.obj.skip(offset_v).limit(limit)
        return list(result)

    def __len__(self):
        return self.obj.count()


class PyMongoPage(paginate.Page):
    """A pagination page that deals with the pymongo cursor object."""

    # This class is a simple subclass of paginate.Page, but instantiates
    #   the class with the PyMongoWrapper
    def __init__(self, *args, **kwargs):
        super(PyMongoPage, self).__init__(*args, wrapper_class=PyMongoWrapper, **kwargs)
