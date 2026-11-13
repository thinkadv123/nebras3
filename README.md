# Nebras Technology website

A static, multi-page website for Nebras Technology, built from the `nebras3` design PDF (21 pages).

## Pages
| Section | Files |
|---|---|
| Home | `index.html` |
| Company | `about.html`, `leadership.html`, `milestones.html` |
| Solutions | `solutions.html` |
| Radiology | `radiology.html`, `paxtreme.html`, `oneris.html`, `oneaccred.html`, `onerad.html`, `instashare.html`, `neoq.html` |
| Endoscopy | `endoscopy.html`, `endostream.html`, `oneendo.html` |
| Dental | `dental.html`, `dentalore-cloud.html`, `dentalore-ds.html` |
| Other | `clients.html`, `news.html`, `contact.html` |

## Structure
- `assets/css/style.css`: all styles (Poppins + Inter, brand colors, responsive layouts)
- `assets/js/main.js`: mobile menu, team carousels, scroll reveal, demo-request form (opens an e-mail to info@nebrastech.com)
- `assets/img/`: logos, photos, product screenshots and client logos extracted from the design
- `_build/build.py`: generator for all pages (shared header, footer and templates)

## Editing
Edit content in `_build/build.py`, then regenerate the pages:

```bash
python3 _build/build.py
```

## Running locally
Open `index.html` in a browser, or serve the folder:

```bash
python3 -m http.server 8000
```

The site is plain HTML/CSS/JS, so it can be hosted on GitHub Pages or any static host.
