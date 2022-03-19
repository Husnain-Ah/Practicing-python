# %02d means an integer, left padded with zeros up to 2 digits

from datetime import datetime
now = datetime.now()

print ('%02d/%02d/%04d' % (now.month, now.day, now.year))
#'%02d-%02d-%04d' would make dashes inbetween the dates