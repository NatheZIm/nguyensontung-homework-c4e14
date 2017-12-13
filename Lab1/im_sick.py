from gmail import *
from random import *
from datetime import *
t = datetime.now().time()
reason = ["Xe máy em đang đi bị tuột xích","do bà em bị ốm","hôm qua em đi đá bóng bị gãy chân , hôm nay em phải đi khám mắt"]
html_content = '''<p style="text-align: center;">Cộng h&ograve;a - X&atilde; hội -Chủ Nghĩa - Việt Nam</p>
<p style="text-align: center;">Độc lập - Tự Do - Hạnh ph&uacute;c</p>
<h2 style="text-align: center;">Đơn xin nghỉ học&nbsp;</h2>
<p>&nbsp;</p>
<p>Em ch&agrave;o thầy,</p>
<p>Em viết đơn n&agrave;y để xin ph&eacute;p thầy cho em nghỉ buổi học h&ocirc;m nay , {{REASON}} , em hứa sẽ l&agrave;m b&agrave;i đầy đủ trước khi đến lớp</p>
<p>Em cảm ơn thầy</p>
<p style="text-align: right;">Học Sinh của thầy</p>
<p style="text-align: right;">T&ugrave;ng</p>
<p style="text-align: right;">Nguyễn Sơn T&ugrave;ng</p>'''
pick = choice(reason)
html_content = html_content.replace("{{REASON}}",pick)
if t == "07:00:00":
    gmail = GMail("blazingsenpai@gmail.com","tungsaker")
    msg = Message("Ola Senor",to = "nguyensontung311@gmail.com",html = html_content)
    gmail.send(msg)
