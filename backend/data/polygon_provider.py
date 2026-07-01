"""
Polygon.io data provider implementation
"""

import os
import aiohttp
from typing import Dict, List, Any, Optional
from datetime import datetime
import pandas as pd
from backend.data.base_provider import BaseDataProvider


class PolygonDataProvider(BaseDataProvider):
    """Polygon.io market data provider"""
    
    def __init__(self):
        api_key = os.getenv('POLYGON_API_KEY')
        super().__init__(api_key)
        self.base_url = 'https://api.polygon.io'
        
    async def get_quote(self, symbol: str) -> Dict[str, Any]:
        """Get current quote using Polygon.io"""
        url = f'{self.base_url}/v3/quotes/{symbol}'
        params = {'apikey': self.api_key}
        
        async with aiohttp.ClientSession() as session:
            async with session.get(url, params=params) as resp:
                if resp.status == 200:
                    data = await resp.json()
                    return data.get('result', {})
                return {}
    
    async def get_historical_data(
        self,
        symbol: str,
        timeframe: str,
        start_date: datetime,
        end_date: datetime
    ) -> pd.DataFrame:
        """Get historical OHLCV data from Polygon.io"""
        url = f'{self.base_url}/v2/aggs/ticker/{symbol}/range/1/{timeframe}'
        params = {
            'from': start_date.strftime('%Y-%m-%d'),
            'to': end_date.strftime('%Y-%m-%d'),
            'apikey': self.api_key
        }
        
        async with aiohttp.ClientSession() as session:
            async with session.get(url, params=params) as resp:
                if resp.status == 200:
                    data = await resp.json()
                    results = data.get('results', [])
                    df = pd.DataFrame(results)
                    df['t'] = pd.to_datetime(df['t'], unit='ms')
                    return df
                return pd.DataFrame()
    
    async def get_trades(
        self,
        symbol: str,
        limit: int = 100
    ) -> List[Dict[str, Any]]:
        """Get recent trades from Polygon.io"""
        url = f'{self.base_url}/v3/trades/{symbol}'
        params = {
            'limit': limit,
            'apikey': self.api_key
        }
        
        async with aiohttp.ClientSession() as session:
            async with session.get(url, params=params) as resp:
                if resp.status == 200:
                    data = await resp.json()
                    return data.get('results', [])
                return []
    
    async def get_order_book(self, symbol: str) -> Dict[str, Any]:
        """Get current order book (DOM)"""
        # Polygon doesn't provide order book directly
        # This would need a different provider or aggregation
        return {'bids': [], 'asks': []}
    
    async def connect(self):
        """Connect to Polygon.io"""
        self.session = aiohttp.ClientSession()
    
    async def disconnect(self):
        """Disconnect from Polygon.io"""
        if self.session:
            await self.session.close()
    
    async def subscribe_quotes(self, symbols: List[str], callback):
        """Subscribe to real-time quotes - requires WebSocket"""
        # Would use Polygon.io WebSocket API
        pass
    
    async def subscribe_trades(self, symbols: List[str], callback):
        """Subscribe to real-time trades - requires WebSocket"""
        # Would use Polygon.io WebSocket API
        pass
