(function () {
  function el(tag, attrs, children) {
    const node = document.createElement(tag);
    Object.entries(attrs || {}).forEach(([key, value]) => {
      if (key === 'className') node.className = value;
      else if (key === 'textContent') node.textContent = value;
      else node.setAttribute(key, value);
    });
    (children || []).forEach((child) => node.appendChild(child));
    return node;
  }

  function renderQuiz(root, data) {
    let answered = 0;
    let score = 0;
    const summary = el('div', { className: 'quiz-summary', role: 'status', 'aria-live': 'polite' });
    const cards = [];

    function updateSummary() {
      const total = data.questions.length;
      const remaining = total - answered;
      const pct = answered ? Math.round((score / answered) * 100) : 0;
      summary.textContent = answered === 0
        ? `Ready: ${total} questions. Answer from memory first, then use feedback to learn the navigation logic.`
        : `Answered ${answered}/${total}. Current score: ${score}/${answered} (${pct}%). ${remaining} remaining.`;
      if (answered === total) {
        const finalPct = Math.round((score / total) * 100);
        summary.textContent = `Complete. Final score: ${score}/${total} (${finalPct}%). Review any missed navigation cues, then retry after a short break.`;
      }
    }

    data.questions.forEach((q, index) => {
      const card = el('article', { className: 'quiz-card' });
      const meta = el('div', { className: 'quiz-meta', textContent: `Question ${index + 1} of ${data.questions.length}` });
      const fieldset = el('fieldset');
      const legend = el('legend', { textContent: q.prompt });
      const options = el('div', { className: 'options' });
      const feedback = el('div', { className: 'feedback', 'aria-live': 'polite' });
      let isAnswered = false;

      q.choices.forEach((choice, choiceIndex) => {
        const button = el('button', { className: 'option', type: 'button', textContent: choice });
        button.addEventListener('click', () => {
          if (isAnswered) return;
          isAnswered = true;
          answered += 1;
          const correct = choiceIndex === q.answer;
          if (correct) score += 1;
          Array.from(options.children).forEach((btn, i) => {
            btn.disabled = true;
            if (i === q.answer) btn.classList.add('correct');
            if (i === choiceIndex && i !== q.answer) btn.classList.add('incorrect');
          });
          feedback.classList.add('show', correct ? 'good' : 'bad');
          feedback.innerHTML = `
            <div class="label">${correct ? 'Correct' : 'Not quite'}</div>
            <p>${q.feedback}</p>
            <p class="muted"><strong>Source check:</strong> ${q.evidence}</p>
          `;
          updateSummary();
        });
        options.appendChild(button);
      });

      fieldset.append(legend, options, feedback);
      card.append(meta, fieldset);
      root.appendChild(card);
      cards.push(card);
    });

    const controls = el('div', { className: 'button-row no-print' });
    const reset = el('button', { className: 'primary-button secondary', type: 'button', textContent: 'Reset quiz' });
    reset.addEventListener('click', () => window.location.reload());
    controls.appendChild(reset);
    root.prepend(summary);
    root.appendChild(controls);
    updateSummary();
  }

  document.addEventListener('DOMContentLoaded', () => {
    const root = document.getElementById('quiz-root');
    if (!root || !window.quizData) return;
    renderQuiz(root, window.quizData);
  });
})();
