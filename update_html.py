import codecs
import re
import sys

html_path = r"g:\マイドライブ\ゼミ\liwc\実験計画\uso\倫理審査_研究計画書_候補1.html"

try:
    with codecs.open(html_path, "r", "utf-8") as f:
        text = f.read()
except Exception as e:
    print(f"Failed to read file: {e}")
    sys.exit(1)

# 1. 候補1 -> 候補2
text = text.replace("候補1（筆記開示パラダイム）", "候補2（感情状態操作・出来事記述パラダイム）")

# 2. 研究計画 ~ 9.公表方法
text = re.sub(
    r'<h3>実施手順</h3>.*?<hr>\s*<!-- ========== 9\. 公表方法 ========== -->',
    r'''<h3>実施手順</h3>
        <p>本研究は、感情状態の操作による構成概念妥当性検証実験である（五十嵐ら, 2022の手続きに基づく）。参加者間デザインにより、参加者をポジティブ感情条件、ネガティブ感情条件、統制条件のいずれか1条件にランダムに割り当てて実施する。</p>

        <h4>フロー図</h4>
        <div class="flow">【実験の全体フロー】

  ┌──────────────────────────────────────────────┐
  │ ステップ1：同意取得・実験説明（5分）         │
  │   ・研究説明書を用いた口頭説明               │
  │   ・同意書への署名                           │
  └──────────────┬───────────────────────────────┘
                  ↓
  ┌──────────────────────────────────────────────┐
  │ ステップ2：事前質問紙（15分）                │
  │   ・属性情報（年齢、性別等）                 │
  │   ・BFS（日本語版Big Five短縮版）            │
  │   ・STAI（状態-特性不安尺度）                │
  │   ・POMS短縮版（気分プロフィール）           │
  └──────────────┬───────────────────────────────┘
                  ↓
  ┌──────────────────────────────────────────────┐
  │ ステップ3：Biopacセンサ装着・ベースライン    │
  │           測定（5分）                        │
  │   ・EDA100Cモジュール：非利き手第2・第3指    │
  │   ・ECG/PPGモジュール                        │
  │   ・安静座位にてベースライン5分測定          │
  └──────────────┬───────────────────────────────┘
                  ↓
  ┌──────────────────────────────────────────────┐
  │ ステップ4：筆記セッション（10分）            │
  │                                              │
  │ 指定された条件のテーマについて、200文字以上   │
  │ でPCに記述させる。                           │
  │                                              │
  │ 【A：ポジティブ感情条件】最近経験したポジ    │
  │   ティブな出来事                             │
  │ 【B：ネガティブ感情条件】最近経験したネガ    │
  │   ティブな出来事                             │
  │ 【C：統制条件】特に何もない平凡な一日の出    │
  │   来事                                       │
  │                                              │
  │ ※筆記中はBiopacで生理反応を連続記録         │
  └──────────────┬───────────────────────────────┘
                  ↓
  ┌──────────────────────────────────────────────┐
  │ ステップ5：事後質問紙（5分）                 │
  │   ・事後POMS短縮版                           │
  │   ・操作チェック（快・不快度 1項目、         │
  │     インパクト 2項目：五十嵐ら, 2022）       │
  │   ・PANAS（顕在的感情の測定：16項目）        │
  │   ・筆記体験の主観評価（評価VAS）            │
  └──────────────┬───────────────────────────────┘
                  ↓
  ┌──────────────────────────────────────────────┐
  │ ステップ6：デブリーフィング・謝礼付与（5分） │
  │   ・研究目的の全体説明と謝礼付与             │
  │   ・一時的不快感への対処説明・相談窓口案内   │
  └──────────────────────────────────────────────┘

  所要時間合計：約45〜50分</div>

        <h4>研究実施体制</h4>
        <ul>
            <li><strong>研究実施代表者</strong>：〔氏名〕（卒論執筆者）── 実験の計画・実施・データ解析の全般を担当</li>
            <li><strong>指導教員</strong>：〔氏名〕── 研究計画の監督・倫理的事項の確認</li>
            <li><strong>実施場所</strong>：〔大学名〕〔キャンパス名〕〔建物名〕〔部屋番号〕の個室実験室</li>
        </ul>

        <h4>群分けの内訳</h4>
        <p>参加者間デザインにより、以下の3群にランダムに割り当てる（各群約30名、計約90名）。<br>
        1. ポジティブ感情条件群<br>
        2. ネガティブ感情条件群<br>
        3. 統制条件群</p>

        <h4>収集データの分析・解析方法</h4>

        <p><strong>分析1：構成概念妥当性の検証（質問紙指標との関連）</strong><br>
            KAISEKIの各カテゴリスコアと、質問紙指標（Big Five、STAI、POMS）のピアソン相関分析を実施する。理論的根拠：Pennebaker &amp; King（1999）が実証したように、日本語でも同様のパターン（例：神経症傾向とネガティブ感情語の相関など）が再現できるかを検証する。</p>

        <p><strong>分析2：条件間比較（感情状態の操作チェックと妥当性確認）</strong><br>
            操作チェック項目およびPANASの得点を従属変数とした一要因分散分析（3条件）を行う。KAISEKIスコア比較：感情的プロセスカテゴリ等のスコアを従属変数とし一要因分散分析で条件間の差を検証する。ポジティブ条件でポジティブな語が、ネガティブ条件でネガティブな語が有意に多くなることを確認できれば妥当性の証拠とする。</p>

        <p><strong>分析3：J-LIWCとの比較</strong><br>
            同一テキストに対するKAISEKIとJ-LIWC2015の解析結果を比較する（相関係数の差の検定）。KAISEKIのカテゴリスコアが同等以上に実験条件を弁別できる場合、優位性の証拠とする。</p>

        <p><strong>分析4：生理-言語対応</strong><br>
            筆記中のEDA変化量、HR/HRV指標（生理指標）とKAISEKIの各カテゴリスコアの相関・重回帰分析を実施する。理論的根拠：Lieberman et al.（2007）らが示す感情と言語化・生理的反応の連動。</p>

        <p><strong>統計的基準</strong>：有意水準α = .05（両側）、多重比較補正：Tukey法またはBenjamini-Hochberg法、効果量：η²、r等を報告する。</p>

        <hr>

        <!-- ========== 9. 公表方法 ========== -->''',
    text,
    flags=re.DOTALL
)

