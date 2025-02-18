import wikipedia
wikipedia.set_lang("ja") # 言語設定を日本語にする
titles = wikipedia.search("漫才") # 『漫才』で検索をかける
print(titles)
"""output example
['漫才', '漫才協会', 'NHK上方漫才コンテスト', 'ANZEN漫才', 'Ytv漫才新人賞', 'MBS漫才アワード', 'オールザッツ漫才', '上方漫才大賞', 'ダウンタウン (お笑いコン ビ)', '漫才ブーム']
"""
# 『漫才』の全ページ情報を取得
page_content = wikipedia.page("漫才").content
print(page_content)
"""output example 漫才(まんざい)は、2人ないしそれ以上の複数人による寄席演芸の一種目。通常はコ...... """
# 要約文を取得
page_summary = wikipedia.page("漫才").summary 
print(page_summary)
# ページのHTML情報を取得
page_html = wikipedia.page("漫才").html() 
print(page_html)