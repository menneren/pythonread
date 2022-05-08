'''字符串劈分'''
s='hello world Python'
lst=s.split()
print(lst)
sl='hello|world|Python'
print(sl.split(sep='|'))
print(sl.split(sep='|',maxsplit=1))
print('---------------------------')
'''rsplit()右侧劈分'''
print(s.rsplit())
print(sl.rsplit('|'))
print(sl.rsplit(sep='|',maxsplit=1))


