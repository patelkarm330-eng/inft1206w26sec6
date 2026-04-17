const btn = document.getElementById('toggle-comments');
const comments = document.getElementById('comments-list');

btn.addEventListener('click', () => {
  if (comments.style.display === 'none') {
    comments.style.display = 'block';
    btn.textContent = 'Hide comments';
  } else {
    comments.style.display = 'none';
    btn.textContent = 'Show comments';
  }
});