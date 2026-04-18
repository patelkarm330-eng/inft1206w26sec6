// SHOW/HIDE COMMENTS (accessible)
const showHideBtn = document.querySelector('.show-hide');
const commentWrapper = document.querySelector('.comment-wrapper');

if (commentWrapper) {
  commentWrapper.style.display = 'none';
}

if (showHideBtn) {
  showHideBtn.setAttribute('aria-expanded', 'false');

  showHideBtn.addEventListener('click', () => {
    const isHidden = commentWrapper.style.display === 'none';

    commentWrapper.style.display = isHidden ? 'block' : 'none';
    showHideBtn.textContent = isHidden ? 'Hide comments' : 'Show comments';
    showHideBtn.setAttribute('aria-expanded', isHidden ? 'true' : 'false');
  });
}

// ADDING NEW COMMENTS
const form = document.querySelector('.comment-form');
const nameField = document.querySelector('#name');
const commentField = document.querySelector('#comment');
const list = document.querySelector('.comment-container');

if (form) {
  form.addEventListener('submit', (e) => {
    e.preventDefault();
    submitComment();
  });
}

function submitComment() {
  const listItem = document.createElement('li');
  const namePara = document.createElement('p');
  const commentPara = document.createElement('p');

  namePara.textContent = nameField.value;
  commentPara.textContent = commentField.value;

  listItem.appendChild(namePara);
  listItem.appendChild(commentPara);
  list.appendChild(listItem);

  nameField.value = '';
  commentField.value = '';
}
