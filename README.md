# Order Flow Professional

**Institutional-grade market analysis platform** for professional traders. Bloomberg Terminal meets Bookmap with modular architecture.

## Features

- **Real-time Order Flow** — DOM, Time & Sales, Liquidity Heatmap
- **Professional Charts** — Candlestick, Footprint, Delta, Volume Profile
- **Liquid Heatmap** — GPU-accelerated bubble visualization
- **Volume Analytics** — 20+ volume indicators, profiles, and ratios
- **Market Structure** — Automatic swing detection, fair value gaps, order blocks
- **Drawing Tools** — Trendlines, channels, Fibonacci, risk/reward, measurement
- **Alert Engine** — Price, indicator, volume, DOM, liquidity, webhook alerts
- **Backtesting** — Replay engine with historical data
- **Widget Workspace** — Fully customizable, dockable, multi-monitor support
- **Screener** — Institutional-grade watchlist and scanner
- **Multi-Provider** — Polygon.io, Databento, Alpaca, dxFeed, Interactive Brokers

## Architecture

```
order-flow-professional/
├── backend/
│   ├── core/
│   │   ├── market_data/
│   │   │   ├── providers/
│   │   │   │   ├── polygon_adapter.py
│   │   │   │   ├── databento_adapter.py
│   │   │   │   ├── alpaca_adapter.py
│   │   │   │   └── base.py
│   │   │   ├── tick_processor.py
│   │   │   ├── cache.py
│   │   │   └── manager.py
│   │   ├── order_flow/
│   │   │   ├── dom.py
│   │   │   ├── time_sales.py
│   │   │   ├── trade_direction.py
│   │   │   ├── iceberg_detection.py
│   │   │   └── liquidity_analyzer.py
│   │   ├── charts/
│   │   │   ├── candlestick.py
│   │   │   ├── footprint.py
│   │   │   ├── delta_bars.py
│   │   │   ├── heatmap.py
│   │   │   └── chart_engine.py
│   │   ├── indicators/
│   │   │   ├── volume/
│   │   │   ├── trend/
│   │   │   ├── momentum/
│   │   │   └── custom.py
│   │   ├── market_structure/
│   │   │   ├── swing_detector.py
│   │   │   ├── structure_analyzer.py
│   │   │   └── liquidity_pools.py
│   │   └── storage/
│   │       ├── drawing_manager.py
│   │       ├── layout_manager.py
│   │       └── persistence.py
│   ├── trading/
│   │   ├── backtesting/
│   │   │   ├── replay_engine.py
│   │   │   ├── statistics.py
│   │   │   └── trade_blotter.py
│   │   ├── alerts/
│   │   │   ├── alert_engine.py
│   │   │   ├── conditions.py
│   │   │   └── notifications.py
│   │   └── screeners/
│   │       ├── scanner.py
│   │       └── filters.py
│   ├── websocket/
│   │   ├── server.py
│   │   ├── handlers.py
│   │   └── broadcast.py
│   ├── config/
│   │   ├── settings.py
│   │   ├── themes.py
│   │   ├── templates.py
│   │   └── indicators_config.py
│   ├── api/
│   │   ├── routes.py
│   │   ├── middleware.py
│   │   └── auth.py
│   ├── utils/
│   │   ├── logger.py
│   │   ├── performance.py
│   │   └── validators.py
│   └── main.py
├── frontend/
│   ├── src/
│   │   ├── components/
│   │   │   ├── workspace/
│   │   │   │   ├── DockLayout.tsx
│   │   │   │   ├── Widget.tsx
│   │   │   │   ├── WidgetLibrary.tsx
│   │   │   │   └── LayoutManager.tsx
│   │   │   ├── charts/
│   │   │   │   ├── ChartCanvas.tsx
│   │   │   │   ├── CandlestickChart.tsx
│   │   │   │   ├── FootprintChart.tsx
│   │   │   │   ├── HeatmapChart.tsx
│   │   │   │   └── ChartToolbar.tsx
│   │   │   ├── orderflow/
│   │   │   │   ├── DOM.tsx
│   │   │   │   ├── TimeSales.tsx
│   │   │   │   ├── TradeBlotter.tsx
│   │   │   │   └── OrderFlowPanel.tsx
│   │   │   ├── indicators/
│   │   │   │   ├── IndicatorPanel.tsx
│   │   │   │   ├── VolumeProfile.tsx
│   │   │   │   ├── Footprint.tsx
│   │   │   │   └── IndicatorLibrary.tsx
│   │   │   ├── tools/
│   │   │   │   ├── DrawingToolbar.tsx
│   │   │   │   ├── DrawingCanvas.tsx
│   │   │   │   └── AlertManager.tsx
│   │   │   └── common/
│   │   │       ├── Header.tsx
│   │   │       ├── Toolbar.tsx
│   │   │       ├── StatusBar.tsx
│   │   │       └── Settings.tsx
│   │   ├── store/
│   │   │   ├── workspace/
│   │   │   ├── charts/
│   │   │   ├── orderflow/
│   │   │   ├── alerts/
│   │   │   └── app.ts
│   │   ├── hooks/
│   │   │   ├── useWebSocket.ts
│   │   │   ├── useChart.ts
│   │   │   ├── useDrawing.ts
│   │   │   └── useWorkspace.ts
│   │   ├── services/
│   │   │   ├── websocket.ts
│   │   │   ├── api.ts
│   │   │   ├── storage.ts
│   │   │   └── chart.ts
│   │   ├── types/
│   │   │   ├── market.ts
│   │   │   ├── chart.ts
│   │   │   ├── orderflow.ts
│   │   │   ├── widget.ts
│   │   │   └── indicators.ts
│   │   ├── utils/
│   │   │   ├── formatting.ts
│   │   │   ├── calculations.ts
│   │   │   ├── performance.ts
│   │   │   └── storage.ts
│   │   ├── styles/
│   │   │   ├── global.css
│   │   │   ├── themes.css
│   │   │   ├── workspace.css
│   │   │   └── charts.css
│   │   ├── App.tsx
│   │   └── main.tsx
│   ├── public/
│   ├── package.json
│   ├── tsconfig.json
│   └── vite.config.ts
├── docs/
│   ├── architecture.md
│   ├── data_providers.md
│   ├── chart_types.md
│   ├── indicators.md
│   ├── api.md
│   └── deployment.md
├── docker/
│   ├── Dockerfile
│   ├── docker-compose.yml
│   └── .dockerignore
├── tests/
│   ├── backend/
│   ├── frontend/
│   └── integration/
├── .env.example
├── .gitignore
├── requirements.txt
├── pyproject.toml
└── Makefile
```

## Setup

```bash
# Backend
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt

# Frontend
cd frontend
npm install
npm run dev

# Start
python backend/main.py
```

## Data Providers

- Polygon.io
- Databento
- Alpaca
- dxFeed
- Interactive Brokers
- Binance
- Coinbase Advanced

## Market Coverage

- US Stocks & ETFs
- Futures
- Crypto
- Forex (planned)
- Options (planned)

## Performance

- 60–144 FPS rendering
- Tick-by-tick updates
- GPU-accelerated heatmaps
- Asynchronous indicator calculation
- Real-time DOM and order flow

---

**Built for professional traders. No simulation. Real data only.**
