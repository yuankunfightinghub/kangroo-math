// ════════════════════════════════════════════════════════════════
//  模拟练习题数据
//  共 6 套，每套 24 题（1★×5 + 2★×5 + 3★×5 + 4★×5 + 5★×4）
//  题目来源：185道历年未作答真题 + 32道错题改编题
//  type: 'real' = 真题原图  |  'adapted' = 改编文字题
// ════════════════════════════════════════════════════════════════

const PRACTICE_PAPERS = [
  // ── 第一套 ──────────────────────────────────────────────────
  [
    {year:2013,qnum:1,star:1,ans:null,type:'real',img:'../src/assets/exam-images/2013/q01.png'},
    {year:2023,qnum:2,star:1,ans:null,type:'real',img:'../src/assets/exam-images/2023/q02.png'},
    {year:2025,qnum:2,star:1,ans:null,type:'real',img:'../src/assets/exam-images/2025/q02.png'},
    {year:2015,qnum:4,star:1,ans:null,type:'real',img:'../src/assets/exam-images/2015/q04.png'},
    {year:2019,qnum:4,star:1,ans:null,type:'real',img:'../src/assets/exam-images/2019/q04.png'},
    {year:2014,qnum:6,star:2,ans:null,type:'real',img:'../src/assets/exam-images/2014/q06.png'},
    {year:2015,qnum:6,star:2,ans:null,type:'real',img:'../src/assets/exam-images/2015/q06.png'},
    {year:2024,qnum:8,star:2,ans:null,type:'real',img:'../src/assets/exam-images/2024/q08.png'},
    {year:2020,qnum:8,star:2,ans:null,type:'real',img:'../src/assets/exam-images/2020/q08.png'},
    {year:2015,qnum:8,star:2,ans:null,type:'real',img:'../src/assets/exam-images/2015/q08.png'},
    {year:2020,qnum:15,star:3,ans:null,type:'real',img:'../src/assets/exam-images/2020/q15.png'},
    {year:2021,qnum:13,star:3,ans:null,type:'real',img:'../src/assets/exam-images/2021/q13.png'},
    {year:2016,qnum:11,star:3,ans:null,type:'real',img:'../src/assets/exam-images/2016/q11.png'},
    {year:2025,qnum:15,star:3,ans:null,type:'real',img:'../src/assets/exam-images/2025/q15.png'},
    {year:2025,qnum:13,star:3,ans:null,type:'real',img:'../src/assets/exam-images/2025/q13.png'},
    {year:2025,qnum:20,star:4,ans:null,type:'real',img:'../src/assets/exam-images/2025/q20.png'},
    {year:2013,qnum:14,star:4,ans:null,type:'real',img:'../src/assets/exam-images/2013/q14.png'},
    {year:2024,qnum:17,star:4,ans:null,type:'real',img:'../src/assets/exam-images/2024/q17.png'},
    {year:2016,qnum:15,star:4,ans:null,type:'real',img:'../src/assets/exam-images/2016/q15.png'},
    {year:2015,qnum:19,star:4,ans:null,type:'real',img:'../src/assets/exam-images/2015/q19.png'},
    {year:2017,qnum:18,star:5,ans:null,type:'real',img:'../src/assets/exam-images/2017/q18.png'},
    {year:2016,qnum:18,star:5,ans:null,type:'real',img:'../src/assets/exam-images/2016/q18.png'},
    {year:2020,qnum:24,star:5,ans:null,type:'real',img:'../src/assets/exam-images/2020/q24.png'},
    {year:2015,qnum:24,star:5,ans:null,type:'real',img:'../src/assets/exam-images/2015/q24.png'},
  ],

  // ── 第二套 ──────────────────────────────────────────────────
  [
    {year:2015,qnum:3,star:1,ans:null,type:'real',img:'../src/assets/exam-images/2015/q03.png'},
    {year:2013,qnum:4,star:1,ans:null,type:'real',img:'../src/assets/exam-images/2013/q04.png'},
    {year:2020,qnum:5,star:1,ans:null,type:'real',img:'../src/assets/exam-images/2020/q05.png'},
    {year:2022,qnum:4,star:1,ans:null,type:'real',img:'../src/assets/exam-images/2022/q04.png'},
    {year:2023,qnum:3,star:1,ans:null,type:'real',img:'../src/assets/exam-images/2023/q03.png'},
    {year:2020,qnum:10,star:2,ans:null,type:'real',img:'../src/assets/exam-images/2020/q10.png'},
    {year:2020,qnum:6,star:2,ans:null,type:'real',img:'../src/assets/exam-images/2020/q06.png'},
    {year:2015,qnum:10,star:2,ans:null,type:'real',img:'../src/assets/exam-images/2015/q10.png'},
    {year:2021,qnum:6,star:2,ans:null,type:'real',img:'../src/assets/exam-images/2021/q06.png'},
    {year:2022,qnum:6,star:2,ans:null,type:'real',img:'../src/assets/exam-images/2022/q06.png'},
    {year:2020,qnum:12,star:3,ans:null,type:'real',img:'../src/assets/exam-images/2020/q12.png'},
    {year:2023,qnum:12,star:3,ans:null,type:'real',img:'../src/assets/exam-images/2023/q12.png'},
    {year:2013,qnum:10,star:3,ans:null,type:'real',img:'../src/assets/exam-images/2013/q10.png'},
    {year:2014,qnum:10,star:3,ans:null,type:'real',img:'../src/assets/exam-images/2014/q10.png'},
    {year:2025,qnum:12,star:3,ans:null,type:'real',img:'../src/assets/exam-images/2025/q12.png'},
    {year:2025,qnum:19,star:4,ans:null,type:'real',img:'../src/assets/exam-images/2025/q19.png'},
    {year:2022,qnum:16,star:4,ans:null,type:'real',img:'../src/assets/exam-images/2022/q16.png'},
    {year:2025,qnum:16,star:4,ans:null,type:'real',img:'../src/assets/exam-images/2025/q16.png'},
    {year:2013,qnum:15,star:4,ans:null,type:'real',img:'../src/assets/exam-images/2013/q15.png'},
    {year:2022,qnum:20,star:4,ans:null,type:'real',img:'../src/assets/exam-images/2022/q20.png'},
    {year:2015,qnum:23,star:5,ans:null,type:'real',img:'../src/assets/exam-images/2015/q23.png'},
    {year:2014,qnum:20,star:5,ans:null,type:'real',img:'../src/assets/exam-images/2014/q20.png'},
    {year:2024,qnum:23,star:5,ans:null,type:'real',img:'../src/assets/exam-images/2024/q23.png'},
    {year:2019,qnum:24,star:5,ans:null,type:'real',img:'../src/assets/exam-images/2019/q24.png'},
  ],

  // ── 第三套 ──────────────────────────────────────────────────
  [
    {year:2014,qnum:4,star:1,ans:null,type:'real',img:'../src/assets/exam-images/2014/q04.png'},
    {year:2019,qnum:1,star:1,ans:null,type:'real',img:'../src/assets/exam-images/2019/q01.png'},
    {year:2021,qnum:1,star:1,ans:null,type:'real',img:'../src/assets/exam-images/2021/q01.png'},
    {year:2014,qnum:2,star:1,ans:null,type:'real',img:'../src/assets/exam-images/2014/q02.png'},
    {year:2024,qnum:4,star:1,ans:null,type:'real',img:'../src/assets/exam-images/2024/q04.png'},
    {year:2021,qnum:7,star:2,ans:null,type:'real',img:'../src/assets/exam-images/2021/q07.png'},
    {year:2019,qnum:6,star:2,ans:null,type:'real',img:'../src/assets/exam-images/2019/q06.png'},
    {year:2019,qnum:10,star:2,ans:null,type:'real',img:'../src/assets/exam-images/2019/q10.png'},
    {year:2018,qnum:5,star:2,ans:null,type:'real',img:'../src/assets/exam-images/2018/q05.png'},
    {year:2019,qnum:7,star:2,ans:null,type:'real',img:'../src/assets/exam-images/2019/q07.png'},
    {year:2013,qnum:12,star:3,ans:null,type:'real',img:'../src/assets/exam-images/2013/q12.png'},
    {year:2025,qnum:11,star:3,ans:null,type:'real',img:'../src/assets/exam-images/2025/q11.png'},
    {year:2018,qnum:11,star:3,ans:null,type:'real',img:'../src/assets/exam-images/2018/q11.png'},
    {year:2014,qnum:12,star:3,ans:null,type:'real',img:'../src/assets/exam-images/2014/q12.png'},
    {year:2021,qnum:14,star:3,ans:null,type:'real',img:'../src/assets/exam-images/2021/q14.png'},
    {year:2016,qnum:14,star:4,ans:null,type:'real',img:'../src/assets/exam-images/2016/q14.png'},
    {year:2018,qnum:14,star:4,ans:null,type:'real',img:'../src/assets/exam-images/2018/q14.png'},
    {year:2018,qnum:13,star:4,ans:null,type:'real',img:'../src/assets/exam-images/2018/q13.png'},
    {year:2024,qnum:18,star:4,ans:null,type:'real',img:'../src/assets/exam-images/2024/q18.png'},
    {year:2021,qnum:19,star:4,ans:null,type:'real',img:'../src/assets/exam-images/2021/q19.png'},
    {year:2022,qnum:21,star:5,ans:null,type:'real',img:'../src/assets/exam-images/2022/q21.png'},
    {year:2025,qnum:23,star:5,ans:null,type:'real',img:'../src/assets/exam-images/2025/q23.png'},
    {year:2013,qnum:18,star:5,ans:null,type:'real',img:'../src/assets/exam-images/2013/q18.png'},
    {year:2020,qnum:22,star:5,ans:null,type:'real',img:'../src/assets/exam-images/2020/q22.png'},
  ],

  // ── 第四套 ──────────────────────────────────────────────────
  [
    {year:2013,qnum:2,star:1,ans:null,type:'real',img:'../src/assets/exam-images/2013/q02.png'},
    {year:2022,qnum:1,star:1,ans:null,type:'real',img:'../src/assets/exam-images/2022/q01.png'},
    {year:2020,qnum:3,star:1,ans:null,type:'real',img:'../src/assets/exam-images/2020/q03.png'},
    {year:2025,qnum:3,star:1,ans:null,type:'real',img:'../src/assets/exam-images/2025/q03.png'},
    {year:2014,qnum:1,star:1,ans:null,type:'real',img:'../src/assets/exam-images/2014/q01.png'},
    {year:2025,qnum:7,star:2,ans:null,type:'real',img:'../src/assets/exam-images/2025/q07.png'},
    {year:2020,qnum:7,star:2,ans:null,type:'real',img:'../src/assets/exam-images/2020/q07.png'},
    {year:2017,qnum:7,star:2,ans:null,type:'real',img:'../src/assets/exam-images/2017/q07.png'},
    {year:2013,qnum:7,star:2,ans:null,type:'real',img:'../src/assets/exam-images/2013/q07.png'},
    {year:2021,qnum:9,star:2,ans:null,type:'real',img:'../src/assets/exam-images/2021/q09.png'},
    {year:2022,qnum:14,star:3,ans:null,type:'real',img:'../src/assets/exam-images/2022/q14.png'},
    {year:2023,qnum:14,star:3,ans:null,type:'real',img:'../src/assets/exam-images/2023/q14.png'},
    {year:2015,qnum:14,star:3,ans:null,type:'real',img:'../src/assets/exam-images/2015/q14.png'},
    {year:2020,qnum:13,star:3,ans:null,type:'real',img:'../src/assets/exam-images/2020/q13.png'},
    {year:2023,qnum:15,star:3,ans:null,type:'real',img:'../src/assets/exam-images/2023/q15.png'},
    {year:2023,qnum:16,star:4,ans:null,type:'real',img:'../src/assets/exam-images/2023/q16.png'},
    {year:2021,qnum:18,star:4,ans:null,type:'real',img:'../src/assets/exam-images/2021/q18.png'},
    {year:2025,qnum:17,star:4,ans:null,type:'real',img:'../src/assets/exam-images/2025/q17.png'},
    {year:2014,qnum:16,star:4,ans:null,type:'real',img:'../src/assets/exam-images/2014/q16.png'},
    {year:2016,qnum:16,star:4,ans:null,type:'real',img:'../src/assets/exam-images/2016/q16.png'},
    {year:2020,qnum:23,star:5,ans:null,type:'real',img:'../src/assets/exam-images/2020/q23.png'},
    {year:2021,qnum:21,star:5,ans:null,type:'real',img:'../src/assets/exam-images/2021/q21.png'},
    {year:2024,qnum:22,star:5,ans:null,type:'real',img:'../src/assets/exam-images/2024/q22.png'},
    {year:2024,qnum:21,star:5,ans:null,type:'real',img:'../src/assets/exam-images/2024/q21.png'},
  ],

  // ── 第五套 ──────────────────────────────────────────────────
  [
    {year:2019,qnum:3,star:1,ans:null,type:'real',img:'../src/assets/exam-images/2019/q03.png'},
    {year:2017,qnum:3,star:1,ans:null,type:'real',img:'../src/assets/exam-images/2017/q03.png'},
    {year:2021,qnum:2,star:1,ans:null,type:'real',img:'../src/assets/exam-images/2021/q02.png'},
    {year:2014,qnum:3,star:1,ans:null,type:'real',img:'../src/assets/exam-images/2014/q03.png'},
    {year:2020,qnum:2,star:1,ans:null,type:'real',img:'../src/assets/exam-images/2020/q02.png'},
    {year:2014,qnum:5,star:2,ans:null,type:'real',img:'../src/assets/exam-images/2014/q05.png'},
    {year:2024,qnum:6,star:2,ans:null,type:'real',img:'../src/assets/exam-images/2024/q06.png'},
    {year:2017,qnum:5,star:2,ans:null,type:'real',img:'../src/assets/exam-images/2017/q05.png'},
    {year:2025,qnum:8,star:2,ans:null,type:'real',img:'../src/assets/exam-images/2025/q08.png'},
    {year:2016,qnum:7,star:2,ans:null,type:'real',img:'../src/assets/exam-images/2016/q07.png'},
    {year:2018,qnum:12,star:3,ans:null,type:'real',img:'../src/assets/exam-images/2018/q12.png'},
    {year:2024,qnum:15,star:3,ans:null,type:'real',img:'../src/assets/exam-images/2024/q15.png'},
    {year:2020,qnum:11,star:3,ans:null,type:'real',img:'../src/assets/exam-images/2020/q11.png'},
    {year:2025,qnum:14,star:3,ans:null,type:'real',img:'../src/assets/exam-images/2025/q14.png'},
    {year:2015,qnum:13,star:3,ans:null,type:'real',img:'../src/assets/exam-images/2015/q13.png'},
    {year:2022,qnum:17,star:4,ans:null,type:'real',img:'../src/assets/exam-images/2022/q17.png'},
    {year:2018,qnum:16,star:4,ans:null,type:'real',img:'../src/assets/exam-images/2018/q16.png'},
    {year:2021,qnum:16,star:4,ans:null,type:'real',img:'../src/assets/exam-images/2021/q16.png'},
    {year:2020,qnum:17,star:4,ans:null,type:'real',img:'../src/assets/exam-images/2020/q17.png'},
    {year:2017,qnum:15,star:4,ans:null,type:'real',img:'../src/assets/exam-images/2017/q15.png'},
    {year:2025,qnum:24,star:5,ans:null,type:'real',img:'../src/assets/exam-images/2025/q24.png'},
    {year:2013,qnum:17,star:5,ans:null,type:'real',img:'../src/assets/exam-images/2013/q17.png'},
    {year:2017,qnum:19,star:5,ans:null,type:'real',img:'../src/assets/exam-images/2017/q19.png'},
    {year:2018,qnum:19,star:5,ans:null,type:'real',img:'../src/assets/exam-images/2018/q19.png'},
  ],

  // ── 第六套 ──────────────────────────────────────────────────
  [
    {year:2020,qnum:1,star:1,ans:null,type:'real',img:'../src/assets/exam-images/2020/q01.png'},
    {year:2013,qnum:3,star:1,ans:null,type:'real',img:'../src/assets/exam-images/2013/q03.png'},
    {year:2024,qnum:1,star:1,ans:null,type:'real',img:'../src/assets/exam-images/2024/q01.png'},
    {year:2015,qnum:5,star:1,ans:null,type:'real',img:'../src/assets/exam-images/2015/q05.png'},
    {year:2025,qnum:1,star:1,ans:null,type:'real',img:'../src/assets/exam-images/2025/q01.png'},
    {year:2020,qnum:9,star:2,ans:null,type:'real',img:'../src/assets/exam-images/2020/q09.png'},
    {year:2018,qnum:6,star:2,ans:null,type:'real',img:'../src/assets/exam-images/2018/q06.png'},
    {year:2019,qnum:8,star:2,ans:null,type:'real',img:'../src/assets/exam-images/2019/q08.png'},
    {year:2017,qnum:2,star:2,ans:null,type:'real',img:'../src/assets/exam-images/2017/q02.png'},
    {year:2016,qnum:2,star:2,ans:null,type:'real',img:'../src/assets/exam-images/2016/q02.png'},
    {year:2022,qnum:12,star:3,ans:null,type:'real',img:'../src/assets/exam-images/2022/q12.png'},
    {year:2024,qnum:14,star:3,ans:null,type:'real',img:'../src/assets/exam-images/2024/q14.png'},
    {year:2021,qnum:15,star:3,ans:null,type:'real',img:'../src/assets/exam-images/2021/q15.png'},
    {year:2020,qnum:14,star:3,ans:null,type:'real',img:'../src/assets/exam-images/2020/q14.png'},
    {year:2019,qnum:13,star:3,ans:null,type:'real',img:'../src/assets/exam-images/2019/q13.png'},
    {year:2021,qnum:20,star:4,ans:null,type:'real',img:'../src/assets/exam-images/2021/q20.png'},
    {year:2020,qnum:16,star:4,ans:null,type:'real',img:'../src/assets/exam-images/2020/q16.png'},
    {year:2022,qnum:19,star:4,ans:null,type:'real',img:'../src/assets/exam-images/2022/q19.png'},
    {year:2017,qnum:13,star:4,ans:null,type:'real',img:'../src/assets/exam-images/2017/q13.png'},
    {year:2017,qnum:16,star:4,ans:null,type:'real',img:'../src/assets/exam-images/2017/q16.png'},
    {year:2022,qnum:24,star:5,ans:null,type:'real',img:'../src/assets/exam-images/2022/q24.png'},
    {year:2018,qnum:17,star:5,ans:null,type:'real',img:'../src/assets/exam-images/2018/q17.png'},
    {year:2023,qnum:24,star:5,ans:null,type:'real',img:'../src/assets/exam-images/2023/q24.png'},
    {year:2024,qnum:24,star:5,ans:null,type:'real',img:'../src/assets/exam-images/2024/q24.png'},
  ],
];

