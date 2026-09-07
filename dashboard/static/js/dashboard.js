async function loadCases() {
  const target = document.querySelector('#cases');
  if (!target) return;
  const response = await fetch('/api/cases');
  const cases = await response.json();
  target.innerHTML = cases.map(item => `<article class="metric"><strong>${item.title}</strong><p>${item.description}</p><small>Score: ${item.score} | ${item.status}</small></article>`).join('');
}
loadCases();
