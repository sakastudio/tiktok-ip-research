# AIを完パケにするか、3Dを完パケにするか

調査日: 2026-07-27
対象の問い: 『tiktok-drama-research.md』末尾の2点
1. AIから骨格推定を行い、カメラワークも含めて3D化・レンダリングして完パケを3Dで行うワークフローは妥当か
2. 将来的にAIへの寛容度が上がり、AIでも純粋にコンテンツを好きになる未来は来るか（昔の3Dもそうだったように）

---

## 0. 要旨

| 論点 | 結論 |
|---|---|
| 寛容度は上がるか | 見た目への寛容度は上がる。労力・出自への反発は上がっていない。そして見た目の寛容度が上がっても得しない（同時に希少性がゼロになるため） |
| 3Dを完パケにする判断 | 正しい。ただし理由は「AI叩き回避」ではなく、0.5秒カット割りとIP一貫性という要求仕様に対する最適解だから |
| 提案ワークフロー | 修正が必要。AI生成動画からのカメラ・骨格推定は原理的に破綻する経路。AIは上流（企画〜アセット）、3Dは下流（キャラ・モーション・カメラ・レンダリング）に置く |
| 判断の決め手 | 3Dルートは寛容度が上がる未来でも上がらない未来でも正解になる。AI完パケルートは上がらないと負け、上がっても差別化が消えて勝ちきれない |

---

## 1. 問いを2つの軸に分解する

「AIへの寛容度」を一枚岩で扱うと結論を誤ります。実際には性質の異なる2つの反発が重なっています。

| 軸 | 内容 | 3DCG・ボカロにあったか | 2026年時点の状態 |
|---|---|---|---|
| 見た目の軸 | 不気味、安っぽい、動きが変、AIっぽい | あった | 解消に向かっている |
| 労力・出自の軸 | 学習データの出自、労働置換、努力していない | ほぼ無かった | 悪化している |

3DCGとボカロの類推が成立するのは前者だけです。後者はAI固有で、しかも技術進歩では解決しません。

---

## 2. 「昔の3Dも同じ立ち位置だった」の検証

### 2.1 見た目の軸は、実際に3Dと同じ道を辿る

