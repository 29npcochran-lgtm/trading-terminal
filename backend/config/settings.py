"""Application configuration and constants."""

import os
from typing import Dict, Any

# Chart Configuration
CHART_CONFIG = {
    'background': '#000000',
    'grid': '#1a1a1a',
    'axis': '#5f5f5f',
    'text': '#ffffff',
    'bull_candle': '#00C853',
    'bear_candle': '#FF3D57',
    'volume': '#808080',
    'selection': '#3FA9F5',
    'crosshair': '#777777',
}

# Extended Hours Configuration
EXTENDED_HOURS_CONFIG = {
    'premarket_start': '04:00',
    'premarket_end': '09:30',
    'afterhours_start': '16:00',
    'afterhours_end': '20:00',
    'color': '#FFD54F',
    'opacity': 0.15,
}

# Timeframe Configuration
TIMEFRAMES = ['1m', '2m', '5m', '15m', '30m', '1H', '4H', '1D', '1W']

# Default Indicators
DEFAULT_INDICATORS = [
    {
        'type': 'volume_profile',
        'name': 'Fixed Range Volume Profile',
        'config': {
            'range': 'hourly',
            'display': ['POC', 'VAH', 'VAL', 'histogram']
        }
    },
    {
        'type': 'volume_profile',
        'name': 'Visible Range Volume Profile',
        'config': {
            'range': 'dynamic',
            'display': ['POC', 'VAH', 'VAL']
        }
    },
    {
        'type': 'choppiness_index',
        'name': 'Choppiness Index',
        'config': {
            'length': 14,
            'thresholds': [38.2, 61.8]
        }
    },
    {
        'type': 'macd',
        'name': 'MACD',
        'config': {
            'fast': 12,
            'slow': 26,
            'signal': 9,
            'display': ['histogram', 'signal', 'macd_line']
        }
    },
    {
        'type': 'rsi',
        'name': 'RSI',
        'config': {
            'length': 14,
            'thresholds': [70, 30]
        }
    },
    {
        'type': 'volume_ratio',
        'name': 'Volume Ratio',
        'config': {
            'formula': 'buy_volume / sell_volume',
            'display': 'histogram'
        }
    },
]

# Volume Indicators
VOLUME_INDICATORS = [
    'volume',
    'relative_volume',
    'volume_oscillator',
    'volume_delta',
    'volume_ratio',
    'volume_momentum',
    'volume_roc',
    'volume_trend',
    'mfi',
    'obv',
    'vwap',
    'anchored_vwap',
    'vwma',
    'pvt',
    'ad',
    'cmf',
    'eom',
    'klinger',
    'force_index',
    'nvi',
    'pvi',
    'di',
    'vwmacd',
]

# Trend Indicators
TREND_INDICATORS = [
    'ema',
    'sma',
    'hull_ma',
    'supertrend',
    'bollinger_bands',
    'keltner_channels',
    'donchian',
    'ichimoku',
    'parabolic_sar',
    'linear_regression',
    'regression_channel',
]

# Momentum Indicators
MOMENTUM_INDICATORS = [
    'rsi',
    'stochastic',
    'cci',
    'momentum',
    'roc',
    'williams_r',
    'aroon',
    'adx',
]

# Market Structure Detection
MARKET_STRUCTURE_CONFIG = {
    'detect_swing_highs': True,
    'detect_swing_lows': True,
    'detect_bos': True,
    'detect_mss': True,
    'detect_choc': True,
    'detect_liquidity_pools': True,
    'detect_fvg': True,
    'detect_order_blocks': True,
    'detect_breaker_blocks': True,
    'detect_premium_discount': True,
}

# Chart Types
CHART_TYPES = [
    'candlestick',
    'hollow_candles',
    'ohlc',
    'line',
    'area',
    'heikin_ashi',
    'renko',
    'range_bars',
    'point_figure',
    'kagi',
    'tick_charts',
    'volume_bars',
    'delta_bars',
    'footprint_bars',
]

# Refresh Rates (milliseconds)
REFRESH_RATES = {
    'trades': 0,  # Immediate
    'dom': 0,  # Immediate
    'heatmap': 0,  # Tick-by-tick
    'volume': 0,  # Tick-by-tick
    'indicators': 0,  # Live
    'charts': 3000,  # 3 seconds max
}

