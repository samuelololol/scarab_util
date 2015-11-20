#!/usr/bin/env python
# -*- coding: utf-8 -*-
__date__= 'Nov 20, 2015 '
__author__= 'samuel'


def InsertAbove(file_path, insert_text, target_text):
    _insert(file_path, insert_text, target_text, under=False)

def InsertUnder(file_path, insert_text, target_text):
    _insert(file_path, insert_text, target_text, under=True)

def _insert(file_path, insert_text, target_text, under=False):
    filecontent = []
    with open(file_path, 'r') as f:
        for line in f.readlines():
            filecontent.append(line)

    for idx, line in enumerate(filecontent):
        if target_text in line:
            lineno = idx
            indent_len = len(line) - len(line.lstrip())
            proper_indent_text = _normalize_text(insert_text, indent_len)
            if under: lineno += 1
            for insert_line in proper_indent_text:
                filecontent.insert(lineno, insert_line)
                lineno += 1
            break

    with open(file_path, 'wb') as f:
        for line in filecontent:
            f.write(line)

def _normalize_text(text_src, indent_len):
    text_content = []
    indent_min = 65536
    lindent = lambda line: len(line) - len(line.lstrip())

    for line in text_src:
        indent_v = lindent(line)
        if indent_min > indent_v:
            indent_min = indent_v

    indent_diff = indent_len - indent_min
    for line in text_src:
        if indent_diff >= 0:
            text_content.append(' '*indent_diff + line)
        else:
            text_content.append(line[(-1)*indent_diff:])
    return text_content


def main():
    import subprocess
    print subprocess.Popen(['cp', 'mytext.ori', 'mytext.txt']).communicate()[0]
    InsertUnder('./mytext.txt', ['<<<<<<<\n','right here\n', '<<<<<<<\n'], '123')

if __name__ == '__main__':
    main()
