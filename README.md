# The IR Reading Room 📚

**John's private, old-fashioned library for International Relations articles.** Type a topic, get classic blue links to the relevant scholarship — in English, French, German, Russian or Chinese. Filter for freely available full text or search everything. Translate any article page to English in one click, and collect articles into a reading list that can be emailed as PDFs.

## How it works

- Searches the **[OpenAlex](https://openalex.org)** catalogue of 250M+ scholarly works, directly from your browser (no middleman, no tracking).
- **Access filter**: *All articles* ↔ *Readily available (free full text only)* — the latter keeps only open-access works.
- **Language filter**: any language, or specifically English / French / German / Russian / Chinese. Original titles are shown as published.
- **Translate** button: opens the article's page through Google Translate (English). For PDF-only articles it opens Google's document translation, which produces a translated copy you can download.
- **Reading list**: tick articles, then
  - **Email via Vibe** — downloads a small selection file; attach it in your Vibe chat and ask Vibe to fetch the articles and email them to you as PDFs (open-access ones can be attached),
  - **Open mail draft** — opens your own mail app with the whole list, links and free PDF links included,
  - **Copy list** — plain text, ready to paste anywhere.
- If you search in one language with English keywords, the room suggests the native term (e.g. *tribute system* → *朝贡体系* for Chinese).
- Optional ⚙ Settings: your email address and a free personal OpenAlex API key, stored only in your browser.

## Install it

Open the live site and add it to your home screen (iPhone: Share → *Add to Home Screen*; Android: menu → *Install app*; desktop Chrome/Edge: the install icon in the address bar). It then works offline for reading collected lists.

## Privacy

Nothing about your searches or reading is stored anywhere but this device's browser storage. Requests go straight from your browser to the OpenAlex index and to Google Translate when you click translate.

## Tech notes

- Single-page app, no build step, no CDN: plain HTML/CSS/JS + a service worker (`sw.js`) for offline use.
- `manifest.webmanifest` — install/app info; `icons/` — app icons.
- localStorage keys: `irr-settings`, `irr-basket`.
