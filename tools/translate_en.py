"""English translations for the Japanese UI text the working (Japan) extraction pulls out of
`main` - car paint colours today, more text sources (tools/wear_texts.txt, titles, ...) later.
Kept as a separate substitution layer rather than hand-edited into the generated files, since
cardb.py/weartexts.py/etc. overwrite those every run: translate(text) is called right before a
string is handed to render_text, so the extraction pipeline itself stays untouched and still
reads the working Japan binary.
"""

# car paint colours (tools/cars.json "texts", cardb.py TEXT_FIRST on): standard automotive
# colour names (base hue + finish: mica/metallic/pearl/solid), not creative text
CAR_COLORS = {
    "シルバー": "Silver", "レッド": "Red", "イエロー": "Yellow", "ホワイト": "White", "ブラック": "Black",
    "カッパーレッドマイカ": "Copper Red Mica", "ギャラクシーグレーマイカ": "Galaxy Grey Mica",
    "サンライトシルバーメタリック": "Sunlight Silver Metallic", "ブリリアントブラック": "Brilliant Black",
    "ストミーブルーマイカ": "Stormy Blue Mica", "ハイランドグリーン": "Highland Green",
    "ウイニングブルーメタリック": "Winning Blue Metallic", "チタニウムグレーメタリックБ": "Titanium Grey Metallic",
    "スノーフレイクホワイトパールマイカ": "Snowflake White Pearl Mica", "ライトニングイエロー": "Lightning Yellow",
    "ベロシティレッドマイカ": "Velocity Red Mica", "サンバーストイエロー": "Sunburst Yellow",
    "イノセントブルーマイカ": "Innocent Blue Mica", "ヴィンテージレッド": "Vintage Red", "ピュアホワイト": "Pure White",
    "ブレイズレッド": "Blaze Red", "クリスタルホワイト": "Crystal White", "シャドーシルバーマイカ": "Shadow Silver Mica",
    "ブレイブブルーマイカ": "Brave Blue Mica", "コバートグレー": "Covert Grey", "クラシックレッド": "Classic Red",
    "メテオブルーメタリック": "Meteor Blue Metallic", "メロウイエローマイカ": "Mellow Yellow Mica",
    "モイストシルバーメタリック": "Moist Silver Metallic", "ブラックマイカ": "Black Mica",
    "ラディアントエボニーマイカ": "Radiant Ebony Mica", "レッドメタリック": "Red Metallic",
    "クールシルバーメタリック": "Cool Silver Metallic", "ライトニングブルーマイカ": "Lightning Blue Mica",
    "ファントムブラックパール": "Phantom Black Pearl", "ホワイトパール": "White Pearl",
    "ミディアムパープリッシュグレーマイカ": "Medium Purplish Grey Mica", "レッドソリッド": "Red Solid",
    "ホワイトソリッド": "White Solid", "ランスブルー": "Lance Blue", "スコーティアホワイト": "Scotia White",
    "サテライトシルバー": "Satellite Silver", "アイセルブルー": "Icel Blue", "ピレネーブラック": "Pyrenees Black",
    "ダンデライオンイエロー": "Dandelion Yellow", "パルマーレッド": "Palmer Red", "ピレーネブラック": "Pyrenees Black",
    "クイーンズシルバー": "Queens Silver", "モナコレッド": "Monaco Red", "パッションレッド": "Passion Red",
    "ギャラクシーホワイト": "Galaxy White", "シンフォニックシルバー": "Symphonic Silver", "マリアナブルー": "Mariana Blue",
    "アルティメイトメタルシルバー": "Ultimate Metal Silver", "タイタニウムグレー": "Titanium Grey",
    "ブリリアントホワイトパール": "Brilliant White Pearl", "バイブラントレッド": "Vibrant Red",
    "ダークメタルグレー": "Dark Metal Grey", "スーパーブラック": "Super Black", "ブレードシルバー": "Blade Silver",
    "イエローソリッド": "Yellow Solid", "プレミアムブルー": "Premium Blue", "ダイヤモンドブラック": "Diamond Black",
    "ダイヤモンドシルバー": "Diamond Silver", "バーニングレッド": "Burning Red", "サンセットオレンジ": "Sunset Orange",
    "モンテレーブルー": "Monterey Blue", "スーパーレッド": "Super Red", "イエローパール": "Yellow Pearl",
    "センシティブシルバー": "Sensitive Silver", "ブラックパール": "Black Pearl", "ダークブルーパール": "Dark Blue Pearl",
    "シルバー(M)ツートン": "Silver (M) Two-Tone", "ワイン(M)ツートン": "Wine (M) Two-Tone",
    "グランプリオレンジ": "Grand Prix Orange", "モンテカルロシルバー": "Monte Carlo Silver",
    "デイトナレッド": "Daytona Red", "ル・マンイエロー": "Le Mans Yellow", "グランプリホワイト": "Grand Prix White",
    "ミッドナイトブルー": "Midnight Blue", "スパークリングシルバー": "Sparkling Silver",
    "ブリリアントブルー": "Brilliant Blue", "パールホワイト": "Pearl White", "イエロイッシュシルバー": "Yellowish Silver",
    "ダークグリーン": "Dark Green", "ダークグレイ": "Dark Grey", "スカイラインレッド": "Skyline Red",
    "スカイラインシルバーメタリック": "Skyline Silver Metallic", "スカイラインホワイト": "Skyline White",
    "スカイラインブラウン": "Skyline Brown", "ガングレーメタリック": "Gun Grey Metallic",
    "ブラックパールメタリック": "Black Pearl Metallic", "レッドパール": "Red Pearl",
    "スパークシルバーメタリック": "Spark Silver Metallic", "ミッドナイトパープル": "Midnight Purple",
    "ディープマリンブルー": "Deep Marine Blue", "ソニックシルバー": "Sonic Silver", "アクティブレッド": "Active Red",
    "ベイサイドブルー": "Bayside Blue", "ミレニアムジェイド": "Millennium Jade",
    "ダークグレー・メタリック": "Dark Grey Metallic", "ＷＲブルー・マイカ": "WR Blue Mica",
    "ライトニングレッド": "Lightning Red", "ミッドナイトブルー・パール": "Midnight Blue Pearl",
    "スパークシルバー・メタリック": "Spark Silver Metallic", "WRブルー・マイカ": "WR Blue Mica",
    "ソリッドレッド": "Solid Red", "クリスタルグレー・メタリック": "Crystal Grey Metallic",
    "オブシディアンブラック・パール": "Obsidian Black Pearl", "プレミアムシルバー・メタリック": "Premium Silver Metallic",
    "ブラックトパーズ・マイカ": "Black Topaz Mica", "カシミヤイエロー": "Cashmere Yellow",
    "グランブルー・マイカ": "Grand Blue Mica", "アークティックシルバー": "Arctic Silver", "クールグレー": "Cool Grey",
    "アークティックホワイト・パール": "Arctic White Pearl", "ブリリアントシルバー・メタリック": "Brilliant Silver Metallic",
    "ガーネットレッド・パール": "Garnet Red Pearl", "リーガルブルー・パール": "Regal Blue Pearl",
    "シルバーメタリック/グレーメタリック": "Silver Metallic / Grey Metallic", "レッドマイカ": "Red Mica",
    "ダークグレーメタリック": "Dark Grey Metallic", "クリムソンマイカ": "Crimson Mica", "ホワイトマイカ": "White Mica",
    "シルバーメタリックグラファイト": "Silver Metallic Graphite", "スーパーホワイトБ": "Super White",
    "スーパーレッドД": "Super Red", "スーパーブライトイエロー": "Super Bright Yellow",
    "ブルーマイカメタリック": "Blue Mica Metallic", "スーパーホワイトГ": "Super White",
    "ダークグリーンマイカ": "Dark Green Mica", "ブルーメタリック": "Blue Metallic", "スーパーレッドБ": "Super Red",
    "ストロングブルーメタリック": "Strong Blue Metallic", "シルバーメタリック": "Silver Metallic",
    "ダークブルーマイカ": "Dark Blue Mica", "ワインレッドマイカ": "Wine Red Mica",
    "ホワイトパールマイカ": "White Pearl Mica", "スーパーシルバーВメタリック": "Super Silver Metallic",
    "ガッちゃんパープル": "Gatchan Purple", "ホワイトパールクリスタルシャイン": "White Pearl Crystal Shine",
    "ボルドーマイカ": "Bordeaux Mica", "シルバーマイカメタリック": "Silver Mica Metallic",
    "エレガントパールトーニング": "Elegant Pearl Toning", "アクアシルバートーニング": "Aqua Silver Toning",
    "ライトグリーンメタリック": "Light Green Metallic", "ダークグリーンマイカメタリック": "Dark Green Mica Metallic",
    "ダークブルー": "Dark Blue", "シルキーホワイト・パール": "Silky White Pearl",
    "ピスタチオグリーン・オパール": "Pistachio Green Opal", "プリズムブルー・メタリック": "Prism Blue Metallic",
    "ベリーレッド・メタリック": "Berry Red Metallic", "シャイニーシルバー・メタリック": "Shiny Silver Metallic",
    "個人タクシー": "Private Taxi", "教習車": "Driving School Car",
    "アルティメイトオパールブラック": "Ultimate Opal Black",
}

