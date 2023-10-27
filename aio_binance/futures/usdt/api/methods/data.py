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
    
    async def get_data_top_long_short_account_ratio(self,
                                                    symbol: str,
                                                    period: str,
                                                    **kwargs) -> dict:
        """**Top Trader Long/Short Ratio (Accounts)**
        Notes:
            ``GET /futures/data/topLongShortAccountRatio``
        See Also:
            https://developers.binance.com/docs/binance-trading-api/futures#top-trader-longshort-ratio-accounts
        Args:
            symbol: the trading symbol.
            period: period to fetch
        Keyword Args:
            TODO
        """
        return await self._fetch(
            'GET',
            'get_data_top_long_short_account_ratio',
            '/futures/data/topLongShortAccountRatio',
            symbol=symbol,
            period=period,
            **self._to_api(kwargs)
        )
    
    async def get_data_top_long_short_position_ratio(self,
                                                     symbol: str,
                                                     period: str,
                                                     **kwargs) -> dict:
        """**Top Trader Long/Short Ratio (Positions)**
        Notes:
            ``GET /futures/data/topLongShortPositionRatio``
        See Also:
            https://developers.binance.com/docs/binance-trading-api/futures#top-trader-longshort-ratio-positions
        Args:
            symbol: the trading symbol.
            period: period to fetch
        Keyword Args:
            TODO
        """
        return await self._fetch(
            'GET',
            'get_data_top_long_short_position_ratio',
            '/futures/data/topLongShortPositionRatio',
            symbol=symbol,
            period=period,
            **self._to_api(kwargs)
        )
    
    async def get_data_long_short_ratio(self,
                                        symbol: str,
                                        period: str,
                                        **kwargs) -> dict:
        """**Long/Short Ratio**
        Notes:
            ``GET /futures/data/globalLongShortAccountRatio``
        See Also:
            https://developers.binance.com/docs/binance-trading-api/futures#longshort-ratio
        Args:
            symbol: the trading symbol.
            period: period to fetch
        Keyword Args:
            TODO
        """
        return await self._fetch(
            'GET',
            'get_data_long_short_ratio',
            '/futures/data/globalLongShortAccountRatio',
            symbol=symbol,
            period=period,
            **self._to_api(kwargs)
        )
    
    async def get_data_taker_long_short_ratio(self,
                                              symbol: str,
                                              period: str,
                                              **kwargs) -> dict:
        """**Taker Buy/Sell Volume**
        Notes:
            ``GET /futures/data/takerlongshortRatio``
        See Also:
            https://developers.binance.com/docs/binance-trading-api/futures#taker-buysell-volume
        Args:
            symbol: the trading symbol.
            period: period to fetch
        Keyword Args:
            TODO
        """
        return await self._fetch(
            'GET',
            'get_data_taker_long_short_ratio',
            '/futures/data/takerlongshortRatio',
            symbol=symbol,
            period=period,
            **self._to_api(kwargs)
        )