# 3. 10. 対象者数
text = re.sub(
    r'<h2>10\. 対象者数とその設定根拠</h2>.*?</p>\s*<hr>',
    r'''<h2>10. 対象者数とその設定根拠</h2>
        <p><strong>対象者総数：90名</strong>（各群30名、最低各群25名）</p>
        <p><strong>対象者数の設定根拠：</strong>本研究における主要な分析は、3条件（ポジティブ、ネガティブ、統制）の一要因分散分析である。五十嵐ら (2022) の手続きに準じ、各種心理効果等の効果量 f = 0.35（中〜大程度）、有意水準 α = 0.05、検出力 1 - β = 0.80 で G*Power 3 (Faul et al., 2007) により検定力分析を行った場合、要請されるサンプルサイズは約84名となる。実験途中の脱落や文字数不足による除外を考慮し全体で90名を目標とする。</p>

        <hr>''',
    text,
    flags=re.DOTALL
)

# 4. 13. 除外条件
text = re.sub(
    r'<h2>13\. 研究開始後に対象者を除外する条件</h2>.*?</ol>\s*<hr>',
    r'''<h2>13. 研究開始後に対象者を除外する条件</h2>
        <ol>
            <li>指定されたテーマに関する記述が200文字未満であった場合、または記述内容が全くのナンセンス・無意味であった場合（五十嵐ら, 2022）。</li>
            <li>指定されたテーマに明らかに沿っていない内容を記述したと判断される場合。</li>
            <li>生理データに測定機器の不具合による重大なアーティファクトが含まれ有効なデータとして使用できない場合。</li>
            <li>質問紙の回答に明らかなランダム回答パターンが認められた場合。</li>
        </ol>

        <hr>''',
    text,
    flags=re.DOTALL
)

