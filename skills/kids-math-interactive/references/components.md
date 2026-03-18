# CSS Component Reference

Complete CSS class reference for the kids-math-interactive skill.

## Table of Contents
1. Layout & Cards
2. Voice Buttons
3. Concept Boxes
4. Method Cards (Interactive)
5. Example Cards & Guide Chain
6. Feynman Box
7. Quiz Components
8. Animations
9. Hero & Navigation

---

## 1. Layout & Cards

```css
.container { max-width: 920px; margin: 0 auto; padding: 0 16px; }

.card {
  background: var(--card);
  border-radius: 24px;
  box-shadow: 0 6px 28px rgba(74,55,40,.07);
  padding: 28px;
  margin-bottom: 24px;
  border: 2px solid transparent;
  transition: .3s;
  position: relative;
}
.card:hover { border-color: var(--mint); }

.badge {
  display: inline-block;
  padding: 5px 16px;
  border-radius: 50px;
  font-size: 13px;
  font-weight: 700;
  color: #fff;
  margin-bottom: 12px;
}

/* Section visibility */
.sec { display: none; }
.sec.on { display: block; animation: fi .4s; }
```

## 2. Voice Buttons

```css
.vbtn {
  display: inline-flex;
  align-items: center;
  gap: 5px;
  padding: 8px 16px;
  border-radius: 50px;
  border: none;
  font-size: 14px;
  font-weight: 700;
  cursor: pointer;
  transition: .3s;
}
.vbtn:hover { transform: scale(1.06); }
.vbtn.playing { animation: pu 1s infinite; }

/* Color variants */
.vbtn-mint  { background: var(--mint);  color: #fff; }
.vbtn-rose  { background: var(--rose);  color: #fff; }
.vbtn-lilac { background: var(--lilac); color: #fff; }
.vbtn-sky   { background: var(--sky);   color: #fff; }
.vbtn-peach { background: var(--peach); color: #fff; }

/* Top-right positioning in cards */
.card-voice {
  position: absolute;
  top: 16px;
  right: 16px;
  z-index: 2;
}
```

## 3. Concept Boxes

```css
.cbox {
  border-radius: 20px;
  padding: 22px;
  margin: 14px 0;
  position: relative;
  overflow: hidden;
  /* Add border-left: 5px solid <color> inline */
  /* Add background: rgba(<color>, .1) inline */
}
.cbox h4 { margin-bottom: 8px; font-size: 19px; }
.cbox p { font-size: 16px; line-height: 1.8; }
```

Usage pattern:
```html
<div class="cbox" style="background:rgba(244,167,187,.1);border-left:5px solid var(--rose);position:relative">
  <div class="card-voice" style="position:absolute;top:12px;right:12px">
    <button class="vbtn vbtn-rose" onclick="tv(this,'voice text here')">🔊</button>
  </div>
  <h4 style="color:var(--rose-deep)">➕ Concept Title</h4>
  <p>Concept explanation...</p>
</div>
```

## 4. Method Cards (Interactive)

```css
.mcard {
  border-radius: 20px;
  padding: 22px;
  margin-bottom: 16px;
  cursor: pointer;
  transition: .3s;
  position: relative;
  overflow: hidden;
}
.mcard:hover { transform: translateY(-2px); box-shadow: 0 6px 20px rgba(0,0,0,.08); }
.mcard .mhead { display: flex; align-items: center; gap: 14px; }
.mcard .micon { font-size: 40px; flex-shrink: 0; }
.mcard .mtitle { font-size: 19px; font-weight: 900; }
.mcard .msub { font-size: 14px; margin-top: 3px; }
.mcard .mhint {
  position: absolute; right: 18px; top: 50%;
  transform: translateY(-50%); font-size: 24px; transition: .3s;
}
.mcard.open .mhint { transform: translateY(-50%) rotate(180deg); }

/* Expandable detail area */
.mdetail { max-height: 0; overflow: hidden; transition: max-height .5s; padding: 0 4px; }
.mdetail.open { max-height: 900px; padding: 18px 4px; }

/* Animated steps */
.mstep {
  display: flex; gap: 12px; align-items: flex-start;
  margin-bottom: 12px;
  opacity: 0; transform: translateX(-20px); transition: .4s;
}
.mstep.show { opacity: 1; transform: none; }
.mstep .snum {
  width: 34px; height: 34px; border-radius: 50%;
  display: flex; align-items: center; justify-content: center;
  font-weight: 900; font-size: 15px; color: #fff; flex-shrink: 0;
}
.mstep .scontent {
  background: rgba(255,255,255,.7); border-radius: 14px;
  padding: 12px 16px; flex: 1; font-size: 16px; line-height: 1.7;
}

/* Reveal button */
.reveal-btn {
  padding: 12px 24px; border-radius: 14px;
  border: 2.5px dashed; font-weight: 700; font-size: 15px;
  cursor: pointer; transition: .3s; background: #fff; margin-top: 10px;
}
.reveal-btn:hover { transform: scale(1.05); }
```

