# Cyrillinki 🇷🇸

A Progressive Web App for learning Serbian Cyrillic alphabet and common words using spaced repetition.

**[Live Demo](https://vanpelt.github.io/cyrillic/)** | **[Install as PWA](#installation)**

## Overview

Cyrillinki is a client-side flashcard application that helps you master the Serbian Cyrillic alphabet and expand your vocabulary through scientifically proven spaced repetition techniques. Built as a lightweight PWA with no backend required, it works entirely in your browser with offline support.

## Features

- **🧠 Spaced Repetition Algorithm** - Implements Anki's SM-2 algorithm for optimal learning intervals
- **📚 Two Learning Modes**:
  - **Alphabet Mode**: Master all 30 Serbian Cyrillic letters with pronunciation guides
  - **Words Mode**: Practice 100 common Serbian words with transliterations and meanings
- **📊 Progress Tracking** - Visual statistics for new, learning, and review cards
- **⌨️ Keyboard Shortcuts**:
  - `Space`: Show answer
  - `1`: Again (reset interval)
  - `2`: Hard (shorter interval)
  - `3`: Good (standard interval)
  - `4`: Easy (longer interval)
- **📱 Progressive Web App**:
  - Install on mobile devices and desktop
  - Works offline after first visit
  - No app store required
- **💾 Local Persistence** - All progress saved in browser localStorage
- **🎨 Dark Mode** - Automatic theme switching with manual toggle
- **📐 Responsive Design** - Optimized for all screen sizes

## Installation

### As a Web App (Desktop/Mobile)

1. Visit [https://vanpelt.github.io/cyrillic/](https://vanpelt.github.io/cyrillic/)
2. On mobile: Tap the share button and select "Add to Home Screen"
3. On desktop: Look for the install prompt or use the browser menu to install

The app will work offline after installation!

### For Development

```bash
# Clone the repository
git clone https://github.com/vanpelt/cyrillic.git
cd cyrillic

# Start development server with live reload
python dev.py
```

The app will be available at http://localhost:8000

## Architecture

Cyrillinki is a **single-file application** with a modern, minimalist architecture:

- **Single HTML file** (`index.html`) - Contains HTML structure, styling, and JavaScript logic
- **No build process** - Uses Tailwind CSS via CDN, no compilation required
- **Client-side only** - No backend, no database, no server required
- **localStorage persistence** - Card progress and settings stored locally
- **SM-2 Algorithm** - Proven spaced repetition system for optimal retention

### Data Structure

- **Alphabet dataset**: 30 Serbian Cyrillic letters with Latin equivalents and pronunciation
- **Words dataset**: 100 common Serbian words with transliteration and English meanings
- **Card class**: Implements SM-2 algorithm with easiness factor, intervals, and repetition tracking

### localStorage Keys

- `serbianCards` - Progress data for alphabet mode
- `serbianWordsCards` - Progress data for words mode
- `serbianSettings` - User preferences (mode selection, theme)

## Technologies

- **HTML5** - Semantic markup with PWA meta tags
- **Tailwind CSS** - Utility-first styling via CDN
- **Vanilla JavaScript** - Modern ES6+ with classes and modules
- **localStorage API** - Client-side data persistence
- **Service Worker** - PWA support and offline functionality

## Development

The development server (`dev.py`) provides:
- Live reload on file changes
- CORS-enabled local hosting
- Port 8000 by default

No build step, transpilation, or bundling required. Edit `index.html` and refresh!

## Deployment

Automatic deployment to GitHub Pages via GitHub Actions (`.github/workflows/deploy.yml`). Every push to the `main` branch deploys the latest version.

No build step required - the workflow simply uploads all static files.

## Contributing

Contributions are welcome! This project is designed to be simple and maintainable:

1. Fork the repository
2. Make your changes to `index.html`
3. Test locally with `python dev.py`
4. Submit a pull request

## License

MIT License - feel free to use and modify for your own learning projects!

## Acknowledgments

- Spaced repetition algorithm based on [Anki's SM-2](https://faqs.ankiweb.net/what-spaced-repetition-algorithm.html)
- Serbian language datasets compiled from common vocabulary lists
- Built with modern web standards for maximum compatibility

---

**Happy learning! Срећно учење! 🎓**
