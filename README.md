# Cyrillinki - Serbian Cyrillic Learning App

A flashcard app for learning Serbian Cyrillic alphabet and common words using spaced repetition.

## Features

- **Spaced Repetition Algorithm** - Uses Anki's SM-2 algorithm for optimal learning
- **Two Learning Modes**:
  - Alphabet mode: Learn all 30 Serbian Cyrillic letters
  - Words mode: Practice 100 common Serbian words
- **Progress Tracking** - Tracks new, learning, and review cards
- **Keyboard Shortcuts**:
  - Space: Show answer
  - 1-4: Grade cards (Again, Hard, Good, Easy)
- **Responsive Design** - Works on desktop and mobile devices
- **No Build Required** - Uses Tailwind CSS via CDN

## Usage

Simply open `index.html` in your browser. The app works entirely client-side using localStorage for persistence.

## Development

To run locally with live reload:

```bash
python dev.py
```

This starts a development server on http://localhost:8000

## Technologies

- HTML5
- Tailwind CSS (via CDN)
- Vanilla JavaScript
- localStorage for data persistence