## 5. Example Cards & Guide Chain

```css
.excard {
  background: #fff; border-radius: 24px;
  box-shadow: 0 6px 28px rgba(74,55,40,.07);
  overflow: hidden; margin-bottom: 28px;
  border: 3px solid var(--lemon);
}
.exhdr {
  padding: 16px 24px; color: #fff;
  display: flex; justify-content: space-between; align-items: center;
}
.exbody { padding: 24px; }
.qbox {
  border: 2.5px dashed; border-radius: 16px;
  padding: 18px; margin-bottom: 16px;
  font-size: 17px; line-height: 1.8;
}

/* Answer options */
.ex-opts { display: grid; grid-template-columns: repeat(auto-fit, minmax(130px, 1fr)); gap: 10px; margin: 14px 0; }
.ex-opt {
  padding: 14px; border-radius: 14px;
  border: 2.5px solid var(--light-muted); background: #fff;
  font-size: 17px; font-weight: 700; cursor: pointer;
  transition: .3s; text-align: center;
}
.ex-opt:hover { border-color: var(--rose); background: #FFF5F7; transform: scale(1.03); }
.ex-opt.correct { border-color: var(--mint-deep); background: #E8F5EE; pointer-events: none; }
.ex-opt.wrong { border-color: var(--coral); background: #FDE8E5; animation: shake .4s; }
.ex-opt.dim { opacity: .45; pointer-events: none; }

/* Guide chain — sequential unlock */
.guide-chain { margin-top: 18px; }
.guide-item {
  margin-bottom: 12px; border-radius: 16px; overflow: hidden;
  border: 2.5px solid #e8e0d8; transition: .3s;
}
.guide-item.unlocked { border-color: var(--sky); }
.guide-q {
  padding: 14px 18px; font-size: 16px; font-weight: 700;
  cursor: pointer; display: flex; align-items: center; gap: 10px;
  transition: .3s; color: var(--muted);
}
.guide-item.unlocked .guide-q { color: var(--dark); background: rgba(167,203,232,.12); }
.guide-item.unlocked .guide-q:hover { background: rgba(167,203,232,.25); }
.guide-a {
  max-height: 0; overflow: hidden; transition: max-height .4s;
  font-size: 16px; line-height: 1.8; color: #5A4A3F;
  background: rgba(253,246,240,.6);
}
.guide-a.open { max-height: 350px; padding: 14px 18px; }
.guide-lock { font-size: 12px; color: var(--light-muted); margin-left: auto; }
```

## 6. Feynman Box

```css
.feynman-box {
  margin-top: 18px; border-radius: 20px; overflow: hidden;
  border: 3px solid var(--mint); display: none;
}
.feynman-box.show { display: block; animation: fi .5s; }
.feynman-hdr {
  background: linear-gradient(135deg, var(--mint), var(--mint-deep));
  padding: 16px 20px; color: #fff; font-weight: 900; font-size: 18px;
}
.feynman-body { padding: 20px; }
.feynman-step { display: flex; gap: 12px; align-items: flex-start; margin-bottom: 12px; }
.feynman-step .fn {
  width: 32px; height: 32px; border-radius: 50%;
  background: var(--mint);
  display: flex; align-items: center; justify-content: center;
  font-weight: 900; font-size: 14px; color: #fff; flex-shrink: 0;
}
.feynman-step .fc {
  background: rgba(168,216,203,.15); border-radius: 14px;
  padding: 12px 16px; flex: 1; font-size: 16px; line-height: 1.7;
}
```

## 7. Quiz Components

