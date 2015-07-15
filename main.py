#!/usr/bin/env python

import logging
from logging import StreamHandler
from loggerformatter import NewFormatter


Logger = logging.getLogger('logger.test')

Handler = StreamHandler()
Handler.setFormatter(NewFormatter())

Logger.addHandler(Handler)
Logger.setLevel(logging.DEBUG)


class Obj(object):
    def __init__(self):
        self.first_name = 'Balthazar'
        self.last_name = 'Picsou'


if __name__ == "__main__":
    print('-- running main')
    msg = 'test int({!s}), float({:.2f}), attribute({obj.first_name} {obj.last_name})'  # NOQA
    obj = Obj()
    Logger.info(
        msg,
        int(42),
        float(42.128497),
        extra={
            'obj': obj,
        },
    )
    print('-- end main')
