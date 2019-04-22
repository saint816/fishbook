"""
 Created by 七月 on 2018-1-29.
"""
__author__ = '七月'


class TradeInfo:
    def __init__(self, trades):
        self.total = 0
        self.trades = []
        self.__parse(trades)

    def __parse(self, trades):
        self.total = len(trades)
        self.trades = [self.__map_to_trade(gift) for gift in trades]

    def __map_to_trade(self, single):

        if single.create_datetime:
            time = single.create_datetime.strftime('%Y-%m-%d')
        else:
            time = '未知'

        return dict(
            user_name=single.user.nickname,
            time=time,
            id=single.id
        )
