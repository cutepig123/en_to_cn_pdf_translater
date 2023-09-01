# Introduction

A tool to translate English language pdf files to Chinese language pdf files

将英文pdf翻译成中文文档的工具

# Pre-requirements

The tool depends on following s/ws

- Python 3.8
- Microsoft Office 2016

It is written in Python. It depends on following python packages

- coloredlogs
- docx
- win32com
- selenium
- requests

# How to use

```bash
python main.py <the folder that contains the English version docx files>
```

eg

Original files in folder

```
G:\done>dir

 Directory of G:\done

2021/02/21  下午 02:07    <DIR>          .
2021/02/21  下午 02:07    <DIR>          ..
2020/11/22  下午 07:53        12,058,453 4dx_book.docx
```

Call command

```bash
python main.py G:\done
```

New files in the folder

```
G:\done>dir
 Directory of G:\done

2021/02/21  下午 02:07    <DIR>          .
2021/02/21  下午 02:07    <DIR>          ..
2020/11/22  下午 07:53        12,058,453 4dx_book.docx
2021/02/21  下午 01:14        12,094,133 4dx_book.docx-0.10-cn.docx
2021/02/21  下午 01:16        12,133,565 4dx_book.docx-0.20-cn.docx
2021/02/21  下午 01:18        12,173,398 4dx_book.docx-0.30-cn.docx
2021/02/21  下午 01:19        12,192,609 4dx_book.docx-0.40-cn.docx
2021/02/21  下午 01:20        12,208,961 4dx_book.docx-0.50-cn.docx
2021/02/21  下午 01:22        12,227,574 4dx_book.docx-0.60-cn.docx
2021/02/21  下午 01:24        12,259,462 4dx_book.docx-0.70-cn.docx
2021/02/21  下午 01:26        12,296,467 4dx_book.docx-0.80-cn.docx
2021/02/21  下午 01:27        12,319,642 4dx_book.docx-0.90-cn.docx
2021/02/21  下午 01:35        12,336,922 4dx_book.docx-cn-contents.docx
2021/02/21  下午 01:36         7,854,292 4dx_book.docx-cn-contents.pdf
2021/02/21  下午 01:29        12,336,919 4dx_book.docx-cn.docx
```

the final pdf file is `4dx_book.docx-cn-contents.pdf`

TODO

* [X] 实现Flask服务器，允许用户上传文件
  * [X] 上传文件大小限制
* [ ] 权限管理
  * [ ] 每个ip每一天最多免费翻译5页
  * [ ] 超过5页需要付款
* [ ] 扫码付款
  * [ ] paypal
  * [ ] alilay
  * [ ] wechat
