word_forbidden = "非法游行"
text = input("请输入内容：")
if "非法游行" in text:
    text_1=text.replace("非法游行","****")
    print(text_1)
else:
    print(text)
