# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

Cyrillinki is a Progressive Web App (PWA) for learning Serbian Cyrillic alphabet and common words using spaced repetition. It's a client-side-only application using vanilla HTML, CSS (Tailwind via CDN), and JavaScript with localStorage for persistence.

## Architecture

- **Single-file application**: Everything is contained in `index.html` - HTML structure, Tailwind styling, and JavaScript logic
- **No build process**: Uses Tailwind CSS via CDN, no compilation or bundling required
- **Data persistence**: Uses browser localStorage to store card progress and settings
- **Spaced repetition**: Implements Anki's SM-2 algorithm for optimal learning intervals
- **Two learning modes**: Alphabet mode (30 Cyrillic letters) and Words mode (100 common Serbian words)

## Development Commands

```bash
# Start development server with live reload
python dev.py
```

The development server runs on http://localhost:8000 by default.

## Key Application Components

### Data Structure
- `alphabet` array: 30 Serbian Cyrillic letters with latin equivalents and pronunciation
- `commonWords` array: 100 common Serbian words with latin transliteration and meanings
- `Card` class: Implements SM-2 spaced repetition algorithm with persistence

### Core Features
- **Spaced repetition**: Cards are scheduled based on user performance using intervals
- **Progress tracking**: Statistics for new/learning/review cards with visual progress bar
- **Keyboard shortcuts**: Space (show answer), 1-4 (grade cards)
- **Settings**: Toggle between alphabet and words mode
- **PWA support**: Manifest file for mobile installation

### localStorage Keys
- `serbianCards`: Progress data for alphabet mode
- `serbianWordsCards`: Progress data for words mode  
- `serbianSettings`: User preferences (wordsMode boolean)

## Deployment

Automatic deployment to GitHub Pages via `.github/workflows/deploy.yml` on pushes to main branch. The workflow simply uploads all files as static content - no build step required.

## Code Style Notes

- Uses modern JavaScript (ES6+ classes, const/let, arrow functions)
- Tailwind CSS classes for all styling
- Mobile-responsive design with touch-friendly interactions
- PWA-ready with proper meta tags and manifest