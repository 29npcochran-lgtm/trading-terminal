# Order Flow Professional

**Institutional-grade market analysis platform** for professional traders. Bloomberg Terminal meets Bookmap with modular architecture.

## 🚀 Quick Start

### Deploy to Vercel
```bash
vercel --prod
```

### Local Development
```bash
pip install -r requirements.txt
cp .env.example .env
python app.py
```

## ✨ Features

- **Real-time Order Flow** — DOM, Time & Sales, Liquidity Heatmap
- **Professional Charts** — Candlestick, Footprint, Delta, Volume Profile
- **Volume Analytics** — 20+ volume indicators and profiles
- **Market Structure** — Automatic swing detection, order blocks
- **Alert Engine** — Price, indicator, volume alerts with webhooks
- **Multi-Provider** — Polygon.io, Databento, Alpaca, dxFeed, Interactive Brokers

## 📦 Tech Stack

- **Backend**: Flask, Python, asyncio
- **Real-time**: WebSockets, Socket.IO
- **Data**: Pandas, NumPy
- **Database**: SQLAlchemy, PostgreSQL/SQLite
- **Caching**: Redis
- **Deployment**: Vercel (Serverless)

## 🗂️ Structure

```
backend/
├── config/settings.py       # Configuration
├── api/routes.py           # REST endpoints
├── data/                   # Market data providers
├── indicators/technical.py # Technical indicators
├── charts/                 # Chart engines
└── services/              # Business logic
```

## 📝 Environment Variables

```
FLASK_ENV=production
PORT=8000
POLYGON_API_KEY=your_key
ALPACA_API_KEY=your_key
DATABASE_URL=postgresql://localhost/db
REDIS_URL=redis://localhost:6379
```

## 🧪 Testing

```bash
pytest
pytest --cov=backend
```

## 📄 License

MIT License

---

**Status**: Production Ready ✅ | **Deployment**: Vercel
