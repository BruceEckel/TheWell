// The Well — the lamp. No framework, no dependencies.
(function () {
  var root = document.documentElement;
  var saved = null;
  try { saved = localStorage.getItem("well-theme"); } catch (e) {}
  if (saved === "light" || saved === "dark") root.setAttribute("data-theme", saved);

  function effective() {
    var t = root.getAttribute("data-theme");
    if (t) return t;
    return window.matchMedia && window.matchMedia("(prefers-color-scheme: dark)").matches
      ? "dark" : "light";
  }

  document.addEventListener("DOMContentLoaded", function () {
    var lamp = document.querySelector(".lamp");
    if (!lamp) return;
    lamp.addEventListener("click", function () {
      var next = effective() === "dark" ? "light" : "dark";
      root.setAttribute("data-theme", next);
      try { localStorage.setItem("well-theme", next); } catch (e) {}
    });
  });
})();
