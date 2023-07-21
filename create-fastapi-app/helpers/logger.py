import logging
import sys

logging.basicConfig(level=logging.INFO, handlers=[logging.StreamHandler(sys.stdout)],
                    format=f'%(asctime)s %(levelname)s | %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S')

logger = logging.getLogger("logger")
