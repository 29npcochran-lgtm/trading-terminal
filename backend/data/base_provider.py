"""
Market data provider base class
"""

from abc import ABC, abstractmethod
from typing import Dict, List, Any, Optional
from datetime import datetime
import pandas as pd


class BaseDataProvider(ABC):
    """Base class for market data providers"""
    
    def __init__(self, api_key: str, **kwargs):
        self.api_key = api_key
        self.session = None
        self.config = kwargs
        
    @abstractmethod
    async def get_quote(self, symbol: str) -> Dict[str, Any]:
        """Get current quote for a symbol"""
        pass
    
    @abstractmethod
    async def get_historical_data(
        self, 
        symbol: str, 
        timeframe: str,
        start_date: datetime,
        end_date: datetime
    ) -> pd.DataFrame:
        """Get historical OHLCV data"""
        pass
    
    @abstractmethod
    async def get_trades(
        self,
        symbol: str,
        limit: int = 100
    ) -> List[Dict[str, Any]]:
        """Get recent trades (order flow)"""
        pass
    
    @abstractmethod
    async def get_order_book(self, symbol: str) -> Dict[str, Any]:
        """Get current order book (DOM)"""
        pass
    
    @abstractmethod
    async def connect(self):
        """Connect to data provider"""
        pass
    
    @abstractmethod
    async def disconnect(self):
        """Disconnect from data provider"""
        pass
    
    @abstractmethod
    async def subscribe_quotes(self, symbols: List[str], callback):
        """Subscribe to real-time quotes"""
        pass
    
    @abstractmethod
    async def subscribe_trades(self, symbols: List[str], callback):
        """Subscribe to real-time trades"""
        pass
