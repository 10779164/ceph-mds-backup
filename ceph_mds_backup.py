#!/usr/bin/python
import logging
import time
from  executor import execute

time_fmt=time.strftime('%Y%m%d%H%M%S')
backup_dest='/backup/ceph/mds/'
file_name='mds_backup_'+str(time_fmt)
cmd="cephfs-journal-tool --rank=cephfs:0 journal export "+backup_dest+file_name


class Logger():
    def __init__(self, logname, loglevel, logger):
	self.logger = logging.getLogger(logger)
	self.logger.setLevel(logging.DEBUG)

	fh = logging.FileHandler(logname)
	fh.setLevel(logging.DEBUG)

	formatter = logging.Formatter('%(asctime)s -- %(name)s -- %(levelname)s --- %(message)s')
	fh.setFormatter(formatter)

	self.logger.addHandler(fh)
	
    def getlog(self):
	return self.logger


if __name__=='__main__':
    logger=Logger(logname='/var/log/ceph_mds_backup.log', loglevel=1, logger="ceph mds backup").getlog()
    try:
        execute(cmd)
        logger.info('OK')
    except Exception,e:
        logger.error(str(e))



