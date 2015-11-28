#!/usr/bin/env python
# -*- coding: utf-8 -*-
__date__= 'Nov 20, 2015 '
__author__= 'samuel'


def InsertAbove(file_path, insert_text, target_text, after=None, before=None):
    _insert(file_path, insert_text, target_text, after=after, before=before, under=False)

def InsertUnder(file_path, insert_text, target_text, after=None, before=None):
    _insert(file_path, insert_text, target_text, after=after, before=before, under=True)

def AppendAbove(file_path, insert_text, target_text, after=None, before=None):
    _append(file_path, insert_text, target_text, after=None, before=before, under=False)

def AppendUnder(file_path, insert_text, target_text, after=None, before=None):
    _append(file_path, insert_text, target_text, after=None, before=before, under=True)


def _insert(file_path, insert_text, target_text, after=None, before=None, under=False):
    filecontent = []
    with open(file_path, 'r') as f:
        for line in f.readlines():
            filecontent.append(line)

    after_status = True if after == None else False
    before_status = True if before == None else False
    met_status = False
    for idx, line in enumerate(filecontent):
        if before_status != True:
            if isinstance(before, list):
                if len([x for x in before if x in line]) > 0:
                    before_status = True
                    break
            else:
                if before in line:
                    before_status = True
                    break
        if after_status != True:
            if isinstance(after, list):
                #after one of string in 'after' list
                if len([x for x in after if x in line]) > 0:
                    after_status = True
                    continue
            else:
                if after not in line:
                    after_status = True
                    continue
        if isinstance(target_text, list):
            if len([x for x in target_text if x in line]) > 0:
                met_status = True
                lineno = idx
                indent_len = len(line) - len(line.lstrip())
                proper_indent_text = _normalize_text(insert_text, indent_len)
                if under: lineno += 1
                for insert_line in proper_indent_text:
                    filecontent.insert(lineno, insert_line)
                    lineno += 1
                break
        else:
            if target_text in line:
                met_status = True
                lineno = idx
                indent_len = len(line) - len(line.lstrip())
                proper_indent_text = _normalize_text(insert_text, indent_len)
                if under: lineno += 1
                for insert_line in proper_indent_text:
                    filecontent.insert(lineno, insert_line)
                    lineno += 1
                break

    if (before_status == False) and (after_status == False):
        raise Exception('before/after not met')
    if met_status == False:
        raise Exception('target not met')

    with open(file_path, 'wb') as f:
        for line in filecontent:
            f.write(line)

def _append(file_path, insert_text, target_text, after=None, before=None, under=False):
    filecontent = []
    with open(file_path, 'r') as f:
        for line in f.readlines():
            filecontent.append(line)

    last_appear_position = -1
    proper_indent = 0

    after_status = True if after == None else False
    before_status = True if before == None else False
    met_status = False
    for idx, line in enumerate(filecontent):
        if before_status != True:
            if isinstance(before, list):
                if len([x for x in before if x in line]) > 0:
                    before_status = True
                    break
            else:
                if before in line:
                    before_status = True
                    break
        if after_status != True:
            if isinstance(after, list):
                #after one of string in 'after' list
                if len([x for x in after if x in line]) > 0:
                    after_status = True
                    continue
            else:
                if after not in line:
                    after_status = True
                    continue
        if isinstance(target_text, list):
            if len([x for x in target_text if x in line]) > 0:
                last_appear_position = idx
                proper_indent = len(line) - len(line.lstrip())
                continue
        else:
            if target_text in line:
                last_appear_position = idx
                proper_indent = len(line) - len(line.lstrip())
                continue

    if (before_status == False) and (after_status == False):
        raise Exception('before/after not met')

    #not found
    if last_appear_position < 0:
        print 'did not find target string to append'
        raise Exception('target not met')

    #found then append
    lineno = last_appear_position
    proper_indent_text = _normalize_text(insert_text, proper_indent)
    if under: lineno += 1
    for insert_line in proper_indent_text:
        filecontent.insert(lineno, insert_line)
        lineno += 1

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
    print subprocess.Popen(['cp', 'routes.py.ori', 'routes.py']).communicate()[0]

    to_add_string_list = [
            '               <<<<<<<\n',
            '               right here\n',
            '               <<<<<<<\n'
            ]
    to_match_string = "#apis"

    InsertUnder('./routes.py', to_add_string_list, to_match_string)

if __name__ == '__main__':
    main()
