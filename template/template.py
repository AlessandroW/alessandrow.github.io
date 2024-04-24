#!/usr/bin/env python3
from pathlib import Path

from mako.template import Template
from mako.lookup import TemplateLookup

TEMPLATE_DIR = Path(__file__).parent / "html"
OUTPUT_DIR = Path(__file__).parent.parent


def render(filename):
    lookup = TemplateLookup(directories=[TEMPLATE_DIR])
    website = Template(filename=str(TEMPLATE_DIR / filename), lookup=lookup)
    with open(OUTPUT_DIR / filename, "w") as f:
        f.write(website.render())


if __name__ == "__main__":
    render("index.html")
    render("index_en.html")
    render("impressum_datenschutz.html")