# tools/wear_texts.txt (tools/weartexts.py): the part-install confirmation banner
# (clSeqTgWearPartsAeroThread::run). Sticker names here match actual in-game items, including
# the Namco/Pac-Man promotional decals that already exist in the original data - translating
# their existing label text, not creating new references to them.
WEAR_TEXTS = {
    "純正パーツに交換完了！": "Genuine parts installed!",
    "エアロパーツセットＡ装着完了！": "Aero Parts Set A installed!",
    "エアロパーツセットＢ装着完了！": "Aero Parts Set B installed!",
    "エアロパーツセットＣ装着完了！": "Aero Parts Set C installed!",
    "エアロパーツセット装着完了！": "Aero Parts Set installed!",
    "純正ボンネットに交換完了！": "Genuine bonnet installed!",
    "ＦＲＰボンネット(ダクト付き)装着完了！": "FRP Bonnet (with Duct) installed!",
    "カーボンボンネット(純正形状)装着完了！": "Carbon Bonnet (Genuine Shape) installed!",
    "カーボンボンネット(ダクト付き)装着完了！": "Carbon Bonnet (with Duct) installed!",
    "純正ウィングに交換完了！": "Genuine wing installed!",
    "車種別ウィング装着完了！": "Model-Specific Wing installed!",
    "ＧＴウィング(ストレート)装着完了！": "GT Wing (Straight) installed!",
    "ＧＴウィング(３Ｄ形状)装着完了！": "GT Wing (3D Shape) installed!",
    "ウィングを取り外し完了！": "Wing removed!",
    "純正ミラーに交換完了！": "Genuine mirrors installed!",
    "エアロミラー装着完了！": "Aero Mirrors installed!",
    "装着完了！": "Installed!",
    "純正ホイールに交換完了！": "Genuine wheels installed!",
    "取り外し完了！": "Removed!",
    "ネオン管（ストレート）グリーン装着完了！": "Neon Tube (Straight) Green installed!",
    "ネオン管（ストレート）ブルー装着完了！": "Neon Tube (Straight) Blue installed!",
    "ネオン管（ストレート）パープル装着完了！": "Neon Tube (Straight) Purple installed!",
    "ネオン管（ストレート）レッド装着完了！": "Neon Tube (Straight) Red installed!",
    "ネオン管（ストレート）イエロー装着完了！": "Neon Tube (Straight) Yellow installed!",
    "ネオン管(ストレート)ダークパープル装着完了！": "Neon Tube (Straight) Dark Purple installed!",
    "ネオン管（スポット）グリーン装着完了！": "Neon Tube (Spot) Green installed!",
    "ネオン管（スポット）ブルー装着完了！": "Neon Tube (Spot) Blue installed!",
    "ネオン管（スポット）パープル装着完了！": "Neon Tube (Spot) Purple installed!",
    "ネオン管（スポット）レッド装着完了！": "Neon Tube (Spot) Red installed!",
    "ネオン管（スポット）イエロー装着完了！": "Neon Tube (Spot) Yellow installed!",
    "ネオン管（スポット）ダークパープル装着完了！": "Neon Tube (Spot) Dark Purple installed!",
    "ステッカー（ラインパターン１）装着完了！": "Sticker (Line Pattern 1) installed!",
    "ステッカー（ラインパターン２）装着完了！": "Sticker (Line Pattern 2) installed!",
    "ステッカー（ファイアーパターン１）装着完了！": "Sticker (Fire Pattern 1) installed!",
    "ステッカー（ファイアーパターン２）装着完了！": "Sticker (Fire Pattern 2) installed!",
    "ステッカー（ナムコ）装着完了！": "Sticker (Namco) installed!",
    "ステッカー（パックマン）装着完了！": "Sticker (Pac-Man) installed!",
    "ステッカー（ワークスカラー）装着完了！": "Sticker (Works Color) installed!",
    "ステッカー（ラインパターン３）装着完了！": "Sticker (Line Pattern 3) installed!",
    "ステッカー（ファイアーパターン３）装着完了！": "Sticker (Fire Pattern 3) installed!",
    "ステッカー（トライバル）装着完了！": "Sticker (Tribal) installed!",
}