# 5. 負担とリスク 16-18
text = re.sub(
    r'<h2>16\. 対象者の負担</h2>.*?</p>\s*<hr>\s*<!-- 19 -->',
    r'''<h2>16. 対象者の負担</h2>
        <p><strong>負担の有無：</strong> ☑ ②ある</p>
        <ol>
            <li><strong>時間的拘束</strong>：実験参加のために約45〜50分の時間を拘束される。</li>
            <li><strong>筆記課題の遂行</strong>：指定されたテーマ（最近経験したポジティブな出来事、ネガティブな出来事、または平凡な一日の出来事）について、PCを用いて200文字以上の文章を記述する負担がある。</li>
            <li><strong>質問紙への回答</strong>：事前・事後合わせて約150項目の質問紙（事前のBFS・STAI等、事後のPOMS・PANAS等）に回答する。</li>
            <li><strong>センサ装着</strong>：Biopac用電極を非利き手の指等に装着し、実験中維持する（軽度の不快感の可能性）。</li>
        </ol>

        <hr>

        <!-- 17 -->
        <h2>17. 予測されるリスク</h2>
        <p><strong>リスクの有無：</strong> ☑ ②ある</p>
        <ol>
            <li><strong>一時的な心理的不快感</strong>：ネガティブ感情条件に割り当てられた場合、ネガティブな出来事を想起・記述することにより一時的に不快感や悲しみ等のネガティブな気分が喚起される可能性がある。ただし先行研究（Baikie et al., 2012; Stockton et al., 2014; 五十嵐ら, 2022）によれば、自己の感情体験を言語的に記述・報告する手続きにおいて、参加者のストレスレベルの持続的な上昇や心理的健康の悪化が直接引き起こされるわけではないことが示されている。</li>
            <li><strong>フラッシュバックのリスク（極めて低い）</strong>：除外基準で精神疾患治療中の者や重篤なトラウマ体験直後の者を除外することでリスクを最小化している。</li>
            <li><strong>生理計測に伴う負担</strong>：センサの装着により、極めて稀に皮膚に軽度のかゆみ等が発生する可能性がある。</li>
        </ol>

        <hr>

        <!-- 18 -->
        <h2>18. 負担、リスク及び利益をふまえた総合的評価</h2>
        <h4>負担・リスクを最小化するための方策</h4>
        <ol>
            <li><strong>事前スクリーニング</strong>：除外基準（精神疾患治療中の者等）により高リスク者の参加を回避。</li>
            <li><strong>任意性とテーマ提示時の確認</strong>：割り当てられたテーマでの記述を希望しない場合は直ちに実験を中止できることを伝える。</li>
            <li><strong>安全な実験室環境</strong>：オンライン実験と異なり、実験者が近傍（別室等）に待機するため早急な対応が可能。</li>
            <li><strong>事後ケア</strong>：デブリーフィングでの説明、および学生相談室・カウンセリングセンターの連絡先配布。</li>
            <li><strong>生理計測の安全性</strong>：非侵襲的であり、異常を感じた場合は自己判断での取り外しも可能であることを説明する。</li>
        </ol>
        <h4>総合的評価</h4>
        <p>本研究における参加者の負担・リスクは、時間的拘束と一部の条件におけるネガティブな気分の一時的な喚起等に留まる。これらは、先行研究（五十嵐ら, 2022 等）によって安全性が確認された一般的な手続きである。本研究の科学的利益として（1）日本語における文脈理解型言語解析システム（KAISEKI）の妥当性が生理指標・質問紙指標との連動を含めて実証されること、（2）日本人の心理的特性と言語表出の関係について新たな知見が提供されることが挙げられる。参加者への負担に対する安全配慮は十分に準備されており、以上から、<strong>負担・リスクは利益を上回らない</strong>と判断する。
        </p>

        <hr>

        <!-- 19 -->''',
    text,
    flags=re.DOTALL
)

