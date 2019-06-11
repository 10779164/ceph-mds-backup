import os
import logging
from  executor import execute

log_dir=os.path.join('/var/log/mds_backup')

if not os.path.exists(log_dir):
    os.makedirs(log_dir)

logger = logging.getlogger()
logging.debug('DEBUG')