# tools/storysel_texts.txt: the story mode rival-select screen's chapter titles and the
# ramps/locations shown with them - short labels (like a level-select menu), not the rival
# dialogue itself (that is sttune_texts.txt, left in Japanese); the ramp names are real Tokyo/
# Osaka highway interchanges, so translated the same way as a place name
STORYSEL_TEXTS = {
    "悪魔のＺ復活前編": "Devil Z's Revival - Part 1", "悪魔のＺ復活後編": "Devil Z's Revival - Part 2",
    "とびきりのＧＴ－Ｒ編": "The Exceptional GT-R", "赤坂ストレート編": "Akasaka Straight",
    "モンスターマシン前編": "Monster Machine - Part 1", "モンスターマシン後編": "Monster Machine - Part 2",
    "Ｒ２００ＣＬＵＢ前編": "R200 CLUB - Part 1", "Ｒ２００ＣＬＵＢ後編": "R200 CLUB - Part 2",
    "阪神高速環状前編": "Hanshin Expwy Loop - Part 1", "阪神高速環状後編": "Hanshin Expwy Loop - Part 2",
    "幻のＦＣ前編": "The Phantom FC - Part 1", "幻のＦＣ後編": "The Phantom FC - Part 2",
    "ガレージＡＣＥ前編": "Garage ACE - Part 1", "ガレージＡＣＥ後編": "Garage ACE - Part 2",
    "幻のＦ１タービン前編": "The Phantom F1 Turbo - Part 1", "幻のＦ１タービン後編": "The Phantom F1 Turbo - Part 2",
    "イシダ編": "Ishida", "地上のゼロ編": "Zero on the Ground",
    "ＦＤマスター前編": "FD Master - Part 1", "ＦＤマスター後編": "FD Master - Part 2",
    "チューナー編前編": "The Tuner - Part 1", "チューナー編後編": "The Tuner - Part 2",
    "スタートランプ": "Start Ramp", "神田橋ランプ": "Kandabashi Ramp", "汐留ランプ": "Shiodome Ramp",
    "芝公園ランプ": "Shiba Koen Ramp", "有明ランプ": "Ariake Ramp", "木場ランプ": "Kiba Ramp",
    "臨海副都心ランプ": "Rinkai Fukutoshin Ramp", "大黒ふ頭ランプ": "Daikoku Futo Ramp",
    "空港中央ランプ": "Airport Central Ramp", "芝浦ランプ": "Shibaura Ramp", "汐入ランプ": "Shioiri Ramp",
    "羽田ランプ": "Haneda Ramp", "道頓堀ランプ": "Dotonbori Ramp", "箱根往路": "Hakone Outbound",
    "箱根復路": "Hakone Return", "御殿場": "Gotemba", "丸の内ランプ": "Marunouchi Ramp", "箱根": "Hakone",
}

TRANSLATIONS = {}
TRANSLATIONS.update(CAR_COLORS)
TRANSLATIONS.update(WEAR_TEXTS)
TRANSLATIONS.update(STORYSEL_TEXTS)


def translate(text):
    """text unchanged if there's no translation for it yet (so partially-translated sources
    still pack cleanly); logs anything untranslated to stderr once, for tools/translate_check.py
    to catch later."""
    return TRANSLATIONS.get(text, text)