```css
.quiz-sec {
  background: linear-gradient(135deg, rgba(197,179,217,.2), rgba(244,167,187,.15));
  border-radius: 24px; padding: 28px; margin-bottom: 24px;
  border: 3px solid var(--lilac);
}
.quiz-q { font-size: 18px; font-weight: 700; margin: 16px 0 12px; line-height: 1.8; }
.qopts { display: grid; grid-template-columns: 1fr 1fr; gap: 10px; }
.qopt {
  padding: 14px; border-radius: 14px;
  border: 2.5px solid #d8d0c8; background: #fff;
  font-size: 17px; font-weight: 700; cursor: pointer;
  transition: .3s; text-align: center;
}
.qopt:hover { border-color: var(--lilac); background: rgba(197,179,217,.1); transform: scale(1.03); }
.qopt.correct { border-color: var(--mint-deep); background: #E8F5EE; }
.qopt.wrong { border-color: #F0988C; background: #FDE8E5; }
.qopt.dis { pointer-events: none; opacity: .55; }

.qfb {
  margin-top: 12px; padding: 14px; border-radius: 14px;
  font-size: 16px; font-weight: 700; display: none; line-height: 1.7;
}
.qfb.show { display: block; animation: fi .3s; }
.qfb.ok { background: rgba(168,216,203,.25); color: #2E6B52; }
.qfb.no { background: rgba(249,228,167,.3); color: #8B6914; }

/* Progress dots */
.qnav { display: flex; justify-content: center; gap: 6px; margin-top: 14px; flex-wrap: wrap; }
.qdot { width: 11px; height: 11px; border-radius: 50%; background: #d8d0c8; transition: .3s; cursor: pointer; }
.qdot.done { background: var(--mint); }
.qdot.cur { background: var(--lilac); transform: scale(1.35); }

/* Stars */
.star { font-size: 22px; transition: .3s; }
.star.on { animation: sp .5s; }

/* Nav button */
.nbtn {
  display: none; /* shown via .show class */
  align-items: center; gap: 5px;
  padding: 11px 22px; border-radius: 50px; border: none;
  color: #fff; font-size: 15px; font-weight: 700;
  cursor: pointer; margin-top: 12px; transition: .3s;
}
.nbtn.show { display: inline-flex; }
.nbtn:hover { transform: scale(1.06); }
```

## 8. Animations

```css
@keyframes fi { from { opacity: 0; transform: translateY(10px); } to { opacity: 1; transform: none; } }
@keyframes pu { 0%, 100% { opacity: 1; } 50% { opacity: .5; } }
@keyframes shake { 0%, 100% { transform: translateX(0); } 25% { transform: translateX(-6px); } 75% { transform: translateX(6px); } }
@keyframes sp { 0% { transform: scale(0); } 50% { transform: scale(1.4); } 100% { transform: scale(1); } }
@keyframes fl { 0%, 100% { transform: translateY(0) rotate(0); } 50% { transform: translateY(-14px) rotate(8deg); } }
```

## 9. Hero & Navigation

```css
.hero {
  background: linear-gradient(135deg, var(--rose) 0%, var(--lemon) 40%, var(--mint) 70%, var(--sky) 100%);
  padding: 50px 24px 64px; text-align: center;
  position: relative; overflow: hidden;
}
.hero::after {
  content: ''; position: absolute; bottom: -2px; left: 0; right: 0;
  height: 40px; background: var(--bg);
  border-radius: 50% 50% 0 0 / 100% 100% 0 0;
}
.hero h1 {
  font-size: clamp(32px, 7vw, 52px); color: #fff;
  text-shadow: 2px 3px 0 rgba(74,55,40,.12);
}

/* Floating emoji decorations */
.ef {
  position: absolute; font-size: 36px;
  animation: fl 4s ease-in-out infinite; opacity: .6;
}

/* Pill navigation */
.nav { display: flex; gap: 8px; padding: 20px 0; overflow-x: auto; scrollbar-width: none; }
.nav::-webkit-scrollbar { display: none; }
.pill {
  flex-shrink: 0; padding: 12px 22px; border-radius: 50px;
  border: 2.5px solid var(--rose); background: #fff;
  color: var(--rose-deep); font-weight: 700; font-size: 16px;
  cursor: pointer; transition: .3s; white-space: nowrap;
}
.pill:hover, .pill.on {
  background: var(--rose); color: #fff;
  transform: scale(1.05); border-color: var(--rose);
}

@media (max-width: 600px) {
  .qopts, .ex-opts { grid-template-columns: 1fr; }
  .exbody, .card { padding: 20px; }
}
```
