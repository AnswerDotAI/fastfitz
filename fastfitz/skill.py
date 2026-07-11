"""Read, search, and visually preview PDFs with fastfitz (an ergonomic layer over PyMuPDF/fitz). Use this when a task needs PDF contents: text extraction first, rendered previews when layout, tables, stamps, signatures, or scan quality matter.

Core idioms (patched onto fitz objects by importing this skill):

- `pdf = fitz.open(path)`; `len(pdf)` pages; `pdf[0]` is a `Page`.
- `pdf.text(pages=None)` -- plain text with `--- page N ---` markers. Start here: it answers most questions without spending image tokens.
- `pdf.search_for(q)` -- `[(page, rects)]` for pages containing `q`. Rects are per-line; a match that wraps lines returns multiple rects.
- `pg.preview()` / `pg.preview(q)` / `pg.preview(clip=rect)` -- render the whole page, the union of `q`'s hit rects, or an explicit region, as a PNG `Image` that displays inline (end the cell with the bare call). Default `dpi=150`; lower for thumbnails, higher for fine print.
- A bare `pg` expression displays the page (via `_repr_png_`).

Prefer `preview(q)` crops over whole-page renders: cheaper and easier to read. For scanned/image-only PDFs `text()` returns little -- go straight to previews.

NB: fastfitz (like PyMuPDF) is AGPL-3.0.
"""
from fastfitz.core import *
