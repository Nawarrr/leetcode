# Question
# https://leetcode.com/problems/defanging-an-ip-address/

# Descryption
# Given a valid (IPv4) IP address, return a defanged version of that IP address.
#A defanged IP address replaces every period "." with "[.]".

class Solution(object):
    def defangIPaddr(self, address):
        """
        :type address: str
        :rtype: str
        """
        return address.replace('.' , '[.]')