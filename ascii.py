import re


def wrap_ascii_art(html_content):
    # 使用正则表达式匹配<pre class="logo">和</pre>之间的内容
    pattern = r'(<pre class="logo">)([\s\S]*?)(</pre>)'

    def wrap_chars(match):
        pre_start, ascii_art, pre_end = match.groups()
        # 将每个字符(包括空格)用<span>包裹
        wrapped_art = "".join(
            f'<span class="char">{char}</span>' if char != "\n" else "\n"
            for char in ascii_art
        )
        return f"{pre_start}{wrapped_art}{pre_end}"

    # 使用re.sub替换匹配到的内容
    wrapped_html = re.sub(pattern, wrap_chars, html_content)
    return wrapped_html


# 测试函数
html_content = """
<pre class="logo">
   ____      _                        
  / __ \ ___(_)_   _ _ __ _   _ _   _ 
 / / _` / __| | | | | '__| | | | | | |
| | (_| \__ \ | |_| | |  | |_| | |_| |
 \ \__,_|___/_|\__, |_|   \__, |\__,_|
  \____/       |___/      |___/       
</pre>
"""

wrapped_html = wrap_ascii_art(html_content)
print(wrapped_html)
