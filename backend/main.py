#!/usr/bin/env python3
"""
Order Flow Professional - Main Application Entry Point

Institutional-grade market analysis platform with real-time order flow,
advanced charting, and professional-grade analytics.
"""

import os
import logging
from flask import Flask, jsonify
from flask_cors import CORS
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Configure logging
logging.basicConfig(
    level=os.getenv('LOG_LEVEL', 'INFO'),
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

def create_app():
    """Create and configure Flask application."""
    app = Flask(__name__)
    
    # Configuration
    app.config['JSON_SORT_KEYS'] = False
    app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # 16MB
    app.config['PROPAGATE_EXCEPTIONS'] = True
    
    # CORS
    CORS(app, resources={
        r"/api/*": {
            "origins": "*",
            "methods": ["GET", "POST", "PUT", "DELETE", "OPTIONS"],
            "allow_headers": ["Content-Type", "Authorization"],
            "max_age": 3600
        }
    })
    
    # Health check
    @app.route('/health', methods=['GET'])
    def health():
        return jsonify({
            'status': 'healthy',
            'version': '1.0.0',
            'service': 'Order Flow Professional'
        }), 200
    
    @app.route('/api/version', methods=['GET'])
    def version():
        return jsonify({
            'version': '1.0.0',
            'name': 'Order Flow Professional',
            'environment': os.getenv('FLASK_ENV', 'production')
        }), 200
    
    # Error handlers
    @app.errorhandler(404)
    def not_found(error):
        return jsonify({'error': 'Not found', 'status': 404}), 404
    
    @app.errorhandler(500)
    def internal_error(error):
        logger.error(f'Internal error: {error}')
        return jsonify({'error': 'Internal server error', 'status': 500}), 500
    
    @app.errorhandler(400)
    def bad_request(error):
        return jsonify({'error': 'Bad request', 'status': 400}), 400
    
    return app

if __name__ == '__main__':
    app = create_app()
    port = int(os.getenv('PORT', 5000))
    debug = os.getenv('FLASK_ENV') == 'development'
    
    logger.info(f'🚀 Starting Order Flow Professional on port {port}')
    logger.info(f'Debug mode: {debug}')
    logger.info(f'Environment: {os.getenv("FLASK_ENV", "production")}')
    
    app.run(host='0.0.0.0', port=port, debug=debug, threaded=True)