# 6. テーブル修正
text = re.sub(
    r'<h4>ⅰ．内容</h4>\s*<table>.*?</table>',
    r'''<h4>ⅰ．内容</h4>
        <table>
            <tr>
                <th>データの種類</th>
                <th>具体的内容</th>
                <th>収集方法</th>
            </tr>
            <tr>
                <td>属性情報</td>
                <td>年齢、性別（自由記述）、学歴、職業（属性）、利き手</td>
                <td>紙面またはオンラインフォーム</td>
            </tr>
            <tr>
                <td>質問紙データ</td>
                <td>BFS（Big Five）、STAI（状態-特性不安尺度）、POMS短縮版、出来事の快・不快度・インパクト、PANAS（顕在的感情測定）、筆記体験の主観評価（VAS等）</td>
                <td>紙面またはオンラインフォーム</td>
            </tr>
            <tr>
                <td>筆記テキスト</td>
                <td>指定されたテーマ（ポジティブ、ネガティブ、または平凡な一日の出来事）に関する記述（200文字以上）</td>
                <td>PC上のテキストエディタへの入力</td>
            </tr>
            <tr>
                <td>生理データ</td>
                <td>SCR/EDA（非利き手に電極装着）、HR/HRV（所定部位に電極装着）</td>
                <td>Biopac等を用いた連続記録</td>
            </tr>
            <tr>
                <td>同意書</td>
                <td>参加者の署名入り同意書（氏名を含む）</td>
                <td>紙面</td>
            </tr>
        </table>''',
        text,
        flags=re.DOTALL
)

# 7. References
text = re.sub(
    r'<div class="ref">\s*<h3>参考文献</h3>.*?</div>',
    r'''<div class="ref">
            <h3>参考文献</h3>
            <p>1. Baikie, K. A., Geerligs, L., &amp; Wilhelm, K. (2012). Expressive writing and positive writing for participants with neurological illness: A randomized controlled trial. <em>Health Psychology</em>, 31(4), 428-436.</p>
            <p>2. Faul, F., Erdfelder, E., Lang, A.-G., &amp; Buchner, A. (2007). G*Power 3. <em>Behavior Research Methods</em>, 39(2), 175–191.</p>
            <p>3. Frattaroli, J. (2006). Experimental disclosure and its moderators: A meta-analysis. <em>Psychological Bulletin</em>, 132(6), 823–865.</p>
            <p>4. Hockemeyer, J. R., Smyth, J. M., Anderson, C. F., &amp; Stone, A. A. (1999). Is it safe to write? <em>Psychosomatic Medicine</em>, 61(1), 99.</p>
            <p>5. Igarashi, T., Okuda, S., &amp; Sasahara, K. (2022). Development of the Japanese version of the LIWC dictionary 2015. <em>Frontiers in Psychology</em>, 13, 841534.</p>
            <p>6. Lieberman, M. D., et al. (2007). Putting feelings into words. <em>Psychological Science</em>, 18(5), 421–428.</p>
            <p>7. Panzeri, A., et al. (2021). Linguistic predictors of psychological adjustment in healthcare workers. <em>IJERPH</em>, 18(24), 13302.</p>
            <p>8. Pennebaker, J. W. (1997). <em>Opening up: The healing power of expressing emotions</em>. Guilford Press.</p>
            <p>9. Pennebaker, J. W., Boyd, R. L., Jordan, K., &amp; Blackburn, K. (2015). <em>The development and psychometric properties of LIWC2015</em>.</p>
            <p>10. Pennebaker, J. W., &amp; King, L. A. (1999). Linguistic styles. <em>JPSP</em>, 77(6), 1296–1312.</p>
            <p>11. Steiger, J. H. (1980). Tests for comparing elements of a correlation matrix. <em>Psychological Bulletin</em>, 87(2), 245–251.</p>
            <p>12. Stockton, H., Joseph, S., &amp; Hunt, N. (2014). Expressive writing and posttraumatic growth: An exploratory study. <em>Humanistic Psychologist</em>, 42(4), 384-394.</p>
        </div>''',
        text,
        flags=re.DOTALL
)

try:
    with codecs.open(html_path, "w", "utf-8") as f:
        f.write(text)
    print("HTML replacement complete.")
except Exception as e:
    print(f"Failed to write file: {e}")
    sys.exit(1)
