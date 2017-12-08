#!/usr/bin/env python3
# -*- coding: utf-8 -*-
__author__ = 'leonard tia'

import asyncio
import conf.config
import www.ORM.models as md
import www.ORM.orm as orm

loop = asyncio.get_event_loop()
db_conf = conf.config.configs.get('db')
async def main():
    await orm.create_pool(loop=loop,**db_conf)
    u = md.User(name='leonard_tia',email='test@example.com',passwd='123456',image='about:blank')
    await u.save()

    s = md.User()
    aa = await s.findAll(where='name=\'leonard_tia\'',orderBy='created_at desc')
    for a in aa:
        print(a)
loop.run_until_complete(main())