# ArtEmotion API

ArtEmotion is a Python-based API that transforms emotions into various forms of artistic expressions, such as poetry, stories, and visual art descriptions. It leverages the power of prompting techniques to produce creative outputs based on user inputs.

## Features

- Translate emotions into artistic outputs.
- Flexible customization with parameters for art form, style, language, and context.
- JSON-based input and output for easy integration.

---

## Table of Contents

- [Getting Started](#getting-started)
- [API Endpoints](#api-endpoints)
- [Parameters](#parameters)
- [Example Usage](#example-usage)
- [Installation](#installation)

---

## Getting Started

### Prerequisites

- Python 3.12+
- A virtual environment (recommended)

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/artemotion.git
   cd artemotion
   ```

2. Create and activate a virtual environment:

   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   ```

3. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Run the API server:

   ```bash
   python -m app.main
   ```

The server will run on `http://localhost:8000` by default.

---

## API Endpoints

### `POST /generate`

- **Description**: Generate artistic content based on user inputs.
- **Request Body**:
  ```json
  {
    "emotion": "string",
    "art_form": "string",
    "style": "string (optional)",
    "language": "string (optional)",
    "context": "string (optional)"
  }
  ```
- **Response**:
  ```json
  {
    "emotion": "string",
    "description": "string",
    "art_form": "string",
    "style": "string",
    "language": "string",
    "output": "string"
  }
  ```

---

## Parameters

- **Emotion**: (Required) The primary emotion or mood to convey.
- **Art Form**: (Required) The desired artistic output (e.g., poetry, short story, visual description).
- **Style**: (Optional) The tone or style for the output (e.g., romantic, surreal).
- **Language**: (Optional) The language for the output (e.g., English, Spanish).
- **Context**: (Optional) Additional details or scenarios for the generated content.

---

## Example Usage

### Request

```json
POST /generate HTTP/1.1
Content-Type: application/json

{
  "emotion": "melancholy",
  "art_form": "poetry",
  "style": "romantic",
  "language": "English",
  "context": "a rainy evening in autumn"
}
```

### Response

```json
{
  "emotion": "melancholy",
  "description": "A deep sense of longing and introspection, evoked by a rain-soaked autumn evening.",
  "art_form": "poetry",
  "style": "romantic",
  "language": "English",
  "output": "In autumn's wane, where twilight sighs, / Rain whispers soft, beneath gray skies..."
}
```

---

## Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-name`).
3. Commit your changes (`git commit -m "Add feature"`).
4. Push to the branch (`git push origin feature-name`).
5. Open a Pull Request.

---

# Thanks for seeing.
