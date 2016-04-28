import os
import time

source = ['/Users/puronglong/Desktop/demo']

target_dir = '/Users/puronglong/Desktop/'

target = target_dir + time.strftime('%Y%m%d%H%M%S') + '-demo' + '.zip'

zip_command = "zip -qr '%s' %s" %(target, ' '.join(source))

if os.system(zip_command) == 0:
	print 'Successful backup to', target

else:
	print 'backup Failed.'

