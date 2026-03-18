# JavaScript Interaction Patterns

## Table of Contents
1. Voice Toggle System
2. Tab Navigation
3. Method Card Expand/Collapse
4. Step-by-Step Reveal
5. Example Problem Flow (Answer → Guide → Feynman)
6. Quiz System

---

## 1. Voice Toggle System

```javascript
let cBtn = null;
function tv(btn, text) {
  // If already playing, stop
  if (btn.classList.contains('playing')) {
    speechSynthesis.cancel();
    btn.classList.remove('playing');
    btn.innerHTML = btn.dataset.o || '🔊';
    cBtn = null;
    return;
  }
  // Stop any other playing voice
  if (cBtn) {
    speechSynthesis.cancel();
    cBtn.classList.remove('playing');
    cBtn.innerHTML = cBtn.dataset.o || '🔊';
  }
  // Start playing
  btn.dataset.o = btn.innerHTML;
  btn.innerHTML = '⏹';
  btn.classList.add('playing');
  cBtn = btn;

  const u = new SpeechSynthesisUtterance(text);
  u.lang = 'zh-CN';
  u.rate = 0.82;
  u.pitch = 1.15;
  const v = speechSynthesis.getVoices();
  const zh = v.find(x => x.name.includes('Tingting') || x.name.includes('Xiaoxiao'))
           || v.find(x => x.lang.startsWith('zh'));
  if (zh) u.voice = zh;
  u.onend = () => {
    btn.classList.remove('playing');
    btn.innerHTML = btn.dataset.o;
    cBtn = null;
  };
  speechSynthesis.speak(u);
}

// Preload voices
if ('speechSynthesis' in window) {
  speechSynthesis.getVoices();
  speechSynthesis.onvoiceschanged = () => speechSynthesis.getVoices();
}
```

## 2. Tab Navigation

```javascript
document.querySelectorAll('.pill').forEach(p => {
  p.addEventListener('click', () => {
    document.querySelectorAll('.pill').forEach(x => x.classList.remove('on'));
    document.querySelectorAll('.sec').forEach(x => x.classList.remove('on'));
    p.classList.add('on');
    document.getElementById(p.dataset.s).classList.add('on');
    // Cancel voice when switching tabs
    speechSynthesis.cancel();
    if (cBtn) { cBtn.classList.remove('playing'); cBtn.innerHTML = cBtn.dataset.o; cBtn = null; }
  });
});
```

## 3. Method Card Expand/Collapse

```javascript
function toggleMethod(card) {
  const detail = card.querySelector('.mdetail');
  const isOpen = detail.classList.contains('open');
  // Close all others first
  document.querySelectorAll('.mdetail').forEach(x => x.classList.remove('open'));
  document.querySelectorAll('.mcard').forEach(x => x.classList.remove('open'));
  if (!isOpen) {
    detail.classList.add('open');
    card.classList.add('open');
  }
}
```

## 4. Step-by-Step Reveal

```javascript
function revealSteps(containerId) {
  const container = document.getElementById(containerId);
  const steps = container.querySelectorAll('.mstep');
  steps.forEach((step, i) => {
    setTimeout(() => step.classList.add('show'), i * 400);
  });
  // Hide the reveal button
  container.previousElementSibling.style.display = 'none';
}
```

## 5. Example Problem Flow

### Data Structure

```javascript
const exData = {
  ex1: {
    opts: [
      { t: '(A) 1元', v: false },
      { t: '(B) 2元', v: true },   // v:true = correct answer
      { t: '(C) 3元', v: false },
    ],
    guide: [
      {
        q: 'Question text shown to child',
        a: 'Answer text revealed on click',
        vc: 'Voice text for speech synthesis'
      },
      // ... more guide steps
    ]
  }
};
```

### Init Example Options

```javascript
function initEx(id, data) {
  const el = document.getElementById(id + '-opts');
  data.opts.forEach((o, i) => {
    const btn = document.createElement('div');
    btn.className = 'ex-opt';
    btn.textContent = o.t;
    btn.onclick = () => handleEx(id, data, i);
    el.appendChild(btn);
  });
}
```

### Handle Answer Selection

