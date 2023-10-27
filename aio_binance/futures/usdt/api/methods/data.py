class Data:

    async def get_data_open_interest_hist(self,
                                          symbol: str,
                                          period: str,
                                          **kwargs) -> dict:
        """**Open Interest Statistics**
        Notes:
            ``GET /futures/data/openInterestHist``
        See Also:
            https://developers.binance.com/docs/binance-trading-api/futures#open-interest-statistics
        Args:
            symbol: the trading symbol.
            period: period to fetch
        Keyword Args:
            TODO
        """
        return await self._fetch(
            'GET',
            'get_data_open_interest_hist',
            '/futures/data/openInterestHist',
            symbol=symbol,
            period=period,
            **self._to_api(kwargs)
        )