// ════════════════════════════════════════════════════════════════
//  改编题数据（错题知识点改编，文字题）
//  共32道，独立于真题套卷，作为附加练习
// ════════════════════════════════════════════════════════════════
const ADAPTED_QUESTIONS = [
  // ── 1★ 改编题（原错题：1-2星，换成生活化场景）──────────
  {
    id:'W01', star:1, category:'立体图形·格子计数',
    text:'小明在方格纸上浇花，不小心把水浇到了旁边的格子上。如图所示，水从水桶溢出后，共沾湿了多少个完整的小方格？',
    hint:'提示：数一数被水完整覆盖的小格子数量，边缘不完整的不算。',
    options:['A. 14','B. 16','C. 18','D. 19','E. 20'],
    ans:2, ansLetter:'C',
    origin:'2022 Q08 — 方格纸墨水格子计数'
  },
  {
    id:'W02', star:1, category:'立体图形·缺失计数',
    text:'邻居家正在用相同的小砖块砌一道圆弧形花坛挡墙，如图所示，墙还没砌完，有几个位置空着。请问还缺几块这样形状的砖才能砌完？',
    hint:'提示：数一数弧形中还没有填满的空位。',
    options:['A. 6','B. 7','C. 8','D. 9','E. 10'],
    ans:2, ansLetter:'C',
    origin:'2017 Q06 — 冰屋缺砖计数'
  },
  {
    id:'W03', star:1, category:'逻辑推理·集合排除',
    text:'小区超市门口的招牌上写着"蔬菜水果"四个字，但招牌上还混杂了很多其他字。请问下面哪个字【不在】"蔬菜水果"这四个字里？',
    hint:'提示：先确认"蔬"、"菜"、"水"、"果"这四个字，再找选项中不属于这四个字的那个。',
    options:['A. 蔬','B. 果','C. 花','D. 菜','E. 水'],
    ans:2, ansLetter:'C',
    origin:'2016 Q01 — 黑板字母KOALA排除'
  },
  {
    id:'W04', star:1, category:'逻辑推理·图形共同元素',
    text:'公园里有四个路口，每个路口各放了三种路障形状：有圆形、三角形、正方形、菱形。请问下面哪种形状在【每个路口都出现过】？\n（A路口：圆形、三角形、正方形；B路口：三角形、菱形、正方形；C路口：圆形、三角形、菱形；D路口：三角形、正方形、菱形）',
    hint:'提示：找出在A、B、C、D四个路口都出现的形状。',
    options:['A. 圆形','B. 三角形','C. 正方形','D. 菱形','E. 以上都有'],
    ans:1, ansLetter:'B',
    origin:'2015 Q01 — 四图公共图形'
  },
  {
    id:'W05', star:1, category:'图形计数·嵌套三角形',
    text:'爸爸给小华做了一个由三角形拼成的风筝图案，如图所示。请问这个风筝图案里，一共有多少个三角形？（包括大的、小的、以及由小三角形拼成的大三角形，全部都要数进去）',
    hint:'提示：先数最小的三角形，再数由2个、3个小三角形组成的更大三角形，别重复也别遗漏。',
    options:['A. 4','B. 5','C. 6','D. 7','E. 8'],
    ans:3, ansLetter:'D',
    origin:'2015 Q02 — 人物图案三角形计数'
  },
  {
    id:'W06', star:1, category:'数与运算·两步计算',
    text:'妈妈从超市买回10个苹果，她把其中4个分给了邻居，然后又把剩下苹果的一半放进了冰箱。请问冰箱里放了几个苹果？',
    hint:'提示：第一步算分给邻居后还剩多少，第二步算剩下的一半是多少。',
    options:['A. 2','B. 3','C. 4','D. 5','E. 6'],
    ans:1, ansLetter:'B',
    origin:'2025 Q05 — 气球两步运算'
  },
  {
    id:'W07', star:1, category:'路径方向·转向追踪',
    text:'小明在方格公园里散步，他从入口出发：先向北走3格，再向右转走2格，再向前走2格，然后向左转走3格。请问小明现在面朝哪个方向？',
    hint:'提示：画一画，追踪每次转向后的朝向。向右转=顺时针转90°，向左转=逆时针转90°。',
    options:['A. 东','B. 南','C. 西','D. 北','E. 无法确定'],
    ans:3, ansLetter:'D',
    origin:'2023 Q08 — 迷宫路径方向'
  },
  {
    id:'W08', star:1, category:'图形组合·计数',
    text:'园艺师傅用特殊的五瓣花形砖铺花坛，左图是一块花形砖的形状，右图是用这种砖铺成的一小块花坛图案。请问右图中一共用了多少块花形砖？',
    hint:'提示：仔细数一数，每一块花形砖只算一次，注意被其他砖遮住的部分。',
    options:['A. 5','B. 6','C. 7','D. 8','E. 9'],
    ans:2, ansLetter:'C',
    origin:'2018 Q03 — 四角星拼图计数'
  },
  {
    id:'W09', star:1, category:'立体图形·格子缺失',
    text:'奶奶织了一块5×5方格的毛毯，但因为中间有几处断线，部分格子没有织出来（如图，空白格子表示没织出来）。请问这块毛毯里有多少个小方格【没有】织出来？',
    hint:'提示：数一数图中的空白格子数量。',
    options:['A. 6','B. 7','C. 8','D. 9','E. 10'],
    ans:2, ansLetter:'C',
    origin:'2014 Q07 — 25格大正方形缺失格'
  },

  // ── 2★ 改编题（保留考察点，换场景+数字）──────────────
  {
    id:'W10', star:2, category:'平面图形·旋转规律',
    text:'小陀螺比赛中，裁判给一个风车形状的陀螺拍摄了旋转中的3张照片（每次旋转角度相同）。照片1、2、3如图所示。请问第6次旋转后，陀螺看起来是哪种样子？',
    hint:'提示：找出旋转规律，每次转多少度？6次后相当于转了几圈或剩多少角度？',
    options:['A. 样子A','B. 样子B','C. 样子C','D. 样子D','E. 样子E'],
    ans:3, ansLetter:'D',
    origin:'2017 Q11 — 形状旋转6次后样子'
  },
  {
    id:'W11', star:2, category:'平面图形·剪拼',
    text:'妈妈把一块正方形饼干按如图所示切成了4块。下面哪种形状【不能】用这4块饼干拼成？（饼干块可以翻转和旋转，但不能重叠）',
    hint:'提示：4块拼在一起面积是固定的，先排除面积不对的选项。再思考哪种形状用这4块无法凑成。',
    options:['A. 长方形','B. 平行四边形','C. 三角形','D. T形','E. L形'],
    ans:3, ansLetter:'D',
    origin:'2014 Q11 — 正方形4块拼图'
  },
  {
    id:'W12', star:2, category:'立体图形·表面积',
    text:'小朋友用5个完全相同的小木块粘在一起做礼物盒模型，要给模型外表面全部涂上颜色。下面哪种摆法需要涂色的面【最少】？（粘在一起的面不用涂）',
    hint:'提示：两个木块粘在一起，各自少涂1面，共少涂2面。木块摆得越紧凑，粘合面越多，涂色面越少。',
    options:['A. 一排平放','B. 正方体堆叠','C. L形摆放','D. 十字形','E. 塔形竖放'],
    ans:1, ansLetter:'B',
    origin:'2019 Q14 — 4个立方体涂色面积最小'
  },
  {
    id:'W13', star:2, category:'逻辑推理·叠放顺序',
    text:'图书馆书架上有8本书叠放在一起，第2本在最下面，第7本在最上面。从叠放图可以看出各书的压盖关系。请问第4层（从下往上数第4本）是哪本书？',
    hint:'提示：从已知的最上（7号）和最下（2号）出发，根据图中每本书的压盖关系，逐层推断出第4层是哪本。',
    options:['A. 1号','B. 3号','C. 4号','D. 5号','E. 6号'],
    ans:3, ansLetter:'D',
    origin:'2014 Q15 — 7根棍叠放中间是哪根'
  },
  {
    id:'W14', star:2, category:'路径方向·折纸剪切',
    text:'小明把一张纸对折两次，然后剪了两刀，如图所示。把纸展开后，这张纸被分成了多少张？',
    hint:'提示：对折一次，一刀会剪出2个切口；对折两次，一刀会剪出4个切口。仔细分析每一刀展开后的效果。',
    options:['A. 3','B. 4','C. 5','D. 6','E. 8'],
    ans:2, ansLetter:'C',
    origin:'2019 Q12 — Patricia折纸剪出几张'
  },
  {
    id:'W15', star:2, category:'路径方向·最短路径',
    text:'博物馆里有5行4列共20个展厅，每两个相邻展厅之间有一扇门。参观者从左上角的A展厅出发，想到达右下角的B展厅，请问至少需要经过多少扇门？',
    hint:'提示：从A到B，需要往右走3步、往下走4步，共7步，每步经过一扇门。',
    options:['A. 5','B. 6','C. 7','D. 8','E. 9'],
    ans:2, ansLetter:'C',
    origin:'2016 Q12 — Baby Roo最少经几扇门'
  },
  {
    id:'W16', star:2, category:'路径方向·最短路径+序列',
    text:'在方格公园里（每格1米），小兔要从起点出发，按顺序经过写有P→A→R→K四个字母的路标，最后到达终点。请问按最短路线走，共需走多少米？（P在(1,3)，A在(2,1)，R在(4,2)，K在(5,4)，终点在(6,4)，坐标从左下角算起）',
    hint:'提示：依次计算起点→P→A→R→K→终点各段的最短曼哈顿距离，然后相加。',
    options:['A. 12','B. 14','C. 16','D. 18','E. 20'],
    ans:1, ansLetter:'B',
    origin:'2014 Q13 — K到O收集KANGAROO字母最短距离'
  },
  {
    id:'W17', star:2, category:'数数策略·重叠计数',
    text:'客厅方格地板（10×10格）上铺了5块不同颜色的长方形地毯，相互有重叠。请问有多少个方格同时被【至少3块】地毯压住？（地毯位置如图所示）',
    hint:'提示：分别找出被3块、4块、5块地毯同时覆盖的格子，全部加起来。',
    options:['A. 2','B. 3','C. 4','D. 5','E. 6'],
    ans:2, ansLetter:'C',
    origin:'2025 Q10 — 方格地板4块地毯重叠计数'
  },
  {
    id:'W18', star:2, category:'数数策略·排列约束',
    text:'农场主有一个4×4的鸡蛋托盘，要放白色和棕色鸡蛋。规定：任意两个棕色鸡蛋不能挨着（上下、左右、斜角都不能相邻）。请问托盘里最多可以放几个棕色鸡蛋？',
    hint:'提示：可以用"棋盘格"方式思考，把16格分成8黑8白，棕色蛋只放在黑色格或白色格能放几个？注意斜角也不能相邻的限制会更严格。',
    options:['A. 4','B. 5','C. 6','D. 7','E. 8'],
    ans:0, ansLetter:'A',
    origin:'2016 Q09 — 母鸡棕蛋不相邻最多放几个'
  },
  {
    id:'W19', star:2, category:'数数策略·逻辑计算',
    text:'学校图书馆有14张阅览桌，每张桌子有1盏台灯和2把椅子。今天下午，共有18把椅子上有人坐。请问有多少张桌子【没有】人坐？',
    hint:'提示：18把椅子坐了人，意思是至少有几张桌子有人？（每张桌子最多坐2把椅子）然后用14减去有人的桌子数。',
    options:['A. 2','B. 3','C. 4','D. 5','E. 6'],
    ans:3, ansLetter:'D',
    origin:'2016 Q13 — 楼里房间和窗户灯的关系'
  },
  {
    id:'W20', star:2, category:'数数策略·等价换算',
    text:'跳蚤市场里的交换规则是：2个玩具车可以换5个橡皮泥，3个橡皮泥可以换4块积木。请问6个玩具车可以换多少块积木？',
    hint:'提示：先用换算规则算出6个玩具车能换多少橡皮泥，再算这些橡皮泥能换多少积木。注意换算时数量要整除。',
    options:['A. 16','B. 18','C. 20','D. 24','E. 30'],
    ans:2, ansLetter:'C',
    origin:'2017 Q09 — 宝石城宝石换花换算'
  },
  {
    id:'W21', star:2, category:'立体图形·俯视图',
    text:'小明把5个不同颜色的圆环（从大到小：红、橙、黄、绿、蓝），从大到小依次套在一根柱子上（大的在下，小的在上）。从正上方往下看，能看到几个圆环的颜色？',
    hint:'提示：最上面的蓝色最小，不会遮住其他颜色的边缘；每一个圆环都有边缘露出来，所以能看到全部颜色。',
    options:['A. 1','B. 2','C. 3','D. 4','E. 5'],
    ans:4, ansLetter:'E',
    origin:'2022 Q13 — 圆盘叠放俯视图'
  },
  {
    id:'W22', star:2, category:'度量单位·空间路径长度',
    text:'邮递员要在一个长2米、宽1米、高1米的纸箱外面绑一条丝带。丝带从底部中心出发，绕箱子一圈后回到顶部中心（如图所示），打结处再额外用1米丝带。请问丝带总共需要多少米？',
    hint:'提示：绕箱子一圈：需要经过两个宽面(各1米)和两个长面(各2米)，共2+1+2+1=6米，加上上下各1米共2米，再加打结1米。',
    options:['A. 7','B. 8','C. 9','D. 10','E. 11'],
    ans:2, ansLetter:'C',
    origin:'2024 Q13 — 礼物盒绑丝带总长'
  },
  {
    id:'W23', star:2, category:'度量单位·时间推算',
    text:'地铁从起点站到终点站总共用45分钟，中间经过5段路程。已知各段用时分别是：6分钟、8分钟、？分钟、9分钟、7分钟。问号处应该是几分钟？',
    hint:'提示：把所有段的时间加起来等于45分钟，用45减去已知的四段时间就是问号。',
    options:['A. 12','B. 13','C. 14','D. 15','E. 16'],
    ans:3, ansLetter:'D',
    origin:'2019 Q16 — 火车各站间运行时间推算'
  },
  {
    id:'W24', star:2, category:'度量单位·时钟计算',
    text:'小明看了一场时长3小时45分钟的马拉松比赛直播，直播结束时时钟显示的是下午3时20分。请问直播是从几点几分开始的？',
    hint:'提示：3时20分减去3小时45分钟。先减3小时得到12时20分，再减45分钟，注意借位。',
    options:['A. 上午10时35分','B. 上午11时05分','C. 上午11时35分','D. 中午12时05分','E. 中午12时35分'],
    ans:2, ansLetter:'C',
    origin:'2017 Q14 — 现在1:30，两个半小时前是几点'
  },

  // ── 4★/5★ 改编题（略增难度）──────────────────────────
  {
    id:'W25', star:5, category:'路径方向·等差数列间隔',
    text:'一段公路两侧各种了一排树：左侧每隔5米种一棵，从起点到终点共种了21棵（含两端）；右侧每隔4米种一棵，从起点到终点共种了26棵（含两端）。请问这段公路有多少米长？',
    hint:'提示：左侧：(21-1)×5=100米；右侧：(26-1)×4=100米。两侧结果一致才是正确答案。',
    options:['A. 80米','B. 96米','C. 100米','D. 104米','E. 120米'],
    ans:2, ansLetter:'C',
    origin:'2015 Q18 — 跑道旗子间隔距离'
  },
  {
    id:'W26', star:5, category:'路径方向·约束路径计数',
    text:'一只蚂蚁在六边形蜂巢格子网上行走，只能经过【白色格子】，从C格走到D格，每个格子只能经过一次。请问共有多少种不同的走法？（格子布局如图所示）',
    hint:'提示：用枚举法，从C出发，逐步列举所有可能的路径，注意只走白格且不重复。',
    options:['A. 4','B. 5','C. 6','D. 7','E. 8'],
    ans:3, ansLetter:'D',
    origin:'2020 Q19 — 蜜蜂六边形格子路径计数'
  },
  {
    id:'W27', star:5, category:'路径方向·方向约束路线',
    text:'小机器人只能【前进或右转】，不能左转也不能后退。从黑点出发，下面5条路线中，哪条是小机器人【可以】走完的？（路线图如图，黑点是起点）',
    hint:'提示：沿每条路线检查，如果遇到需要左转才能继续的情况，这条路线就不行。只有全程都只需前进或右转的路线才符合。',
    options:['A. 路线A','B. 路线B','C. 路线C','D. 路线D','E. 路线E'],
    ans:2, ansLetter:'C',
    origin:'2022 Q23 — 小凯的车只能左转走哪条路'
  },
  {
    id:'W28', star:5, category:'逻辑推理·等差数列+方程',
    text:'小蜗牛连续4天爬坡，每天比前一天多爬3厘米。第4天爬的距离是第1天的2.5倍。请问这4天小蜗牛一共爬了多少厘米？',
    hint:'提示：设第1天爬a厘米，则第4天=a+9厘米，由a+9=2.5a，解出a=6。四天总距离：6+9+12+15=42厘米。',
    options:['A. 36','B. 42','C. 48','D. 54','E. 60'],
    ans:1, ansLetter:'B',
    origin:'2015 Q20 — Joy猫捉老鼠三天总数'
  },
  {
    id:'W29', star:5, category:'逻辑推理·传递性推理',
    text:'学校运动会上，6名同学（A、B、C、D、E、F）按跑步速度用箭头标记，箭头从慢指向快。已知：A→C，B→A，B→D，C→E，D→F，E→F。请问谁的速度【最慢】？（没有箭头指向他）',
    hint:'提示：找出没有任何箭头"指向"的人，说明没有比他更慢的，他就是最慢的。或者找只有箭头"从他出发"没有"指向他"的。',
    options:['A. A','B. B','C. C','D. D','E. E'],
    ans:1, ansLetter:'B',
    origin:'2020 Q20 — 箭头高矮关系推断最矮的人'
  },
  {
    id:'W30', star:5, category:'逻辑推理·逆向计算',
    text:'马拉松比赛中，小李到达终点时，他前面跑完的人比他多3人，他后面还没到终点的人数是他前面人数的一半。请问这次比赛共有多少人参加？',
    hint:'提示：设他前面有x人，则x=他后面人数的2倍，后面人数=x/2。总人数=x+1+x/2。代入"前面比他多3"这个信息：前面人数=后面人数+3，则x=x/2+3，解出x=6，后面3人，总共10人。',
    options:['A. 9','B. 10','C. 11','D. 12','E. 13'],
    ans:1, ansLetter:'B',
    origin:'2023 Q21 — Emma舞蹈比赛第三名共几人'
  },
  {
    id:'W31', star:5, category:'平面图形·不规则面积',
    text:'城市规划图上有5块绿地（A~E），每块绿地的边界都由方格线组成（如图）。请问哪块绿地的面积【最大】？',
    hint:'提示：用"数格子法"：完整的格子直接数，被边界切成一半的格子算0.5。比较各绿地的总面积。',
    options:['A. A绿地','B. B绿地','C. C绿地','D. D绿地','E. E绿地'],
    ans:3, ansLetter:'D',
    origin:'2022 Q18 — 不规则草坪面积最小'
  },
  {
    id:'W32', star:5, category:'平面图形·图形拼接',
    text:'小明有8个完全相同的等腰直角三角形（如图左所示）。他用全部8个三角形拼出一个完整图案（不重叠、不留空、不剪切）。下面哪个图案是【不可能】拼出来的？',
    hint:'提示：8个等腰直角三角形的总面积是固定的，如果某个图案的面积对不上，就不可能。还要考虑形状上的可行性。',
    options:['A. 大正方形','B. 长方形','C. 六边形','D. 十字形','E. 平行四边形'],
    ans:2, ansLetter:'C',
    origin:'2023 Q17 — Elvis 6个三角形拼图'
  },
];
