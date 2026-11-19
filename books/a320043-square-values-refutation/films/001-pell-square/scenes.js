'use strict';
FILM.hud = false;
function heading(en, zh) {
  txt(en, 120, 195, {size: 46, fam: F.disp, w: 700, c: C.white});
  txt(zh, 120, 245, {size: 30, fam: F.zh, c: C.cyan});
}
function formula(s, y, colour=C.white, alpha=1, size=42, x=W / 2) {
  txt(s, x, y, {size, fam: F.math, align: 'center', c: colour, a: alpha});
}
function footer() { txt('Haobo Ma · Wenlin Zhang', 120, 930, {size: 24, fam: F.disp, c: C.dim}); }
SCENES.question = S => {
  heading('ANOTHER SQUARE', '三个之外，还有平方值');
  panel(130, 300, 1660, 410, 1, C.cyan, 'OEIS A320043');
  formula('a(n) = Σ (n + 1 − k)² k / gcd(n + 1 − k, k)³', 420, C.white, at(S, 0, 0.8), 38);
  formula('1 = 1²      196 = 14²      7,376,656 = 2,716²', 535, C.cyan, at(S, 0, 0.8, 2), 38);
  formula('n = 708,158,976', 655, C.now, at(S, 1, 0.8), 56);
  badgeQ(S, [[1, 'another square', 'computed']]);
  footer();
};
SCENES.prime_row = S => {
  heading('PRIME ROWS REMOVE THE GCDs', '素数行消去最大公因数');
  panel(120, 285, 1680, 460, 1, C.cyan, 'p PRIME, n = p − 1');
  formula('gcd(p − k, k) = 1', 390, C.cyan, at(S, 0, 0.7), 52);
  formula('a(p − 1) = Σₖ₌₁ᵖ⁻¹ (p − k)² k', 505, C.white, at(S, 1, 0.8), 43);
  formula('a(p − 1) = p²(p² − 1) / 12', 635, C.now, at(S, 1, 0.8, 2), 56);
  formula('p² − 12y² = 1  ⇒  a(p − 1) = (py)²', 705, C.argued, at(S, 2, 0.8), 38);
  badgeQ(S, [[0, 'Every denominator disappears', 'computed'], [2, 'p squared minus 12 y squared equals 1', 'argued']]);
  footer();
};
SCENES.pell = S => {
  heading('THE PELL ENGINE', 'Pell 递推引擎');
  panel(120, 280, 1680, 480, 1, C.mag, 'DESCENT');
  formula('x² − 12y² = 1', 390, C.white, at(S, 0, 0.7), 60);
  formula('(x,y) ↦ (7x − 24y, 7y − 2x)', 520, C.cyan, at(S, 1, 0.8), 42);
  formula('xₜ + yₜ√12 = (7 + 2√12)ᵗ', 645, C.now, at(S, 1, 0.8, 2), 48);
  formula('x₀ = 1,  x₁ = 7,  xₜ₊₂ = 14xₜ₊₁ − xₜ', 715, C.argued, at(S, 2, 0.8), 36);
  badgeQ(S, [[1, 'preserving the equation', 'argued'], [2, 'lists every prime-successor candidate', 'computed']]);
  footer();
};
SCENES.certificate = S => {
  heading('THE WITNESS AND A REJECTED CANDIDATE', '见证与被排除的候选');
  panel(120, 270, 780, 500, 1, C.cyan, 'PELL TERMS');
  const vals = ['7', '97', '1351 = 7·193', '18817 = 31·607', '708158977'];
  vals.forEach((v, i) => txt(v, 185, 375 + i * 72, {size: i === 4 ? 34 : 31, fam: F.mono, c: i === 4 ? C.now : C.white, a: at(S, 0, 0.5, i * 0.7)}));
  panel(970, 270, 830, 500, 1, C.argued, 'FINITE CHECK');
  formula('p = 708,158,977', 380, C.now, at(S, 0, 0.7), 42, 1385);
  formula('py = 144,767,444,036,350,576', 485, C.cyan, at(S, 1, 0.8), 32, 1385);
  formula('1310719 ∣ r₆₅₅₃₆', 625, C.argued, at(S, 2, 0.8), 46, 1385);
  formula('candidate is composite', 700, C.open, at(S, 2, 0.8, 2), 32, 1385);
  badgeQ(S, [[1, 'Multiplying p by y', 'computed'], [2, 'rules out the proposed candidate', 'argued']]);
  footer();
};
SCENES.boundary = S => {
  heading('WHAT IS CHECKED?', '哪些内容已检查？');
  panel(120, 300, 1680, 390, 1, C.lean, 'FORMAL SCOPE');
  formula('Three-index rule disproved', 420, C.lean, at(S, 0, 0.8), 58);
  formula('Written: Pell criterion · minimality · product · divisor formula', 550, C.argued, at(S, 0, 0.8, 2), 33);
  formula('Open: all square indices · infinitely many Pell primes', 650, C.open, at(S, 1, 0.8), 34);
  badgeQ(S, [[0, 'Lean proof checks', 'lean'], [1, 'does not classify every square index', 'open']]);
  footer();
};
FILM.poster = () => {
  ctx.fillStyle = C.bg; ctx.fillRect(0, 0, W, H);
  heading('PELL NUMBERS AND THE COUNTEREXAMPLE', 'Pell 数与反例');
  panel(120, 300, 1680, 410, 1, C.cyan, 'OEIS A320043');
  formula('a(p − 1) = p²(p² − 1) / 12', 430, C.white, 1, 52);
  formula('p² − 12y² = 1  ⇒  a(p − 1) = (py)²', 555, C.now, 1, 43);
  formula('a(708,158,976) = 144,767,444,036,350,576²', 665, C.cyan, 1, 33);
  txt('Haobo Ma · Wenlin Zhang', 120, 930, {size: 28, fam: F.disp, c: C.white});
};
