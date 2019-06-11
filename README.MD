# ceph mds backup

## Create backup directory
    # mkdir -p /backup/ceph/mds/

## Clone backup code
    # cd /root/ceph
    # git clone https://github.com/10779164/ceph-mds-backup.git
    
## Add crontab
    # crontab -e
#### 0 23 * * * /usr/bin/python /root/ceph/ceph-mds-backup/ceph_mds_backup.py

## Install module executor if need
    # pip install executor