日本の3DCGアニメは長く酷評されてきました。90年代後半から導入が進んだものの、海外主流のフル3DCGではなく、3DCG映像を従来のセルアニメ風に変換して2D画像と合成する作品が多数を占めた、という経緯があります（[サブリメイション](https://www.sublimation.co.jp/column/works_20220311/)）。ハイブリッド方式（メカ・背景・プロップをCG、キャラを2D作画）は高評価を得る一方、フル3DCGは酷評されがち、という非対称が長く続きました（[Real Sound](https://realsound.jp/movie/2021/08/post-841121.html)）。

重要なのは解決の仕方です。「もっとリアルにする」で解決したのではなく、セルシェーディング／セルルックという別の様式を発明し、既存の美意識に接続することで解決しました。

ボカロも完全に同型です。初期のLEONやLOLAはロボット的な声で注目されず、2010年頃までは「機械の声」の違和感が強かった。それが「違和感を味として捉える」という聴き手側の意識変化を経て一般化しました（[spollup](https://spollup.jp/column/why-vocaloid-was-accepted/)、[ボカロの歴史](https://utai.tech/posts/vocaloid/history)）。合成音声であることが逆に作曲者の個性を前面に出す、という積極的な意味づけまで発生しています。

ハリウッドのCGIも同じ構造です。スターウォーズ prequel 以降にバックラッシュが起き、いまも「CG臭い」批判とプラクティカルエフェクト回帰の潮流がある。ただしVFX批評家は「物理と digital を両方うまく使って良い映画を作っている作品」には文句を言わない（[Den of Geek](https://www.denofgeek.com/movies/a-brief-history-of-practical-effects-in-cinema-in-10-movies/)、[Creative Bloq](https://www.creativebloq.com/features/defending-cgi-in-movies)）。

歴史のパターンは「技術の痕跡を隠して勝った」ではなく「痕跡を様式として自立させて勝った」です。この点でAI動画も、AIっぽさを消す方向より、AIでしかできない絵を様式化する方が筋がいい。この軸に関する読みは正しいと思われます。

### 2.2 労力・出自の軸は、3Dには存在しなかった

誰も「3DCGは他人の絵を盗んでいる」とは言わなかったし、ボカロに「歌手の仕事を奪う」という批判はほとんど立ちませんでした。AIには美的な軸に加えて、学習データの出自と労働置換という道徳・経済の軸があります。

これは技術が進歩しても消えません。消えるとしたら、法とライセンスが決着したときです。

### 2.3 法制度の現状（2026年7月時点）

| 事案 | 状況 |
|---|---|
| 訴訟件数 | 西側主要法域だけで training-data 訴訟が35件以上係争中（2026年Q2）([Presenc AI Tracker](https://presenc.ai/research/ai-training-data-lawsuit-tracker-2026)) |
| Bartz v. Anthropic | 15億ドルで和解（2025年8月合意、9月に予備承認）。約50万件の海賊版著作物に1件3,000ドル超の見込み。ただし将来の学習ライセンスは付与されない ([McKool Smith](https://www.mckoolsmith.com/newsroom-ailitigation-46)) |
| Disney / Universal / WB v. Midjourney | Disney・Universalが2025年6月提訴、DreamWorks が後に参加、WBが2025年9月4日に提訴。初期段階で公判日未定 ([Techweez](https://techweez.com/2026/07/07/midjourney-disney-universal-warner-copyright-lawsuit/)) |
| Getty Images v. Stability AI | 潜在賠償額で最大級の案件のひとつ |
| Thaler v. Perlmutter | 2026年3月2日に最高裁が cert denial。D.C.巡回区の2025年3月判決（著作権には人間の著作者性が必要）が確定 ([terms.law](https://terms.law/2026/01/15/midjourney-commercial-use-rights-complete-2026-guide/)) |

最後の1件は感情論ではなく実務の話です。純粋なAI生成物には米国で著作権が付かない（人間の創作的寄与部分のみ）。IPを育てるという目的に対して構造的に不利です。3Dモデル・リグ・アニメーションを自分で作れば、そこは人間の著作物として保護されます。

---

## 3. 受容度データ（2026年時点）

寛容度が上がっている証拠は見つかりませんでした。むしろ逆方向のデータが揃います。

### 3.1 消費者調査

Canva × The Harris Poll（2026年、消費者3,547人・マーケティング責任者1,415人、米英豪仏独日印の7カ国）([Canva Newsroom](https://www.canva.com/newsroom/news/marketing-ai-report-2026/))

| 設問 | 結果 |
|---|---|
| AIの方が良い結果を出せるとしても人間が作った広告のほうがいい | 78% |
| AI生成広告は「何かが足りない」と分かる | 70% |
| 良い広告には依然として人間の関与が必要 | 87% |
| AIが有用・関連性を出すなら広告でのAI利用は受け入れる | 68% |
| 開示が必要になると考える | 70%（うち56%が2〜5年以内と予想） |
| AI利用に関する正式な社内ポリシーがあれば安心 | 74% |

さらに、「AIを多用するブランドは信頼が下がる」と答えた消費者は2025年の20%から2026年に40%へ倍増。2026年には米国消費者の半数が「顧客向けコンテンツ・広告に生成AIを使わないブランドから買いたい」と回答しています。可視化されたAI生成マーケティングで「ブランドをより信頼する」は7%、「信頼が下がる」は31%（[Canva](https://www.canva.com/newsroom/news/marketing-ai-report-2026/)、[eMarketer](https://www.emarketer.com/content/shoppers-aren-t-impressed-by-ai-generated-marketing)、[KO Insights](https://www.koinsights.com/the-authenticity-premium-why-consumers-are-rejecting-ai-generated-content/)）。

「AI slop」のメディア言及量は9倍に増加、マーケティング責任者の41%が実務上の課題と認識しています。

### 3.2 世代差 — Gen Zは最も使い、最も嫌っている

| 指標 | 数値 |
|---|---|
| AI生成コンテンツを能動的に嫌う（「AI slopが品質を下げている」） | 41% |
| 警戒的（何が本物か分からない） | 31% |
| 肯定的 | 28% |
| ネガティブ or 警戒の合計 | 72% |

（[Attest / Gen Z media consumption 2026](https://www.askattest.com/blog/research/gen-z-media-consumption)）

しかもGen ZはAI利用率が最も高い世代です。感情は逆方向に振れており、excitement は14pt下落して22%、hopefulness は9pt下落して18%、anger は9pt上昇して31%（[Gallup](https://news.gallup.com/poll/708224/gen-adoption-steady-skepticism-climbs.aspx)、[Adweek](https://www.adweek.com/adweek-wire/new-shift-report-gen-z-is-embracing-ai-and-sounding-the-alarm-on-it/)）。

ただし Canva の調査では、Gen Z・ミレニアルの70%が「作り方より広告のvibeを見る」、69%が「実在の人物が登場するならAI関与を受け入れる」とも答えており、単純な拒否ではありません。

### 3.3 採用と信頼の乖離（これが一番重要な構造）

| 指標 | 2023 | 2024 | 2025 | 2026 |
|---|---|---|---|---|
| 米国成人のAIチャットボット利用 | 23% | 33% | — | 49% |
| ChatGPT利用 | 18% | — | 34% | 44% |
| チャットボット出力を信頼 | — | — | — | 29%（横ばい） |

（[Pew Research Center](https://www.pewresearch.org/short-reads/2026/03/12/key-findings-about-how-americans-view-artificial-intelligence/)、[Digital Applied](https://www.digitalapplied.com/blog/pew-americans-and-ai-2026-data-marketing-implications)）

採用は上がり続けるが信頼は上がらない。「使う」と「好む」は完全に別の指標です。ここを混同すると「みんな使ってるんだから寛容度は上がっている」という誤読が起きます。

Stanford AI Index 2026 も同型です。グローバルで「ベネフィットの方が大きい」は55%（2024）→59%（2025）と微増する一方、「不安を感じる」は52%に上昇。米国で「懸念より期待が上回る」はわずか10%（AI専門家は56%）。仕事への影響では専門家73%が改善を期待するのに対し一般は23%（[Stanford HAI 2026 AI Index — Public Opinion](https://hai.stanford.edu/ai-index/2026-ai-index-report/public-opinion)、[eWeek](https://www.eweek.com/news/stanford-ai-index-2026-trust-gap-neuron/)）。

### 3.4 日本固有のデータ — 反発は「AI」より「隠蔽」に向いている

株式会社システムリサーチ調査（2026年6月）([PR TIMES](https://prtimes.jp/main/html/rd/p/000000215.000144334.html)、[まんたんウェブ](https://mantan-web.jp/prtimes/article/20260704prt00m200000118a.html))

| 設問 | 結果 |
|---|---|
| AI生成だと分かった場合「少し抵抗を感じる」 | 38.3% |
| 同「不信感を持つ」 | 20.2% |
| ネガティブ計 | 58.5% |
| AI生成だと見抜ける自信がない | 58.5% |
| 知らずに見ていたと思う | 60.1% |
| AI生成であることを表示してほしい | 62.7% |
| AIだと分からないまま使われることに抵抗 | 66.0% |

同調査は「AI生成画像・動画そのものに強い拒否感を示す人は多くない」とも記録しています。日本の反発の主対象はAIそのものより隠蔽です。ここは戦略上使える差分で、制作過程を出す運用と相性がいい。

pixiv は2026年2月18日にガイドライン改定を発表（3月18日施行）。大量投稿や、AI生成なのに「AI生成作品」ステータスを付けない虚偽申告を明確に禁止し、違反可能性の高い作品を検索非表示にする機能を追加予定（[ITmedia](https://www.itmedia.co.jp/aiplus/article/2602/18/1260218132/)）。Xも2026年3月に「AIで生成」ラベルを含むコンテンツ開示機能を導入。2026年1月にはpixiv主催のAI不使用イラコンで「AI魔女狩り」騒動が発生しています（[note / 質感LoRA研究工房](https://note.com/texture_lora_lab/n/nc847cb2dd546)）。

---

## 4. 実際に数字は落ちるのか（最も決定的なデータ）

### 4.1 TikTok 110万投稿の実測

Journal of Consumer Research 掲載論文「Made With AI: Consumer Engagement With Social Media Containing AI Disclosures」（2026）([JCR](https://academic.oup.com/jcr/advance-article/doi/10.1093/jcr/ucag013/8672493?login=false))

- TikTok投稿110万件を分析。AIGCラベル付きは、視聴数を統制した上でいいねが7〜8%減
- 実験の効果量: 全体で Cohen's d = .21〜.26、ラベルに気づいた層では d = .45〜.63
- フォロワー数に関わらず発生（インフルエンサー特有の現象ではない）

### 4.2 メカニズムが本題

この研究の価値は数字より因果の特定にあります。以下の代替仮説を実験で潰しています。

| 代替仮説 | 検証結果 |
|---|---|
| 品質が低いと思われるから | 開示を外すと差が消える。品質評価に有意差なし |
| AI嫌悪があるから | AI肯定派の参加者でも効果が残存 |
| 唯一性が失われるから | desire-for-unique-products 尺度による調整効果なし |
| コンテンツへの警戒 | コメントにリスク・道徳に関する語彙の増加なし |

実際に効いていた経路は Study 5 の直列媒介で確認された次の連鎖です。

```
AIGC開示 → 作者の労力が低いと認識される → パラソーシャル結合が弱まる → エンゲージメントが下がる
```

つまりAI開示のダメージは、コンテンツの出来ではなく「作者との絆」の部分に入ります。

これが今回の意思決定の核心です。一発ネタの消費型コンテンツならダメージは小さい。しかし「キャラに愛着を持たせてIPを育てる」という目的に対しては、一番効く場所を正確に殴られます。そして『tiktok-drama-research.md』の方針は明確に後者です。

同論文 Study 6 は「作者の労力を強調する開示」が損失を緩和しうることを示唆しており、対策の方向も同じ場所を指しています。

### 4.3 プラットフォーム制度の現状

TikTok

- C2PA Content Credentials を2025年1月に統合。主要プラットフォームで初めてメタデータによるAIコンテンツの自動検出・ラベル付けを実施
- C2PAメタデータ / 不可視ピクセル透かし / 自動分類モデルの3層構成。累計30億本以上にAIGCラベルを付与（[TikTok Newsroom](https://newsroom.tiktok.com/tiktok-ssa-shares-more-ways-to-spot-shape-and-understand-ai-generated-content?lang=en-ZA)、[Tech Times](https://www.techtimes.com/articles/320282/20260713/tiktok-has-labeled-3-billion-ai-videos-here-what-research-says-they-miss.htm)）
- 2026年3月以降、AI生成の顔・声はアプリ内ラベルでの開示が必須
- 公式には「AIGCラベルは開示メカニズムであり配信シグナルではない」（2025 Transparency Report）。ただしラベルなしでAIと通報されたコンテンツは強くderank。Creator Rewards Program はそもそもAI生成コンテンツを対象外
- 免除対象: AI字幕、AI説明文、AI提案ハッシュタグ、テキストオーバーレイ、脚本補助、フック文の生成
- ユーザーがフィード内のAI量を制御できる Manage Topics 機能をテスト中

（[auditsocials](https://www.auditsocials.com/blog/tiktok-ai-content-disclosure-rules-2026)、[storrito](https://storrito.com/resources/tiktoks-2026-ai-labeling-rules-and-what-they-signal-for-platform-governance/)）

YouTube

- 2025年7月15日、従来の「repetitious content」ポリシーを「inauthentic content」に改称・厳格化
- 収益化不可の3類型: 反復的なAI生成動画 / 感情を煽る・不快なクリップ / 健康・金融など機微領域の合成ペルソナ
- 2026年7月にさらに明確化（[TechCrunch 2026-07-20](https://techcrunch.com/2026/07/20/youtube-clarifies-policies-around-ai-slop-and-upsetting-videos/)、[Android Headlines](https://www.androidheadlines.com/2026/07/youtube-monetization-rules-ai-slop-inauthentic-content.html)）
- 公式の線引き: AIツールの禁止ではなく、人間の創造性を「拡張」ではなく「置換」するAI駆動コンテンツの禁止。開示それ自体は視聴者制限や収益化剥奪の理由にならない

---

## 5. 供給側がすでに飽和している

Kapwing 調査（2026年6月報道）([Media Innovation](https://media-innovation.jp/article/2026/06/24/143442.html))

- 新規TikTokアカウントのFYP初期500本のうち294本、59%がAI slop。YouTube Shortsは21%で約3倍の差
- 手法: 20カテゴリ10,742本以上を人力検証。AI生成の映像・脚本・音声を目視確認

| カテゴリ | AI比率 |
|---|---|
| kids | 57.4%（#cartoonkids 97%、#babysong 83%） |
| education / science | 35.0% |
| health | 33.8% |
| history | 33.5% |
| fitness | 1.6% |
| music | 1.5% |
| fashion | 1.3% |

ここから2点。

第一に、「AIで作れる」はすでに差別化になっていません。フィードの6割です。

第二に、これは『tiktok-drama-research.md』の「知識・教養系」案に直接効きます。education が35%でAI slopの密集地帯であり、クイズノック的フォーマットをAIで素直にやると、いま最も供給過剰な場所に飛び込むことになる。逆に言えば「知識・教養 × ドラマ × 一貫した世界観」に向かう判断は、競争回避の意味でも正しい方向です。

なお同記事はAI／人間コンテンツのエンゲージメント比較の直接データは提示していません。

---

## 6. 反証: AIでもIPは育つ（公平に見る）

「AIだとIPが育たない」は事実として間違いです。反証を先に置きます。

### 6.1 事例

Neuro-sama（AI VTuber）
- 2026年1月、Twitchで最も購読されているチャンネルに。2026年1月2日時点でアクティブサブ16.2万、全人間ストリーマーを上回った
- 2025年12月末に自身のHype Train世界記録を更新、記録のハットトリック
- ファンコミュニティ「The Swarm」が形成され、2024年後半には VTuber of the Year にノミネート
- CHI 2026 に学術論文「My Favorite Streamer is an LLM」が採択。ファンは受動的な視聴者ではなく能動的な共同創作者であり、AIの技術的構成を理解した上で情緒的愛着と折り合いをつけ、一貫したペルソナをコミュニティ文化にまで拡張している、と分析されている

（[Dot Esports](https://dotesports.com/streaming/news/neuro-most-subscribed-twitch)、[CHI 2026](https://dl.acm.org/doi/10.1145/3772318.3790891)、[arXiv](https://arxiv.org/html/2509.10427v1)）

Xania Monet（AI音楽）
- ミシシッピの詩人 Telisha "Nikki" Jones が作詞し Suno で制作。Billboardチャート入り
- 2025年9月に Hallwood Media と数百万ドル規模の契約（入札は300万ドルに達したと報道）
- 米国ストリーミングだけで初期カタログが5万ドル超を生成

Breaking Rust（AI音楽）
- "Walk My Walk" が Billboard Country Digital Song Sales で1位。ただしBillboard自身の分析では、11月6日終了週のトラックDLは約3,000件。「チャートに乗る ≠ 人気がある」

（[Billboard](https://www.billboard.com/pro/ai-music-artists-charts-popular/)、[Forbes](https://www.forbes.com/sites/conormurray/2025/11/05/creator-behind-billboard-charting-ai-artist-xania-monet-defends-her-music-against-backlash-from-kehlani-and-more/)）

ツインズひなひま（2025年3月地上波）
- KaKa Creation × フロンティアワークス。本編の95%以上のカットでAI支援
- 実態は「プロンプト一発出し」ではなく、3Dとモーションキャプチャでキャラアニメを作り、仕上げ・彩色を中心にAIで手描きセルアニメ的な絵作りに寄せる構成（サポーティブAI）
- 視聴者評価は「思いのほか悪くなかった。びっくりするような破綻は無かった」「TVやスマホでながら観する分には文句ない」「ただし映画館のスクリーンで観たいとは思わない」

（[Yahoo!ニュース / まつもとあつし](https://news.yahoo.co.jp/expert/articles/2240f963d6dd2f301fe4b9a1946b1b32934c3533)、[Ledge.ai](https://ledge.ai/articles/twins_hinahima_2025spring)、[AdverTimes](https://www.advertimes.com/20250930/article515782/)）

Tilly Norwood（炎上側）
- Particle6（CEO: Eline Van der Velden）が制作したAI「俳優」
- SAG-AFTRAが公式に否定。「人間の俳優ではなく、引き出すべき人生経験を持たない」
- 2026年7月に長編映画「Misaligned」主演が発表され、批判がさらに激化

（[BNN Bloomberg](https://www.bnnbloomberg.ca/business/artificial-intelligence/2026/07/17/creator-defends-ai-actor-tilly-norwood-after-feature-film-backlash/)、[CBC](https://www.cbc.ca/lite/story/1.7647478)、[Forbes](https://www.forbes.com/sites/conormurray/2026/03/10/ai-actress-tilly-norwood-responds-to-backlash-in-debut-song-ais-not-the-enemy/)）

### 6.2 パターン抽出

並べると分岐点がはっきりします。

| | 構造 | 結果 |
|---|---|---|
| Neuro-sama | 人間が設計した3Dの器・キャラ設定の中でAIが振る舞う。制作者（Vedal）が可視 | 成功 |
| ツインズひなひま | 3D+モーキャプの器の上でAIが仕上げを担う | 実験として成立 |
| Xania Monet | 人間が作詞し、AIが音を作る。制作者が名乗り出ている | チャート入り |
| Tilly Norwood | AIが人間の役割そのものを代替すると宣言 | 業界団体レベルで拒絶 |

判定軸は「AIを使ったかどうか」ではなく「作者の意図と労力が見えるかどうか」です。これはJCRの媒介分析（perceived effort → parasocial connection）と完全に一致しており、業界事例と学術データという独立した2系統が同じ結論を指しています。

そして Neuro-sama は、今回検討している構成そのものです。AIが中身を動かし、3Dの器が完パケを担う。この方向にはすでに最強クラスの実証例があります。

---

## 7. 提案ワークフローの技術評価

対象: 「AIから骨格推定を行い、カメラワークも含めて3D化、レンダリングし完パケは3D上で行う」

### 7.1 骨格推定そのものは実用水準

単眼動画からのmocapは2026年時点で主要関節が光学式と2〜3cm差まで来ています（[StraySpark](https://www.strayspark.studio/blog/ai-mocap-indie-developers-2026-comparison)）。

| ツール | 特徴 |
|---|---|
| Move.ai | マーカーレスの本命。Move Pro は2〜十数台のカメラを同期し神経ポーズ推定＋生体力学ソルブ。単眼の Move One もあるが、足の接地と奥行き曖昧性は Pro が明確に上 |
| Autodesk Flow Studio（旧 Wonder Studio） | 単眼フッテージから体・顔・手のモーションとAIカメラトラックを同時取得 |
| DeepMotion / Rokoko Video / QuickMagic | Webcam〜動画ファイルからの手軽な変換 |
| EasyMocap（OSS） | HRNet / MediaPipe 等の2Dキーポイント検出＋CNN初期化で単眼動画から抽出 |
| Cascadeur / MetaHuman Animator | 補正・顔まわり |

ここは問題ありません。

### 7.2 ソースをAI生成動画にすると壊れる

これが技術的な致命点で、研究レベルで明示されている既知の限界です。

生成動画はカメラ軌跡が未知であり、かつ剛体性が保たれていない。背景がソフトに変形し、色がフリッカーする。そのためCOLMAPのようなSfMが rigidity violation により収束せず、背景SfM経由でのカメラ／体のポーズ推定が成立しない（[Vidu4D, arXiv:2405.16822](https://arxiv.org/pdf/2405.16822)）。

最新のカメラ推定でも条件付きです。MegaSaM は DROID-SLAM / COLMAP / Fast3R を精度で上回り MonST3R より高速ですが、「動体が視野を支配する場合」「カメラ運動と物体運動が共線の場合」に破綻すると明記されています。VGGT は推論は速いが特徴点が少ない場面で弱い（[arXiv:2605.12027](https://arxiv.org/pdf/2605.12027)）。

縦型構図でキャラが画面を占める絵は、この破綻条件にほぼ完全に一致します。つまり一番やりたい構図が一番苦手な条件です。

### 7.3 そもそも情報を捨てて推定し直している

より根本的な問題として、3Dで作るならカメラは推定するものではなく指定するものです。Unity の Cinemachine + Timeline で直接置く方が速く、正確で、再現可能で、後から直せる。AI動画からカメラを逆算するのは、自分が持っている情報を一度捨てて推定し直す工程になっています。

加えて、0.5〜1秒カットの絵作りに必要なのは実写的に正確なモーションではありません。アニメのカット割りは実写モーションをそのまま写しても気持ちよくならず、ポーズtoポーズ・タメツメ・誇張が要る。オムオムアニメ（@omom_animee）がクオリティの割に伸びているのは、まさにそこが効いているからです。

### 7.4 修正案 — AIを上流、3Dを下流に固定する

| 工程 | 担当 | 具体 |
|---|---|---|
| 企画・脚本 | AI | ネタ出し、脚本、オチの分岐案 |
| 絵コンテ | AI | イメージボード、構図案、カット割り案 |
| キャラ・アセット | AI + 人 | キャラデザ案、背景・プロップのコンセプト、image-to-3Dの入力、テクスチャ |
| モーション | 実写mocap | 自分 or 演者をiPhone/webcamで撮影 → 単眼mocap → リターゲット。AI動画からではなく実写リファレンスから取る |
| カメラ・カット割り | 3D（人） | Unity Timeline + Cinemachine で直接指定。ここが0.5秒カットの心臓部 |
| レンダリング | 3D | セルルック |
| 音・仕上げ | AI | リップシンク、音声、BGM、サムネ、投稿文 |

AI 3Dアセット生成の2026年水準（image-to-3D の入力として使える）:

| ツール | 評価 |
|---|---|
| Rodin (Hyper3D) Gen-2 | 100億パラメータ、クアッドトポロジー、T/Aポーズ強制、多画像融合。クリーンアップなしで実パイプラインに入る唯一格との評価 |
| Hunyuan3D | テクスチャ・PBR品質でトップ。image-to-3D 向き |
| Tripo | Smart Mesh P1.0 で約2秒のクアッドリトポ。ゲームエンジン最適化 |
| Meshy-6 | 低ポリ生成、クアッド／トライ選択可。バランス型 |

ただしヒーローアセットとアニメーションするキャラは依然クリーンアップか人手レビューが必要（[3DAI Studio](https://www.3daistudio.com/state-of-ai-3d-generation-2026)、[Indie Hackers](https://www.indiehackers.com/post/best-ai-3d-model-generator-in-2026-i-tested-9-of-the-best-and-here-is-what-i-found-70ecab1a0a)）。

先行実装:

- 個人制作: VRoid Studio → UniVRM → Unity(URP + lilToon) + Cinemachine / Timeline。Timelineでカメラワークをアニメーションとして組み、複数カットをイージングで接続する運用が確立している（[note / DEL-ZIG](https://note.com/dlzig7/n/n85faea168133?hl=en)、[Extra Ordinary, the Series](https://extra-ordinary.tv/2020/07/20/setting-the-scene-vroid-unity-for-animated-cartoons/)）
- 商用ツール: Reallusion が2026年に iClone 8 / Character Creator 5 で「Hybrid AI」を正式な製品戦略として発表。previz を AI Studio でフォトリアル／スタイライズド化、AI Motion Capture で動画→モーションデータ、CC Wrap でAI生成3Dモデルを標準トポロジーに取り込む（[Reallusion Magazine](https://magazine.reallusion.com/2026/04/08/reallusion-announces-2026-vision-redefining-3d-production-through-the-power-of-hybrid-ai/)、[befores & afters](https://beforesandafters.com/2026/04/14/the-power-of-hybrid-ai-reallusion-announces-2026-vision/)）

業界の解も個人の解も同じ方向を指しています。そして moorestech で Unity を触っている以上、この工程は既存スキルの直接転用です。判断材料として最も大きい要素だと考えます。

---

## 8. 0.5秒カットの経済性（3Dを選ぶ本当の理由）

AI叩き回避よりこちらが本命です。

### 8.1 AI動画のコスト構造

AI動画は「1カット = 1生成」です。カットを増やすとコストが線形に増え、同時にカット間の一貫性が崩れるリスクも増える。

- 得意なのは3〜10秒。長尺になるほどキャラ一貫性と物理法則の破綻が目立つ
- キャラ一貫性を保つには「参照画像 → Image-to-Video」の2段フローが鉄則、とされている。裏返せば放置すると崩れる
- アニメ調特有の破綻: 線は綺麗でも動いた瞬間にキャラが3D的に変形する、握手や手のつなぎ方など細かい指示が反映されない、瞬きの指示が守られず目を閉じたまま固まる、カメラが変わると骨格が揺れる

（[note / ミツカル](https://note.com/ai_mitsukaru/n/n352b38c849d7)、[Cochi AI Blog](https://cochi-404.hatenablog.com/entry/2026/03/04/152956)）

2026年7月時点のAPI単価:

| モデル | 単価 | 特徴 |
|---|---|---|
| Seedance 2.0 Fast | $0.022/秒 | 2026年2月登場。最もバランス型との評価 |
| Wan 2.6 | $0.05〜0.07/秒 | 生成約20秒。試行錯誤向き |
| Kling 3.0 | $0.10/秒 | Multi-Shot Storyboard、多角度の被写体一貫性が強い。Omni は2キャラの会話を音素単位でリップシンク |

（[buildmvpfast API costs](https://www.buildmvpfast.com/api-costs/ai-video)、[Atlas Cloud](https://www.atlascloud.ai/blog/guides/best-ai-video-generation-models-2026)）

概算（筆者試算、実運用のリテイク率で大きくブレる）:
60秒動画を0.5秒カットで作ると120カット。各カット2秒生成として240秒分。Kling 3.0 なら約$24/本。ただし一発OK率が低いため実際は3〜5倍を見込む必要があり、かつ同一キャラが120カット保つ保証がない。

### 8.2 3Dのコスト構造

シーンを一度組めば、カメラを増やすコストはほぼゼロ（レンダリング時間のみ）。120カットは「Timelineにカメラを120個置く」であって、追加の生成コストが発生しません。キャラは同一アセットなので、一貫性は「保証」ではなく「定義」です。

### 8.3 要求仕様との重なり

| 要求仕様 | AI動画 | 3D |
|---|---|---|
| 1秒に1〜2カット | カット数に比例してコスト増、一貫性リスク増 | 追加コストほぼゼロ |
| 一貫した世界観・同一キャラ | 最も苦手。参照画像運用でも崩れる | 定義上保証される |
| 長期シリーズ・IP育成 | 資産が蓄積しない | キャラ・セット・モーションが資産化 |
| リテイク・後修正 | 再生成（結果が変わる） | パラメータ変更で決定論的 |

要求仕様が、AI動画が最も苦手でかつ3Dが最も得意な領域に、ちょうど重なっています。

---

## 9. 判断の決め手 — 両方の未来で正解になるか

| 未来 | 3Dルート | AI完パケルート |
|---|---|---|
| 寛容度が上がらない | 「AI叩きを受けない」が効いて勝つ | 負ける |
| 寛容度が上がる | 資産（キャラ・世界・リグ・モーションライブラリ）が残る | 全員が同じことをできるため差別化が消える。勝ちきれない |

非対称です。3Dルートはどちらの未来でも正解になり、AI完パケルートは片方で負けもう片方でも勝ちきれない。しかもフィードの59%がすでにAIである以上、後者の未来は半分到来しています。

補強材料として、ツール依存のリスクがあります。OpenAIは2026年3月24日にSora終了を発表、4月26日にWeb／アプリを停止（APIは2026年9月24日終了）。アカウント関連データは期日後に完全削除。月800〜1200万ドルの計算コストに対し収益200万ドル未満だったと報じられ、2026年初頭には品質面でも計測可能なカテゴリでリーダーではなくなっていたとされます。2026年6月時点で後継の発表はありません（[OpenAI Help Center](https://help.openai.com/en/articles/20001152-what-to-know-about-the-sora-discontinuation)、[TechXplore](https://techxplore.com/news/2026-04-sora-shutdown-reveals-limits-ai.html)、[Miraflow](https://miraflow.ai/blog/why-openai-shut-down-sora-2026)）。

パイプラインの中核を外部モデルに置くと、それが消えたときにIPごと止まります。3Dアセットは自分のディスクにあります。

---

## 10. リスクと反論（3Dルートの弱点）

### 10.1 3Dでも「AIっぽい」と言われるリスクは消えない

人間のAI動画識別精度は、動画のみの刺激で50.7%。統計的に当てずっぽうと区別できません（Communications of the ACM, 2025年9月）。別研究でも約51%。Runway の Turing Reel 調査では9.5%しか確実に見分けられず、53%の消費者はAI改変動画を正しく識別できない（[Kapwing 統計まとめ](https://www.kapwing.com/resources/55-ai-generated-video-statistics-disclosure-detection-and-trust/)、[arXiv:2605.24287](https://arxiv.org/pdf/2605.24287)）。

裏返すと誤爆も同じだけ起きます。実際、100時間以上かけた人力作品がAI認定されて r/Art をBANされた事例（Ben Moran）があり、以後は匿名を希望する作家も出ています（[How-To Geek](https://www.howtogeek.com/before-accusing-an-artist-of-using-ai-read-this/)、[BuzzFeed News](https://www.buzzfeednews.com/article/chrisstokelwalker/art-subreddit-illustrator-ai-art-controversy)）。San Diego Comic-Con は2026年のアートショーでAI作品を全面禁止しています。

完全な回避策は存在しません。最も効く防御は制作過程を出すこと（メイキング、タイムラプス、Unity画面、mocap撮影風景）。JCRの媒介分析で効いていたのが「労力が見えるか」である以上、理屈とも一致します。

なお、上記の識別精度データはフォトリアル映像の話です。アニメ調AI動画は前述の破綻（動いた瞬間の3D的変形、指の破綻、瞬きの固着）が出やすく、実際にはもっと見抜かれやすいと考えるべきです。

### 10.2 初期コストが重い

パイプライン構築に数週間〜数ヶ月かかり、1本目のコストはAIより明確に高い。「まず伸びるか試したい」フェーズには不向きです。

対策は、ネタの正解を探す作業とパイプラインを作る作業を分けること。

### 10.3 セルルックの選択は必須に近い

3D受容史（2.1節）が示す通り、日本市場ではフルリアル3Dよりセルルックの方が受け入れられます。ここで手を抜くと、AI忌避を避けた先で3D忌避に当たります。

---

## 11. 実行計画

| Phase | 期間の目安 | 内容 | 検証すること |
|---|---|---|---|
| 0 | 〜2週間 | 3Dは触らない。AIでも手描きでも既存素材でも可。「2秒で分かる」「最後まで見せる」「0.5〜1秒カット」の3条件だけ守ったネタを20本投げる | ネタの当たり方だけ |
| 1 | 当たりが1つ出たら | そのフォーマット専用に3Dセットを組む。VRoid → UniVRM → Unity(URP + lilToon) + Cinemachine / Timeline。キャラ2〜3体、セット1つ | 1本を1日で出せるか |
| 2 | 継続 | モーションライブラリ蓄積。自撮りmocap（Move One / Flow Studio / QuickMagic）で汎用モーション（驚く、指差す、ズッコケる、振り向く、ツッコむ）を50〜100個 | 制作時間の逓減 |
| 3 | 定常 | AIを上流に固定配置（ネタ出し、絵コンテ、背景コンセプト、image-to-3D、リップシンク、音声）。下流（キャラ・モーション・カメラ・レンダリング）は3Dのまま | 週次の投稿本数 |

開示方針:
最終画がAI生成でなければ、TikTok / YouTube のAIGCラベル義務には該当しません（対象はリアルな人物・声の合成であり、3Dレンダリングのアニメ表現ではない）。ただし日本の調査で66%が反発しているのは隠蔽なので、制作過程は積極的に見せる方が得です。「AIを使っていない」と主張するのではなく「どこで何を使ったか」を出すのが、JCRの知見とも日本の調査結果とも整合します。

---

## 12. 付録: 探しているフォーマットには名前がある

『tiktok-drama-research.md』で挙げられた条件

- 単話でも完結
- 全体として一貫した世界観
- 全体を通してストーリーが少しずつ進行していく

これはシチュエーション・コメディ（sitcom）の構造そのものです。固定の舞台、固定のキャラ、毎話独立、しかし通しで見ると関係が進む。「クラブあるある：すみで」が自然にそうなっていったのは、この構造に収束したからだと考えられます。

そして sitcom は舞台を意図的に固定する形式なので、3Dの経済性と完全に噛み合います。セットを一度作れば全話で使い回せる。狙っているフォーマットと選ぼうとしている技術が、偶然ではなく構造的に一致しています。

参考として、縦型ショートドラマの先行者ごっこ倶楽部（@gokko5club / 株式会社GOKKO）は2021年結成、4年で累計100億回再生・SNS総フォロワー560万人。脚本・撮影・編集・投稿・マーケティング・視聴データ分析までワンチームで内製し、2025年2月には自社課金プラットフォームを開始してIP化を進めています（[PR TIMES](https://prtimes.jp/main/html/rd/p/000000054.000090916.html)、[日経クロストレンド](https://xtrend.nikkei.com/atcl/contents/18/01271/00004/)）。工程の内製化とIP化という方向性は、今回の3Dパイプライン内製と同じ発想です。

---

## 出典一覧

### 消費者意識・受容度
- [Canva Marketing AI Report 2026（Harris Poll、消費者3,547人・日本含む7カ国）](https://www.canva.com/newsroom/news/marketing-ai-report-2026/)
- [Stanford HAI 2026 AI Index — Public Opinion](https://hai.stanford.edu/ai-index/2026-ai-index-report/public-opinion)
- [Stanford AI Index 2026: The Trust Gap Hits Critical Levels（eWeek）](https://www.eweek.com/news/stanford-ai-index-2026-trust-gap-neuron/)
- [Pew Research Center: Key findings about how Americans view AI（2026-03-12）](https://www.pewresearch.org/short-reads/2026/03/12/key-findings-about-how-americans-view-artificial-intelligence/)
- [Pew: Half of Americans Now Use AI Chatbots in 2026（Digital Applied）](https://www.digitalapplied.com/blog/pew-americans-and-ai-2026-data-marketing-implications)
- [Gallup: Gen Z's AI Adoption Steady, but Skepticism Climbs](https://news.gallup.com/poll/708224/gen-adoption-steady-skepticism-climbs.aspx)
- [Attest: Gen Z media consumption 2026](https://www.askattest.com/blog/research/gen-z-media-consumption)
- [Adweek: Gen Z Is Embracing AI and Sounding the Alarm on It](https://www.adweek.com/adweek-wire/new-shift-report-gen-z-is-embracing-ai-and-sounding-the-alarm-on-it/)
- [eMarketer: Shoppers aren't impressed by AI-generated marketing](https://www.emarketer.com/content/shoppers-aren-t-impressed-by-ai-generated-marketing)
- [KO Insights: The Authenticity Premium](https://www.koinsights.com/the-authenticity-premium-why-consumers-are-rejecting-ai-generated-content/)
- [IAB: The AI Ad Gap Widens](https://www.iab.com/insights/the-ai-gap-widens/)

### 日本の調査・プラットフォーム
- [システムリサーチ AI生成画像・動画に関する意識調査（2026年6月、PR TIMES）](https://prtimes.jp/main/html/rd/p/000000215.000144334.html)
- [同調査（まんたんウェブ）](https://mantan-web.jp/prtimes/article/20260704prt00m200000118a.html)
- [pixiv ガイドライン改定へ（ITmedia、2026-02-18）](https://www.itmedia.co.jp/aiplus/article/2602/18/1260218132/)
- [AI作品の投稿でBANされないための完全チェックリスト【2026年版】](https://note.com/texture_lora_lab/n/nc847cb2dd546)

### エンゲージメントへの実測影響
- [Made With AI: Consumer Engagement With Social Media Containing AI Disclosures（Journal of Consumer Research, 2026）](https://academic.oup.com/jcr/advance-article/doi/10.1093/jcr/ucag013/8672493?login=false)
- [AI in the spotlight: The impact of AI disclosure on user engagement in short-form videos（Computers in Human Behavior）](https://www.sciencedirect.com/science/article/abs/pii/S0747563224003169)
- [AI content labeling and user engagement on social media（Electronic Markets, 2026）](https://link.springer.com/article/10.1007/s12525-026-00883-2)
- [How Users Perceive and React to Labeled AI-Generated Content（縦断研究, 2026）](https://www.tandfonline.com/doi/full/10.1080/10447318.2026.2618553)

### プラットフォームポリシー
- [TechCrunch: YouTube clarifies policies around AI slop and upsetting videos（2026-07-20）](https://techcrunch.com/2026/07/20/youtube-clarifies-policies-around-ai-slop-and-upsetting-videos/)
- [Android Headlines: YouTube Targets AI Slop（2026-07）](https://www.androidheadlines.com/2026/07/youtube-monetization-rules-ai-slop-inauthentic-content.html)
- [TikTok Newsroom: More ways to spot, shape and understand AI-generated content](https://newsroom.tiktok.com/tiktok-ssa-shares-more-ways-to-spot-shape-and-understand-ai-generated-content?lang=en-ZA)
- [TikTok Has Labeled 3 Billion AI Videos（Tech Times, 2026-07-13）](https://www.techtimes.com/articles/320282/20260713/tiktok-has-labeled-3-billion-ai-videos-here-what-research-says-they-miss.htm)
- [TikTok AI Content Policy 2026: 4-Tier Labels & Penalties](https://www.auditsocials.com/blog/tiktok-ai-content-disclosure-rules-2026)
- [TikTok's 2026 AI labeling rules（Storrito）](https://storrito.com/resources/tiktoks-2026-ai-labeling-rules-and-what-they-signal-for-platform-governance/)

### 供給飽和
- [TikTokもAI生成動画が氾濫、新規ユーザーのフィードは6割（Kapwing調査 / Media Innovation, 2026-06-24）](https://media-innovation.jp/article/2026/06/24/143442.html)

### 3DCG・ボカロ・CGIの受容史
- [日本のフル3DCGアニメはなぜ酷評されるのか（Real Sound）](https://realsound.jp/movie/2021/08/post-841121.html)
- [セルルックアニメーションっていったい何？（サブリメイション）](https://www.sublimation.co.jp/column/works_20220311/)
- [3DCG 使用法の違いに起因するアニメと非アニメの境界線の考察（名古屋大学）](https://www.lang.nagoya-u.ac.jp/media/public/200803/sano.pdf)
- [ボーカロイドが受け入れられた理由（スポルアップ）](https://spollup.jp/column/why-vocaloid-was-accepted/)
- [ボカロの歴史（utai.tech）](https://utai.tech/posts/vocaloid/history)
- [A Brief History of Practical Effects in Cinema（Den of Geek）](https://www.denofgeek.com/movies/a-brief-history-of-practical-effects-in-cinema-in-10-movies/)
- [CGI in movies, what's not to like?（Creative Bloq）](https://www.creativebloq.com/features/defending-cgi-in-movies)

### AI IP の成功・失敗事例
- [AI VTuber Neuro-sama becomes Twitch's Most Subscribed Channel（Dot Esports, 2026-01）](https://dotesports.com/streaming/news/neuro-most-subscribed-twitch)
- [My Favorite Streamer is an LLM: Discovering, Bonding, and Co-Creating in AI VTuber Fandom（CHI 2026）](https://dl.acm.org/doi/10.1145/3772318.3790891)
- [同論文プレプリント（arXiv:2509.10427）](https://arxiv.org/html/2509.10427v1)
- [Billboard: AI Music Artists Are on the Charts, But They Aren't That Popular — Yet](https://www.billboard.com/pro/ai-music-artists-charts-popular/)
- [Forbes: Creator behind Billboard-charting AI artist Xania Monet defends her music](https://www.forbes.com/sites/conormurray/2025/11/05/creator-behind-billboard-charting-ai-artist-xania-monet-defends-her-music-against-backlash-from-kehlani-and-more/)
- [BNN Bloomberg: Creator defends AI 'actor' Tilly Norwood after feature film backlash（2026-07-17）](https://www.bnnbloomberg.ca/business/artificial-intelligence/2026/07/17/creator-defends-ai-actor-tilly-norwood-after-feature-film-backlash/)
- [CBC: Meet Tilly Norwood, the AI 'actress' prompting backlash](https://www.cbc.ca/lite/story/1.7647478)
- [「AIでお手軽に」じゃなかった「ツインズひなひま」（まつもとあつし / Yahoo!ニュース）](https://news.yahoo.co.jp/expert/articles/2240f963d6dd2f301fe4b9a1946b1b32934c3533)
- [フロンティアワークス、AI活用で挑む新作アニメ「ツインズひなひま」（Ledge.ai）](https://ledge.ai/articles/twins_hinahima_2025spring)
- [本格"AIアニメ"『ツインズひなひま』は業界に変化をもたらすか（AdverTimes）](https://www.advertimes.com/20250930/article515782/)

### 法制度
- [AI Training Data Lawsuit Tracker 2026（Presenc AI）](https://presenc.ai/research/ai-training-data-lawsuit-tracker-2026)
- [Midjourney Commercial Use Rights: 2026 Guide（Thaler cert denial 含む）](https://terms.law/2026/01/15/midjourney-commercial-use-rights-complete-2026-guide/)
- [AI Infringement Case Updates（McKool Smith）](https://www.mckoolsmith.com/newsroom-ailitigation-46)
- [Disney, Universal, and Warner Bros. Sue Midjourney（Techweez, 2026-07-07）](https://techweez.com/2026/07/07/midjourney-disney-universal-warner-copyright-lawsuit/)

### 技術（mocap・カメラ推定・3D生成・AI動画）
- [Vidu4D: Single Generated Video to High-Fidelity 4D Reconstruction（arXiv:2405.16822）](https://arxiv.org/pdf/2405.16822)
- [4DVGGT-D: 4D Visual Geometry Transformer（arXiv:2605.12027）](https://arxiv.org/pdf/2605.12027)
- [Reconstructing 4D Spatial Intelligence: A Survey（arXiv:2507.21045）](https://arxiv.org/pdf/2507.21045)
- [AI Motion Capture for Indie Devs in 2026（StraySpark）](https://www.strayspark.studio/blog/ai-mocap-indie-developers-2026-comparison)
- [EasyMocap: The Revolutionary Toolbox for 3D Motion Capture](https://www.blog.brightcoding.dev/2026/02/20/easymocap-the-revolutionary-toolbox-for-3d-motion-capture)
- [QuickMagic: AI Motion Capture from Video & Text](https://www.quickmagic.ai/)
- [State of AI 3D Generation 2026（3DAI Studio）](https://www.3daistudio.com/state-of-ai-3d-generation-2026)
- [Best AI 3D Model Generator in 2026: I Tested 9（Indie Hackers）](https://www.indiehackers.com/post/best-ai-3d-model-generator-in-2026-i-tested-9-of-the-best-and-here-is-what-i-found-70ecab1a0a)
- [Reallusion Announces 2026 Vision: Redefining 3D Production through Hybrid AI](https://magazine.reallusion.com/2026/04/08/reallusion-announces-2026-vision-redefining-3d-production-through-the-power-of-hybrid-ai/)
- [The Power of Hybrid AI: Reallusion 2026 Vision（befores & afters）](https://beforesandafters.com/2026/04/14/the-power-of-hybrid-ai-reallusion-announces-2026-vision/)
- [How to Create an Environment for Filming VRoid/VRM in Unity（note / DEL-ZIG）](https://note.com/dlzig7/n/n85faea168133?hl=en)
- [Setting the scene: VRoid + Unity for animated cartoons（Extra Ordinary, the Series）](https://extra-ordinary.tv/2020/07/20/setting-the-scene-vroid-unity-for-animated-cartoons/)
- [AI Video Generation API Pricing（July 2026, buildmvpfast）](https://www.buildmvpfast.com/api-costs/ai-video)
- [Best AI Video Generation Models in 2026（Atlas Cloud）](https://www.atlascloud.ai/blog/guides/best-ai-video-generation-models-2026)
- [動画生成AI アニメ編 おすすめランキング 2026（note / ミツカル）](https://note.com/ai_mitsukaru/n/n352b38c849d7)
- [2026年最新 アニメ風AIモデルの未来はどう進化するのか（Cochi AI Blog）](https://cochi-404.hatenablog.com/entry/2026/03/04/152956)
- [What to know about the Sora discontinuation（OpenAI Help Center）](https://help.openai.com/en/articles/20001152-what-to-know-about-the-sora-discontinuation)
- [Sora shutdown reveals costly limits of AI video generation（TechXplore, 2026-04）](https://techxplore.com/news/2026-04-sora-shutdown-reveals-limits-ai.html)
- [Why OpenAI Killed Sora（Miraflow）](https://miraflow.ai/blog/why-openai-shut-down-sora-2026)

### AI検出精度・誤爆
- [55 AI-Generated Video Statistics: Disclosure, Detection, and Trust（Kapwing）](https://www.kapwing.com/resources/55-ai-generated-video-statistics-disclosure-detection-and-trust/)
- [Humans Cannot Detect AI-Generated Media But Communities May（arXiv:2605.24287）](https://arxiv.org/pdf/2605.24287)
- [Before Accusing an Artist of Using AI, Read This（How-To Geek）](https://www.howtogeek.com/before-accusing-an-artist-of-using-ai-read-this/)
- [A Huge Subreddit Suspended A User For Posting AI Art, But The Work Is 100% Human-Made（BuzzFeed News）](https://www.buzzfeednews.com/article/chrisstokelwalker/art-subreddit-illustrator-ai-art-controversy)
- [San Diego Comic-Con Draws a Line: No AI Art Allowed at 2026 Event](https://www.aol.com/articles/san-diego-comic-con-draws-003900609.html)

### 縦型ショートドラマ市場
- [ごっこ倶楽部、100億回再生を樹立（株式会社GOKKO / PR TIMES）](https://prtimes.jp/main/html/rd/p/000000054.000090916.html)
- [ごっこ倶楽部は課金型ドラマを年50本以上制作（日経クロストレンド）](https://xtrend.nikkei.com/atcl/contents/18/01271/00004/)
- [ショート動画のシリーズ化｜日本企業の成功事例3選（HolyTech）](https://holytech.jp/column/short-movie-case-study-global-latest-tiktok-2026-guide/)
- [AIキャラクター連続投稿型ショートドラマ 新フォーマット事例15選 2026年版](https://nightension.com/shortdramalab/blog38)
