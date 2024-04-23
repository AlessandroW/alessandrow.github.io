"use strict";
function setTheme(theme) {
  const html = document.documentElement;
  html.dataset.theme = theme;
}
window.onbeforeunload = () => {
  for(const form of document.getElementsByTagName('form')) {
    form.reset();
  }
}

if (window.matchMedia && window.matchMedia('(prefers-color-scheme: dark)').matches) {
    setTheme("dark")
}
