"""
API routes for market data
"""

from flask import Blueprint, jsonify, request
import asyncio
import os
from backend.data.polygon_provider import PolygonDataProvider

api_bp = Blueprint('api', __name__, url_prefix='/api')

# Initialize provider
polygon = PolygonDataProvider()


@api_bp.route('/market/quote/<symbol>', methods=['GET'])
def get_quote(symbol):
    """Get current quote for a symbol"""
    try:
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        quote = loop.run_until_complete(polygon.get_quote(symbol))
        loop.close()
        
        return jsonify({
            'symbol': symbol,
            'data': quote,
            'status': 'success'
        }), 200
    except Exception as e:
        return jsonify({
            'error': str(e),
            'status': 'error'
        }), 500


@api_bp.route('/market/trades/<symbol>', methods=['GET'])
def get_trades(symbol):
    """Get recent trades for a symbol"""
    try:
        limit = request.args.get('limit', 100, type=int)
        
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        trades = loop.run_until_complete(polygon.get_trades(symbol, limit))
        loop.close()
        
        return jsonify({
            'symbol': symbol,
            'trades': trades,
            'count': len(trades),
            'status': 'success'
        }), 200
    except Exception as e:
        return jsonify({
            'error': str(e),
            'status': 'error'
        }), 500


@api_bp.route('/market/stats/<symbol>', methods=['GET'])
def get_stats(symbol):
    """Get market statistics for a symbol"""
    return jsonify({
        'symbol': symbol,
        'volume': 0,
        'vwap': 0,
        'delta': 0,
        'status': 'initialized'
    }), 200


@api_bp.route('/indicators/list', methods=['GET'])
def list_indicators():
    """List available indicators"""
    indicators = [
        'sma', 'ema', 'rsi', 'macd', 'bbands',
        'atr', 'adx', 'obv', 'mfi', 'vpt',
        'volume_profile', 'choppiness', 'volume_ratio'
    ]
    return jsonify({
        'indicators': indicators,
        'count': len(indicators),
        'status': 'success'
    }), 200


@api_bp.route('/charts/types', methods=['GET'])
def chart_types():
    """Get available chart types"""
    types = [
        'candlestick', 'ohlc', 'line', 'area',
        'heikin_ashi', 'footprint', 'delta',
        'heatmap', 'volume_bars'
    ]
    return jsonify({
        'types': types,
        'count': len(types),
        'status': 'success'
    }), 200


@api_bp.route('/health', methods=['GET'])
def health():
    """Health check"""
    return jsonify({
        'status': 'healthy',
        'service': 'API',
        'version': '1.0.0'
    }), 200
