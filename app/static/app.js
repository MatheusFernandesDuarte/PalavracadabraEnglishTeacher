async function fetchWord() {
    const level = document.getElementById('level-slider').value;
    const url = `/api/random?level=${level}`;
    const res = await fetch(url);
    const data = await res.json();
    document.getElementById('word-display').textContent = data.word.toUpperCase();
}
document.getElementById('level-slider').addEventListener('input', fetchWord);
window.onload = fetchWord;
