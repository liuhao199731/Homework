'''
大数加法
'''

# list1 = [7,7,7]
# list2 = [8,8,8,8,8,8,8]

list1 = [7,7,7,7,7]
list2 = [8,8,8,8]

def Sum_l1_l2(list1,list2):
    len1 = len(list1)
    len2 = len(list2)

    # 两种情况，第一种：数组1的长度小于数组2的长度，第二种情况反过来。
    if len1 <= len2:
        # 较大和较小的数组长度
        minlen = len1
        maxlen = len2
        # 新建立一个与较长数组长度一致的全为0的数组
        new_maxlen = []
        for i in range(maxlen):
            new_maxlen.append(0)
        # 数组的后一部分保存较短数组的值
        new_maxlen[-minlen:] = list1
        # 开始计算相加,由于存在进位可能，因此最大长度要+1
        for i in range(1,maxlen+1):
            # 从数组尾部开始算，对应位置相加
            i = -i
            temp = new_maxlen[i] + list2[i]
            # 如果和大于10，则保留个位数值，并进位
            if temp >= 10:
                temp = temp - 10
                new_maxlen[i] = temp
                # 数组的第一位需要进位，进位后超出数组范围，因此在数组前插入数值
                if i == -maxlen:
                    new_maxlen.insert(0,1)
                # 数组的第二位至最后一位需要进位，且没有超出数组范围，则直接在新建的数组的前一位加1
                else:
                    new_maxlen[i-1] = new_maxlen[i-1] + 1
            # 不需进位的情况
            else:
                new_maxlen[i] = temp

    # 第二种情况
    else:
        minlen = len2
        maxlen = len1
        new_maxlen = []
        for i in range(maxlen):
            new_maxlen.append(0)
        new_maxlen[-minlen:] = list2
        for i in range(1, maxlen + 1):
            i = -i
            temp = new_maxlen[i] + list1[i]
            if temp >= 10:
                temp = temp - 10
                new_maxlen[i] = temp
                if i == -maxlen:
                    new_maxlen.insert(0, 1)
                else:
                    new_maxlen[i - 1] = new_maxlen[i - 1] + 1
            else:
                new_maxlen[i] = temp
    return new_maxlen

#测试
print (Sum_l1_l2(list1,list2))