# Data Provider Configuration
DATA_PROVIDERS = {
    'polygon': {
        'name': 'Polygon.io',
        'tier': 1,
        'api_key_env': 'POLYGON_API_KEY',
        'base_url': 'https://api.polygon.io',
    },
    'databento': {
        'name': 'Databento',
        'tier': 1,
        'api_key_env': 'DATABENTO_API_KEY',
        'base_url': 'https://api.databento.com',
    },
    'alpaca': {
        'name': 'Alpaca',
        'tier': 1,
        'api_key_env': 'ALPACA_API_KEY',
        'secret_key_env': 'ALPACA_SECRET_KEY',
        'base_url': 'https://paper-api.alpaca.markets',
    },
    'dxfeed': {
        'name': 'dxFeed',
        'tier': 1,
        'api_key_env': 'DXFEED_API_KEY',
    },
    'interactive_brokers': {
        'name': 'Interactive Brokers',
        'tier': 1,
        'account_env': 'IB_ACCOUNT',
        'api_key_env': 'IB_API_KEY',
    },
    'binance': {
        'name': 'Binance',
        'tier': 1,
        'api_key_env': 'BINANCE_API_KEY',
        'secret_key_env': 'BINANCE_SECRET_KEY',
        'base_url': 'https://api.binance.com',
    },
    'coinbase': {
        'name': 'Coinbase Advanced',
        'tier': 1,
        'api_key_env': 'COINBASE_API_KEY',
        'secret_key_env': 'COINBASE_SECRET_KEY',
        'base_url': 'https://api.coinbase.com',
    },
}

# Supported Assets
ASSETS = {
    'stocks': {'name': 'US Stocks', 'enabled': True},
    'etfs': {'name': 'ETFs', 'enabled': True},
    'futures': {'name': 'Futures', 'enabled': True},
    'crypto': {'name': 'Cryptocurrency', 'enabled': True},
    'forex': {'name': 'Forex', 'enabled': False},
    'options': {'name': 'Options', 'enabled': False},
}

# Performance Configuration
PERFORMANCE_CONFIG = {
    'target_fps': 144,
    'min_fps': 60,
    'max_workers': int(os.getenv('MAX_WORKERS', 8)),
    'cache_expiry': int(os.getenv('CACHE_EXPIRY', 300)),
    'enable_gpu_acceleration': True,
    'async_indicators': True,
    'lazy_loading': True,
}

# Alert Configuration
ALERT_TYPES = [
    'price',
    'indicator',
    'delta',
    'volume',
    'dom',
    'liquidity',
    'heatmap',
    'footprint',
    'time',
]

ALERT_ACTIONS = [
    'webhook',
    'email',
    'desktop_notification',
    'sound',
    'log',
]

# Drawing Tools
DRAWING_TOOLS = [
    'cursor',
    'crosshair',
    'trend_line',
    'ray',
    'horizontal_line',
    'vertical_line',
    'parallel_channel',
    'rectangle',
    'circle',
    'ellipse',
    'arrow',
    'brush',
    'text',
    'anchored_vwap',
    'fibonacci_retracement',
    'fibonacci_extension',
    'pitchfork',
    'gann_fan',
    'risk_reward',
    'measurement',
]

# Screener Configuration
SCREENER_FILTERS = [
    'volume',
    'float',
    'gap',
    'atr',
    'sector',
    'relative_strength',
    'news',
    'options_activity',
    'market_cap',
    'exchange',
    'country',
    'liquidity',
]

# Database Configuration
DATABASE_CONFIG = {
    'driver': os.getenv('DATABASE_DRIVER', 'sqlite'),
    'url': os.getenv('DATABASE_URL', 'sqlite:///trading.db'),
    'echo': os.getenv('FLASK_ENV') == 'development',
    'pool_size': 10,
    'max_overflow': 20,
}

# Redis Configuration
REDIS_CONFIG = {
    'url': os.getenv('REDIS_URL', 'redis://localhost:6379/0'),
    'decode_responses': True,
    'socket_connect_timeout': 5,
    'socket_timeout': 5,
}

# WebSocket Configuration
WEBSOCKET_CONFIG = {
    'max_connections': 1000,
    'heartbeat_interval': 30,
    'heartbeat_timeout': 60,
    'message_queue_size': 100,
}
