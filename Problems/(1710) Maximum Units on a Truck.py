class Solution:
    # O(nLogn) Time O(1) Space
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        boxTypes.sort( key= lambda unit:unit[1],reverse=True)

        units = 0
        for i in boxTypes:
            if truckSize <= 0: return units
            units+= min(truckSize , i[0])*i[1]
            truckSize -= i[0]
        return units