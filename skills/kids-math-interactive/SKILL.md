---
name: kids-math-interactive
description: "Create interactive math learning websites for children aged 5-10. Use this skill whenever the user wants to build an educational math web app, interactive learning page, math quiz game, or any child-friendly HTML-based math teaching tool. Triggers include: requests for 'math learning site', 'interactive math for kids', 'math quiz game', 'educational web app for children', 'math practice website', or any mention of building a web-based math learning experience for young children. Also triggers when the user provides math knowledge points, example problems, or curriculum content and wants it turned into an interactive web experience. This skill handles the full pipeline: macaron color theming, speech synthesis integration, guided example walkthroughs, interactive quizzes, and step-by-step reveal animations. Use this skill even if the user just says 'make this into a fun learning page' when math content is involved."
---

# Kids Math Interactive — Child-Friendly Learning Website Builder

## Overview

Build production-grade interactive math learning websites for children (ages 5-10) with:
- Macaron pastel color scheme (soft, eye-friendly)
- Chinese Web Speech API voice narration (toggle play/stop)
- Interactive method cards with step-by-step reveal animations
- Guided example problem flow (answer → guided questions → Feynman explanation)
- Quiz system with encouraging feedback and retry mechanics
- Mobile-first responsive design (iPad optimized)

## Design System

### Macaron Color Palette (MUST USE)

```css
:root {
  --bg: #FDF6F0;        /* Cream warm white background */
  --card: #FFFFFF;
  --rose: #F4A7BB;       /* Rose pink — primary accent */
  --rose-deep: #E8839E;
  --mint: #A8D8CB;        /* Mint green — success, Feynman */
  --mint-deep: #7CC4B2;
  --lemon: #F9E4A7;       /* Lemon yellow — highlights */
  --lemon-deep: #F0D078;
  --lilac: #C5B3D9;       /* Lilac purple — quiz, challenges */
  --lilac-deep: #A68EC1;
  --sky: #A7CBE8;          /* Sky blue — guides, concepts */
  --sky-deep: #7DB4D9;
  --peach: #F5C5A3;        /* Peach orange — warnings, reverse thinking */
  --peach-deep: #E8A87C;
  --dark: #4A3728;         /* Warm dark brown — text */
  --muted: #8B7D75;        /* Muted brown — secondary text */
}
```

### Typography

- Title font: `'ZCOOL KuaiLe', cursive` (from Google Fonts) — playful, child-friendly
- Body font: `'Noto Sans SC', sans-serif` (from Google Fonts) — clean Chinese support
- Base font size: `17px` (larger than normal for kids on tablets)
- Line height: `1.7`

### Font Import (MUST INCLUDE)
```html
<link href="https://fonts.googleapis.com/css2?family=Noto+Sans+SC:wght@400;700;900&family=ZCOOL+KuaiLe&display=swap" rel="stylesheet">
```

## Architecture — 4 Sections

Every learning page has exactly 4 tab-sections, navigated via pill buttons:

### Section 1: 💡 概念详解 (Concept Details)
- One `.cbox` card per concept with colored left border
- Voice button (🔊) positioned at **top-right** of each card (`position:absolute;top:12px;right:12px`)
- Emoji-rich, short paragraphs, bold key terms
- Each concept has a different macaron color

### Section 2: 🛠 学习技巧 (Interactive Methods)
- Expandable `.mcard` cards — click to toggle open/close
- Each card contains:
  1. A **challenge question** (e.g., "count these fruits!")
  2. A **reveal button** ("👆 点我看解法！")
  3. Hidden `.mstep` steps that animate in one-by-one (400ms delay each)
  4. A voice button at the bottom
- Steps use numbered circles (`.snum`) with the method's theme color

### Section 3: 📖 例题精讲 (Example Problem Walkthrough)
This is the most complex section. The flow is:

```
Show problem → Child selects answer
  ├─ CORRECT → Show "🎉 答对了" → Unlock guide chain
  └─ WRONG → Show two buttons:
       ├─ "🔄 再试试哦" → Reset, let child retry
       └─ "📖 有点难哦，学学解法" → Mark correct answer, then unlock guide chain

Guide Chain (sequential unlock):
  Q1 (unlocked) → click → show answer + 🔊 → unlock Q2
  Q2 → click → show answer + 🔊 → unlock Q3
  ...
  Last Q → click → show answer → AUTO-SHOW Feynman box

Feynman Box:
  Green-bordered card with 3-step simple explanation + voice button
```

