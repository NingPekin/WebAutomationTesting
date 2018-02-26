from allpairspy import AllPairs
# username["valid","invalid","null","specific characters"]
# email["valid","invalid","specific characters"]
# password["valid","too short","null","specific characters"]
# button["done","cancel"]

parameters = \
    [
    ["testpairwise", "test","","!@#@#"],
    ["testpairwise@gmail.com", "test","!@$!@$!@%"],
    ["testpairwise", "0", "", "!$!@@#@#@%"],
    ["done", "cancel"]
    ]

print("PAIRWISE:")
for i, pairs in enumerate(AllPairs(parameters)):
    print("{:2d}: {}".format(i, pairs))

# output:
#  0: ['testpairwise', 'testpairwise@gmail.com', 'testpairwise', 'done']
#  1: ['test', 'test', '0', 'done']
#  2: ['', '!@$!@$!@%', '', 'done']
#  3: ['!@#@#', '!@$!@$!@%', '!$!@@#@#@%', 'cancel']
#  4: ['!@#@#', 'test', 'testpairwise', 'cancel']
#  5: ['', 'testpairwise@gmail.com', '!$!@@#@#@%', 'cancel']
#  6: ['test', 'testpairwise@gmail.com', '', 'cancel']
#  7: ['testpairwise', '!@$!@$!@%', '0', 'cancel']
#  8: ['!@#@#', 'testpairwise@gmail.com', '0', 'done']
#  9: ['testpairwise', 'test', '!$!@@#@#@%', 'done']
# 10: ['test', '!@$!@$!@%', 'testpairwise', 'done']
# 11: ['', 'test', 'testpairwise', 'done']
# 12: ['', 'test', '0', 'done']
# 13: ['test', 'test', '!$!@@#@#@%', 'done']
# 14: ['testpairwise', 'test', '', 'done']
# 15: ['!@#@#', 'test', '', 'done']