```javascript
function handleEx(id, data, idx) {
  const opts = document.querySelectorAll(`#${id}-opts .ex-opt`);
  const res = document.getElementById(id + '-result');

  if (data.opts[idx].v) {
    // CORRECT
    opts.forEach((o, i) => {
      o.classList.add('dim');
      if (data.opts[i].v) o.classList.add('correct');
    });
    res.style.display = 'block';
    res.style.background = 'rgba(168,216,203,.2)';
    res.style.color = '#2E6B52';
    res.innerHTML = '🎉 答对了！现在一步步想想你是怎么得到答案的——';
    setTimeout(() => buildGuide(id, data), 800);
  } else {
    // WRONG — show two buttons
    opts[idx].classList.add('wrong');
    res.style.display = 'block';
    res.style.background = 'rgba(249,228,167,.25)';
    res.style.color = '#8B6914';
    res.innerHTML = `
      <div style="margin-bottom:12px">💡 这个答案不太对哦，没关系！</div>
      <div style="display:flex;gap:10px;flex-wrap:wrap">
        <button onclick="retryEx('${id}',${idx})"
          style="padding:10px 20px;border-radius:50px;border:2.5px solid var(--mint);
          background:#fff;color:var(--mint-deep);font-size:15px;font-weight:700;cursor:pointer">
          🔄 再试试哦</button>
        <button onclick="learnEx('${id}')"
          style="padding:10px 20px;border-radius:50px;border:2.5px solid var(--lilac);
          background:#fff;color:var(--lilac-deep);font-size:15px;font-weight:700;cursor:pointer">
          📖 有点难哦，学学解法</button>
      </div>`;
  }
}

function retryEx(id, wrongIdx) {
  document.querySelectorAll(`#${id}-opts .ex-opt`)[wrongIdx].classList.remove('wrong');
  document.getElementById(id + '-result').style.display = 'none';
}

function learnEx(id) {
  const data = exData[id];
  const opts = document.querySelectorAll(`#${id}-opts .ex-opt`);
  opts.forEach((o, i) => {
    o.classList.add('dim');
    if (data.opts[i].v) o.classList.add('correct');
  });
  const res = document.getElementById(id + '-result');
  res.style.background = 'rgba(167,203,232,.15)';
  res.style.color = 'var(--sky-deep)';
  res.innerHTML = '📖 没关系！正确答案已经标出来了。我们一起来看看怎么解——';
  setTimeout(() => buildGuide(id, data), 800);
}
```

### Build Guide Chain (Sequential Unlock)

```javascript
function buildGuide(id, data) {
  const chain = document.getElementById(id + '-guide');
  chain.style.display = 'block';
  chain.scrollIntoView({ behavior: 'smooth', block: 'center' });

  data.guide.forEach((g, i) => {
    const item = document.createElement('div');
    item.className = 'guide-item';
    item.id = `${id}-g${i}`;
    if (i === 0) item.classList.add('unlocked');

    const qDiv = document.createElement('div');
    qDiv.className = 'guide-q';
    qDiv.innerHTML = `
      <span class="gicon">${i < data.guide.length - 1 ? '💬' : '🚀'}</span>
      ${g.q}
      <span class="guide-lock">${i === 0 ? '👆 点击' : '🔒'}</span>`;

    const aDiv = document.createElement('div');
    aDiv.className = 'guide-a';
    aDiv.innerHTML = `
      <p>${g.a}</p>
      <button class="vbtn vbtn-sky" style="margin-top:8px"
        onclick="event.stopPropagation();tv(this,'${g.vc.replace(/'/g, "\\'")}')">🔊</button>`;

    qDiv.onclick = () => {
      if (!item.classList.contains('unlocked')) return;
      if (aDiv.classList.contains('open')) return;
      aDiv.classList.add('open');
      qDiv.querySelector('.guide-lock').textContent = '✅';

      setTimeout(() => {
        const next = document.getElementById(`${id}-g${i + 1}`);
        if (next) {
          next.classList.add('unlocked');
          next.querySelector('.guide-lock').textContent = '👆 点击';
          next.scrollIntoView({ behavior: 'smooth', block: 'center' });
        } else {
          // All done — show Feynman box
          const feynman = document.getElementById(id + '-feynman');
          feynman.classList.add('show');
          feynman.scrollIntoView({ behavior: 'smooth', block: 'center' });
        }
      }, 600);
    };

    item.appendChild(qDiv);
    item.appendChild(aDiv);
    chain.appendChild(item);
  });
}
```

## 6. Quiz System

```javascript
const quizData = [
  {
    src: '2025-Q1',        // Source reference
    d: '★',               // Difficulty
    q: '【2025·Q1】题目文字',
    opts: ['选项A', '选项B', '选项C', '选项D'],
    ans: 0,                // Correct answer index
    ok: '🎉 正确反馈',
    no: '💡 错误提示'
  },
  // ... more questions
];

let currentQ = 0, stars = 0;
let answered = new Array(quizData.length).fill(false);

function renderQuiz() {
  // 1. Render star progress bar
  // 2. Render navigation dots
  // 3. Render current question with difficulty badge + source tag
  // 4. Render options
  // 5. If already answered, show correct answer highlighted
  // 6. Previous/Next buttons
}

function checkAnswer(idx) {
  if (answered[currentQ]) return;
  const q = quizData[currentQ];
  if (idx === q.ans) {
    // Mark correct, increment stars, show feedback
    answered[currentQ] = true;
    stars++;
    renderQuiz(); // Re-render to update stars
  } else {
    // Shake wrong option, show hint, auto-clear after 2.2s
  }
}
```
