#coding=utf-8
import sys
import os
class Solution(object):
    def compareVersion(self, version1, version2):
        """
        :type version1: str
        :type version2: str
        :rtype: int
        """
        def is_zero(list):
            for i in range(0,len(list)):
                if list[i] != '0':
                    return False
            return True
        version1_list = version1.split('.')
        version2_list = version2.split('.')
        version1_length = len(version1_list)
        version2_length = len(version2_list)
        
        if version1_length > version2_length:
            tag = '1'
        elif version1_length < version2_length:
            tag = '2'
        else:
            tag = '3'

        length = min(version1_length, version2_length)
        for i in range(0,length):
            if int(version1_list[i]) > int(version2_list[i]):
                return 1
            elif int(version1_list[i]) < int(version2_list[i]):
                return -1

        if tag == '1':
            print version2_length, version1_list[version2_length:]
            if is_zero(version1_list[version2_length:]):
                return 0
            else:
                return 1
        elif tag == '2':
            if is_zero(version2_list[version1_length:]):
                return 0
            else:
                return -1
        elif tag == '3':
            return 0

if __name__ == '__main__':
    a = '1.0'
    b = '1.2'
    s = Solution()
    print s.compareVersion(a,b)
            
        
        
        
        
