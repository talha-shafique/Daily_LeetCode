class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l,r=0,1 #l=for buying r=for selling
        maxP=0

        while r<len(prices):
            # A profitable transection is a one which has low buying price
            # and high selling price.
            if prices[l]<prices[r]:
                profit=prices[r]-prices[l]
                maxP=max(maxP, profit)
            # And if there is a price leser than our previous buying price
            # then we will update it to that price as we want to keep our
            # buying price at the lowest to maximize our profit.
            else:
                l=r
            r=r+1
        return maxP



            



            



































        # min_price=float('inf')
        # max_profit=0

        # for l in range(len(prices)-1):
        #     print('l:',prices[l])
        #     r=l+1
        #     print('r:',prices[r])
            
        #     min_price=min(prices[l],min_price)
        #     if l >0 and min_price==prices[l-1]:
        #         continue
        #     print('min_price',min_price)
        #     while r<len(prices):

        #         # print('r:',r,'in loop of l:',l)
        #         # if r>l+1 and prices[r] == max_profit:
        #         #     continue
        #         # if prices[r]>min_price:
        #         #     profit=prices[r]-min_price
        #         #     max_profit=max(profit,max_profit)
        #         #     print('max_profit',max_profit)
        #         # r+=1
        # return max_profit





            

            




        