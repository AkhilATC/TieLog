# TieLog 🪢

The TieLog implements log rotation in Python based on time or size.The TieLog uses python logging, based on time/size log data is archived. That helps to free up space.	

## installation

```
python3 setup.py install
```

## Usage

```python3
# Size based log rotation
from TieLog.log_rotation import SizeBasedLogRotater as SBLR
logger = SBLR(size=100, rotate=5, filename="temp").as_logger
# Time based log rotation
from TieLog.log_rotation import TimeBasedLogRotator as TBLR
logger = TBLR(rotate=5, filename="temp", interval=10, time_span="m").as_logger

```
