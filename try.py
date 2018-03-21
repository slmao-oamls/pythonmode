
# try:
# 	print('try...')
# 	r=10/0
# 	print('result:',r)
# except ZeroDivisionError as e:
# 	print('except:',e)
# finally:
# 	print('finally...')

# print('end')

 # import logging


# def foo(s):
# 	return 10/int(s)

# def bar(s):
# 	return foo(s)*2

# def main():
# 	try:
# 		bar('0')
# 	except Exception as e:
# 		logging.exception(e)
	
# main()
# print('end')

import logging
logging.basicConfig(level=logging.INFO)
from functools import reduce


def str2num(s):
    return float(s)

def calc(exp):
    ss = exp.split('+')
    logging.info('ss=%s'% ss)
    ns = map(str2num, ss)
    return reduce(lambda acc, x: acc + x, ns)

def main():
	try:		
	    r = calc('100 + 200 + 345')
	    print('100 + 200 + 345 =', r)
	    r = calc('99 + 88 + 7.6')
	    print('99 + 88 + 7.6 =', r)
	except Exception as e:
		logging.exception(e)

main()