**Key rules:**
- Child MUST answer (or click "学学解法") before seeing any explanation
- Guide questions unlock ONE AT A TIME — must view current to unlock next
- Feynman box only appears AFTER all guide questions are viewed
- Wrong answer shows TWO buttons (retry + learn), not auto-dismiss

### Section 4: 🎮 闯关挑战 (Quiz Challenge)
- Star progress bar (⭐/☆ for each question)
- Navigation dots to jump between questions
- Each question shows: difficulty badge + source reference tag
- Wrong answer: shake animation + hint text + auto-clear after 2.2s
- Correct answer: mark green + show encouraging feedback
- Previous/Next buttons for navigation

## Voice System (Web Speech API)

```javascript
// Toggle pattern: click to play, click again to stop
let currentBtn = null;
function toggleVoice(btn, text) {
  if (btn.classList.contains('playing')) {
    speechSynthesis.cancel();
    btn.classList.remove('playing');
    btn.innerHTML = btn.dataset.orig;
    currentBtn = null;
    return;
  }
  // Stop any existing playback
  if (currentBtn) {
    speechSynthesis.cancel();
    currentBtn.classList.remove('playing');
    currentBtn.innerHTML = currentBtn.dataset.orig;
  }
  btn.dataset.orig = btn.innerHTML;
  btn.innerHTML = '⏹';
  btn.classList.add('playing');
  currentBtn = btn;

  const u = new SpeechSynthesisUtterance(text);
  u.lang = 'zh-CN';
  u.rate = 0.82;   // Slower for kids
  u.pitch = 1.15;  // Slightly higher, friendlier
  // Prefer high-quality Chinese voices
  const voices = speechSynthesis.getVoices();
  const best = voices.find(v =>
    v.name.includes('Tingting') || v.name.includes('Xiaoxiao')
  ) || voices.find(v => v.lang.startsWith('zh'));
  if (best) u.voice = best;
  u.onend = () => {
    btn.classList.remove('playing');
    btn.innerHTML = btn.dataset.orig;
    currentBtn = null;
  };
  speechSynthesis.speak(u);
}
```

**Voice button rules:**
- All voice buttons use the toggle pattern (play/stop)
- Only ONE voice can play at a time
- Voice buttons in concept cards: positioned top-right of card
- Voice buttons in methods/examples: inline after content
- Button changes to ⏹ while playing, with `.playing` CSS animation
- Switching tabs cancels any playing voice

## CSS Component Reference

Read `references/components.md` for the full CSS class reference including:
- `.vbtn` variants (`.vbtn-rose`, `.vbtn-mint`, `.vbtn-lilac`, `.vbtn-sky`, `.vbtn-peach`)
- `.cbox` concept boxes
- `.mcard` method cards with `.mdetail` and `.mstep`
- `.excard` example cards with `.guide-chain` and `.feynman-box`
- `.quiz-sec` quiz section components
- Animation keyframes

## Content Guidelines

### Language & Tone
- Use Chinese (zh-CN) throughout
- Speak like a fun older friend, NOT a teacher
- Use "我们一起" "你觉得呢" "你注意到了吗"
- NEVER say "这题很简单" or "你应该知道"
- On wrong answers: "这个想法很有创意！不过让我们再看看……"
- Use plenty of emoji in content (🎈🦘⭐🎉✅❌💡🔍)

### Voice Text Rules
- Write voice text as natural spoken Chinese (not reading aloud written text)
- Keep each voice segment under 30 seconds (~80-100 Chinese characters)
- Use pauses: "……" in text creates natural speech pauses
- Voice text should be self-contained (understandable without seeing the screen)

## Input Requirements

When the user provides content to build into a learning page, expect:
1. **Module name** — e.g., "计数与数感"
2. **Core concepts** — 3-5 concepts with explanations
3. **Learning methods** — 3-5 methods with names and descriptions
4. **Example problems** — 1-3 problems with:
   - Question text and options
   - Guided question chain (4-5 progressive questions with answers)
   - Feynman-style 3-step explanation
5. **Quiz questions** — 5-20 questions with options, correct answer, and feedback

## Output

A single self-contained `.html` file with:
- All CSS inline in `<style>` tag
- All JavaScript inline in `<script>` tag
- Google Fonts loaded via CDN link
- No external dependencies beyond the font CDN
- Mobile-responsive (works on iPad in Safari)
- File saved to `/mnt/user-data/outputs/`
