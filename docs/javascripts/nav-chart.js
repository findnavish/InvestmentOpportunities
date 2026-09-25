document$.subscribe(async () => {
  const el = document.getElementById("navChart");
  if (!el || typeof Chart === "undefined") return;
  const data = await (await fetch("nav.json", { cache: "no-store" })).json();
  new Chart(el, {
    type: "line",
    data: {
      labels: data.map(d => d.t.replace("T", " ").slice(0, 16)),
      datasets: [
        { label: "Model portfolio (NAV, start = 100)", data: data.map(d => d.nav), borderWidth: 2, pointRadius: 0, tension: 0.2 },
        { label: "SOXX (start = 100)", data: data.map(d => d.soxx), borderWidth: 1.5, borderDash: [5, 4], pointRadius: 0, tension: 0.2 }
      ]
    },
    options: { responsive: true, interaction: { mode: "index", intersect: false },
               scales: { x: { ticks: { maxTicksLimit: 8 } } } }
  });
});
